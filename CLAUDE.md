# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Two loosely-coupled things live here:

1. **A personal Hugo blog** (`hugo.toml`, `layouts/`, `content/`, `static/`) deployed to GitHub
   Pages as a **user site** at `https://askalexsharov.github.io/`.
2. **`erigon-prs/`** — a self-contained data pipeline that mines the author's GitHub PR history
   (Erigon database/storage work) and curates it into blog-post seeds under
   `docs/features/pr_highlights.md`. This feeds the blog; posts written from it are tagged
   `pr_highligh`.

`old/` is an **archived previous version of the site** — not part of the build, not maintained.
Don't edit it. It contains a dead git submodule (`old/themes/uBlogger`) whose pinned commit no
longer exists upstream (see Gotchas).

## Hugo blog

**Themeless.** There is no Hugo theme; every template under `layouts/` is hand-written
(`_default/baseof.html` + `single`/`list`/`terms`, `index.html` for the home page, `partials/`).
Styling is plain CSS in `static/css/main.css` — **no SCSS/Sass pipeline**, so the *non-extended*
Hugo binary is sufficient.

Content model: posts live in `content/posts/` with **TOML front matter** (`+++` fences, see
`archetypes/default.md`). New posts default to `draft = true` — flip to `false` to publish. Only
a `tag` taxonomy is enabled (categories intentionally omitted). `hugo.toml` `[params]` drives the
site description/author/footer.

### Commands

```bash
hugo server -D            # local dev server, -D includes drafts
hugo --gc --minify        # production build into ./public (gitignored)
hugo new content posts/my-post.md   # scaffold a post from the archetype
```

CI pins **Hugo 0.163.3 (extended)**; locally any recent Hugo works since there's no SCSS.

### Deployment (important constraints)

- Pushing to **`master`** triggers `.github/workflows/hugo.yml`, which builds and deploys to Pages.
  GitHub Pages **source must be "GitHub Actions"** (`build_type: workflow`), not the legacy
  branch build — otherwise it tries to Jekyll-build the Hugo source.
- This is a **user site**: it only serves from the domain root if the repo is named exactly
  **`AskAlexSharov.github.io`**. As any other name it publishes under a `/repo/` path prefix.
- The workflow checks out with **`submodules: false`** on purpose (see Gotchas) and overrides
  `--baseURL` from the Pages config, so the hardcoded `baseURL` in `hugo.toml` only matters for
  local builds.

## `erigon-prs/` data pipeline

Reproduces the PR dataset behind `docs/features/pr_highlights.md`. Run from inside `erigon-prs/`;
needs an authenticated `gh` CLI.

```bash
bash gql_fetch.sh author     authored.jsonl     # all authored PRs  (GraphQL)
bash gql_fetch.sh reviewed-by reviewed.jsonl    # all reviewed PRs
python3 curate.py                               # -> important_prs.md + all_prs.csv
bash fetch_bodies.sh                            # PR bodies for shortlist.json -> bodies.jsonl
```

- `gql_fetch.sh` uses the GitHub **GraphQL** API (5000 pts/hr), not REST search (30/min) which is
  too slow/fragile here. GitHub search caps any query at 1000 results, so it buckets by **year**
  and sub-buckets by **quarter** when a year exceeds 1000; duplicates are deduped in `curate.py`.
- `curate.py` scores PRs by keyword **on the title only** (strong DB/algorithm terms qualify
  alone; common terms need pairing; dep-bumps/CI/typos excluded), dedups authored+reviewed by
  `(repo, number)`, and is deterministic — re-running yields identical output.
- `ledgerwatch/erigon` and `erigontech/erigon` are the **same repo** (transferred; the old path
  redirects). But **other** repos share PR numbers, so always key PRs by `(repo, number)` / URL,
  never by number alone.

## Gotchas

- **Dead submodule:** `old/themes/uBlogger` points at an upstream commit that's been GC'd
  (`upload-pack: not our ref`). Never fetch submodules in CI or locally for a build — it fails.
  The deploy workflow sets `submodules: false` for this reason.
- **TOML ordering in `hugo.toml`:** all scalar keys (e.g. `enableRobotsTXT`, `title`) **must come
  before any `[table]` header**. A scalar placed after `[taxonomies]` gets absorbed into that
  table — a past bug turned `paginate`/`enableRobotsTXT` into bogus taxonomies that generated
  stray `/10/` and `/true/` output pages.
- Use `locale` (not the deprecated `languageCode`) and `site.Language.Locale` in templates —
  required since Hugo 0.158.
- `.claude/` is gitignored; this repo is **public**, so keep session/local data out of commits.
