# PR Highlights — Erigon technical deep-dives

> **Original brief:** fetch all my PRs in erigontech (and reviewed by me — likely my team / my
> ideas), going deep in history, and pull out the important ones with deep technical decisions:
> algorithms, disk formats, database formats, isolation levels, database guarantees, etc.
> Then create blog posts from the "great PRs", tagged **`pr_highligh`**.

Curated from **every PR authored or reviewed by [@AskAlexSharov](https://github.com/AskAlexSharov)**
across the `erigontech` and `ledgerwatch` orgs, back to 2019.

- **10,093** unique PRs fetched (4,941 authored in erigontech, 710 in ledgerwatch, plus reviewed).
- **2,225** flagged as touching deep technical topics — full grouped list in [`erigon-prs/important_prs.md`](../../erigon-prs/important_prs.md).
- **113** high-confidence "decision" PRs (authored + merged + strong signal) in [`erigon-prs/shortlist.json`](../../erigon-prs/shortlist.json).
- The ⭐ entries below are the strongest **blog-post seeds** — each a real algorithmic / format / durability / isolation decision. Posts created from them get the tag **`pr_highligh`**.

> Raw data: [`erigon-prs/all_prs.csv`](../../erigon-prs/all_prs.csv) (all 10,093), `authored.jsonl`, `reviewed.jsonl`. Curation is reproducible via `erigon-prs/curate.py`.

---

## 1. Database guarantees & durability (fsync, crash-consistency)

- ⭐ [`erigon#1433`](https://github.com/erigontech/erigon/pull/1433) · 2021-01 — **lmdb: move fsync inside commit.** Prevents the next write transaction from starting before the previous transaction's fsync has finished — a durability/ordering correctness fix.
  *Blog angle: "Where to put the fsync: durability vs. throughput in an embedded KV store."*
- ⭐ [`erigon#6222`](https://github.com/erigontech/erigon/pull/6222) · 2022-11 — **Exec new blocks in `TxNoSync`, prune + commit in `TxnSync`.** Deliberately relaxes durability during execution for speed, then forces a durable sync at a safe checkpoint before sending notifications.
  *Blog angle: "Trading fsync for throughput safely: no-sync execution with durable checkpoints."*
- ⭐ [`erigon#7713`](https://github.com/erigontech/erigon/pull/7713) · 2023 — **Fix `canRunCycleInOneTransaction`: users could see partial writes.** A read-isolation guarantee — readers must not observe a half-applied sync cycle.
  *Blog angle: "Read isolation in a staged pipeline: never expose partial writes."*
- [`erigon#6825`](https://github.com/erigontech/erigon/pull/6825) · 2022 — Downloader: commit "incomplete" markers with fsync (they matter more than "complete") — crash-consistency ordering of on-disk state markers.
- [`erigon#10004`](https://github.com/erigontech/erigon/pull/10004) · 2024 — Downloader atomic-fs: trust `Create()` semantics instead of re-checking `.lock`.
- Durability knobs: [`#18795`](https://github.com/erigontech/erigon/pull/18795) env vars to disable fsync · [`#16110`](https://github.com/erigontech/erigon/pull/16110) prune back to commit-with-fsync · [`#16781`](https://github.com/erigontech/erigon/pull/16781) revert nosync periodic flusher · [`#10293`](https://github.com/erigontech/erigon/pull/10293) recsplit `NoFsync` flag.

## 2. Transaction isolation & one-tx-per-cycle architecture

- ⭐ [`erigon#6348`](https://github.com/erigontech/erigon/pull/6348) · 2022-12 — **Always run a non-initial sync cycle in a single `RwTx`** (broke the dependency on `CurrentHeader`). Makes a whole multi-stage cycle one atomic read-write transaction.
  *Blog angle: "One transaction per cycle: making a multi-stage pipeline atomic."*
- ⭐ [`erigon#1897`](https://github.com/erigontech/erigon/pull/1897) · 2021 — **Move staged sync to a transaction** (+862/-915) — the foundational refactor that put the staged-sync loop under explicit DB transactions.
- Transaction-scoping the ETL/stages: [`#1660`](https://github.com/erigontech/erigon/pull/1660) etl→rwtx · [`#1727`](https://github.com/erigontech/erigon/pull/1727)/[`#1726`](https://github.com/erigontech/erigon/pull/1726) history/IH stages→rwtx · [`#1692`](https://github.com/erigontech/erigon/pull/1692) drop etl `onLoadCommit` hook · [`#1806`](https://github.com/erigontech/erigon/pull/1806) exec-unwind ETL ("solves the `TXN_FULL` problem").

## 3. Storage engine internals (MDBX / LMDB)

- ⭐ [`erigon#3323`](https://github.com/erigontech/erigon/pull/3323) · 2022-01 — **MDBX page size.** Larger pages to lift the ~8 TB DB-size ceiling (max DB size is bounded by page size in the B-tree mmap engine).
  *Blog angle: "Why page size caps your database at 8 TB — and how raising it works."*
- ⭐ [`erigon#1213`](https://github.com/erigontech/erigon/pull/1213) · 2020-10 — **LMDB: skip freelist search for large page sequences** (new `SetMaxFreelistReuse` API). Above a threshold, contiguous-freelist scanning costs more than growing the file.
  *Blog angle: "Freelist fragmentation: when page reuse costs more than growth."*
- ⭐ [`erigon#9781`](https://github.com/erigontech/erigon/pull/9781) · 2024 — **Commit each prune batch so freed pages return to the freelist for the next batch.** Time-bounded, committed prune batches keep memory flat.
  *Blog angle: "Pruning a B-tree without exploding the freelist."*
- Geometry/memory tuning: [`#9175`](https://github.com/erigontech/erigon/pull/9175) hard-limit dirty pages · [`#6231`](https://github.com/erigontech/erigon/pull/6231) & [`erigon-lib#770`](https://github.com/ledgerwatch/erigon-lib/pull/770) expose `dirtySpace` · [`#1515`](https://github.com/erigontech/erigon/pull/1515) match LMDB dirty-list size · [`erigon-lib#582`](https://github.com/ledgerwatch/erigon-lib/pull/582) expose growth step.
- Engine migration: [`#2199`](https://github.com/erigontech/erigon/pull/2199) switch to `mdbx-go` module (−115k lines) · [`#5392`](https://github.com/erigontech/erigon/pull/5392) vendor libmdbx `.c` instead of submodule.

## 4. Compression & encoding algorithms

- ⭐ [`erigon#19191`](https://github.com/erigontech/erigon/pull/19191) · 2026 — **Replace the C SA-IS lib with Go's `index/suffixarray`.** The C suffix-array builder did `malloc` syscalls hostile to the Go runtime; the stdlib version is GC-friendlier (±900 lines each way).
  *Blog angle: "Dropping C for Go's suffixarray: syscalls, the GC, and dictionary building."*
- ⭐ [`erigon-lib#223`](https://github.com/ledgerwatch/erigon-lib/pull/223) / [`#234`](https://github.com/ledgerwatch/erigon-lib/pull/234) + [`erigon#3265`](https://github.com/erigontech/erigon/pull/3265) / [`#3211`](https://github.com/erigontech/erigon/pull/3211) — **Parallel dictionary compressor** (`ParallelCompressor`, `DecompressedFile`). One compressor for both parallel and serial work.
  *Blog angle: "Building a parallel dictionary compressor for terabyte snapshots."*
- ⭐ [`erigon#5130`](https://github.com/erigontech/erigon/pull/5130) · 2022 — **Condensed Huffman pattern tables** for the `.seg` dictionary codec.
- ⭐ [`erigon#14780`](https://github.com/erigontech/erigon/pull/14780) · 2025 — **Page-level compression for history files** (+756 lines). Compress at page granularity rather than per word.
- ⭐ [`erigon#12951`](https://github.com/erigontech/erigon/pull/12951) · 2024 — **`d_lru`: cache decompressed values.** Decompressing `CodeDomain` values was ~7% of execution time.
- ⭐ [`erigon#20567`](https://github.com/erigontech/erigon/pull/20567) · 2026 — **B-tree index warmup reads key-only**, skipping value decompression (only pivot keys are needed). Highest keyword-density PR in the set.
- ⭐ [`erigon#14604`](https://github.com/erigontech/erigon/pull/14604) · 2025 — **Snappy compression for `commitment.v`** — 2× size reduction, and stops the shared dictionary from being "over-flooded by good patterns."
- Per-domain compression decisions: [`#11696`](https://github.com/erigontech/erigon/pull/11696) keys-compression for `commitment.kv` >64 steps · [`#11712`](https://github.com/erigontech/erigon/pull/11712) `storage.kv` · [`#18740`](https://github.com/erigontech/erigon/pull/18740) move compression `.Add()`→`.Compress()`.
- Decompressor hardening: [`#3395`](https://github.com/erigontech/erigon/pull/3395) `WithReadAhead` · [`#3225`](https://github.com/erigontech/erigon/pull/3225) fast `Count()` · [`#7228`](https://github.com/erigontech/erigon/pull/7228) reject bad dicts · [`#4882`](https://github.com/erigontech/erigon/pull/4882) catch `maxDepth` underflow · [`#18490`](https://github.com/erigontech/erigon/pull/18490) remove `condense`.
- ⭐ Historical: [`bolt#2`](https://github.com/ledgerwatch/bolt/pull/2) / [`bolt#11`](https://github.com/ledgerwatch/bolt/pull/11) — **optional key-prefix compression in `bolt`**, Erigon's original storage engine.

## 5. Indexing & minimal-perfect-hashing (RecSplit / Elias-Fano)

- ⭐ [`erigon#20640`](https://github.com/erigontech/erigon/pull/20640) · 2026 — **Off-heap Elias-Fano build.** Building EF for 3 billion keys burned 3 GB of RAM and OOM'd; moved the construction off-heap.
  *Blog angle: "Off-heap Elias-Fano: indexing 3 billion keys without OOM."*
- ⭐ [`erigon#15960`](https://github.com/erigontech/erigon/pull/15960) · 2025 — **Internal existence filter based on `fuse_filter`** baked into `.efi`/`.kvi` files (bumps their major version).
  *Blog angle: "Fuse filters vs. Bloom: cheaper existence checks inside index files."*
- ⭐ [`erigon#3465`](https://github.com/erigontech/erigon/pull/3465) · 2022 — **Parallel transaction-index build** + recsplit offset-collector reset + faster ETL flush.
- [`erigon#20566`](https://github.com/erigontech/erigon/pull/20566) `eliasfano32` `searchUpperReverse` off-by-one fix · backward-compat: [`#16282`](https://github.com/erigontech/erigon/pull/16282)/[`#16281`](https://github.com/erigontech/erigon/pull/16281)/[`#15986`](https://github.com/erigontech/erigon/pull/15986) · [`#21871`](https://github.com/erigontech/erigon/pull/21871) `SmallSortableBuffers` for the bucket collector.

## 6. On-disk / snapshot (`.seg`) formats & write amplification

- ⭐ [`erigon#3140`](https://github.com/erigontech/erigon/pull/3140) · 2021-12 — **Add word-count to `.seg`** (breaking snapshot-format change).
- ⭐ [`erigon-lib#355`](https://github.com/ledgerwatch/erigon-lib/pull/355) · 2022 — **Add `emptyWordsCount` to the `.seg` header** (breaking `.seg` format).
- ⭐ [`erigon#7607`](https://github.com/erigontech/erigon/pull/7607) · 2023 — **`DumpBodies`: break dependency on `body.BaseTxNum`** — a step toward storing canonical + non-canonical bodies in one table to cut write amplification.
  *Blog angle: "Table layout and write amplification: one table for canonical & non-canonical bodies."*
- [`#19443`](https://github.com/erigontech/erigon/pull/19443) skip `.idt` when word-compression is off · [`#3286`](https://github.com/erigontech/erigon/pull/3286) parallel compressor allows empty words · [`#3558`](https://github.com/erigontech/erigon/pull/3558) block-snapshot merge · [`#3724`](https://github.com/erigontech/erigon/pull/3724) seed large `.seg` files.

## 7. Erigon3 state model — txNum, domains, commitment

- ⭐ [`erigon#5176`](https://github.com/erigontech/erigon/pull/5176) · 2022-08 — **Erigon22: basic txNum forward/unwind** — the transaction-number-indexed state model underpinning Erigon3.
  *Blog angle: "txNum: indexing chain state by transaction number instead of block."*
- ⭐ [`erigon#5051`](https://github.com/erigontech/erigon/pull/5051) · 2022-08 — **Working PlainState unwind** for the flat-state representation.
- ⭐ [`erigon#8855`](https://github.com/erigontech/erigon/pull/8855) / [`#8853`](https://github.com/erigontech/erigon/pull/8853) · 2023 — **`UnwindTo` only moves to blocks that have a committed state root** — a consistency guarantee on where you're allowed to rewind.
- [`#13276`](https://github.com/erigontech/erigon/pull/13276) make `.kvi` the default commitment index · [`#20958`](https://github.com/erigontech/erigon/pull/20958) in-mem commitment existence filter · [`#17019`](https://github.com/erigontech/erigon/pull/17019) move commitment/changeset DB format out of `db/state`.

---

### Suggested first posts (highest-impact ⭐, broad appeal)

1. **`erigon#1433` + `#6222`** — the fsync story: durability ordering and no-sync execution.
2. **`erigon#3323` + `#1213`** — storage-engine limits: the 8 TB page-size ceiling and freelist reuse.
3. **`erigon#20640` + `#15960`** — perfect hashing at scale: off-heap Elias-Fano and fuse filters.
4. **`erigon#19191`** — replacing C with Go's suffixarray in the compressor.
5. **`erigon#5176`** — the txNum state model (Erigon3's core idea).
