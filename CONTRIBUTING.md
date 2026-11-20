# Contributing

This directory is only useful if it stays **verified**. Every entry must meet
the standard below; pull requests that don't will be asked to fix it first.

## The verification standard

1. **Live page checked.** Before adding or updating a program, open its
   program page (or the project's own docs/repo) in a browser and read the
   current terms. Aggregator listings (bugbounty.fyi, BountyOperator, etc.)
   are leads, not sources — they still list dead programs as active.
2. **Date recorded.** Set `last_verified` to the date you checked, in
   `YYYY-MM-DD` format. Never copy another entry's date.
3. **Figures sourced or marked unknown.** Reward ranges, KYC, and fees come
   from the program page. If a figure isn't on the page, leave
   `reward_min`/`reward_max` as `null` and write "check program page" in
   `reward_notes`. **Never invent a figure.**
4. **Status is honest.** Use `gated` for live programs that charge a fee,
   require a stake, need reputation points, or require platform verification
   to file. Use `closed`/`paused`/`dead` with a note explaining why and when
   to re-check.
5. **Links must resolve.** Run `python3 scripts/check-links.py` before
   opening a PR. A `FAIL` must be fixed; a `FLAGGED` result (anti-bot 403
   etc.) needs a human browser check noted in the PR.

## How to update

1. Edit `programs.yaml` — it is the source of truth.
2. Regenerate the README: `python3 scripts/generate_readme.py`
3. Check links: `python3 scripts/check-links.py`
4. Commit `programs.yaml`, `README.md`, and `link-check-results.md` together.

## What never goes in here

- Contact email addresses — link to the program page instead.
- Wallet addresses, API keys, or secrets.
- Findings, report text, or payout claims from anyone's live hunts.
  Program facts only.
