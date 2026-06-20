# PR Highlights — Erigon technical deep-dives

> **Original brief:** fetch all my PRs in erigontech (and reviewed by me — likely my team / my
> ideas), going deep in history, and pull out the important ones with deep technical decisions:
> algorithms, disk formats, database formats, isolation levels, database guarantees, etc.
> Then create blog posts from the "great PRs", tagged **`pr_highligh`**.

Curated from **every PR authored or reviewed by [@AskAlexSharov](https://github.com/AskAlexSharov)**
across the `erigontech` / `ledgerwatch` orgs, back to 2019.

- **10,093** unique PRs fetched · **2,225** flagged technical ([`erigon-prs/important_prs.md`](../../erigon-prs/important_prs.md)) · full data in [`erigon-prs/all_prs.csv`](../../erigon-prs/all_prs.csv).
- ⭐ marks the strongest **blog-post seeds** (real algorithmic / format / isolation / memory decisions). Posts get the tag **`pr_highligh`**.

---

## 1. Storage engine internals (MDBX / LMDB)

- ⭐ [`erigon#3323`](https://github.com/erigontech/erigon/pull/3323) · 2022-01 — **MDBX page size.** Larger pages lift the ~8 TB DB-size ceiling (max DB size is bounded by page size in the B-tree mmap engine).
  *Angle: "Why page size caps your database at 8 TB."*
- ⭐ [`erigon#1213`](https://github.com/erigontech/erigon/pull/1213) · 2020-10 — **LMDB: skip freelist search for large page sequences** (`SetMaxFreelistReuse`). Above a threshold, scanning the contiguous freelist costs more than growing the file.
  *Angle: "Freelist fragmentation: when page reuse costs more than growth."*
- ⭐ [`erigon#9781`](https://github.com/erigontech/erigon/pull/9781) · 2024 — **Commit each prune batch so freed pages return to the freelist for the next batch.** Time-bounded committed batches keep memory flat.
- Geometry/memory tuning: [`#9175`](https://github.com/erigontech/erigon/pull/9175) hard-limit dirty pages · [`#6231`](https://github.com/erigontech/erigon/pull/6231) & [`erigon-lib#770`](https://github.com/ledgerwatch/erigon-lib/pull/770) expose `dirtySpace` · [`#1515`](https://github.com/erigontech/erigon/pull/1515) match LMDB dirty-list size · [`erigon-lib#582`](https://github.com/ledgerwatch/erigon-lib/pull/582) expose growth step.
- Engine migration: [`#2199`](https://github.com/erigontech/erigon/pull/2199) switch to `mdbx-go` module (−115k lines) · [`#5392`](https://github.com/erigontech/erigon/pull/5392) vendor libmdbx `.c` instead of submodule.

## 2. Memory: off-heap, mmap & madvise

- ⭐ [`erigon#20640`](https://github.com/erigontech/erigon/pull/20640) · 2026 — **Off-heap Elias-Fano build.** Building EF for 3 billion keys burned 3 GB of heap and OOM'd; moved construction off-heap.
  *Angle: "Off-heap data structures in Go to dodge the GC."*
- ⭐ [`erigon#21858`](https://github.com/erigontech/erigon/pull/21858) · 2026 — **Cut typed-transaction `Hash()` allocations** (no `[]any`, no reflection) after spotting a "GC stop-the-world spike" on Bloatnet — slice alloc + boxing removed.
  *Angle: "Chasing a GC stop-the-world spike to a `[]any` cast."*
- ⭐ [`erigon#20136`](https://github.com/erigontech/erigon/pull/20136) · 2026 — **Arena-based `MatchFinder` for the patricia trie.** The `node` struct (with an `any` field) was cache-unfriendly; arena allocation makes it compact.
- ⭐ [`erigon#21792`](https://github.com/erigontech/erigon/pull/21792) · 2026 — **Existence filter to `mmap` + `madv_will_need`.** With real throughput numbers (Storage-domain-on-mmap 33 tx/s vs all-in-mem 32 vs all-on-mmap 30).
  *Angle: "madvise as a tuning knob: when mmap beats RAM."*
- [`#1712`](https://github.com/erigontech/erigon/pull/1712) enable `MADV_RANDOM` · [`#21482`](https://github.com/erigontech/erigon/pull/21482) merge on a private `mmap` with `madv_sequential` · [`#21777`](https://github.com/erigontech/erigon/pull/21777) off-heap EF inside `.bt` build · [`#840`](https://github.com/erigontech/erigon/pull/840) cap mmap size (4 TB broke on Raspberry Pi).

## 3. ETL & external sorting

- ⭐ [`erigon#2352`](https://github.com/erigontech/erigon/pull/2352) · 2021 — **Enforce the "oldest appeared" property at load time** — the ETL collector must keep the first-seen value for a key regardless of buffer flushes (found by shrinking the buffer to 128 KB).
  *Angle: "External merge-sort as ETL: correctness when your buffer is smaller than your data."*
- ⭐ [`erigon#19848`](https://github.com/erigontech/erigon/pull/19848) · 2026 — **Track key insertion order to swap `SortStable` for `Sort`** — recovers stability cheaply, faster collector flush.
- ⭐ [`erigon#19780`](https://github.com/erigontech/erigon/pull/19780) · 2026 — **Zero-copy `memDataProvider`** (+736 lines), benchmarked under a 1 GB `MemoryMax` cgroup.
- [`#19996`](https://github.com/erigontech/erigon/pull/19996) pool of bufwriters · [`#19531`](https://github.com/erigontech/erigon/pull/19531) limit background sort to 1 goroutine/collector · [`erigon-lib#474`](https://github.com/ledgerwatch/erigon-lib/pull/474) configurable ETL limit · [`erigon-lib#307`](https://github.com/ledgerwatch/erigon-lib/pull/307) less-alloc recsplit ETL.

## 4. Parallelism & pipelines

- ⭐ [`erigon#19538`](https://github.com/erigontech/erigon/pull/19538) · 2026 — **Parallel RecSplit** (+467 lines): parallelize minimal-perfect-hash construction across buckets.
- ⭐ [`erigon#19944`](https://github.com/erigontech/erigon/pull/19944) · 2026 — **`PagedWriter`: fix the producer bottleneck** by moving page serialization off the producer goroutine — classic pipeline rebalancing.
- [`#19514`](https://github.com/erigontech/erigon/pull/19514) prepare recsplit for parallelism · [`#20281`](https://github.com/erigontech/erigon/pull/20281) unify `COMPRESS_WORKERS` for pagedWriter + compressor · [`#19677`](https://github.com/erigontech/erigon/pull/19677) worker presets · [`#8853`](https://github.com/erigontech/erigon/pull/8853)/[`#8892`](https://github.com/erigontech/erigon/pull/8892) minimize background build impact (1 goroutine by default).

## 5. Compression & encoding algorithms

- ⭐ [`erigon#19191`](https://github.com/erigontech/erigon/pull/19191) · 2026 — **Replace the C SA-IS lib with Go's `index/suffixarray`.** The C suffix-array builder did `malloc` syscalls hostile to the Go runtime; stdlib is GC-friendlier.
  *Angle: "Dropping C for Go's suffixarray in a dictionary compressor."*
- ⭐ [`erigon-lib#223`](https://github.com/ledgerwatch/erigon-lib/pull/223) / [`#234`](https://github.com/ledgerwatch/erigon-lib/pull/234) + [`erigon#3265`](https://github.com/erigontech/erigon/pull/3265) / [`#3211`](https://github.com/erigontech/erigon/pull/3211) — **Parallel dictionary compressor** (`ParallelCompressor`, `DecompressedFile`).
- ⭐ [`erigon#5130`](https://github.com/erigontech/erigon/pull/5130) · 2022 — **Condensed Huffman pattern tables** for the `.seg` codec.
- ⭐ [`erigon#14780`](https://github.com/erigontech/erigon/pull/14780) · 2025 — **Page-level compression for history files** (+756).
- ⭐ [`erigon#12951`](https://github.com/erigontech/erigon/pull/12951) · 2024 — **`d_lru`: cache decompressed values** (decompressing `CodeDomain` was ~7% of execution).
- ⭐ [`erigon#20567`](https://github.com/erigontech/erigon/pull/20567) · 2026 — **B-tree warmup reads key-only**, skipping value decompression.
- Per-domain: [`#11696`](https://github.com/erigontech/erigon/pull/11696) keys-compression for `commitment.kv` >64 steps · [`#11712`](https://github.com/erigontech/erigon/pull/11712) `storage.kv` · [`#18740`](https://github.com/erigontech/erigon/pull/18740) move compression `.Add()`→`.Compress()`.
- Decompressor: [`#3395`](https://github.com/erigontech/erigon/pull/3395) `WithReadAhead` · [`#3225`](https://github.com/erigontech/erigon/pull/3225) fast `Count()` · [`#7228`](https://github.com/erigontech/erigon/pull/7228) reject bad dicts · [`#4882`](https://github.com/erigontech/erigon/pull/4882) catch `maxDepth` underflow.
- ⭐ Historical: [`bolt#2`](https://github.com/ledgerwatch/bolt/pull/2) / [`bolt#11`](https://github.com/ledgerwatch/bolt/pull/11) — **key-prefix compression in `bolt`**, Erigon's original storage engine.

## 6. Indexing & minimal-perfect-hashing (RecSplit / Elias-Fano)

- ⭐ [`erigon#15960`](https://github.com/erigontech/erigon/pull/15960) · 2025 — **Internal existence filter based on `fuse_filter`** baked into `.efi`/`.kvi` files (bumps their major version).
  *Angle: "Fuse filters vs. Bloom: cheaper existence checks inside index files."*
- ⭐ [`erigon#3465`](https://github.com/erigontech/erigon/pull/3465) · 2022 — **Parallel transaction-index build** + recsplit offset-collector reset.
- [`#20566`](https://github.com/erigontech/erigon/pull/20566) `eliasfano32` `searchUpperReverse` off-by-one fix · backward-compat [`#16282`](https://github.com/erigontech/erigon/pull/16282)/[`#15986`](https://github.com/erigontech/erigon/pull/15986) · [`#16892`](https://github.com/erigontech/erigon/pull/16892) keep `fuse_filter` in app memory instead of mmap.

## 7. Bitmaps & inverted indices (logs, receipts, traces)

- ⭐ [`erigon#1124`](https://github.com/erigontech/erigon/pull/1124) · 2020-09 — **Bitmap indices for logs** — the original roaring-bitmap index for log/topic lookups.
  *Angle: "Roaring bitmaps for Ethereum log indexing."*
- ⭐ [`erigon#19995`](https://github.com/erigontech/erigon/pull/19995) · 2026 — **Replace a bitmap with a `u32` array in `collate`** — fewer allocs; even `bitmap32` allocated too much, worst case a 1.5 MB array.
  *Angle: "When a flat array beats a roaring bitmap."*
- [`#1159`](https://github.com/erigontech/erigon/pull/1159) history-style sharding for bitmap indices · [`#1165`](https://github.com/erigontech/erigon/pull/1165) switch to the Go roaring impl (Alpine) · [`#20396`](https://github.com/erigontech/erigon/pull/20396) standalone inverted-index slices → fixed-size arrays (LogAddr/LogTopic/TracesFrom/TracesTo).

## 8. On-disk / snapshot (`.seg`) formats & write amplification

- ⭐ [`erigon#3140`](https://github.com/erigontech/erigon/pull/3140) · 2021-12 — **Add word-count to `.seg`** (breaking snapshot-format change).
- ⭐ [`erigon-lib#355`](https://github.com/ledgerwatch/erigon-lib/pull/355) · 2022 — **Add `emptyWordsCount` to the `.seg` header** (breaking format).
- ⭐ [`erigon#7607`](https://github.com/erigontech/erigon/pull/7607) · 2023 — **`DumpBodies`: drop the dependency on `body.BaseTxNum`** — step toward storing canonical + non-canonical bodies in one table to cut write amplification.
- [`#19443`](https://github.com/erigontech/erigon/pull/19443) skip `.idt` when word-compression off · [`#3286`](https://github.com/erigontech/erigon/pull/3286) compressor allows empty words · [`#3558`](https://github.com/erigontech/erigon/pull/3558) block-snapshot merge.

## 9. Snapshot distribution: Downloader, BitTorrent & webseed

- ⭐ [`erigon#8176`](https://github.com/erigontech/erigon/pull/8176) · 2023-09 — **`--webseeds`**: augment BitTorrent snapshot distribution with HTTP web seeds.
  *Angle: "Distributing a multi-TB chain over BitTorrent + web seeds."*
- ⭐ [`erigon#8346`](https://github.com/erigontech/erigon/pull/8346) · 2023-10 — **Fetch `.torrent` files from a webseeds provider** (−591 lines) instead of bundling them.
- ⭐ [`erigon#17434`](https://github.com/erigontech/erigon/pull/17434) · 2025 — **Drop the MDBX store from the Downloader** (−273): simpler state, fewer moving parts.
- [`#4125`](https://github.com/erigontech/erigon/pull/4125) torrent mmap store · [`#14779`](https://github.com/erigontech/erigon/pull/14779) `torrent_create --all` by default · [`#17433`](https://github.com/erigontech/erigon/pull/17433) remove the `rclone` client.

## 10. Pruning, history retention & file merge

- ⭐ [`erigon#19914`](https://github.com/erigontech/erigon/pull/19914) · 2026 — **Prune via `Put(Current)` instead of `DelCurrent+Put`** (−342 lines) — a cheaper MDBX cursor primitive for the prune hot path.
- ⭐ [`erigon#19441`](https://github.com/erigontech/erigon/pull/19441) · 2026 — **Prioritize Domain merge over History merge** — merge History only when Domain has nothing left, minimizing Domain file count (block-exec only needs latest-state Domains).
  *Angle: "Merge scheduling: prioritizing the files the hot path reads."*
- [`#20321`](https://github.com/erigontech/erigon/pull/20321) `NO_DEEP_MERGE_HISTORY` · [`#8606`](https://github.com/erigontech/erigon/pull/8606) retire = prune→retire→prune · [`#19895`](https://github.com/erigontech/erigon/pull/19895) skip in-mem history accumulation for offline exec · [`#9781`](https://github.com/erigontech/erigon/pull/9781) committed prune batches (see §1).

## 11. Trie & commitment — state root / Hex Patricia

- ⭐ [`erigon#21789`](https://github.com/erigontech/erigon/pull/21789) · 2026 — **Skip the `GetLatest` lookup for new branch nodes** by passing `prevVal` (the metadata is already in the trie) — measurable exec speedup on Bloatnet.
  *Angle: "Incremental state-root: avoiding redundant commitment reads."*
- [`#20963`](https://github.com/erigontech/erigon/pull/20963) unify the commitment-branch referencing predicate · [`#13276`](https://github.com/erigontech/erigon/pull/13276) make `.kvi` the default commitment index · [`#20958`](https://github.com/erigontech/erigon/pull/20958) in-mem commitment existence filter · [`#17019`](https://github.com/erigontech/erigon/pull/17019) move commitment/changeset DB format out of `db/state`.

## 12. Erigon3 state model — txNum & domains

- ⭐ [`erigon#5176`](https://github.com/erigontech/erigon/pull/5176) · 2022-08 — **Erigon22: basic txNum model** — the transaction-number-indexed state model underpinning Erigon3.
  *Angle: "txNum: indexing chain state by transaction number, not block."*

## 13. KV streaming & remote DB (gRPC)

- ⭐ [`erigon#788`](https://github.com/erigontech/erigon/pull/788) · 2020-07 — **gRPC-based remote DB** — expose the embedded KV store over gRPC (origin of the remote-KV interface).
  *Angle: "A streaming gRPC interface over an embedded KV store."*
- ⭐ [`erigon#1909`](https://github.com/erigontech/erigon/pull/1909) · 2021 — **Reuse stateless cursors within a transaction** (reimplementing the old `TxDb` at the KV level).
- ⭐ [`erigon#20085`](https://github.com/erigontech/erigon/pull/20085) · 2026 — **`NewStreamFromPool`: zero-alloc** — pooled streams, no per-call closure.
- [`#14535`](https://github.com/erigontech/erigon/pull/14535) make streams safe against concurrent `RwTx` update/delete · [`#2786`](https://github.com/erigontech/erigon/pull/2786) don't close cursors at tx end (server cleans up).

## 14. Execution / EVM micro-architecture

- ⭐ [`erigon#20351`](https://github.com/erigontech/erigon/pull/20351) · 2026 — **Array-based EVM interpreter stack** — replace the slice/pointer stack with a fixed array.
  *Angle: "An array-based EVM stack."*
- [`#20372`](https://github.com/erigontech/erigon/pull/20372) index-based range over log topics (avoid copying 32-byte `common.Hash` each iteration) · see also `#21858` (typed-tx `Hash()` allocs, §2).

---

### Suggested first posts (highest-impact ⭐)

1. **`#3323` + `#1213`** — storage-engine limits: the 8 TB page-size ceiling and freelist reuse.
2. **`#20640` + `#21858` + `#20136`** — fighting the Go GC: off-heap Elias-Fano, killing a `[]any` cast, arena allocation.
3. **`#15960`** — fuse filters vs. Bloom inside index files.
4. **`#19191`** — replacing C with Go's suffixarray in the compressor.
5. **`#8176` + `#8346`** — distributing a multi-TB chain over BitTorrent + web seeds.
6. **`#5176`** — the txNum state model (Erigon3's core idea).
