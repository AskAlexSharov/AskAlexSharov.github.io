#!/usr/bin/env bash
# Fetch all PRs (authored or reviewed) by a user across orgs via the GraphQL API.
# GraphQL has a 5000-point/hr budget (vs REST search's 30/min), so this is fast.
# Search still caps at 1000 results/query, so we bucket by year and sub-bucket
# by quarter for any year that exceeds 1000. Duplicates are deduped in curate.py.
set -u

USER_LOGIN="AskAlexSharov"
ORGS=("erigontech" "ledgerwatch")
YEARS=(2019 2020 2021 2022 2023 2024 2025 2026)
OUT_DIR="$(cd "$(dirname "$0")" && pwd)"

QUERY='query($q:String!,$cursor:String){search(query:$q,type:ISSUE,first:100,after:$cursor){issueCount pageInfo{hasNextPage endCursor} nodes{... on PullRequest{number title url state merged createdAt repository{nameWithOwner} labels(first:8){nodes{name}}}}}}'

LAST_COUNT=0

fetch_bucket() { # kind org from to out
  local kind="$1" org="$2" from="$3" to="$4" out="$5"
  local q="org:$org $kind:$USER_LOGIN type:pr created:$from..$to"
  local cursor="" page=0 resp has cnt
  while :; do
    if [ -z "$cursor" ]; then
      resp=$(gh api graphql -f query="$QUERY" -f q="$q" 2>/dev/null)
    else
      resp=$(gh api graphql -f query="$QUERY" -f q="$q" -f cursor="$cursor" 2>/dev/null)
    fi
    if echo "$resp" | jq -e '.errors' >/dev/null 2>&1; then
      echo "    ERROR $org $from: $(echo "$resp" | jq -c '.errors' 2>/dev/null)" >&2
      sleep 3; continue
    fi
    echo "$resp" | jq -c --arg kind "$kind" '
      .data.search.nodes[] | select(.number != null) | {
        number, title, url,
        repo: .repository.nameWithOwner,
        state: (.state | ascii_downcase),
        created_at: .createdAt, merged,
        labels: [.labels.nodes[].name],
        relation: $kind
      }' >> "$out"
    page=$((page+1))
    has=$(echo "$resp" | jq -r '.data.search.pageInfo.hasNextPage')
    cursor=$(echo "$resp" | jq -r '.data.search.pageInfo.endCursor')
    cnt=$(echo "$resp" | jq -r '.data.search.issueCount')
    LAST_COUNT="$cnt"
    [ "$has" != "true" ] && break
    [ "$page" -ge 10 ] && { echo "    cap-hit $org $kind $from ($cnt)" >&2; break; }
    sleep 0.2
  done
  echo "  $org $kind $from..$to count=$cnt pages=$page" >&2
}

run_kind() { # kind out
  local kind="$1" out="$2"; : > "$out"
  for org in "${ORGS[@]}"; do
    for y in "${YEARS[@]}"; do
      fetch_bucket "$kind" "$org" "$y-01-01" "$y-12-31" "$out"
      if [ "${LAST_COUNT:-0}" -gt 1000 ]; then
        echo "  >1000 -> sub-bucketing $org $y by quarter" >&2
        for qr in "01-01:03-31" "04-01:06-30" "07-01:09-30" "10-01:12-31"; do
          fetch_bucket "$kind" "$org" "$y-${qr%%:*}" "$y-${qr##*:}" "$out"
        done
      fi
    done
  done
  echo "DONE $kind -> $out ($(wc -l < "$out") raw rows)" >&2
}

run_kind "$1" "$2"
