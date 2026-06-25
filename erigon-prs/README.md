# erigon-prs — PR history dataset

All PRs **authored or reviewed by [@AskAlexSharov](https://github.com/AskAlexSharov)** across the
`erigontech` and `ledgerwatch` GitHub orgs, fetched deep into history (2019→). Used to curate the
technical-deep-dive highlights in [`../docs/features/pr_highlights.md`](../docs/features/pr_highlights.md).

## Data files
| file | rows | what |
|------|------|------|
| `all_prs.csv` | 10,093 | every unique PR (repo, number, title, state, merged, date, relation, importance flag, score, topics) |
| `authored.jsonl` | 6,651 raw | PRs authored by the user (raw, year/quarter-bucketed, has dupes — dedup happens in `curate.py`) |
| `reviewed.jsonl` | 7,555 raw | PRs reviewed by the user (raw) |
| `important_prs.md` | 2,225 | PRs flagged as deep-technical, grouped by topic |
| `shortlist.json` | 113 | high-confidence "decision" PRs: authored + merged + score ≥ 6, deduped by title |
| `bodies.jsonl` | 113 | title/body/diffstat for the shortlist (used to write grounded descriptions) |

## Scripts (reproduce)
- `gql_fetch.sh <author|reviewed-by> <out.jsonl>` — fetch via the GitHub GraphQL API (year buckets, quarter sub-buckets when a year exceeds the 1000-result cap).
- `curate.py` — dedup authored+reviewed, score titles by technical-topic keywords (strong terms qualify alone; common terms need pairing; dep-bumps/CI/typos excluded), emit `important_prs.md` + `all_prs.csv`.
- `fetch_bodies.sh` — fetch PR bodies + diffstats for `shortlist.json` → `bodies.jsonl`.

Method: keyword/label heuristic over titles, then manual curation of the shortlist from real PR bodies. Refine `GROUPS`/thresholds in `curate.py` and re-run.
