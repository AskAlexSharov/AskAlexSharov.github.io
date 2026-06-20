#!/usr/bin/env bash
# Fetch title/body/diffstat for each PR in shortlist.json -> bodies.jsonl
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"
: > bodies.jsonl

fetch_one() {
  local repo="$1" number="$2"
  gh api "repos/$repo/pulls/$number" --jq "{
    repo: \"$repo\", number: $number,
    title, url: .html_url,
    state, merged: .merged, merged_at,
    additions, deletions, changed_files,
    created_at,
    body: ((.body // \"\") | .[0:900])
  }" -H "Accept: application/vnd.github+json" 2>/dev/null
}
export -f fetch_one

# stream "repo number" pairs, fetch with limited parallelism
jq -r '.[] | "\(.repo) \(.number)"' shortlist.json \
  | xargs -P 5 -L 1 bash -c 'fetch_one "$0" "$1"' \
  >> bodies.jsonl

echo "fetched $(wc -l < bodies.jsonl) / $(jq length shortlist.json) PR bodies"
