#!/usr/bin/env python3
"""Check every program_url + scope_url in programs.yaml.

Usage: python3 scripts/check-links.py [--timeout SECONDS]

- Follows redirects; a final 2xx counts as OK.
- 403/429/503 and Cloudflare-style blocks are FLAGGED, not failed: several
  bounty platforms (notably Remedy / r.xyz) block automated requests while
  serving real browsers fine. Flagged links need a human browser check.
  A connection that the server accepts and then drops mid-response
  (ChunkedEncodingError / RemoteDisconnected) is treated the same way: the
  host is alive, the automation is being filtered. DNS failures and
  timeouts stay FAIL.
- Any other 4xx/5xx, DNS failure, or timeout is a FAIL and must be fixed or
  the entry re-verified before pushing.
- Writes results to link-check-results.md (committed, so readers can see
  when links were last checked) and exits non-zero only on FAILs.

Requires: requests, PyYAML (pip install requests pyyaml).
"""
import argparse
import sys
from datetime import date
from pathlib import Path

try:
    import requests
    import yaml
except ImportError as exc:
    sys.exit(f"Missing dependency: {exc} (pip install requests pyyaml)")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "programs.yaml"
OUT = ROOT / "link-check-results.md"

# Statuses that usually mean anti-bot / rate limiting, not a dead link.
FLAGGED_STATUSES = {403, 429, 503}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def check(url, timeout):
    """Return (verdict, detail): verdict in OK / FLAGGED / FAIL."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout,
                            allow_redirects=True)
    except requests.exceptions.ChunkedEncodingError as exc:
        # Server accepted the connection, then dropped it mid-response:
        # the host is alive, the automation is being filtered (r.xyz does
        # exactly this to non-browser clients while serving browsers fine).
        return "FLAGGED", f"connection dropped mid-response (likely anti-bot — verify in a browser)"
    except requests.exceptions.ConnectionError as exc:
        if "Name or service not known" in str(exc) or "Failed to resolve" in str(exc):
            return "FAIL", f"DNS failure: {exc}"
        if "RemoteDisconnected" in str(exc) or "Connection reset" in str(exc):
            return "FLAGGED", "connection reset by server (likely anti-bot — verify in a browser)"
        return "FAIL", f"ConnectionError: {exc}"
    except requests.exceptions.RequestException as exc:
        return "FAIL", f"{type(exc).__name__}: {exc}"
    code = resp.status_code
    if 200 <= code < 300:
        return "OK", f"HTTP {code}"
    if code in FLAGGED_STATUSES:
        return "FLAGGED", f"HTTP {code} (likely anti-bot — verify in a browser)"
    return "FAIL", f"HTTP {code}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=int, default=25)
    args = parser.parse_args()

    data = yaml.safe_load(DATA.read_text())
    programs = data["programs"]

    results = []  # (program, field, url, verdict, detail)
    seen = set()
    for prog in programs:
        for field in ("program_url", "scope_url"):
            url = prog.get(field)
            if not url or url in seen:
                continue
            seen.add(url)
            verdict, detail = check(url, args.timeout)
            results.append((prog["name"], field, url, verdict, detail))
            print(f"{verdict:8} {detail:55} {prog['name']} [{field}] {url}")

    ok = sum(1 for r in results if r[3] == "OK")
    flagged = sum(1 for r in results if r[3] == "FLAGGED")
    failed = sum(1 for r in results if r[3] == "FAIL")

    lines = [
        "# Link check results",
        "",
        f"Last run: {date.today().isoformat()} (`python3 scripts/check-links.py`)",
        "",
        f"- OK: **{ok}**",
        f"- Flagged (anti-bot / rate-limited — verify in a browser): **{flagged}**",
        f"- Failed: **{failed}**",
        "",
        "| Program | Field | URL | Result | Detail |",
        "|---|---|---|---|---|",
    ]
    for name, field, url, verdict, detail in results:
        lines.append(f"| {name} | {field} | {url} | {verdict} | {detail} |")
    lines.append("")
    OUT.write_text("\n".join(lines))
    print(f"\n{len(results)} unique links: {ok} OK, {flagged} flagged, "
          f"{failed} failed. Wrote {OUT}")

    if failed:
        print("FAILURES present — fix or re-verify before pushing.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
