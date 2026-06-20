#!/usr/bin/env python3
"""Curate 'important' PRs (deep technical decisions) from the fetched JSONL dumps.

Signal is the PR title + labels (we can't read 10k bodies). Strategy:
  - STRONG keywords (unambiguous DB/storage/algorithm terms) qualify a PR alone.
  - WEAK keywords (common Erigon words) need >=2 hits, or 1 weak + 1 strong.
  - NOISE titles (dep bumps, CI, typos, releases) are dropped unless a STRONG hit.
Output: a grouped, deduped, committable markdown of the important PRs.
"""
import json, re, sys, os, glob
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))

# Topic groups -> (strong_keywords, weak_keywords). Matching is substring on a
# lowercased title; short/ambiguous tokens are kept out to protect precision.
GROUPS = {
    "Storage engine (MDBX/LMDB)": (
        ["mdbx", "libmdbx", "lmdb", "mmap", "fsync", "msync", "freelist",
         "free list", "free-list", "dirty space", "dirtyspace", "dirty pages",
         "page size", "growth step", "geometry", "durability", "write-ahead",
         "wal log", "os.sync", "no-sync", "nosync"],
        ["page", "sync", "durable", "flush"],
    ),
    "Isolation & transactions": (
        ["isolation", "mvcc", "snapshot isolation", "long read", "long-read",
         "long running tx", "read transaction", "rwtx", "txnum", "tx num",
         "atomic commit", "acid", "serializable", "stale read", "consistent read"],
        ["transaction", "rollback", "atomic", "commit", "txn", "tx "],
    ),
    "State / domains / commitment": (
        ["commitment", "patricia", "hex patricia", "hph", "plain state",
         "plainstate", "state root", "witness", "trie node"],
        ["domain", "trie", "state", "account", "storage"],
    ),
    "Snapshots / freezer / segments": (
        ["freezer", "retire", "seg file", ".seg", "webseed", "snapshot format",
         "block snapshots", "frozen blocks", "snapshot sync"],
        ["snapshot", "snapshots", "downloader", "torrent", "merge"],
    ),
    "Indexing & perfect hashing": (
        ["elias fano", "elias-fano", "eliasfano", "recsplit", "rec-split",
         "perfect hash", "minimal perfect", "inverted index", "roaring",
         "accessor index", "btree index", "b-tree", ".efi", ".vi"],
        ["bitmap", "btree", "index", "lookup"],
    ),
    "Compression / encoding": (
        ["compress", "decompress", "compression", "dictionary", "huffman",
         "varint", "rlp ", "ssz", "cbor", "codec", "superstring"],
        ["encoding", "encode", "decode", "serialization", "format"],
    ),
    "ETL / staged sync / pruning": (
        ["staged sync", "stagedsync", "sync stage", "etl ", "integrity check",
         "unwind", "reorg"],
        ["prune", "pruning", "collector", "stage", "pipeline", "parallel"],
    ),
    "On-disk / DB format & migration": (
        ["disk format", "on-disk", "file format", "db format", "database format",
         "db migration", "schema migration", "backward compat", "forward compat",
         "db layout", "file layout", "data format"],
        ["migration", "format", "schema", "layout"],
    ),
}

NOISE = re.compile(
    r"\b(bump|dependabot|go\.mod|go\.sum|update dep|deps|ci:|ci |lint|gofmt|"
    r"typo|readme|changelog|comment|rename|nit:|flaky|skip test|disable test|"
    r"wip|draft|release|tag v|version|gofumpt|fmt|golangci|spelling)\b",
    re.I,
)


def classify(title, labels):
    t = " " + title.lower() + " "
    strong_hits, weak_hits, topics = [], [], []
    for group, (strong, weak) in GROUPS.items():
        g_strong = [k for k in strong if k in t]
        g_weak = [k for k in weak if k in t]
        if g_strong or g_weak:
            topics.append(group)
        strong_hits += g_strong
        weak_hits += g_weak
    keep = bool(strong_hits) or len(set(weak_hits)) >= 2
    # Drop pure-noise titles unless a strong signal is present.
    if keep and not strong_hits and NOISE.search(title):
        keep = False
    score = 3 * len(set(strong_hits)) + len(set(weak_hits))
    return keep, score, topics, sorted(set(strong_hits + weak_hits))


def load(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main():
    authored = load(os.path.join(HERE, "authored.jsonl"))
    reviewed = load(os.path.join(HERE, "reviewed.jsonl"))

    # Dedup by (repo, number); merge the authored/reviewed relation.
    merged = {}
    for r in authored + reviewed:
        key = (r["repo"], r["number"])
        if key not in merged:
            merged[key] = dict(r)
            merged[key]["relations"] = set()
        merged[key]["relations"].add(r.get("relation", ""))

    important = []
    for r in merged.values():
        keep, score, topics, hits = classify(r["title"], r.get("labels", []))
        if keep:
            r["score"], r["topics"], r["hits"] = score, topics, hits
            important.append(r)

    # Primary topic = first matched group, by GROUPS order.
    order = list(GROUPS.keys())
    by_topic = defaultdict(list)
    for r in important:
        primary = min(r["topics"], key=lambda g: order.index(g))
        by_topic[primary].append(r)

    total_all = len(merged)
    out = [
        "# Erigon PR highlights — technical deep-dives",
        "",
        f"Curated from **{len(authored)} authored** + **{len(reviewed)} reviewed** "
        f"PRs by [@AskAlexSharov](https://github.com/AskAlexSharov) across the "
        f"`erigontech` and `ledgerwatch` orgs ({total_all} unique). "
        f"**{len(important)}** flagged as deep technical decisions "
        "(algorithms, disk/database formats, isolation, DB guarantees).",
        "",
        "> Heuristic curation from PR titles + labels — refine freely. "
        "Each PR is a candidate seed for a `pr_highligh`-tagged blog post.",
        "",
    ]
    for topic in order:
        rows = by_topic.get(topic)
        if not rows:
            continue
        rows.sort(key=lambda r: (-r["score"], r["repo"], -r["number"]))
        out.append(f"## {topic}  ({len(rows)})")
        out.append("")
        for r in rows:
            rel = "+".join(sorted(x for x in r["relations"] if x)) or "author"
            rel = rel.replace("author", "authored").replace("reviewed-by", "reviewed")
            merged_tag = "merged" if r.get("merged") else r.get("state", "")
            date = (r.get("created_at") or "")[:10]
            out.append(
                f"- [`{r['repo']}#{r['number']}`]({r['url']}) — {r['title']}  "
                f"\n  <sub>{date} · {merged_tag} · {rel} · score {r['score']} · "
                f"{', '.join(r['hits'][:6])}</sub>"
            )
        out.append("")

    md_path = os.path.join(HERE, "important_prs.md")
    with open(md_path, "w") as f:
        f.write("\n".join(out))

    # Also a flat CSV of every fetched PR for reference.
    import csv
    csv_path = os.path.join(HERE, "all_prs.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["repo", "number", "title", "state", "merged", "created_at",
                    "relations", "url", "important", "score", "topics"])
        for r in sorted(merged.values(), key=lambda r: (r["repo"], -r["number"])):
            keep, score, topics, _ = classify(r["title"], r.get("labels", []))
            w.writerow([
                r["repo"], r["number"], r["title"], r.get("state", ""),
                r.get("merged", ""), (r.get("created_at") or "")[:10],
                "+".join(sorted(x for x in r["relations"] if x)), r["url"],
                int(keep), score, "; ".join(topics),
            ])

    print(f"unique PRs: {total_all}")
    print(f"important:  {len(important)}")
    for topic in order:
        if by_topic.get(topic):
            print(f"  {len(by_topic[topic]):4d}  {topic}")
    print(f"wrote {md_path}")
    print(f"wrote {csv_path}")


if __name__ == "__main__":
    main()
