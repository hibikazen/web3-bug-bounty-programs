#!/usr/bin/env python3
"""Generate README.md from programs.yaml.

Usage: python3 scripts/generate_readme.py
Run from the repo root. The README table is generated — do not edit it by
hand; edit programs.yaml and re-run this script.
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "programs.yaml"
OUT = ROOT / "README.md"


def fmt_money(value):
    if value is None:
        return None
    if value == 0:
        return "$0"
    if value >= 1_000_000:
        whole, rem = divmod(value, 1_000_000)
        return f"${whole}.{rem // 100_000}M" if rem else f"${whole}M"
    if value >= 1_000:
        whole, rem = divmod(value, 1_000)
        return f"${whole}.{rem // 100}k" if rem else f"${whole}k"
    return f"${value}"


def reward_range(p):
    lo, hi = fmt_money(p.get("reward_min")), fmt_money(p.get("reward_max"))
    if lo and hi:
        return f"{lo} – {hi}"
    if hi:
        return f"up to {hi}"
    if lo:
        return f"from {lo}"
    return "check program page"


def kyc_cell(p):
    return {"yes": "Yes", "no": "No", "unknown": "Unknown"}.get(p.get("kyc"), "Unknown")


def row(p):
    name = f"[{p['name']}]({p['program_url']})"
    scope = f"[{p['scope']}]({p['scope_url']})" if p.get("scope_url") else p["scope"]
    return (
        f"| {name} | {p['platform']} | {reward_range(p)} | {kyc_cell(p)} | "
        f"{p['submission_fee']} | {scope} | {p['last_verified']} |"
    )


HEADER = """# Web3 Bug Bounty Programs — Verified Directory

A curated directory of **active Web3 bug bounty programs** where every entry
was actually checked against its live program page. The differentiator vs.
stale aggregator lists: each program carries a **last-verified date**, and any
figure that could not be confirmed says so instead of being invented.

> **Verification standard:** a program is listed only if its program page (or
> the project's own docs/repo) was read live. Reward figures come from that
> page or from the maintainer's own survey notes. Anything unconfirmed is
> marked "check program page". See [CONTRIBUTING.md](CONTRIBUTING.md).

## How to use this list

- **Start with Active, no fee** — these cost $0 to file and have no gate.
- **Gated** programs are live, but filing costs a fee, a stake, reputation
  points, or a platform verification step. Read the notes before spending.
- **Closed / Paused / Dead** are kept so you don't waste time on programs
  aggregators still show as active.
- **Always re-check the program page before hunting.** Terms, scope, and
  reward tiers change; the last-verified date tells you how fresh each row is.

## Active — no fee, no gate

| Program | Platform | Reward range | KYC | Fee | Scope | Last verified |
|---|---|---|---|---|---|---|
"""

GATED_HEADER = """
## Gated — live, but filing costs something

| Program | Platform | Reward range | KYC | Fee | Scope | Last verified |
|---|---|---|---|---|---|---|
"""

CLOSED_HEADER = """
## Closed / Paused

| Program | Platform | Reward range | KYC | Fee | Scope | Last verified |
|---|---|---|---|---|---|---|
"""

DEAD_HEADER = """
## Dead — do not trust aggregators that still list these

| Program | Platform | Reward range | KYC | Fee | Scope | Last verified |
|---|---|---|---|---|---|---|
"""

FOOTER = """
## Notes per program

"""


def main():
    data = yaml.safe_load(DATA.read_text())
    programs = data["programs"]

    active = [p for p in programs if p["status"] == "active"]
    gated = [p for p in programs if p["status"] == "gated"]
    closed = [p for p in programs if p["status"] in ("closed", "paused")]
    dead = [p for p in programs if p["status"] == "dead"]

    parts = [HEADER]
    parts += [row(p) for p in active]
    parts.append(GATED_HEADER)
    parts += [row(p) for p in gated]
    parts.append(CLOSED_HEADER)
    parts += [row(p) for p in closed]
    parts.append(DEAD_HEADER)
    parts += [row(p) for p in dead]

    parts.append(FOOTER)
    for p in programs:
        parts.append(f"### {p['name']} ({p['status']})")
        parts.append("")
        parts.append(f"- **Platform:** {p['platform']}")
        parts.append(f"- **Program page:** {p['program_url']}")
        parts.append(f"- **Rewards:** {p['reward_notes']}")
        parts.append(f"- **KYC:** {kyc_cell(p)} · **Fee:** {p['submission_fee']}")
        parts.append(f"- **Last verified:** {p['last_verified']}")
        parts.append(f"- {p['notes']}")
        parts.append("")

    parts.append("---")
    parts.append("")
    parts.append(
        f"_{len(programs)} programs: {len(active)} active, {len(gated)} gated, "
        f"{len(closed)} closed/paused, {len(dead)} dead. "
        "Machine-readable source: [programs.yaml](programs.yaml). "
        "Link status: see [link-check-results.md](link-check-results.md)._"
    )
    parts.append("")

    OUT.write_text("\n".join(parts))
    print(f"Wrote {OUT}: {len(programs)} programs "
          f"({len(active)} active, {len(gated)} gated, "
          f"{len(closed)} closed/paused, {len(dead)} dead)")


if __name__ == "__main__":
    main()
