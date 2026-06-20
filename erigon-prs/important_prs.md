# Erigon PR highlights — technical deep-dives

Curated from **6651 authored** + **7555 reviewed** PRs by [@AskAlexSharov](https://github.com/AskAlexSharov) across the `erigontech` and `ledgerwatch` orgs (10093 unique). **2225** flagged as deep technical decisions (algorithms, disk/database formats, isolation, DB guarantees).

> Heuristic curation from PR titles + labels — refine freely. Each PR is a candidate seed for a `pr_highligh`-tagged blog post.

## Storage engine (MDBX/LMDB)  (655)

- [`erigontech/erigon#21088`](https://github.com/erigontech/erigon/pull/21088) — execution/stagedsync, db/state: parallel-commitment correctness for reorg/unwind + SD recreate  
  <sub>2026-05-10 · merged · reviewed · score 17 · commit, commitment, parallel, reorg, stage, stagedsync</sub>
- [`erigontech/erigon#6426`](https://github.com/erigontech/erigon/pull/6426) — [wip] StagedSync: commit-no-sync - after unwind and after forward stages run  
  <sub>2022-12-24 · closed · authored · score 12 · commit, no-sync, stage, stagedsync, sync, unwind</sub>
- [`erigontech/erigon#20680`](https://github.com/erigontech/erigon/pull/20680) — integrity, stagedsync: cap state collation at block snapshots progress  
  <sub>2026-04-20 · merged · reviewed · score 11 · block snapshots, snapshot, snapshots, stage, stagedsync, state</sub>
- [`erigontech/erigon#19817`](https://github.com/erigontech/erigon/pull/19817) — state, stagedsync: split apply loop into state/index/commitment + decouple accumulator  
  <sub>2026-03-11 · merged · reviewed · score 11 · commit, commitment, index, stage, stagedsync, state</sub>
- [`erigontech/erigon#19712`](https://github.com/erigontech/erigon/pull/19712) — downloader: add torrents from disk after snapshot sync stage  
  <sub>2026-03-07 · merged · reviewed · score 11 · downloader, snapshot, snapshot sync, stage, sync, sync stage</sub>
- [`erigontech/erigon#19749`](https://github.com/erigontech/erigon/pull/19749) — execution/stagedsync: enable deferred commitment updates for parallel fork validation  
  <sub>2026-03-09 · merged · reviewed · score 10 · commit, commitment, parallel, stage, stagedsync, sync</sub>
- [`erigontech/erigon#11629`](https://github.com/erigontech/erigon/pull/11629) — stagedsync: fix astrid sync stage panic due to unintentionally committed tx  
  <sub>2024-08-15 · merged · reviewed · score 10 · commit, stage, stagedsync, sync, sync stage, tx </sub>
- [`erigontech/erigon#21826`](https://github.com/erigontech/erigon/pull/21826) — [r3.5] execution/stagedsync: prune in-RAM overlay when execution unwind is a disk no-op  
  <sub>2026-06-15 · merged · reviewed · score 9 · prune, stage, stagedsync, sync, unwind</sub>
- [`erigontech/erigon#21825`](https://github.com/erigontech/erigon/pull/21825) — execution/stagedsync: prune in-RAM overlay when execution unwind is a disk no-op  
  <sub>2026-06-15 · merged · reviewed · score 9 · prune, stage, stagedsync, sync, unwind</sub>
- [`erigontech/erigon#21824`](https://github.com/erigontech/erigon/pull/21824) — execution/stagedsync: prune in-RAM overlay when execution unwind is a disk no-op  
  <sub>2026-06-15 · merged · reviewed · score 9 · prune, stage, stagedsync, sync, unwind</sub>
- [`erigontech/erigon#21545`](https://github.com/erigontech/erigon/pull/21545) — db/snapshotsync: fix crash due to double close of decompressor   
  <sub>2026-06-01 · merged · reviewed · score 9 · compress, decompress, snapshot, snapshots, sync</sub>
- [`erigontech/erigon#21021`](https://github.com/erigontech/erigon/pull/21021) — prune, state, snapshotsync: bound commitment history retention by block count  
  <sub>2026-05-06 · open · reviewed · score 9 · commit, commitment, prune, snapshot, snapshots, state</sub>
- [`erigontech/erigon#20957`](https://github.com/erigontech/erigon/pull/20957) — db/state: commitment domain existence filter - flags to get it in-mem (now it's on mmap)  
  <sub>2026-05-03 · closed · authored · score 9 · commit, commitment, domain, mmap, state</sub>
- [`erigontech/erigon#9917`](https://github.com/erigontech/erigon/pull/9917) — release decompressor mmap on errors  
  <sub>2024-04-11 · merged · reviewed · score 9 · compress, decompress, mmap</sub>
- [`erigontech/erigon#6348`](https://github.com/erigontech/erigon/pull/6348) — StagedSync: break dependency to CurrentHeader. Always run non-initial cycle in 1 RwTx  
  <sub>2022-12-17 · merged · authored · score 9 · rwtx, stage, stagedsync, sync, tx </sub>
- [`erigontech/erigon#3465`](https://github.com/erigontech/erigon/pull/3465) — snapshot: parallel transaction index, recsplit: reset offset collector, etl: faster flush and load  
  <sub>2022-02-10 · merged · authored · score 9 · collector, flush, index, parallel, recsplit, snapshot</sub>
- [`erigontech/erigon#1433`](https://github.com/erigontech/erigon/pull/1433) — lmdb: move fsync inside commit (to avoid start next write transaction before previous fsync finished)  
  <sub>2021-01-03 · merged · authored · score 9 · commit, fsync, lmdb, sync, transaction</sub>
- [`erigontech/erigon#21200`](https://github.com/erigontech/erigon/pull/21200) — db/snapshotsync, kv/prune: skip downloading old commitment-history snapshots  
  <sub>2026-05-14 · open · reviewed · score 8 · commit, commitment, prune, snapshot, snapshots, sync</sub>
- [`erigontech/erigon#21157`](https://github.com/erigontech/erigon/pull/21157) — [r3.4] execution/stagedsync: find diffset by actually-executed hash on unwind  
  <sub>2026-05-13 · merged · reviewed · score 8 · stage, stagedsync, sync, unwind</sub>
- [`erigontech/erigon#18323`](https://github.com/erigontech/erigon/pull/18323) — Enabled page level compression for accounts history  
  <sub>2025-12-15 · merged · reviewed · score 8 · account, compress, compression, page</sub>
- [`erigontech/erigon#16781`](https://github.com/erigontech/erigon/pull/16781) — [r31] kv/mdbx: revert nosync periodic flusher  
  <sub>2025-08-22 · merged · authored · score 8 · flush, mdbx, nosync, sync</sub>
- [`erigontech/erigon#14229`](https://github.com/erigontech/erigon/pull/14229) — Goroutine for accurate periodic flush (in MDBX_SAFE_NOSYNC mode)  
  <sub>2025-03-19 · merged · reviewed · score 8 · flush, mdbx, nosync, sync</sub>
- [`erigontech/erigon#1521`](https://github.com/erigontech/erigon/pull/1521) — Fixes to unwind logic for the new staged sync  
  <sub>2021-02-27 · merged · reviewed · score 8 · stage, staged sync, sync, unwind</sub>
- [`erigontech/erigon#21662`](https://github.com/erigontech/erigon/pull/21662) — execution/stagedsync: fix receipt transaction index in serial execution  
  <sub>2026-06-07 · merged · reviewed · score 7 · index, stage, stagedsync, sync, transaction</sub>
- [`erigontech/erigon#21247`](https://github.com/erigontech/erigon/pull/21247) — execution/stagedsync, cmd/integration: clear canonical hash above snapshot tip on reset_state  
  <sub>2026-05-18 · merged · reviewed · score 7 · snapshot, stage, stagedsync, state, sync</sub>
- [`erigontech/erigon#21246`](https://github.com/erigontech/erigon/pull/21246) — [r3.4] cmd/integration, execution/stagedsync: clear canonical hash above snapshot tip on reset_state  
  <sub>2026-05-18 · merged · reviewed · score 7 · snapshot, stage, stagedsync, state, sync</sub>
- [`erigontech/erigon#21184`](https://github.com/erigontech/erigon/pull/21184) — [wip] stagedsync, stageloop, storage: informative assert messages for HasAgg type-assertion panics  
  <sub>2026-05-14 · closed · authored · score 7 · format, stage, stagedsync, storage, sync</sub>
- [`erigontech/erigon#20915`](https://github.com/erigontech/erigon/pull/20915) — execution/stagedsync, cmd/utils: --exec.no-prune now disables all DB pruning  
  <sub>2026-04-29 · merged · reviewed · score 7 · prune, pruning, stage, stagedsync, sync</sub>
- [`erigontech/erigon#20905`](https://github.com/erigontech/erigon/pull/20905) — [wip] db/state, stagedsync: add agg.WarmupDB() to pre-warm OS page cache  
  <sub>2026-04-29 · closed · authored · score 7 · page, stage, stagedsync, state, sync</sub>
- [`erigontech/erigon#20901`](https://github.com/erigontech/erigon/pull/20901) — [wip] db/state, stagedsync: add agg.WarmupDB() to pre-warm OS page cache  
  <sub>2026-04-29 · closed · authored · score 7 · page, stage, stagedsync, state, sync</sub>
- [`erigontech/erigon#19885`](https://github.com/erigontech/erigon/pull/19885) — state, stagedsync: enable deferred branch updates for parallel executor  
  <sub>2026-03-14 · merged · reviewed · score 7 · parallel, stage, stagedsync, state, sync</sub>
- [`erigontech/erigon#19583`](https://github.com/erigontech/erigon/pull/19583) — stagedsync: defer state files indexing on restart to reduce startup latency  
  <sub>2026-03-03 · merged · reviewed · score 7 · index, stage, stagedsync, state, sync</sub>
- [`erigontech/erigon#19539`](https://github.com/erigontech/erigon/pull/19539) — [wip] pageLevelCompression: move biz-logic of supporting `v0` files inside `NewPagedReader`   
  <sub>2026-03-01 · open · authored · score 7 · compress, compression, page</sub>
- [`erigontech/erigon#18795`](https://github.com/erigontech/erigon/pull/18795) — mdbx: env variables to disable fsync  
  <sub>2026-01-25 · merged · authored · score 7 · fsync, mdbx, sync</sub>
- [`erigontech/erigon#18740`](https://github.com/erigontech/erigon/pull/18740) — PageLevelCompression: move compression from .Add() method to .Compress()  
  <sub>2026-01-21 · merged · authored · score 7 · compress, compression, page</sub>
- [`erigontech/erigon#18738`](https://github.com/erigontech/erigon/pull/18738) — PageLevelCompression: move compression from .Add() method to .Compress()  
  <sub>2026-01-21 · closed · authored · score 7 · compress, compression, page</sub>
- [`erigontech/erigon#15043`](https://github.com/erigontech/erigon/pull/15043) — Fix a collection of downloader, snapshot sync and torrent related issues  
  <sub>2025-05-14 · merged · reviewed · score 7 · downloader, snapshot, snapshot sync, sync, torrent</sub>
- [`erigontech/erigon#14780`](https://github.com/erigontech/erigon/pull/14780) — [r30] history: page-level compression support  
  <sub>2025-04-28 · merged · authored · score 7 · compress, compression, page</sub>
- [`erigontech/erigon#14679`](https://github.com/erigontech/erigon/pull/14679) — history: page-level compression support  
  <sub>2025-04-21 · merged · authored · score 7 · compress, compression, page</sub>
- [`erigontech/erigon#14013`](https://github.com/erigontech/erigon/pull/14013) — eth/stagedsync: Fix UploaderPipelineStages function comment format  
  <sub>2025-02-28 · merged · reviewed · score 7 · format, pipeline, stage, stagedsync, sync</sub>
- [`erigontech/erigon#10293`](https://github.com/erigontech/erigon/pull/10293) — recsplit: allow pass NoFsync flag as config field   
  <sub>2024-05-13 · merged · authored · score 7 · fsync, recsplit, sync</sub>
- [`erigontech/erigon#9175`](https://github.com/erigontech/erigon/pull/9175) — e35: mdbx - to hard-limit dirty pages  
  <sub>2024-01-09 · merged · authored · score 7 · dirty pages, mdbx, page</sub>
- [`erigontech/erigon#3323`](https://github.com/erigontech/erigon/pull/3323) — Mdbx page size  
  <sub>2022-01-22 · merged · authored · score 7 · mdbx, page, page size</sub>
- [`erigontech/erigon#1213`](https://github.com/erigontech/erigon/pull/1213) — LMDB: don't search pages sequence in freelist if value is > X  
  <sub>2020-10-10 · merged · authored · score 7 · freelist, lmdb, page</sub>
- [`erigontech/mdbx-go#59`](https://github.com/erigontech/mdbx-go/pull/59) — fix for https://github.com/erthink/libmdbx/commit/d522069080a2aeb996c6442d74ad08475d8280f7  
  <sub>2022-03-27 · merged · authored · score 7 · commit, libmdbx, mdbx</sub>
- [`ledgerwatch/erigon-lib#356`](https://github.com/ledgerwatch/erigon-lib/pull/356) — kv: expose mdbx SafeNoSync and OptSyncPeriod options  
  <sub>2022-03-08 · merged · reviewed · score 7 · mdbx, nosync, sync</sub>
- [`erigontech/erigon#21706`](https://github.com/erigontech/erigon/pull/21706) — execution/stagedsync: recover CodePath alongside CodeHashPath in parallel normalizeWriteSet  
  <sub>2026-06-09 · open · reviewed · score 6 · parallel, stage, stagedsync, sync</sub>
- [`erigontech/erigon#21216`](https://github.com/erigontech/erigon/pull/21216) — execution/stagedsync: bump ChangeSets3 chain-tip prune limit  
  <sub>2026-05-15 · merged · reviewed · score 6 · prune, stage, stagedsync, sync</sub>
- [`erigontech/erigon#20865`](https://github.com/erigontech/erigon/pull/20865) — [wip] etl: pre-warm MDBX pages in FlushToDiskAsync goroutine  
  <sub>2026-04-28 · closed · authored · score 6 · flush, mdbx, page, sync</sub>
- [`erigontech/erigon#20716`](https://github.com/erigontech/erigon/pull/20716) — [r34] db/state: preserve per-step unwind entries so Flush reverts every orphan  
  <sub>2026-04-21 · merged · reviewed · score 6 · flush, state, trie, unwind</sub>
- [`erigontech/erigon#19877`](https://github.com/erigontech/erigon/pull/19877) — stagedsync: fix parallel executor deadlock in scheduleExecution  
  <sub>2026-03-13 · merged · reviewed · score 6 · parallel, stage, stagedsync, sync</sub>
- [`erigontech/erigon#19440`](https://github.com/erigontech/erigon/pull/19440) — Revert "[SharovBot] fix(history): correct .vi index page offset for V1 paged snapshot files"  
  <sub>2026-02-24 · merged · authored · score 6 · .vi, index, page, snapshot</sub>
- [`erigontech/erigon#19407`](https://github.com/erigontech/erigon/pull/19407) — stagedsync: defer E2 block indexing on restart to reduce startup latency  
  <sub>2026-02-22 · merged · reviewed · score 6 · index, stage, stagedsync, sync</sub>
- [`erigontech/erigon#18800`](https://github.com/erigontech/erigon/pull/18800) — execution/stagedsync: remove canPrune from serial_exec  
  <sub>2026-01-26 · merged · reviewed · score 6 · prune, stage, stagedsync, sync</sub>
- [`erigontech/erigon#18676`](https://github.com/erigontech/erigon/pull/18676) — execution/stagedsync: fix batch size loop break after change to always pass external tx and sd to loop  
  <sub>2026-01-15 · merged · reviewed · score 6 · stage, stagedsync, sync, tx </sub>
- [`erigontech/erigon#16110`](https://github.com/erigontech/erigon/pull/16110) — prune: switch back to commit with fsync  
  <sub>2025-07-15 · merged · authored · score 6 · commit, fsync, prune, sync</sub>
- [`erigontech/erigon#15937`](https://github.com/erigontech/erigon/pull/15937) — execution/stagedsync: add debug timing logs to exec prune steps  
  <sub>2025-07-04 · merged · reviewed · score 6 · prune, stage, stagedsync, sync</sub>
- [`erigontech/erigon#15923`](https://github.com/erigontech/erigon/pull/15923) — execution/stagedsync: add debug timing logs to exec prune steps  
  <sub>2025-07-03 · merged · reviewed · score 6 · prune, stage, stagedsync, sync</sub>
- [`erigontech/erigon#15098`](https://github.com/erigontech/erigon/pull/15098) — package `resetstate` to not import `stagedsync` package  
  <sub>2025-05-17 · merged · authored · score 6 · stage, stagedsync, state, sync</sub>
- [`erigontech/erigon#14086`](https://github.com/erigontech/erigon/pull/14086) — [wip] Why we even need txNum for statesyncTx? Yep. In RPC we needn't it.  
  <sub>2025-03-05 · closed · reviewed · score 6 · state, sync, txn, txnum</sub>
- [`erigontech/erigon#13800`](https://github.com/erigontech/erigon/pull/13800) — Set default MDBX geometry configuration on existing dirs  
  <sub>2025-02-13 · merged · reviewed · score 6 · geometry, mdbx</sub>
- [`erigontech/erigon#10019`](https://github.com/erigontech/erigon/pull/10019) — stagedSync: Optimize prune old chunks  
  <sub>2024-04-22 · merged · reviewed · score 6 · prune, stage, stagedsync, sync</sub>
- [`erigontech/erigon#9781`](https://github.com/erigontech/erigon/pull/9781) — e35: commit prune batch - to allow pages in FreeList re-use by next prune batch  
  <sub>2024-03-22 · merged · authored · score 6 · commit, freelist, page, prune</sub>
- [`erigontech/erigon#9169`](https://github.com/erigontech/erigon/pull/9169) — silkworm: libmdbx version check  
  <sub>2024-01-08 · merged · reviewed · score 6 · libmdbx, mdbx</sub>
- [`erigontech/erigon#8645`](https://github.com/erigontech/erigon/pull/8645) — added snapshot sync diagnostic information, updated diagnostic channel  
  <sub>2023-11-04 · merged · reviewed · score 6 · format, snapshot, snapshot sync, sync</sub>
- [`erigontech/erigon#7713`](https://github.com/erigontech/erigon/pull/7713) — StagedSync: fix canRunCycleInOneTransaction logic. User can see partial-writes   
  <sub>2023-06-12 · merged · authored · score 6 · stage, stagedsync, sync, transaction</sub>
- [`erigontech/erigon#7712`](https://github.com/erigontech/erigon/pull/7712) — StagedSync:  fix canRunCycleInOneTransaction logic  
  <sub>2023-06-12 · merged · authored · score 6 · stage, stagedsync, sync, transaction</sub>
- [`erigontech/erigon#6825`](https://github.com/erigontech/erigon/pull/6825) — Downloader: "incomplete" markers are more important than "complete", so commit them with fsync   
  <sub>2023-02-10 · merged · authored · score 6 · commit, downloader, fsync, sync</sub>
- [`erigontech/erigon#6231`](https://github.com/erigontech/erigon/pull/6231) — mdbx: expose dirtySpace option  
  <sub>2022-12-07 · merged · authored · score 6 · dirtyspace, mdbx</sub>
- [`erigontech/erigon#6222`](https://github.com/erigontech/erigon/pull/6222) — Exec new blocks in TxnNoSync. Prune after sending notifications in TxnSync  
  <sub>2022-12-07 · merged · authored · score 6 · nosync, prune, sync, txn</sub>
- [`erigontech/erigon#5392`](https://github.com/erigontech/erigon/pull/5392) — remove libmdbx git-submodule, make db-tools work on vendored to mdbx-go .c code (after "make dist")  
  <sub>2022-09-16 · merged · authored · score 6 · libmdbx, mdbx</sub>
- [`erigontech/erigon#3974`](https://github.com/erigontech/erigon/pull/3974) — Update libmdbx source  
  <sub>2022-04-26 · merged · reviewed · score 6 · libmdbx, mdbx</sub>
- [`erigontech/erigon#3894`](https://github.com/erigontech/erigon/pull/3894) — Change libmdbx submodule origin   
  <sub>2022-04-15 · merged · authored · score 6 · libmdbx, mdbx</sub>
- [`erigontech/erigon#3893`](https://github.com/erigontech/erigon/pull/3893) — Change libmdbx submodule origin  
  <sub>2022-04-15 · merged · authored · score 6 · libmdbx, mdbx</sub>
- [`erigontech/erigon#3650`](https://github.com/erigontech/erigon/pull/3650) — set libmdbx submodule to v0.11.5  
  <sub>2022-03-05 · merged · authored · score 6 · libmdbx, mdbx</sub>
- [`erigontech/erigon#3141`](https://github.com/erigontech/erigon/pull/3141) — Prevent use of new snapshots (no 'incremental snapshot sync' feature yet)   
  <sub>2021-12-17 · closed · authored · score 6 · snapshot, snapshot sync, snapshots, sync</sub>
- [`erigontech/erigon#2884`](https://github.com/erigontech/erigon/pull/2884) — HashState stage genesis sync - read PlainState only once  
  <sub>2021-10-28 · merged · reviewed · score 6 · plainstate, stage, state, sync</sub>
- [`erigontech/erigon#2199`](https://github.com/erigontech/erigon/pull/2199) — switch to mdbx-go module, and db-tools to libmdbx submodule  
  <sub>2021-06-19 · merged · authored · score 6 · libmdbx, mdbx</sub>
- [`erigontech/erigon#1919`](https://github.com/erigontech/erigon/pull/1919) — [wip] remove waitgroup from kv_lmdb and kv_mdbx  
  <sub>2021-05-12 · closed · authored · score 6 · lmdb, mdbx</sub>
- [`erigontech/erigon#1899`](https://github.com/erigontech/erigon/pull/1899) — Incremental staged sync for pruning  
  <sub>2021-05-07 · merged · reviewed · score 6 · pruning, stage, staged sync, sync</sub>
- [`erigontech/erigon#1897`](https://github.com/erigontech/erigon/pull/1897) — move staged sync to tx  
  <sub>2021-05-07 · merged · authored · score 6 · stage, staged sync, sync, tx </sub>
- [`erigontech/erigon#1558`](https://github.com/erigontech/erigon/pull/1558) — Align Cursor API with LMDB/MDBX  
  <sub>2021-03-19 · merged · reviewed · score 6 · lmdb, mdbx</sub>
- [`erigontech/erigon#1515`](https://github.com/erigontech/erigon/pull/1515) — mdbx: same dirty list size as lmdb  
  <sub>2021-02-25 · merged · authored · score 6 · lmdb, mdbx</sub>
- [`erigontech/erigon#1417`](https://github.com/erigontech/erigon/pull/1417) — State snapshot sync   
  <sub>2020-12-18 · merged · reviewed · score 6 · snapshot, snapshot sync, state, sync</sub>
- [`erigontech/mdbx-go#222`](https://github.com/erigontech/mdbx-go/pull/222) — Refresh README: erigontech path, libmdbx version badge, quickstart, sourcecraft links  
  <sub>2026-05-23 · merged · reviewed · score 6 · libmdbx, mdbx</sub>
- [`erigontech/mdbx-go#221`](https://github.com/erigontech/mdbx-go/pull/221) — mdbx: expose Refresh / Checkpoint / CommitEmbarkRead / Rollback / Amend / Clone txn APIs  
  <sub>2026-05-23 · merged · reviewed · score 6 · commit, mdbx, rollback, txn</sub>
- [`erigontech/mdbx-go#216`](https://github.com/erigontech/mdbx-go/pull/216) — Readers metrics and last master of libmdbx  
  <sub>2026-05-13 · merged · reviewed · score 6 · libmdbx, mdbx</sub>
- [`erigontech/mdbx-go#206`](https://github.com/erigontech/mdbx-go/pull/206) — [wip] libmdbx ci-devel branch  
  <sub>2026-02-07 · closed · authored · score 6 · libmdbx, mdbx</sub>
- [`erigontech/mdbx-go#185`](https://github.com/erigontech/mdbx-go/pull/185) — Update underlining libmdbx to v0.13.5.6.  
  <sub>2025-03-23 · merged · reviewed · score 6 · libmdbx, mdbx</sub>
- [`ledgerwatch/erigon-lib#883`](https://github.com/ledgerwatch/erigon-lib/pull/883) — Downloader: "incomplete" markers are more important than "complete", so commit them with fsync   
  <sub>2023-02-10 · merged · authored · score 6 · commit, downloader, fsync, sync</sub>
- [`ledgerwatch/erigon-lib#770`](https://github.com/ledgerwatch/erigon-lib/pull/770) — mdbx: dirtySpace option expose  
  <sub>2022-12-07 · merged · authored · score 6 · dirtyspace, mdbx</sub>
- [`ledgerwatch/erigon-lib#643`](https://github.com/ledgerwatch/erigon-lib/pull/643) — remove libmdbx git-submodule, make db-tools work on vendored to mdbx-go .c code (after "make dist") #5392  
  <sub>2022-09-16 · merged · authored · score 6 · libmdbx, mdbx</sub>
- [`ledgerwatch/erigon-lib#582`](https://github.com/ledgerwatch/erigon-lib/pull/582) — mdbx: expose growth step  
  <sub>2022-08-12 · merged · authored · score 6 · growth step, mdbx</sub>
- [`erigontech/erigon#21881`](https://github.com/erigontech/erigon/pull/21881) — execution/stagedsync: remove diaglib.Send calls  
  <sub>2026-06-18 · merged · authored · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#21792`](https://github.com/erigontech/erigon/pull/21792) — bloatnet: StorageDomain move existence filter to mmap+madv_will_need  
  <sub>2026-06-13 · merged · authored · score 5 · domain, mmap, storage</sub>
- [`erigontech/erigon#21373`](https://github.com/erigontech/erigon/pull/21373) — execution/stagedsync: tests for finalize coinbase/burnt fee write invalidation  
  <sub>2026-05-22 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#21212`](https://github.com/erigontech/erigon/pull/21212) — execution/stagedsync: extract minIBS post-apply path into a dedicated method  
  <sub>2026-05-15 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#21210`](https://github.com/erigontech/erigon/pull/21210) — cmd/integration, execution/stagedsync: fix from-0 flow (env-prefix + reset-progress-delete)  
  <sub>2026-05-15 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#20496`](https://github.com/erigontech/erigon/pull/20496) — [r3.4] stagedsync: generate changesets near tip even during initialCycle  
  <sub>2026-04-11 · merged · authored · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#20495`](https://github.com/erigontech/erigon/pull/20495) — stagedsync: generate changesets near tip even during initialCycle  
  <sub>2026-04-11 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#20461`](https://github.com/erigontech/erigon/pull/20461) — [r3.4] db/state: return DomainRoTx IndexReaders to sync.Pool on Close  
  <sub>2026-04-10 · merged · authored · score 5 · domain, index, state, sync, tx </sub>
- [`erigontech/erigon#20458`](https://github.com/erigontech/erigon/pull/20458) — [wip] [r3.4] protocol, stagedsync: count EIP-7002/7251 finalize syscall gas in block gas  
  <sub>2026-04-10 · closed · authored · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#20208`](https://github.com/erigontech/erigon/pull/20208) — commitment: move cleanup to Release() for safer sync.Pool reuse  
  <sub>2026-03-27 · merged · reviewed · score 5 · commit, commitment, sync</sub>
- [`erigontech/erigon#20048`](https://github.com/erigontech/erigon/pull/20048) — [SharovBot] [r3.4] db/kv/mdbx: fix deadlock in async tx channel on context cancellation  
  <sub>2026-03-21 · merged · reviewed · score 5 · mdbx, sync, tx </sub>
- [`erigontech/erigon#19856`](https://github.com/erigontech/erigon/pull/19856) — db/kv/mdbx: fix deadlock in async tx channel on context cancellation  
  <sub>2026-03-12 · merged · reviewed · score 5 · mdbx, sync, tx </sub>
- [`erigontech/erigon#19503`](https://github.com/erigontech/erigon/pull/19503) — PagedWriter: parallel compress  
  <sub>2026-02-26 · merged · authored · score 5 · compress, page, parallel</sub>
- [`erigontech/erigon#19002`](https://github.com/erigontech/erigon/pull/19002) — execution/stagedsync: remove unused args in stageloop hooks  
  <sub>2026-02-06 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#18773`](https://github.com/erigontech/erigon/pull/18773) — execution/stagedsync: cleanup unused code in stages  
  <sub>2026-01-23 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#18733`](https://github.com/erigontech/erigon/pull/18733) — [r33] execution/stagedsync: port --experimental.always-generate-changesets flag for gas repricing benchmarks  
  <sub>2026-01-21 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#18611`](https://github.com/erigontech/erigon/pull/18611) — refactor(stagedsync): remove unused trace constant  
  <sub>2026-01-09 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#18532`](https://github.com/erigontech/erigon/pull/18532) — Erigon: fix collectors with allocators wherever asyncDiskDump=true and tweaked the small ETL buffer as it can only be good   
  <sub>2026-01-02 · closed · reviewed · score 5 · collector, etl , sync</sub>
- [`erigontech/erigon#18354`](https://github.com/erigontech/erigon/pull/18354) — Performance: Commitment asyncronous warmup  
  <sub>2025-12-17 · merged · reviewed · score 5 · commit, commitment, sync</sub>
- [`erigontech/erigon#16653`](https://github.com/erigontech/erigon/pull/16653) — Torrent disk flushing and webseed requesting optimizations  
  <sub>2025-08-15 · merged · reviewed · score 5 · flush, torrent, webseed</sub>
- [`erigontech/erigon#16484`](https://github.com/erigontech/erigon/pull/16484) — execution/stagedsync: handle sync loop block limit exhaustion (#16268)  
  <sub>2025-08-07 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#16268`](https://github.com/erigontech/erigon/pull/16268) — execution/stagedsync: handle sync loop block limit exhaustion  
  <sub>2025-07-24 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#16137`](https://github.com/erigontech/erigon/pull/16137) — execution/stagedsync: measure time spent in initial cycle  
  <sub>2025-07-16 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#16127`](https://github.com/erigontech/erigon/pull/16127) — execution/stagedsync: add stage metrics  
  <sub>2025-07-15 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#16056`](https://github.com/erigontech/erigon/pull/16056) — Fix broken file paths in stagedsync docs  
  <sub>2025-07-11 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#15454`](https://github.com/erigontech/erigon/pull/15454) — sd: try remove Commitment calc from Flush: take 2  
  <sub>2025-06-04 · merged · reviewed · score 5 · commit, commitment, flush</sub>
- [`erigontech/erigon#15408`](https://github.com/erigontech/erigon/pull/15408) — Revert "sd: try remove Commitment calc from Flush (#15318)"  
  <sub>2025-06-02 · merged · reviewed · score 5 · commit, commitment, flush</sub>
- [`erigontech/erigon#15318`](https://github.com/erigontech/erigon/pull/15318) — sd: try remove Commitment calc from Flush  
  <sub>2025-05-29 · merged · authored · score 5 · commit, commitment, flush</sub>
- [`erigontech/erigon#12717`](https://github.com/erigontech/erigon/pull/12717) — stagedsync: add periodic progress logs for long prunning during initial sync  
  <sub>2024-11-13 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#12550`](https://github.com/erigontech/erigon/pull/12550) — stagedsync: revert Sync.Run return error on bad block  
  <sub>2024-10-30 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#12503`](https://github.com/erigontech/erigon/pull/12503) — [wip] prune: no fsync  
  <sub>2024-10-26 · closed · authored · score 5 · fsync, prune, sync</sub>
- [`erigontech/erigon#12082`](https://github.com/erigontech/erigon/pull/12082) — linter recommendations for stagedsync README  
  <sub>2024-09-24 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#11637`](https://github.com/erigontech/erigon/pull/11637) — Prune still affecting chain-tip "fsync"  
  <sub>2024-08-16 · merged · authored · score 5 · fsync, prune, sync</sub>
- [`erigontech/erigon#11495`](https://github.com/erigontech/erigon/pull/11495) — stagedsync: Fix nil panic on custom chains  
  <sub>2024-08-05 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#11402`](https://github.com/erigontech/erigon/pull/11402) — stagedsync: remove loopBreakCheck  
  <sub>2024-07-30 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#11133`](https://github.com/erigontech/erigon/pull/11133) — Call UnwindTo with tx instead of nil in sync_test.go  
  <sub>2024-07-12 · merged · reviewed · score 5 · sync, tx , unwind</sub>
- [`erigontech/erigon#10266`](https://github.com/erigontech/erigon/pull/10266) — E35: Fix MDBX_FULL_TXN on pruning  
  <sub>2024-05-09 · closed · reviewed · score 5 · mdbx, pruning, txn</sub>
- [`erigontech/erigon#10064`](https://github.com/erigontech/erigon/pull/10064) — downloader: remove deprecated manual fsync   
  <sub>2024-04-25 · merged · authored · score 5 · downloader, fsync, sync</sub>
- [`erigontech/erigon#9993`](https://github.com/erigontech/erigon/pull/9993) — downloader: dedicated fsyncDB() func - for clarity and docs  
  <sub>2024-04-19 · closed · authored · score 5 · downloader, fsync, sync</sub>
- [`erigontech/erigon#9907`](https://github.com/erigontech/erigon/pull/9907) — Updating sync stages metrics along with DB update  
  <sub>2024-04-10 · merged · reviewed · score 5 · stage, sync, sync stage</sub>
- [`erigontech/erigon#8141`](https://github.com/erigontech/erigon/pull/8141) — txpool: switch db to durable mode - with fsync outside of pool's global lock  
  <sub>2023-09-06 · merged · authored · score 5 · durable, fsync, sync</sub>
- [`erigontech/erigon#8140`](https://github.com/erigontech/erigon/pull/8140) — txpool: switch db to durable mode - with fsync outside of pool's global lock  
  <sub>2023-09-06 · closed · authored · score 5 · durable, fsync, sync</sub>
- [`erigontech/erigon#8139`](https://github.com/erigontech/erigon/pull/8139) — txpool: switch db to durable mode - with fsync outside of pool's global lock  
  <sub>2023-09-06 · closed · authored · score 5 · durable, fsync, sync</sub>
- [`erigontech/erigon#6693`](https://github.com/erigontech/erigon/pull/6693) — allow enable snapshot sync by cli flag  
  <sub>2023-01-25 · merged · authored · score 5 · snapshot, snapshot sync, sync</sub>
- [`erigontech/erigon#6349`](https://github.com/erigontech/erigon/pull/6349) — [wip] unwind in own no_sync txn  
  <sub>2022-12-17 · closed · authored · score 5 · sync, txn, unwind</sub>
- [`erigontech/erigon#5740`](https://github.com/erigontech/erigon/pull/5740) — add more sync stages to metrics  
  <sub>2022-10-14 · merged · reviewed · score 5 · stage, sync, sync stage</sub>
- [`erigontech/erigon#5425`](https://github.com/erigontech/erigon/pull/5425) — exec22: stagedsync test v1  
  <sub>2022-09-19 · merged · authored · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#4700`](https://github.com/erigontech/erigon/pull/4700) — Torrent: add fsync after piece download  
  <sub>2022-07-13 · merged · authored · score 5 · fsync, sync, torrent</sub>
- [`erigontech/erigon#3923`](https://github.com/erigontech/erigon/pull/3923) — Downloader tables, mdbx-based torrent pieces completion store   
  <sub>2022-04-21 · merged · authored · score 5 · downloader, mdbx, torrent</sub>
- [`erigontech/erigon#2486`](https://github.com/erigontech/erigon/pull/2486) — Update stagedsync readme to show all current stages  
  <sub>2021-08-03 · merged · reviewed · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#2445`](https://github.com/erigontech/erigon/pull/2445) — staged syncs automatically add error prefix about stage number and name  
  <sub>2021-07-26 · merged · authored · score 5 · stage, staged sync, sync</sub>
- [`erigontech/erigon#2336`](https://github.com/erigontech/erigon/pull/2336) — simplify staged sync world  
  <sub>2021-07-10 · merged · authored · score 5 · stage, staged sync, sync</sub>
- [`erigontech/erigon#2317`](https://github.com/erigontech/erigon/pull/2317) — Remove some parameters from stagedsync.Prepare  
  <sub>2021-07-08 · merged · authored · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#2196`](https://github.com/erigontech/erigon/pull/2196) — remove some unused stagedsync params  
  <sub>2021-06-19 · merged · authored · score 5 · stage, stagedsync, sync</sub>
- [`erigontech/erigon#1971`](https://github.com/erigontech/erigon/pull/1971) — better support for mdbx in snapshots  
  <sub>2021-05-20 · merged · authored · score 5 · mdbx, snapshot, snapshots</sub>
- [`erigontech/erigon#1322`](https://github.com/erigontech/erigon/pull/1322) — App code can specify TX flag to don't call FSync  
  <sub>2020-10-30 · merged · authored · score 5 · fsync, sync, tx </sub>
- [`erigontech/erigon#945`](https://github.com/erigontech/erigon/pull/945) — sub-transaction to not call fsync, sub-transactions to not call runtime.LockThread()  
  <sub>2020-08-20 · merged · authored · score 5 · fsync, sync, transaction</sub>
- [`ledgerwatch/erigon-lib#1109`](https://github.com/ledgerwatch/erigon-lib/pull/1109) — txpool: switch db to durable mode - with fsync outside of pool's global lock  
  <sub>2023-09-06 · merged · authored · score 5 · durable, fsync, sync</sub>
- [`ledgerwatch/erigon-lib#1108`](https://github.com/ledgerwatch/erigon-lib/pull/1108) — txpool: switch db to durable mode - with fsync outside of pool's global lock  
  <sub>2023-09-06 · closed · authored · score 5 · durable, fsync, sync</sub>
- [`ledgerwatch/erigon-lib#310`](https://github.com/ledgerwatch/erigon-lib/pull/310) — recsplit: reset offset collector, etl: faster flush and load   
  <sub>2022-02-10 · merged · authored · score 5 · collector, flush, recsplit</sub>
- [`erigontech/erigon#21873`](https://github.com/erigontech/erigon/pull/21873) — snapshotsync: prune blocks in one PruneBlocks call per cycle (#21861)  
  <sub>2026-06-18 · merged · authored · score 4 · prune, snapshot, snapshots, sync</sub>
- [`erigontech/erigon#21861`](https://github.com/erigontech/erigon/pull/21861) — db/rawdb, snapshotsync: cut cursor & per-block allocs in PruneBlocks  
  <sub>2026-06-17 · merged · authored · score 4 · prune, snapshot, snapshots, sync</sub>
- [`erigontech/erigon#21776`](https://github.com/erigontech/erigon/pull/21776) — domain: allow per-domain configuration of "existence filter on mmap"  
  <sub>2026-06-13 · merged · authored · score 4 · domain, mmap</sub>
- [`erigontech/erigon#21571`](https://github.com/erigontech/erigon/pull/21571) — db/snapshotsync: make index building and opening segments safe with other files building events  
  <sub>2026-06-02 · merged · reviewed · score 4 · index, snapshot, snapshots, sync</sub>
- [`erigontech/erigon#21482`](https://github.com/erigontech/erigon/pull/21482) — experiment: merge on own `mmap` with `madv_sequential`  
  <sub>2026-05-28 · merged · authored · score 4 · merge, mmap</sub>
- [`erigontech/erigon#21266`](https://github.com/erigontech/erigon/pull/21266) — cmd/evm: speedup statetest by setting up 1 mdbx env per file  
  <sub>2026-05-19 · merged · reviewed · score 4 · mdbx, state</sub>
- [`erigontech/erigon#20798`](https://github.com/erigontech/erigon/pull/20798) — p2p/protocols/wit, p2p/sentry: validate WitnessPageResponse fields  
  <sub>2026-04-24 · merged · reviewed · score 4 · page, witness</sub>
- [`erigontech/erigon#20643`](https://github.com/erigontech/erigon/pull/20643) — revert: prune: use `Put(Current)` mdbx's method instead of `DelCurrent+Put`  
  <sub>2026-04-18 · merged · authored · score 4 · mdbx, prune</sub>
- [`erigontech/erigon#20281`](https://github.com/erigontech/erigon/pull/20281) — pagedWriter and compressor to use same `COMPRESS_WORKERS` variable and configuration field in `agg`  
  <sub>2026-04-02 · merged · authored · score 4 · compress, page</sub>
- [`erigontech/erigon#20233`](https://github.com/erigontech/erigon/pull/20233) — [WIP] execution/execmodule: fix long-running ro tx in forkchoice causing mdbx growth  
  <sub>2026-03-30 · closed · reviewed · score 4 · mdbx, tx </sub>
- [`erigontech/erigon#19967`](https://github.com/erigontech/erigon/pull/19967) — [wip] experiment: merge on own `mmap` with `madv_sequential`  
  <sub>2026-03-18 · closed · authored · score 4 · merge, mmap</sub>
- [`erigontech/erigon#19914`](https://github.com/erigontech/erigon/pull/19914) — prune: use Put(Current) mdbx's method instead of DelCurrent+Put  
  <sub>2026-03-16 · merged · authored · score 4 · mdbx, prune</sub>
- [`erigontech/erigon#19697`](https://github.com/erigontech/erigon/pull/19697) — [release/3.4] fix(history): reset page counter on recsplit collision retry in buildVI  
  <sub>2026-03-06 · merged · reviewed · score 4 · page, recsplit</sub>
- [`erigontech/erigon#19695`](https://github.com/erigontech/erigon/pull/19695) — fix(history): reset page counter on recsplit collision retry in buildVI  
  <sub>2026-03-06 · merged · reviewed · score 4 · page, recsplit</sub>
- [`erigontech/erigon#19439`](https://github.com/erigontech/erigon/pull/19439) — [wip] merge: enable read-ahead by own `mmap` area + `madvise_`  
  <sub>2026-02-24 · closed · authored · score 4 · merge, mmap</sub>
- [`erigontech/erigon#19382`](https://github.com/erigontech/erigon/pull/19382) — [SharovBot] fix: reduce genesis MDBX map size on Windows to prevent pagefile exhaustion  
  <sub>2026-02-21 · merged · reviewed · score 4 · mdbx, page</sub>
- [`erigontech/erigon#18788`](https://github.com/erigontech/erigon/pull/18788) — prune: remove early-exit based on DirtySpace()   
  <sub>2026-01-24 · merged · authored · score 4 · dirtyspace, prune</sub>
- [`erigontech/erigon#18787`](https://github.com/erigontech/erigon/pull/18787) — prune: remove early-exit based on DirtySpace()  
  <sub>2026-01-24 · merged · authored · score 4 · dirtyspace, prune</sub>
- [`erigontech/erigon#18313`](https://github.com/erigontech/erigon/pull/18313) — db/snapshotsync: remove unused logging and parameters from Merger  
  <sub>2025-12-15 · closed · reviewed · score 4 · merge, snapshot, snapshots, sync</sub>
- [`erigontech/erigon#17434`](https://github.com/erigontech/erigon/pull/17434) — downloader: drop mdbx store  
  <sub>2025-10-13 · merged · authored · score 4 · downloader, mdbx</sub>
- [`erigontech/erigon#16849`](https://github.com/erigontech/erigon/pull/16849) — move `TotalMemory` method from `mmap` to `estimate` package. merge `debug` to `dbg` package  
  <sub>2025-08-27 · merged · authored · score 4 · merge, mmap</sub>
- [`erigontech/erigon#16627`](https://github.com/erigontech/erigon/pull/16627) — skip SnapshotSync in --no-downloader mode   
  <sub>2025-08-14 · merged · reviewed · score 4 · downloader, snapshot, snapshots, sync</sub>
- [`erigontech/erigon#16626`](https://github.com/erigontech/erigon/pull/16626) — skip SnapshotSync in `--no-downloader` mode  
  <sub>2025-08-14 · merged · reviewed · score 4 · downloader, snapshot, snapshots, sync</sub>
- [`erigontech/erigon#16436`](https://github.com/erigontech/erigon/pull/16436) — [wip] page-level compress experiment for .kv files   
  <sub>2025-08-04 · closed · authored · score 4 · compress, page</sub>
- [`erigontech/erigon#15749`](https://github.com/erigontech/erigon/pull/15749) — E3: remove `fixCanonicalChain` + noSync  
  <sub>2025-06-25 · merged · reviewed · score 4 · nosync, sync</sub>
- [`erigontech/erigon#15742`](https://github.com/erigontech/erigon/pull/15742) — [wip] page-level compress experiment for .kv files    
  <sub>2025-06-25 · closed · authored · score 4 · compress, page</sub>
- [`erigontech/erigon#15575`](https://github.com/erigontech/erigon/pull/15575) — E3: Use unbounded MDBX for Engine downloader  
  <sub>2025-06-14 · merged · reviewed · score 4 · downloader, mdbx</sub>
- [`erigontech/erigon#14261`](https://github.com/erigontech/erigon/pull/14261) — Prevent deadlock when shutting down mdbx flusher  
  <sub>2025-03-22 · merged · reviewed · score 4 · flush, mdbx</sub>
- [`erigontech/erigon#14244`](https://github.com/erigontech/erigon/pull/14244) — Force mdbx sync  
  <sub>2025-03-20 · merged · reviewed · score 4 · mdbx, sync</sub>
- [`erigontech/erigon#13952`](https://github.com/erigontech/erigon/pull/13952) — rpcdaemon: Set correct log index on state sync transactions  
  <sub>2025-02-25 · merged · reviewed · score 4 · index, state, sync, transaction</sub>
- [`erigontech/erigon#13545`](https://github.com/erigontech/erigon/pull/13545) — nodedb: use SafeNoSync   
  <sub>2025-01-24 · merged · authored · score 4 · nosync, sync</sub>
- [`erigontech/erigon#13541`](https://github.com/erigontech/erigon/pull/13541) — revert SafeNoSync  
  <sub>2025-01-23 · merged · reviewed · score 4 · nosync, sync</sub>
- [`erigontech/erigon#12770`](https://github.com/erigontech/erigon/pull/12770) — stage_txn_lookup: don't grind all blocks at initial sync   
  <sub>2024-11-19 · merged · authored · score 4 · lookup, stage, sync, txn</sub>
- [`erigontech/erigon#11819`](https://github.com/erigontech/erigon/pull/11819) — Erigon 3: Fix occassional need for reorgs (during first sync in polygon) through a "safety" threshold  
  <sub>2024-09-01 · merged · reviewed · score 4 · reorg, sync</sub>
- [`erigontech/erigon#11540`](https://github.com/erigontech/erigon/pull/11540) — Ottersync: make --all flag to seed .idx, .vi, etc...  
  <sub>2024-08-08 · merged · reviewed · score 4 · .vi, sync</sub>
- [`erigontech/erigon#11244`](https://github.com/erigontech/erigon/pull/11244) — force fsync after notifications sent  
  <sub>2024-07-20 · merged · authored+reviewed · score 4 · fsync, sync</sub>
- [`erigontech/erigon#11200`](https://github.com/erigontech/erigon/pull/11200) — pool: do fsync by non-empty update (e2)  
  <sub>2024-07-17 · merged · authored · score 4 · fsync, sync</sub>
- [`erigontech/erigon#11198`](https://github.com/erigontech/erigon/pull/11198) — pool: do fsync by non-empty update (e3)  
  <sub>2024-07-17 · merged · authored · score 4 · fsync, sync</sub>
- [`erigontech/erigon#10882`](https://github.com/erigontech/erigon/pull/10882) — mdbx: use native removed cursors from MdbxTx  
  <sub>2024-06-24 · closed · reviewed · score 4 · mdbx, tx </sub>
- [`erigontech/erigon#10341`](https://github.com/erigontech/erigon/pull/10341) — Respect the sync limit of blocks insertion when inserting in MDBX.  
  <sub>2024-05-14 · merged · reviewed · score 4 · mdbx, sync</sub>
- [`erigontech/erigon#10227`](https://github.com/erigontech/erigon/pull/10227) — readme: change page size  
  <sub>2024-05-07 · merged · authored · score 4 · page, page size</sub>
- [`erigontech/erigon#10113`](https://github.com/erigontech/erigon/pull/10113) — mdbx: pre-open read pagesize from db  
  <sub>2024-04-29 · merged · authored · score 4 · mdbx, page</sub>
- [`erigontech/erigon#10074`](https://github.com/erigontech/erigon/pull/10074) — downloader: docs on MMAP for data-files r/w and experiments with bufio  
  <sub>2024-04-26 · merged · authored · score 4 · downloader, mmap</sub>
- [`erigontech/erigon#9994`](https://github.com/erigontech/erigon/pull/9994) — dedicated fsyncDB() func - for clarity and docs  
  <sub>2024-04-19 · merged · authored · score 4 · fsync, sync</sub>
- [`erigontech/erigon#9585`](https://github.com/erigontech/erigon/pull/9585) — downloader: --verify to not use mmap. add more concurrency  
  <sub>2024-03-05 · merged · authored · score 4 · downloader, mmap</sub>
- [`erigontech/erigon#9582`](https://github.com/erigontech/erigon/pull/9582) — downloader: --verify to not use mmap. add more concurrency.   
  <sub>2024-03-05 · merged · authored · score 4 · downloader, mmap</sub>
- [`erigontech/erigon#9178`](https://github.com/erigontech/erigon/pull/9178) — mdbx: hard dirtyPages limit   
  <sub>2024-01-09 · merged · authored · score 4 · mdbx, page</sub>
- [`erigontech/erigon#8492`](https://github.com/erigontech/erigon/pull/8492) — mdbx: add lable to commit error  
  <sub>2023-10-16 · merged · authored · score 4 · commit, mdbx</sub>
- [`erigontech/erigon#7872`](https://github.com/erigontech/erigon/pull/7872) — fsync: don't skip error, ability to disable in tests  
  <sub>2023-07-11 · merged · authored · score 4 · fsync, sync</sub>
- [`erigontech/erigon#6457`](https://github.com/erigontech/erigon/pull/6457) — bsc: incrementally calc and store all old snapshots. slower initial stage_snapshots, but faster restart during initial sync  
  <sub>2022-12-28 · merged · authored · score 4 · snapshot, snapshots, stage, sync</sub>
- [`erigontech/erigon#6350`](https://github.com/erigontech/erigon/pull/6350) — mdbx: relax a bit merge limit (still leave it stronger than default)   
  <sub>2022-12-17 · merged · authored · score 4 · mdbx, merge</sub>
- [`erigontech/erigon#6225`](https://github.com/erigontech/erigon/pull/6225) — mdbx bindings: remove txn.RawRead field #769  
  <sub>2022-12-07 · merged · authored · score 4 · mdbx, txn</sub>
- [`erigontech/erigon#6221`](https://github.com/erigontech/erigon/pull/6221) — mdbx: add BeginRwAsync method  
  <sub>2022-12-07 · merged · authored · score 4 · mdbx, sync</sub>
- [`erigontech/erigon#6057`](https://github.com/erigontech/erigon/pull/6057) — mdbx: configure merge threshold  
  <sub>2022-11-16 · merged · authored · score 4 · mdbx, merge</sub>
- [`erigontech/erigon#5379`](https://github.com/erigontech/erigon/pull/5379) — cleaned up storage and retrieval of state sync receipts  
  <sub>2022-09-15 · merged · reviewed · score 4 · state, storage, sync, trie</sub>
- [`erigontech/erigon#4858`](https://github.com/erigontech/erigon/pull/4858) — parity_listStorageKeys: *mdbx.MdbxCursor is not kv.CursorDupSort  
  <sub>2022-07-29 · merged · authored · score 4 · mdbx, storage</sub>
- [`erigontech/erigon#4743`](https://github.com/erigontech/erigon/pull/4743) — mdbx: use OS pagesize by default (but > 4Kb, and < 64Kb)  
  <sub>2022-07-19 · merged · authored · score 4 · mdbx, page</sub>
- [`erigontech/erigon#4378`](https://github.com/erigontech/erigon/pull/4378) — StageSenders: wrong canonical array size at initial sync with snapshots  
  <sub>2022-06-06 · merged · authored · score 4 · snapshot, snapshots, stage, sync</sub>
- [`erigontech/erigon#4247`](https://github.com/erigontech/erigon/pull/4247) — kv_mdbx: atomic closed flag #464  
  <sub>2022-05-24 · merged · authored · score 4 · atomic, mdbx</sub>
- [`erigontech/erigon#4125`](https://github.com/erigontech/erigon/pull/4125) — Torrent: mmap store  
  <sub>2022-05-12 · merged · authored · score 4 · mmap, torrent</sub>
- [`erigontech/erigon#4124`](https://github.com/erigontech/erigon/pull/4124) — Torrent: mmap store  
  <sub>2022-05-12 · merged · authored · score 4 · mmap, torrent</sub>
- [`erigontech/erigon#4123`](https://github.com/erigontech/erigon/pull/4123) — Torrent: mmap store  
  <sub>2022-05-12 · merged · authored · score 4 · mmap, torrent</sub>
- [`erigontech/erigon#3230`](https://github.com/erigontech/erigon/pull/3230) — mdbx: fix gc "retry" issue (slowness of gc during commit)  
  <sub>2022-01-10 · merged · authored · score 4 · commit, mdbx</sub>
- [`erigontech/erigon#3229`](https://github.com/erigontech/erigon/pull/3229) — mdbx: fix gc "retry" issue (slowness of gc during commit)  
  <sub>2022-01-10 · merged · authored · score 4 · commit, mdbx</sub>
- [`erigontech/erigon#2862`](https://github.com/erigontech/erigon/pull/2862) — force some rw tx when db open, to allow mdbx up version signature   
  <sub>2021-10-22 · merged · authored · score 4 · mdbx, tx </sub>
- [`erigontech/erigon#2146`](https://github.com/erigontech/erigon/pull/2146) — remove lmdb from hack, integration, state packages. remove lmdb dbtools  
  <sub>2021-06-11 · merged · authored · score 4 · lmdb, state</sub>
- [`erigontech/erigon#2019`](https://github.com/erigontech/erigon/pull/2019) — Up db schema for mdbx (for all) and up kv version: to 2.0.0  
  <sub>2021-05-26 · merged · authored · score 4 · mdbx, schema</sub>
- [`erigontech/erigon#1891`](https://github.com/erigontech/erigon/pull/1891) — Mdbx tx limit metric  
  <sub>2021-05-06 · merged · authored · score 4 · mdbx, tx </sub>
- [`erigontech/erigon#1885`](https://github.com/erigontech/erigon/pull/1885) — Mdbx page ops metrics  
  <sub>2021-05-06 · merged · authored · score 4 · mdbx, page</sub>
- [`erigontech/erigon#1579`](https://github.com/erigontech/erigon/pull/1579) — MDBX bindings: remove finalizers (write tx require to be closed from same thread)  
  <sub>2021-03-21 · merged · authored · score 4 · mdbx, tx </sub>
- [`erigontech/erigon#1488`](https://github.com/erigontech/erigon/pull/1488) — return nested transactions to mdbx bindings  
  <sub>2021-02-11 · merged · authored · score 4 · mdbx, transaction</sub>
- [`erigontech/erigon#1475`](https://github.com/erigontech/erigon/pull/1475) — mdbx: switch CI to mdbx, fix SeekExact, print slow/big transactions info  
  <sub>2021-02-08 · merged · authored · score 4 · mdbx, transaction</sub>
- [`erigontech/erigon#1472`](https://github.com/erigontech/erigon/pull/1472) — mdbx: C11 atomics performance fix and disable MDBX_ENV_CHECKPID   
  <sub>2021-02-07 · merged · authored · score 4 · atomic, mdbx</sub>
- [`erigontech/erigon#1326`](https://github.com/erigontech/erigon/pull/1326) — mdbx_exclusive_open_for_migrations  
  <sub>2020-10-30 · merged · authored · score 4 · mdbx, migration</sub>
- [`erigontech/erigon#1080`](https://github.com/erigontech/erigon/pull/1080) — IH stage speedup and lmdb custom comparators support  
  <sub>2020-09-08 · merged · authored · score 4 · lmdb, stage</sub>
- [`erigontech/erigon#918`](https://github.com/erigontech/erigon/pull/918) — lmdb transactions of unlimited size  
  <sub>2020-08-13 · merged · authored · score 4 · lmdb, transaction</sub>
- [`erigontech/erigon#905`](https://github.com/erigontech/erigon/pull/905) — lmdb: correct thread lock on non-managed tx  
  <sub>2020-08-11 · merged · authored · score 4 · lmdb, tx </sub>
- [`erigontech/erigon#904`](https://github.com/erigontech/erigon/pull/904) — lmdb allow multi-rollback  
  <sub>2020-08-11 · merged · authored · score 4 · lmdb, rollback</sub>
- [`erigontech/erigon#654`](https://github.com/erigontech/erigon/pull/654) — Experiment with Python+Lmdb and state analytics  
  <sub>2020-06-12 · merged · authored · score 4 · lmdb, state</sub>
- [`erigontech/mdbx-go#217`](https://github.com/erigontech/mdbx-go/pull/217) — mdbx: expose ExactKeyValue/Pair navigation flags + merge last master  
  <sub>2026-05-13 · merged · reviewed · score 4 · mdbx, merge</sub>
- [`erigontech/mdbx-go#108`](https://github.com/erigontech/mdbx-go/pull/108) — mdbx_env_warmup initial commit  
  <sub>2023-06-27 · merged · reviewed · score 4 · commit, mdbx</sub>
- [`erigontech/mdbx-go#44`](https://github.com/erigontech/mdbx-go/pull/44) — mdbx: fix gc "retry" issue (slowness of gc during commit)   
  <sub>2022-01-10 · merged · authored · score 4 · commit, mdbx</sub>
- [`ledgerwatch/erigon-lib#1043`](https://github.com/ledgerwatch/erigon-lib/pull/1043) — fsync: don't skip error, ability to disable in tests  
  <sub>2023-07-11 · merged · authored · score 4 · fsync, sync</sub>
- [`ledgerwatch/erigon-lib#827`](https://github.com/ledgerwatch/erigon-lib/pull/827) — mdbx: proper atomic close  
  <sub>2023-01-10 · merged · authored · score 4 · atomic, mdbx</sub>
- [`ledgerwatch/erigon-lib#786`](https://github.com/ledgerwatch/erigon-lib/pull/786) — mdbx: relax a bit merge limit (still leave it stronger than default)   
  <sub>2022-12-17 · merged · authored · score 4 · mdbx, merge</sub>
- [`ledgerwatch/erigon-lib#769`](https://github.com/ledgerwatch/erigon-lib/pull/769) — mdbx bindings: remove txn.RawRead field  
  <sub>2022-12-07 · merged · authored · score 4 · mdbx, txn</sub>
- [`ledgerwatch/erigon-lib#767`](https://github.com/ledgerwatch/erigon-lib/pull/767) — mdbx: add BeginRwAsync method  
  <sub>2022-12-07 · merged · authored · score 4 · mdbx, sync</sub>
- [`ledgerwatch/erigon-lib#666`](https://github.com/ledgerwatch/erigon-lib/pull/666) — mdbx mergeThreshold option #665  
  <sub>2022-10-03 · merged · authored · score 4 · mdbx, merge</sub>
- [`ledgerwatch/erigon-lib#665`](https://github.com/ledgerwatch/erigon-lib/pull/665) — mdbx mergeThreshold option  
  <sub>2022-10-03 · closed · authored · score 4 · mdbx, merge</sub>
- [`ledgerwatch/erigon-lib#559`](https://github.com/ledgerwatch/erigon-lib/pull/559) — parity_listStorageKeys: *mdbx.MdbxCursor is not kv.CursorDupSort  
  <sub>2022-07-29 · merged · authored · score 4 · mdbx, storage</sub>
- [`ledgerwatch/erigon-lib#530`](https://github.com/ledgerwatch/erigon-lib/pull/530) — mdbx: use OS pagesize by default (but > 4Kb, and < 64Kb)  
  <sub>2022-07-19 · merged · authored · score 4 · mdbx, page</sub>
- [`ledgerwatch/erigon-lib#464`](https://github.com/ledgerwatch/erigon-lib/pull/464) — kv_mdbx: atomic `closed` flag  
  <sub>2022-05-24 · merged · authored · score 4 · atomic, mdbx</sub>
- [`ledgerwatch/erigon-lib#264`](https://github.com/ledgerwatch/erigon-lib/pull/264) — mdbx: allow configure pagesize  
  <sub>2022-01-22 · merged · authored · score 4 · mdbx, page</sub>
- [`ledgerwatch/erigon-lib#228`](https://github.com/ledgerwatch/erigon-lib/pull/228) — mdbx: fix gc "retry" issue (slowness of gc during commit)  
  <sub>2022-01-10 · merged · authored · score 4 · commit, mdbx</sub>
- [`ledgerwatch/erigon-lib#227`](https://github.com/ledgerwatch/erigon-lib/pull/227) — mdbx: fix gc "retry" issue (slowness of gc during commit)  
  <sub>2022-01-10 · merged · authored · score 4 · commit, mdbx</sub>
- [`ledgerwatch/erigon-lib#125`](https://github.com/ledgerwatch/erigon-lib/pull/125) — force some rw tx when db open, to allow mdbx up version signature    
  <sub>2021-10-22 · merged · authored · score 4 · mdbx, tx </sub>
- [`ledgerwatch/erigon-lib#99`](https://github.com/ledgerwatch/erigon-lib/pull/99) — MDBX: Don't block when open db from another process if main process holds long RW tx    
  <sub>2021-10-05 · merged · authored · score 4 · mdbx, tx </sub>
- [`ledgerwatch/lmdb-go#6`](https://github.com/ledgerwatch/lmdb-go/pull/6) — lmdb_no_freepages_sequence_search_for_large_values  
  <sub>2020-10-10 · merged · authored · score 4 · lmdb, page</sub>
- [`erigontech/erigon#21340`](https://github.com/erigontech/erigon/pull/21340) — fusefilter: cleanup NewReader mmap/file on parse failure  
  <sub>2026-05-21 · closed · reviewed · score 3 · mmap</sub>
- [`erigontech/erigon#21288`](https://github.com/erigontech/erigon/pull/21288) — skill: fix mdbx_copy destination path in erigon-mdbx-compact  
  <sub>2026-05-19 · closed · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#21189`](https://github.com/erigontech/erigon/pull/21189) — cmd/integration: add mdbx_copy compact in-place one-liner  
  <sub>2026-05-14 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#21094`](https://github.com/erigontech/erigon/pull/21094) — db/kv/mdbx: comment on 9K roTxsLimiter target  
  <sub>2026-05-11 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#20769`](https://github.com/erigontech/erigon/pull/20769) — db/kv, db/state: use PutCurrent instead of DeleteCurrent+Put in domain flush  
  <sub>2026-04-24 · merged · authored · score 3 · domain, flush, state</sub>
- [`erigontech/erigon#20472`](https://github.com/erigontech/erigon/pull/20472) — plugins/auth: add UCAN core library with EOA signer and MDBX store  
  <sub>2026-04-10 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#20364`](https://github.com/erigontech/erigon/pull/20364) — skill: add erigon-mdbx-compact for MDBX database compaction  
  <sub>2026-04-06 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#19930`](https://github.com/erigontech/erigon/pull/19930) — snapshotsync: make snapshot deletion idempotent  
  <sub>2026-03-16 · merged · reviewed · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#19769`](https://github.com/erigontech/erigon/pull/19769) — ci, execution/tests: run MDBX test temp dirs on a RAM disk  
  <sub>2026-03-10 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#19512`](https://github.com/erigontech/erigon/pull/19512) — [wip] etl: zero-copy fileDataProvider on mmap  
  <sub>2026-02-27 · closed · authored · score 3 · mmap</sub>
- [`erigontech/erigon#19397`](https://github.com/erigontech/erigon/pull/19397) — seg: read-ahead implemented as own `mmap` area + `madvise_` (only concept, no erigon changes)  
  <sub>2026-02-22 · merged · authored · score 3 · mmap</sub>
- [`erigontech/erigon#19281`](https://github.com/erigontech/erigon/pull/19281) — ci: reduce InMem db dirtySpace limit  
  <sub>2026-02-18 · merged · authored · score 3 · dirtyspace</sub>
- [`erigontech/erigon#19198`](https://github.com/erigontech/erigon/pull/19198) — db/mdbx: remove dead debug code and migrate to slices.Sort  
  <sub>2026-02-15 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#19197`](https://github.com/erigontech/erigon/pull/19197) — mdbx: use slices.Sort for bucket names  
  <sub>2026-02-15 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#19021`](https://github.com/erigontech/erigon/pull/19021) — [wip] mdbx: max lag metric  
  <sub>2026-02-07 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#18616`](https://github.com/erigontech/erigon/pull/18616) — Migrate MDBX benchmarks to use b.Loop  
  <sub>2026-01-10 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#18412`](https://github.com/erigontech/erigon/pull/18412) — [wip] mdbx: default gc_aug_limit  
  <sub>2025-12-22 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#18100`](https://github.com/erigontech/erigon/pull/18100) — db/snapshotsync: fix snap.download.to.block incorrect bodies view  
  <sub>2025-11-28 · merged · reviewed · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#17743`](https://github.com/erigontech/erigon/pull/17743) — mdbx 0.13.9  
  <sub>2025-11-01 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#17656`](https://github.com/erigontech/erigon/pull/17656) — mdbx_stat: add Reclaimable space in gb to command  
  <sub>2025-10-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#17621`](https://github.com/erigontech/erigon/pull/17621) — mdbx: to use default flags set  
  <sub>2025-10-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#17574`](https://github.com/erigontech/erigon/pull/17574) — [r3.2] mdbx 0.13.7 with small fix  
  <sub>2025-10-21 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#17517`](https://github.com/erigontech/erigon/pull/17517) — mdbx 0.13.7 with small fix  
  <sub>2025-10-17 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#17461`](https://github.com/erigontech/erigon/pull/17461) — Revert "mdbx: v0.13.8"  
  <sub>2025-10-15 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#17284`](https://github.com/erigontech/erigon/pull/17284) — mdbx: v0.13.8  
  <sub>2025-09-29 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#17274`](https://github.com/erigontech/erigon/pull/17274) — erigon-lib/mmap: remove dead MmapRw from mmap_unix.go  
  <sub>2025-09-29 · merged · reviewed · score 3 · mmap</sub>
- [`erigontech/erigon#16968`](https://github.com/erigontech/erigon/pull/16968) — in_mem_db: reduce dirty space limit  
  <sub>2025-09-03 · merged · authored · score 3 · dirty space</sub>
- [`erigontech/erigon#16966`](https://github.com/erigontech/erigon/pull/16966) — [r32] fuse_filter: keep in app's memory instead of mmap  
  <sub>2025-09-03 · merged · authored · score 3 · mmap</sub>
- [`erigontech/erigon#16938`](https://github.com/erigontech/erigon/pull/16938) — snapshotsync: add support for --snap.download.to.block (shadow.fork.block)  
  <sub>2025-09-01 · merged · reviewed · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#16933`](https://github.com/erigontech/erigon/pull/16933) — dir improvements: move `snapshotsync` from `turbo` to `db`  
  <sub>2025-09-01 · merged · reviewed · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#16892`](https://github.com/erigontech/erigon/pull/16892) —  [r31] fuse_filter: keep in app's memory instead of `mmap`   
  <sub>2025-08-29 · merged · authored · score 3 · mmap</sub>
- [`erigontech/erigon#16862`](https://github.com/erigontech/erigon/pull/16862) — snapshotsync: fix minimal nodes downloading all snapshots  
  <sub>2025-08-27 · merged · reviewed · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#16377`](https://github.com/erigontech/erigon/pull/16377) — New mdbx version (stable v0.13.7 release)  
  <sub>2025-07-30 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#15900`](https://github.com/erigontech/erigon/pull/15900) — [wip] r3.0: mdbx 12   
  <sub>2025-07-02 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#15112`](https://github.com/erigontech/erigon/pull/15112) — mdbx v0.13.6  
  <sub>2025-05-17 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#14856`](https://github.com/erigontech/erigon/pull/14856) — new mdbx-go bindings (cosmetic changes)  
  <sub>2025-05-02 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#14640`](https://github.com/erigontech/erigon/pull/14640) — fix: mdbx.Coalesce is deprecated: always turned on since v0.12, deprecated since v0.13  
  <sub>2025-04-17 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#14361`](https://github.com/erigontech/erigon/pull/14361) — Add state sync logs to index  
  <sub>2025-03-29 · merged · reviewed · score 3 · index, state, sync</sub>
- [`erigontech/erigon#14292`](https://github.com/erigontech/erigon/pull/14292) — new mdbx-go bindings version  
  <sub>2025-03-25 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#14265`](https://github.com/erigontech/erigon/pull/14265) — new mdbx version v13.5  
  <sub>2025-03-22 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#14016`](https://github.com/erigontech/erigon/pull/14016) — mdbx v0.12.13   
  <sub>2025-02-28 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#13967`](https://github.com/erigontech/erigon/pull/13967) — Bump mdbx-go to v0.38.6 release  
  <sub>2025-02-25 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#13951`](https://github.com/erigontech/erigon/pull/13951) — rpcdaemon: Show state sync transactions in `eth_getLogs` (#13924)  
  <sub>2025-02-25 · merged · reviewed · score 3 · state, sync, transaction</sub>
- [`erigontech/erigon#13924`](https://github.com/erigontech/erigon/pull/13924) — rpcdaemon: Show state sync transactions in `eth_getLogs`  
  <sub>2025-02-24 · merged · reviewed · score 3 · state, sync, transaction</sub>
- [`erigontech/erigon#13847`](https://github.com/erigontech/erigon/pull/13847) — Add DB label to MDBX metrics  
  <sub>2025-02-17 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#13822`](https://github.com/erigontech/erigon/pull/13822) — Add NodeDB metrics for DbSize and DirtySpace  
  <sub>2025-02-14 · closed · reviewed · score 3 · dirtyspace</sub>
- [`erigontech/erigon#13678`](https://github.com/erigontech/erigon/pull/13678) — use ReadSequence and add mdbxtx.ResetSequence()  
  <sub>2025-02-03 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#13563`](https://github.com/erigontech/erigon/pull/13563) — [wip] mdbx C traces v0.13.3  
  <sub>2025-01-26 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#13561`](https://github.com/erigontech/erigon/pull/13561) — Revert "mdbx: v0.13.3"  
  <sub>2025-01-25 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#13552`](https://github.com/erigontech/erigon/pull/13552) — mdbx: v0.13.3  
  <sub>2025-01-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#13286`](https://github.com/erigontech/erigon/pull/13286) — Erigon: revert go-mdbx  
  <sub>2024-12-31 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#13205`](https://github.com/erigontech/erigon/pull/13205) — mdbx: v13   
  <sub>2024-12-21 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#12988`](https://github.com/erigontech/erigon/pull/12988) — [wip] mdbx: allow to create table if need - in Accedee mode  
  <sub>2024-12-04 · closed · authored+reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#12922`](https://github.com/erigontech/erigon/pull/12922) — Additional fix for externalCL integration (prevent MDBX_MAP_FULL)  
  <sub>2024-11-29 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#12838`](https://github.com/erigontech/erigon/pull/12838) — mdbx: simplify work with flags  
  <sub>2024-11-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#12657`](https://github.com/erigontech/erigon/pull/12657) — PageToken ad PageSize in IndexRange and DomainRange functions  
  <sub>2024-11-06 · merged · reviewed · score 3 · domain, index, page</sub>
- [`erigontech/erigon#12651`](https://github.com/erigontech/erigon/pull/12651) — [WIP] Reduce dirty space  
  <sub>2024-11-06 · merged · reviewed · score 3 · dirty space</sub>
- [`erigontech/erigon#12617`](https://github.com/erigontech/erigon/pull/12617) — tests: inMem mode - less dirty space  
  <sub>2024-11-05 · closed · authored · score 3 · dirty space</sub>
- [`erigontech/erigon#12338`](https://github.com/erigontech/erigon/pull/12338) — mdbx: use lable to defautl table cfg detection  
  <sub>2024-10-16 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#12315`](https://github.com/erigontech/erigon/pull/12315) — Add early return in `ComputeTxEnv` for state sync transactions  
  <sub>2024-10-15 · merged · reviewed · score 3 · state, sync, transaction</sub>
- [`erigontech/erigon#11506`](https://github.com/erigontech/erigon/pull/11506) — mdbx: remove unused table names and keys  
  <sub>2024-08-06 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#11300`](https://github.com/erigontech/erigon/pull/11300) — Erigon 3: Parallel state flushing  
  <sub>2024-07-23 · merged · reviewed · score 3 · flush, parallel, state</sub>
- [`erigontech/erigon#11238`](https://github.com/erigontech/erigon/pull/11238) — mdbx writemap flag  
  <sub>2024-07-19 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#11125`](https://github.com/erigontech/erigon/pull/11125) — [wip] CI: mdbx v0_13  
  <sub>2024-07-12 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#11073`](https://github.com/erigontech/erigon/pull/11073) — mdbx: disable `MDBX_ENV_CHECKPID` by default  
  <sub>2024-07-08 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#10929`](https://github.com/erigontech/erigon/pull/10929) — readme: manual mdbx recover  
  <sub>2024-06-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#10779`](https://github.com/erigontech/erigon/pull/10779) — mdbx-go: new mdbx_cursor_get func  
  <sub>2024-06-17 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#10769`](https://github.com/erigontech/erigon/pull/10769) — [wip] run CI on mdbx v0.13  
  <sub>2024-06-15 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#10751`](https://github.com/erigontech/erigon/pull/10751) — upgraded mdbx-go version to v0.83.3  
  <sub>2024-06-14 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#10708`](https://github.com/erigontech/erigon/pull/10708) — mdbx-go: reduce CGO overhead for passing external value  
  <sub>2024-06-12 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#10676`](https://github.com/erigontech/erigon/pull/10676) — [wip] run CI on mdbx v0.13  
  <sub>2024-06-09 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#10583`](https://github.com/erigontech/erigon/pull/10583) — e3: increase chaindata dirty space  
  <sub>2024-06-01 · merged · authored · score 3 · dirty space</sub>
- [`erigontech/erigon#10418`](https://github.com/erigontech/erigon/pull/10418) — mdbx: chaindata enable read-ahead by default  
  <sub>2024-05-20 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#10092`](https://github.com/erigontech/erigon/pull/10092) — [wip] e35: mdbx v0_13  
  <sub>2024-04-27 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#10078`](https://github.com/erigontech/erigon/pull/10078) — mdbx: Return err early in iter.Next()  
  <sub>2024-04-26 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#10031`](https://github.com/erigontech/erigon/pull/10031) — mdbx, erigon backup: fix typo  
  <sub>2024-04-23 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#9999`](https://github.com/erigontech/erigon/pull/9999) — mdbx: `Batch()`  
  <sub>2024-04-19 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#9807`](https://github.com/erigontech/erigon/pull/9807) — mdbx: call global func only for chandb   
  <sub>2024-03-26 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#9617`](https://github.com/erigontech/erigon/pull/9617) — e35: mdbx v0_12_10  
  <sub>2024-03-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#9615`](https://github.com/erigontech/erigon/pull/9615) — mdbx: close cursor in ListDBI method  
  <sub>2024-03-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#9572`](https://github.com/erigontech/erigon/pull/9572) — increase chaindata dirtyspace   
  <sub>2024-03-03 · merged · authored · score 3 · dirtyspace</sub>
- [`erigontech/erigon#9216`](https://github.com/erigontech/erigon/pull/9216) — mdbx: reduce 2 times hard dplimit  
  <sub>2024-01-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#9189`](https://github.com/erigontech/erigon/pull/9189) — mdbx: dplimit - support cgroups/gomelimit, avoid using SetOptions after env.Open()  
  <sub>2024-01-10 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#9106`](https://github.com/erigontech/erigon/pull/9106) — Make caplin sync snapshots (all of them)  
  <sub>2023-12-31 · merged · reviewed · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#8961`](https://github.com/erigontech/erigon/pull/8961) — e35: mdbx v0.29.0  
  <sub>2023-12-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8910`](https://github.com/erigontech/erigon/pull/8910) — mdbx: print in logs - real limit  
  <sub>2023-12-06 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8850`](https://github.com/erigontech/erigon/pull/8850) — mdbx: hard-limit of small db's dirty_space   
  <sub>2023-11-29 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8809`](https://github.com/erigontech/erigon/pull/8809) — Keep few beacon block headers in mdbx  
  <sub>2023-11-21 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#8679`](https://github.com/erigontech/erigon/pull/8679) — fix mdbx version in devel branch  
  <sub>2023-11-08 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8635`](https://github.com/erigontech/erigon/pull/8635) — mdbx_empty_kv_dup  
  <sub>2023-11-01 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8628`](https://github.com/erigontech/erigon/pull/8628) — mdbx: use release tag   
  <sub>2023-10-31 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8490`](https://github.com/erigontech/erigon/pull/8490) — mdbx: don't mix modes  
  <sub>2023-10-16 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8470`](https://github.com/erigontech/erigon/pull/8470) — Caplin <-> MDBX  
  <sub>2023-10-13 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#8325`](https://github.com/erigontech/erigon/pull/8325) — mdbx: less warn  
  <sub>2023-09-29 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8300`](https://github.com/erigontech/erigon/pull/8300) — mdbx: less compile warnings  
  <sub>2023-09-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8250`](https://github.com/erigontech/erigon/pull/8250) — mdbx_go: use right version in devel  
  <sub>2023-09-20 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8128`](https://github.com/erigontech/erigon/pull/8128) — exec server: run 1st cycle not in global txn. run exec in async tx, run prune in sync tx. partial progress loss fix (partial fix)  
  <sub>2023-09-05 · merged · authored · score 3 · prune, sync, txn</sub>
- [`erigontech/erigon#8106`](https://github.com/erigontech/erigon/pull/8106) — mdbx: m1 segfault  
  <sub>2023-08-31 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#8061`](https://github.com/erigontech/erigon/pull/8061) — move mdbx to new org  
  <sub>2023-08-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#7905`](https://github.com/erigontech/erigon/pull/7905) — mdbx_to_mdbx: increase read-ahead threads amount   
  <sub>2023-07-18 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#7860`](https://github.com/erigontech/erigon/pull/7860) — mdbx_to_mdbx: to use logger  
  <sub>2023-07-09 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#7850`](https://github.com/erigontech/erigon/pull/7850) — mdbx bug in DeleteCurrentDuplicates() workaround  
  <sub>2023-07-06 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#7841`](https://github.com/erigontech/erigon/pull/7841) — mdbx_to_mdbx: docs  
  <sub>2023-07-04 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#7719`](https://github.com/erigontech/erigon/pull/7719) — kv_mdbx: don't use defer for wg.Add(). not necessary and sometime it checking invalid err variable   
  <sub>2023-06-13 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#7718`](https://github.com/erigontech/erigon/pull/7718) — kv_mdbx: don't use defer for wg.Add(). not necessary and sometime it checking invalid err variable  
  <sub>2023-06-13 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#7703`](https://github.com/erigontech/erigon/pull/7703) — mdbx: tx.GetOne - avoid interface casting  
  <sub>2023-06-11 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#7532`](https://github.com/erigontech/erigon/pull/7532) — StageLoopStep: if node synced - then run initialCycle in 1 tx also (for data consistency)  
  <sub>2023-05-17 · merged · authored · score 3 · stage, sync, tx </sub>
- [`erigontech/erigon#7054`](https://github.com/erigontech/erigon/pull/7054) — mdbx: RangeDupSort iterator   
  <sub>2023-03-08 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6961`](https://github.com/erigontech/erigon/pull/6961) — mdbx: more funcs  
  <sub>2023-02-26 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6927`](https://github.com/erigontech/erigon/pull/6927) — mdbx: to support empty key/values #6923  
  <sub>2023-02-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6923`](https://github.com/erigontech/erigon/pull/6923) — mdbx: to support empty key/values  
  <sub>2023-02-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6830`](https://github.com/erigontech/erigon/pull/6830) — State sync transactions added to debug_traceBlockByNumber call  
  <sub>2023-02-10 · merged · reviewed · score 3 · state, sync, transaction</sub>
- [`erigontech/erigon#6729`](https://github.com/erigontech/erigon/pull/6729) — fix mdbx_stat incompatibility  
  <sub>2023-01-28 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6561`](https://github.com/erigontech/erigon/pull/6561) — simplify mdbx_to_mdbx  
  <sub>2023-01-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6521`](https://github.com/erigontech/erigon/pull/6521) — mdbx: v0.12.3   
  <sub>2023-01-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6455`](https://github.com/erigontech/erigon/pull/6455) — mdbx_to_mdbx better logging  
  <sub>2022-12-28 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6432`](https://github.com/erigontech/erigon/pull/6432) — mdbx: disable feature which not ready yet  
  <sub>2022-12-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6232`](https://github.com/erigontech/erigon/pull/6232) — mdbx: runtime options are changeable in Ascedee mode  
  <sub>2022-12-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6181`](https://github.com/erigontech/erigon/pull/6181) — mdbx: print some logs about settings  
  <sub>2022-12-02 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#6118`](https://github.com/erigontech/erigon/pull/6118) — mdbx: remove deprecated cmp_suffix32 feature   
  <sub>2022-11-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#5925`](https://github.com/erigontech/erigon/pull/5925) — e3: parallel exec - spend time for prune instead of flush when much data in db  
  <sub>2022-11-01 · merged · authored · score 3 · flush, parallel, prune</sub>
- [`erigontech/erigon#5869`](https://github.com/erigontech/erigon/pull/5869) — revert last mdbx change - because some suspicious bug-report #705  
  <sub>2022-10-26 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#5810`](https://github.com/erigontech/erigon/pull/5810) — mdbx_to_mdbx preserve destination  
  <sub>2022-10-20 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#5789`](https://github.com/erigontech/erigon/pull/5789) — grafana: more mdbx internals  
  <sub>2022-10-19 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#5429`](https://github.com/erigontech/erigon/pull/5429) — remove async snapshots interator  
  <sub>2022-09-19 · merged · authored · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#5240`](https://github.com/erigontech/erigon/pull/5240) — mdbx more metrics  
  <sub>2022-08-31 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#5146`](https://github.com/erigontech/erigon/pull/5146) — fix invalid memory address used in stage sync and chainId not set in legacyTx  
  <sub>2022-08-23 · merged · reviewed · score 3 · stage, sync, tx </sub>
- [`erigontech/erigon#5030`](https://github.com/erigontech/erigon/pull/5030) — mdbx: expose_growth_step  
  <sub>2022-08-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4969`](https://github.com/erigontech/erigon/pull/4969) — snapshotsync: HeaderByHash segment loop should break on result (tiny)  
  <sub>2022-08-09 · merged · reviewed · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#4926`](https://github.com/erigontech/erigon/pull/4926) — Mdbx: semaphore fix release   
  <sub>2022-08-04 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4897`](https://github.com/erigontech/erigon/pull/4897) — integration mdbx_to_mdbx   
  <sub>2022-08-02 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4878`](https://github.com/erigontech/erigon/pull/4878) — mdbx: better error msg  
  <sub>2022-08-01 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4750`](https://github.com/erigontech/erigon/pull/4750) — Mdbx: GC BigFoot   
  <sub>2022-07-19 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4720`](https://github.com/erigontech/erigon/pull/4720) — Mdbx: GC BigFoot  
  <sub>2022-07-15 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4719`](https://github.com/erigontech/erigon/pull/4719) — integration to pass mdbx.Accede flag   
  <sub>2022-07-15 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4638`](https://github.com/erigontech/erigon/pull/4638) — Increase mdbx map limit, stable  
  <sub>2022-07-05 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4585`](https://github.com/erigontech/erigon/pull/4585) — prevent downloading new snapshots after initial sync   
  <sub>2022-06-30 · merged · authored · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#4426`](https://github.com/erigontech/erigon/pull/4426) — up mmap-go version to solve Win problem  
  <sub>2022-06-10 · merged · authored · score 3 · mmap</sub>
- [`erigontech/erigon#4353`](https://github.com/erigontech/erigon/pull/4353) — changed syncmode flag to snapshots flag  
  <sub>2022-06-03 · merged · reviewed · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#4282`](https://github.com/erigontech/erigon/pull/4282) — Disable mdbx assert in alpha branch (devel is enough)  
  <sub>2022-05-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4242`](https://github.com/erigontech/erigon/pull/4242) — Revert "mdbx submodule did require github login"  
  <sub>2022-05-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4241`](https://github.com/erigontech/erigon/pull/4241) — mdbx submodule did require github login  
  <sub>2022-05-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4235`](https://github.com/erigontech/erigon/pull/4235) — mdbx: gcc 12, clang 15  
  <sub>2022-05-23 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#4096`](https://github.com/erigontech/erigon/pull/4096) — mdbx_v0.11.7  
  <sub>2022-05-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3916`](https://github.com/erigontech/erigon/pull/3916) — Remove --mdbx.augment.limit cli param  
  <sub>2022-04-19 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3895`](https://github.com/erigontech/erigon/pull/3895) — [stable] Fix for MDBX assert  
  <sub>2022-04-15 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#3876`](https://github.com/erigontech/erigon/pull/3876) — mdbx fix assert  
  <sub>2022-04-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3808`](https://github.com/erigontech/erigon/pull/3808) — Snapshots: geth compatibility, use --syncmode=snap flag  
  <sub>2022-04-01 · merged · authored · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#3775`](https://github.com/erigontech/erigon/pull/3775) — mdbx fix after v0.11.6  
  <sub>2022-03-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3774`](https://github.com/erigontech/erigon/pull/3774) — Mdbx fix after v0.11.6  
  <sub>2022-03-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3771`](https://github.com/erigontech/erigon/pull/3771) — mdbx v0.11.6  
  <sub>2022-03-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3770`](https://github.com/erigontech/erigon/pull/3770) — mdbx v0.11.6  
  <sub>2022-03-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3750`](https://github.com/erigontech/erigon/pull/3750) — Snapshots: initial sync fix  
  <sub>2022-03-22 · merged · authored · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#3748`](https://github.com/erigontech/erigon/pull/3748) — Snapshots: fix for fresh sync  
  <sub>2022-03-21 · merged · authored · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#3714`](https://github.com/erigontech/erigon/pull/3714) — Mdbx: WriteMap fallback on error  
  <sub>2022-03-16 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3711`](https://github.com/erigontech/erigon/pull/3711) — Mdbx: WriteMap fallback on open error  
  <sub>2022-03-16 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3624`](https://github.com/erigontech/erigon/pull/3624) — mdbx v0.11.5 (fix for false-corruption on Linux kernel 4.19)  
  <sub>2022-02-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3509`](https://github.com/erigontech/erigon/pull/3509) — set mdbx submodule to v0.11.4 tag  
  <sub>2022-02-13 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3508`](https://github.com/erigontech/erigon/pull/3508) — set mdbx submodule to v0.11.4 tag  
  <sub>2022-02-13 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3351`](https://github.com/erigontech/erigon/pull/3351) — Mdbx: more 4tb fixes  
  <sub>2022-01-26 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3343`](https://github.com/erigontech/erigon/pull/3343) — Mdbx: configurable corrupt error recommendations  
  <sub>2022-01-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3342`](https://github.com/erigontech/erigon/pull/3342) — MDBX: configurable corrupt error recommendations  
  <sub>2022-01-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3338`](https://github.com/erigontech/erigon/pull/3338) — MDBX: Add recommendations to corruption error message   
  <sub>2022-01-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3337`](https://github.com/erigontech/erigon/pull/3337) — MDBX: Add recommendations to corruption error message  
  <sub>2022-01-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3327`](https://github.com/erigontech/erigon/pull/3327) — mdbx 0.11.4 (fixes for 4tb asserts logic)   
  <sub>2022-01-23 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3324`](https://github.com/erigontech/erigon/pull/3324) — Mdbx 0.11.4 (fixes for 4tb asserts logic)  
  <sub>2022-01-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3313`](https://github.com/erigontech/erigon/pull/3313) — mdbx: MDBX_FORCE_ASSERTIONS=0  
  <sub>2022-01-20 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3087`](https://github.com/erigontech/erigon/pull/3087) — Genesis sync from existing snapshots  
  <sub>2021-12-04 · merged · authored · score 3 · snapshot, snapshots, sync</sub>
- [`erigontech/erigon#3058`](https://github.com/erigontech/erigon/pull/3058) — mdbx: 3tb hard limit   
  <sub>2021-11-30 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3057`](https://github.com/erigontech/erigon/pull/3057) — MDBX: Increase hard limit to 3Tb  
  <sub>2021-11-30 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3015`](https://github.com/erigontech/erigon/pull/3015) — Mdbx fix for signature update   
  <sub>2021-11-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#3014`](https://github.com/erigontech/erigon/pull/3014) — Mdbx fix for signature update  
  <sub>2021-11-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2956`](https://github.com/erigontech/erigon/pull/2956) — mdbx: revert augument limit  
  <sub>2021-11-14 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2889`](https://github.com/erigontech/erigon/pull/2889) — mdbx v0.10.2 to stable branch  
  <sub>2021-10-29 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2871`](https://github.com/erigontech/erigon/pull/2871) — Mdbx reduce augment limit to 8*default  
  <sub>2021-10-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2860`](https://github.com/erigontech/erigon/pull/2860) — Mdbx v0.11.0  
  <sub>2021-10-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2828`](https://github.com/erigontech/erigon/pull/2828) — Mdbx v0.10.5  
  <sub>2021-10-15 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2745`](https://github.com/erigontech/erigon/pull/2745) — downgrade mdbx to v0.10.1  
  <sub>2021-09-30 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2734`](https://github.com/erigontech/erigon/pull/2734) — --mdbx.augment.limit  
  <sub>2021-09-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2686`](https://github.com/erigontech/erigon/pull/2686) — Expose mdbx's txID to remote_kv  
  <sub>2021-09-15 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2578`](https://github.com/erigontech/erigon/pull/2578) — Mdbx v0.10.1  
  <sub>2021-08-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2449`](https://github.com/erigontech/erigon/pull/2449) — mdbx: v0.10.2  
  <sub>2021-07-26 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2305`](https://github.com/erigontech/erigon/pull/2305) — mdbx: add trace info to open error  
  <sub>2021-07-05 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2197`](https://github.com/erigontech/erigon/pull/2197) — mdbx doesn't require switch between Append and AppendDup for DupSort buckets  
  <sub>2021-06-19 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2167`](https://github.com/erigontech/erigon/pull/2167) — Nuke LMDB  
  <sub>2021-06-14 · merged · reviewed · score 3 · lmdb</sub>
- [`erigontech/erigon#2145`](https://github.com/erigontech/erigon/pull/2145) — Mdbx reproducible build  
  <sub>2021-06-11 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2083`](https://github.com/erigontech/erigon/pull/2083) — mdbx 0.10.1  
  <sub>2021-06-03 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2058`](https://github.com/erigontech/erigon/pull/2058) — clean logs when open mdbx  
  <sub>2021-05-31 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#2022`](https://github.com/erigontech/erigon/pull/2022) — switch node db to mdbx  
  <sub>2021-05-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1988`](https://github.com/erigontech/erigon/pull/1988) — mdbx ensure lib version match (for .dll and .o compatibility)  
  <sub>2021-05-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1982`](https://github.com/erigontech/erigon/pull/1982) — Mdbx - make it default db. Lazy buckets renaming.  
  <sub>2021-05-21 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1979`](https://github.com/erigontech/erigon/pull/1979) — Fix mdbx_problem error  
  <sub>2021-05-21 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1975`](https://github.com/erigontech/erigon/pull/1975) — set_snapshot_to_stageSync2  
  <sub>2021-05-20 · merged · authored · score 3 · snapshot, stage, sync</sub>
- [`erigontech/erigon#1961`](https://github.com/erigontech/erigon/pull/1961) — tx.Cursor() ignored error (maybe it's fix for MDBX_PROBLEM)  
  <sub>2021-05-19 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1947`](https://github.com/erigontech/erigon/pull/1947) — move some tests to mdbx  
  <sub>2021-05-17 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1931`](https://github.com/erigontech/erigon/pull/1931) — mdbx_setup_debug - handle response correct way  
  <sub>2021-05-13 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1922`](https://github.com/erigontech/erigon/pull/1922) — Mdbx: fix for MDBX_PROBLEM  
  <sub>2021-05-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1912`](https://github.com/erigontech/erigon/pull/1912) — set default mdbx log level to warning  
  <sub>2021-05-11 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1906`](https://github.com/erigontech/erigon/pull/1906) — mdbx switch to release  
  <sub>2021-05-09 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1870`](https://github.com/erigontech/erigon/pull/1870) — mdbx remove some debug   
  <sub>2021-05-04 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1857`](https://github.com/erigontech/erigon/pull/1857) — Remove MdbxCursor.prefix  
  <sub>2021-05-02 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/erigon#1804`](https://github.com/erigontech/erigon/pull/1804) — mdbx rpcdaemon support, mdbx - switch to master branch  
  <sub>2021-04-26 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1776`](https://github.com/erigontech/erigon/pull/1776) — Mdbx: speedup tests   
  <sub>2021-04-21 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1763`](https://github.com/erigontech/erigon/pull/1763) — Mdbx devel up 3  
  <sub>2021-04-20 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1733`](https://github.com/erigontech/erigon/pull/1733) — Mdbx force madv random  
  <sub>2021-04-16 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1712`](https://github.com/erigontech/erigon/pull/1712) — MDBX: enable MADV_RANDOM  
  <sub>2021-04-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1707`](https://github.com/erigontech/erigon/pull/1707) — [wip] lmdb v0.9.29  
  <sub>2021-04-10 · closed · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#1706`](https://github.com/erigontech/erigon/pull/1706) — Revert "lmdb v0.9.70"  
  <sub>2021-04-10 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#1705`](https://github.com/erigontech/erigon/pull/1705) — lmdb v0.9.70  
  <sub>2021-04-10 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#1689`](https://github.com/erigontech/erigon/pull/1689) — mdbx devel version up  
  <sub>2021-04-08 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1574`](https://github.com/erigontech/erigon/pull/1574) — mdbx: set MDBX_ENABLE_MADVISE=0  
  <sub>2021-03-21 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1553`](https://github.com/erigontech/erigon/pull/1553) — Add mdbx_drop cli tool  
  <sub>2021-03-14 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1536`](https://github.com/erigontech/erigon/pull/1536) — mdbx: remove custom logger  
  <sub>2021-03-03 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1517`](https://github.com/erigontech/erigon/pull/1517) — mdbx: fix master  
  <sub>2021-02-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1514`](https://github.com/erigontech/erigon/pull/1514) — same options as lmdb  
  <sub>2021-02-25 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#1495`](https://github.com/erigontech/erigon/pull/1495) — mdbx: .First() compatibility fix  
  <sub>2021-02-14 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1478`](https://github.com/erigontech/erigon/pull/1478) — Print tables size at end of cycle if table>10Gb, and print freelist size  
  <sub>2021-02-09 · merged · authored · score 3 · freelist</sub>
- [`erigontech/erigon#1465`](https://github.com/erigontech/erigon/pull/1465) — Mdbx increase reclaim limit  
  <sub>2021-02-05 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1462`](https://github.com/erigontech/erigon/pull/1462) — mdbx 0.9.3  
  <sub>2021-02-03 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1461`](https://github.com/erigontech/erigon/pull/1461) — Mdbx new beta version with fixed blockers  
  <sub>2021-01-30 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1415`](https://github.com/erigontech/erigon/pull/1415) — switch tests to lmdb  
  <sub>2020-12-17 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#1413`](https://github.com/erigontech/erigon/pull/1413) — Mdbx devel 5  
  <sub>2020-12-16 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1373`](https://github.com/erigontech/erigon/pull/1373) — Mdbx v0.9.2  
  <sub>2020-11-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1371`](https://github.com/erigontech/erigon/pull/1371) — To mdbx dupfixed  
  <sub>2020-11-23 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1370`](https://github.com/erigontech/erigon/pull/1370) — Sequence in to mdbx  
  <sub>2020-11-23 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1324`](https://github.com/erigontech/erigon/pull/1324) — mdbx_fix_err_check  
  <sub>2020-10-30 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1303`](https://github.com/erigontech/erigon/pull/1303) — LMDB v0.9.27, and add all lmdb cli tools  
  <sub>2020-10-27 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#1235`](https://github.com/erigontech/erigon/pull/1235) — mdbx support  
  <sub>2020-10-13 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/erigon#1206`](https://github.com/erigontech/erigon/pull/1206) — Include lmdb_stat tool  
  <sub>2020-10-08 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#1152`](https://github.com/erigontech/erigon/pull/1152) — (related to lmdb assert) Undupsort IH bucket  
  <sub>2020-09-29 · closed · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#1151`](https://github.com/erigontech/erigon/pull/1151) — (related to lmdb assert) Avoid deleteCurrent on cursor which used for iterations  
  <sub>2020-09-29 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#843`](https://github.com/erigontech/erigon/pull/843) — remove warning from lmdb compilation  
  <sub>2020-08-01 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#840`](https://github.com/erigontech/erigon/pull/840) — reduce mmap limit size (raspbery-pi failed on 4TB)  
  <sub>2020-08-01 · merged · authored · score 3 · mmap</sub>
- [`erigontech/erigon#829`](https://github.com/erigontech/erigon/pull/829) — LMDB: no periodic stale check  
  <sub>2020-07-30 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#795`](https://github.com/erigontech/erigon/pull/795) — lmdb_is_not_friendly_to_empty_values  
  <sub>2020-07-27 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#779`](https://github.com/erigontech/erigon/pull/779) — On mac lmdb can't start with error "cannot allocate memory" until I not reduced magic number  
  <sub>2020-07-24 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#762`](https://github.com/erigontech/erigon/pull/762) — Ci lmdb - reduce memory usage   
  <sub>2020-07-20 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#750`](https://github.com/erigontech/erigon/pull/750) — remove all pools from bolt, badger, lmdb  
  <sub>2020-07-16 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#720`](https://github.com/erigontech/erigon/pull/720) — move lmdb-go under ledgerwatch org  
  <sub>2020-07-07 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#684`](https://github.com/erigontech/erigon/pull/684) — use lmdb.Append method  
  <sub>2020-06-24 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#678`](https://github.com/erigontech/erigon/pull/678) — lmdb append  
  <sub>2020-06-19 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#675`](https://github.com/erigontech/erigon/pull/675) — make lmdb default db  
  <sub>2020-06-18 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#674`](https://github.com/erigontech/erigon/pull/674) — lmdb support empty values, but not empty keys  
  <sub>2020-06-18 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#673`](https://github.com/erigontech/erigon/pull/673) — Lmdb: avoid empty key values in put and seek  
  <sub>2020-06-17 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#667`](https://github.com/erigontech/erigon/pull/667) — Minor lmdb related improvements  
  <sub>2020-06-15 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#664`](https://github.com/erigontech/erigon/pull/664) — Lmdb cursors not always return to pool   
  <sub>2020-06-14 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#649`](https://github.com/erigontech/erigon/pull/649) — Use same lmdb version as in python bindings: version of 2019 year  
  <sub>2020-06-11 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#645`](https://github.com/erigontech/erigon/pull/645) — lmdb bucket stats  
  <sub>2020-06-09 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#640`](https://github.com/erigontech/erigon/pull/640) — fix lmdb mem leak  
  <sub>2020-06-09 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#632`](https://github.com/erigontech/erigon/pull/632) — lmdb version up to 2020  
  <sub>2020-06-06 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#630`](https://github.com/erigontech/erigon/pull/630) — Lmdb and Badger tests  
  <sub>2020-06-06 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#624`](https://github.com/erigontech/erigon/pull/624) — Run tests on lmdb and badger  
  <sub>2020-06-05 · merged · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#589`](https://github.com/erigontech/erigon/pull/589) — [wip] Lmdb: AbstractKV and DB interfaces  
  <sub>2020-05-29 · merged · authored+reviewed · score 3 · lmdb</sub>
- [`erigontech/mdbx-go#226`](https://github.com/erigontech/mdbx-go/pull/226) — mdbx: doc fixes for EstimateDistance/DistributeCursors  
  <sub>2026-06-19 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#225`](https://github.com/erigontech/mdbx-go/pull/225) — mdbx: expose range estimation + cursor distribution/deletion APIs  
  <sub>2026-06-19 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#224`](https://github.com/erigontech/mdbx-go/pull/224) — mdbx: expose OptPrefaultWriteEnable  
  <sub>2026-06-15 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#220`](https://github.com/erigontech/mdbx-go/pull/220) — mdbx: replace interface{} with any (Go 1.18 alias)  
  <sub>2026-05-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#218`](https://github.com/erigontech/mdbx-go/pull/218) — new 0.14.2 mdbx release  
  <sub>2026-05-14 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#213`](https://github.com/erigontech/mdbx-go/pull/213) — mdbx latest master (unreleased 0.14.x)  
  <sub>2026-04-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#208`](https://github.com/erigontech/mdbx-go/pull/208) — mdbx: add Cursor.PutCurrent for DupSort in-place dup replacement  
  <sub>2026-03-16 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#207`](https://github.com/erigontech/mdbx-go/pull/207) — mdbx: add Cursor.PutCurrent for DupSort in-place dup replacement  
  <sub>2026-03-16 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#184`](https://github.com/erigontech/mdbx-go/pull/184) — new version of mdbx  
  <sub>2025-03-21 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#174`](https://github.com/erigontech/mdbx-go/pull/174) — add 0.12.13.0 version to mdbx  
  <sub>2025-02-28 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#169`](https://github.com/erigontech/mdbx-go/pull/169) — added MDBX_opt_gc_time_limit  
  <sub>2025-02-25 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#162`](https://github.com/erigontech/mdbx-go/pull/162) — new v14_1 version of mdbx  
  <sub>2025-02-13 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#161`](https://github.com/erigontech/mdbx-go/pull/161) — Add error handling for MDBX_MAP_FULL with descriptive error messages  
  <sub>2025-02-05 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#160`](https://github.com/erigontech/mdbx-go/pull/160) — Add specific error handling and message for MDBX_MAP_FULL scenario.  
  <sub>2025-02-03 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#158`](https://github.com/erigontech/mdbx-go/pull/158) — mdbx: v0.13.3  
  <sub>2025-01-23 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#157`](https://github.com/erigontech/mdbx-go/pull/157) — mdbx_get_sysraminfo binding  
  <sub>2025-01-16 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#139`](https://github.com/erigontech/mdbx-go/pull/139) — mdbx: v13  
  <sub>2024-04-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#138`](https://github.com/erigontech/mdbx-go/pull/138) — [wip] mdbx: future 13 version, `master` build  
  <sub>2024-03-24 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#136`](https://github.com/erigontech/mdbx-go/pull/136) — mdbx v0_12_10  
  <sub>2024-03-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#130`](https://github.com/erigontech/mdbx-go/pull/130) — mdbx_version description string - e2  
  <sub>2024-01-08 · merged · reviewed · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#128`](https://github.com/erigontech/mdbx-go/pull/128) — mdbx v0.12.9  
  <sub>2023-12-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#122`](https://github.com/erigontech/mdbx-go/pull/122) — mdbx: enable `minicore` by default  
  <sub>2023-11-01 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#120`](https://github.com/erigontech/mdbx-go/pull/120) — mdbx v13 release  
  <sub>2023-10-10 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#104`](https://github.com/erigontech/mdbx-go/pull/104) — mdbx v0.12.6  
  <sub>2023-06-03 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#103`](https://github.com/erigontech/mdbx-go/pull/103) — mdbx_v0.12.5  
  <sub>2023-04-23 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#94`](https://github.com/erigontech/mdbx-go/pull/94) — mdbx v0.12.4  
  <sub>2023-02-21 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#93`](https://github.com/erigontech/mdbx-go/pull/93) — mdbx v0.11.14  
  <sub>2023-02-21 · closed · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#88`](https://github.com/erigontech/mdbx-go/pull/88) — mdbx: v0.12.3  
  <sub>2022-11-30 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#75`](https://github.com/erigontech/mdbx-go/pull/75) — Mdbx: GC BigFoot  
  <sub>2022-07-15 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#65`](https://github.com/erigontech/mdbx-go/pull/65) — mdbx v0.11.7  
  <sub>2022-05-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#61`](https://github.com/erigontech/mdbx-go/pull/61) — mdbx fix assert  
  <sub>2022-04-12 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#58`](https://github.com/erigontech/mdbx-go/pull/58) — mdbx v0.11.6  
  <sub>2022-03-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#54`](https://github.com/erigontech/mdbx-go/pull/54) — mdbx_v0.11.5  
  <sub>2022-02-25 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#53`](https://github.com/erigontech/mdbx-go/pull/53) — MDBX: 4tb fixes  
  <sub>2022-01-27 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#46`](https://github.com/erigontech/mdbx-go/pull/46) — mdbx 0.11.4 (fix for 4Tb assert logic)  
  <sub>2022-01-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#42`](https://github.com/erigontech/mdbx-go/pull/42) — mdbx v0.11.1  
  <sub>2021-10-24 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#41`](https://github.com/erigontech/mdbx-go/pull/41) — mdbx v0.11.0  
  <sub>2021-10-22 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#40`](https://github.com/erigontech/mdbx-go/pull/40) — mdbx version v0.10.5  
  <sub>2021-10-15 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#39`](https://github.com/erigontech/mdbx-go/pull/39) — mdbx_v0.10.5  
  <sub>2021-10-14 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#38`](https://github.com/erigontech/mdbx-go/pull/38) — Mdbx v0.10.4  
  <sub>2021-10-10 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#35`](https://github.com/erigontech/mdbx-go/pull/35) — mdbx downgrade v0.10.1  
  <sub>2021-09-30 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#33`](https://github.com/erigontech/mdbx-go/pull/33) — mdbx_0_10_3  
  <sub>2021-09-07 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#30`](https://github.com/erigontech/mdbx-go/pull/30) — mdbx_v0_10_2  
  <sub>2021-07-26 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#27`](https://github.com/erigontech/mdbx-go/pull/27) — mdbx add -std=gnu11 flag  
  <sub>2021-06-29 · merged · authored · score 3 · mdbx</sub>
- [`erigontech/mdbx-go#19`](https://github.com/erigontech/mdbx-go/pull/19) — mdbx release v0.10.0  
  <sub>2021-05-10 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/bolt#31`](https://github.com/ledgerwatch/bolt/pull/31) — Port freelist based on hashmap feature from etcd repo  
  <sub>2020-05-10 · merged · authored · score 3 · freelist</sub>
- [`ledgerwatch/bolt#25`](https://github.com/ledgerwatch/bolt/pull/25) — fix TestDB_Open_InitialMmapSize - sometimes failing  
  <sub>2020-04-08 · merged · authored · score 3 · mmap</sub>
- [`ledgerwatch/erigon-lib#1093`](https://github.com/ledgerwatch/erigon-lib/pull/1093) — mdbx: m1 segfault  
  <sub>2023-08-31 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#1083`](https://github.com/ledgerwatch/erigon-lib/pull/1083) — move mdbx to new org  
  <sub>2023-08-24 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#1039`](https://github.com/ledgerwatch/erigon-lib/pull/1039) — mdbx bug in DeleteCurrentDuplicates() workaround  
  <sub>2023-07-06 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#1019`](https://github.com/ledgerwatch/erigon-lib/pull/1019) — kv_mdbx: don't use `defer` for wg.Add(). not necessary and sometime it checking invalid `err` variable  
  <sub>2023-06-13 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#1017`](https://github.com/ledgerwatch/erigon-lib/pull/1017) — mdbx: tx.Get - avoid interface casting  
  <sub>2023-06-11 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#925`](https://github.com/ledgerwatch/erigon-lib/pull/925) — mdbx: RangeDupSort iterator  
  <sub>2023-03-08 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#907`](https://github.com/ledgerwatch/erigon-lib/pull/907) — mdbx: more funcs  
  <sub>2023-02-26 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#900`](https://github.com/ledgerwatch/erigon-lib/pull/900) — mdbx: to support empty key/values #6923  
  <sub>2023-02-22 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#898`](https://github.com/ledgerwatch/erigon-lib/pull/898) — mdbx: to support empty key/values  
  <sub>2023-02-22 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#897`](https://github.com/ledgerwatch/erigon-lib/pull/897) — kv/mdbx: Ability to list tables from read-only tx, and enumerate DBs open in a process  
  <sub>2023-02-21 · merged · reviewed · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#824`](https://github.com/ledgerwatch/erigon-lib/pull/824) — mdbx: v0.12.3  
  <sub>2023-01-07 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#771`](https://github.com/ledgerwatch/erigon-lib/pull/771) — mdbx: runtime options are changeable in Ascedee mode  
  <sub>2022-12-07 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#757`](https://github.com/ledgerwatch/erigon-lib/pull/757) — mdbx: reproducibility of benchmarks  
  <sub>2022-12-02 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#744`](https://github.com/ledgerwatch/erigon-lib/pull/744) — mdbx: remove deprecated cmp_suffix32 feature   
  <sub>2022-11-24 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#705`](https://github.com/ledgerwatch/erigon-lib/pull/705) — revert last mdbx change - because some suspicious bug-report  
  <sub>2022-10-26 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#631`](https://github.com/ledgerwatch/erigon-lib/pull/631) — MDBX does support empty keys  
  <sub>2022-09-08 · merged · reviewed · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#614`](https://github.com/ledgerwatch/erigon-lib/pull/614) — mdbx more metrics  
  <sub>2022-08-31 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#613`](https://github.com/ledgerwatch/erigon-lib/pull/613) — mdbx more metrics  
  <sub>2022-08-31 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#583`](https://github.com/ledgerwatch/erigon-lib/pull/583) — txpool: reduce db growth step  
  <sub>2022-08-12 · merged · authored · score 3 · growth step</sub>
- [`ledgerwatch/erigon-lib#567`](https://github.com/ledgerwatch/erigon-lib/pull/567) — mdbx: fix possible semaphore exhaustion on cancelled context  
  <sub>2022-08-03 · merged · reviewed · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#561`](https://github.com/ledgerwatch/erigon-lib/pull/561) — mdbx: better error msg  
  <sub>2022-08-01 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#522`](https://github.com/ledgerwatch/erigon-lib/pull/522) — kv_mdbx_test updated  
  <sub>2022-07-17 · merged · reviewed · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#497`](https://github.com/ledgerwatch/erigon-lib/pull/497) — Implemented ForAmount and MDBX sequencing  
  <sub>2022-06-18 · merged · reviewed · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#496`](https://github.com/ledgerwatch/erigon-lib/pull/496) — Mdbx: GC BigFoot  
  <sub>2022-06-18 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#440`](https://github.com/ledgerwatch/erigon-lib/pull/440) — mdbx_v0.11.7  
  <sub>2022-05-07 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#415`](https://github.com/ledgerwatch/erigon-lib/pull/415) — mdbx: fix assert  
  <sub>2022-04-12 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#399`](https://github.com/ledgerwatch/erigon-lib/pull/399) — Mdbx fix after v0.11.6   
  <sub>2022-03-27 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#398`](https://github.com/ledgerwatch/erigon-lib/pull/398) — Mdbx fix after v0.11.6  
  <sub>2022-03-27 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#395`](https://github.com/ledgerwatch/erigon-lib/pull/395) — mdbx v0.11.6  
  <sub>2022-03-25 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#394`](https://github.com/ledgerwatch/erigon-lib/pull/394) — mdbx v0.11.6  
  <sub>2022-03-25 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#370`](https://github.com/ledgerwatch/erigon-lib/pull/370) — Mdbx: WriteMap fallback on error  
  <sub>2022-03-16 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#369`](https://github.com/ledgerwatch/erigon-lib/pull/369) — Mdbx: WriteMap fallback on open error  
  <sub>2022-03-16 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#351`](https://github.com/ledgerwatch/erigon-lib/pull/351) — [wip] mdbx v0.11.5 (fix for false-corruption on Linux kernel 4.19)  
  <sub>2022-02-25 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#282`](https://github.com/ledgerwatch/erigon-lib/pull/282) — [wip] Mdbx: more 4tb fixes  
  <sub>2022-01-26 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#276`](https://github.com/ledgerwatch/erigon-lib/pull/276) — MDBX: configurable corrupt message recommendations  
  <sub>2022-01-25 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#275`](https://github.com/ledgerwatch/erigon-lib/pull/275) — MDBX: configurable corrupt error recommendations  
  <sub>2022-01-25 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#270`](https://github.com/ledgerwatch/erigon-lib/pull/270) — MDBX: Add recommendations to corruption error message  
  <sub>2022-01-24 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#269`](https://github.com/ledgerwatch/erigon-lib/pull/269) — MDBX: Add recommendations to corruption error message  
  <sub>2022-01-24 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#267`](https://github.com/ledgerwatch/erigon-lib/pull/267) — mdbx 0.11.4  (fixes for 4tb asserts logic)   
  <sub>2022-01-23 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#266`](https://github.com/ledgerwatch/erigon-lib/pull/266) — Mdbx 0.11.4  
  <sub>2022-01-22 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#265`](https://github.com/ledgerwatch/erigon-lib/pull/265) — mdbx: consensus label  
  <sub>2022-01-22 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#256`](https://github.com/ledgerwatch/erigon-lib/pull/256) — mdbx: MDBX_FORCE_ASSERTIONS=0  
  <sub>2022-01-20 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#198`](https://github.com/ledgerwatch/erigon-lib/pull/198) — mdbx: 3tb hard limit   
  <sub>2021-11-30 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#197`](https://github.com/ledgerwatch/erigon-lib/pull/197) — MDBX: Increase hard limit to 3Tb  
  <sub>2021-11-30 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#187`](https://github.com/ledgerwatch/erigon-lib/pull/187) — Mdbx fix for signature update   
  <sub>2021-11-22 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#185`](https://github.com/ledgerwatch/erigon-lib/pull/185) — Mdbx fix for signature update   
  <sub>2021-11-22 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#184`](https://github.com/ledgerwatch/erigon-lib/pull/184) — Mdbx fix for signature update  
  <sub>2021-11-22 · closed · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#161`](https://github.com/ledgerwatch/erigon-lib/pull/161) — mdbx_revert_augument_limit_stable2  
  <sub>2021-11-14 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#160`](https://github.com/ledgerwatch/erigon-lib/pull/160) — mdbx_revert_augument_limit_stable  
  <sub>2021-11-14 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#157`](https://github.com/ledgerwatch/erigon-lib/pull/157) — mdbx: set back big augment limit   
  <sub>2021-11-13 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#134`](https://github.com/ledgerwatch/erigon-lib/pull/134) — Mdbx reduce augment limit to 8*default  
  <sub>2021-10-27 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#123`](https://github.com/ledgerwatch/erigon-lib/pull/123) — Mdbx v0.11.0  
  <sub>2021-10-22 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#112`](https://github.com/ledgerwatch/erigon-lib/pull/112) — mdbx version v0.10.5  
  <sub>2021-10-15 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#107`](https://github.com/ledgerwatch/erigon-lib/pull/107) — mdbx v0.10.4  
  <sub>2021-10-10 · closed · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#95`](https://github.com/ledgerwatch/erigon-lib/pull/95) — downgrade mdbx to v0.10.1  
  <sub>2021-09-30 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#92`](https://github.com/ledgerwatch/erigon-lib/pull/92) — --mdbx.augment.limit  
  <sub>2021-09-27 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#71`](https://github.com/ledgerwatch/erigon-lib/pull/71) — Pool: expose mdbx's txID to remote_kv  
  <sub>2021-09-15 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/erigon-lib#5`](https://github.com/ledgerwatch/erigon-lib/pull/5) — kv and mdbx move  
  <sub>2021-07-28 · merged · authored · score 3 · mdbx</sub>
- [`ledgerwatch/lmdb-go#21`](https://github.com/ledgerwatch/lmdb-go/pull/21) — revert to lmdb v0.9.27  
  <sub>2021-05-18 · merged · authored · score 3 · lmdb</sub>
- [`ledgerwatch/lmdb-go#15`](https://github.com/ledgerwatch/lmdb-go/pull/15) — lmdb_0.9.29  
  <sub>2021-04-10 · merged · authored · score 3 · lmdb</sub>
- [`ledgerwatch/lmdb-go#5`](https://github.com/ledgerwatch/lmdb-go/pull/5) — up lmdb version to 0.9.26  
  <sub>2020-09-11 · closed · authored · score 3 · lmdb</sub>
- [`erigontech/erigon#21753`](https://github.com/erigontech/erigon/pull/21753) — [r3.5] domain: existance filter madvise require page-aligned byte slice  
  <sub>2026-06-11 · merged · authored · score 2 · domain, page</sub>
- [`erigontech/erigon#21745`](https://github.com/erigontech/erigon/pull/21745) — [r3.5] domain: existance filter madvise require page-aligned byte slice  
  <sub>2026-06-11 · closed · authored · score 2 · domain, page</sub>
- [`erigontech/erigon#21744`](https://github.com/erigontech/erigon/pull/21744) — [r3.6] domain: existance filter madvise require page-aligned byte slice  
  <sub>2026-06-11 · merged · authored · score 2 · domain, page</sub>
- [`erigontech/erigon#21743`](https://github.com/erigontech/erigon/pull/21743) — [bloatnet] domain: existance filter madvise require page-aligned byte slice  
  <sub>2026-06-11 · merged · authored · score 2 · domain, page</sub>
- [`erigontech/erigon#21525`](https://github.com/erigontech/erigon/pull/21525) — batch call fcu along with InsertBlocks in block collector's flush  
  <sub>2026-05-30 · merged · reviewed · score 2 · collector, flush</sub>
- [`erigontech/erigon#21444`](https://github.com/erigontech/erigon/pull/21444) — execution/execmodule: return FCU result without waiting for flush+commit  
  <sub>2026-05-27 · merged · reviewed · score 2 · commit, flush</sub>
- [`erigontech/erigon#20425`](https://github.com/erigontech/erigon/pull/20425) — execution/state: drop ethconfig.Sync dependency from StateV3  
  <sub>2026-04-08 · merged · reviewed · score 2 · state, sync</sub>
- [`erigontech/erigon#20004`](https://github.com/erigontech/erigon/pull/20004) — cl: fall back to local head state when remote checkpoint sync fails (backport #19998)  
  <sub>2026-03-19 · merged · reviewed · score 2 · state, sync</sub>
- [`erigontech/erigon#19998`](https://github.com/erigontech/erigon/pull/19998) — cl: fall back to local head state when remote checkpoint sync fails  
  <sub>2026-03-19 · merged · reviewed · score 2 · state, sync</sub>
- [`erigontech/erigon#19944`](https://github.com/erigontech/erigon/pull/19944) — PagedWriter: solve producer-bottelneck by moving pageSerialization from producer to workers   
  <sub>2026-03-17 · merged · authored · score 2 · page, serialization</sub>
- [`erigontech/erigon#19531`](https://github.com/erigontech/erigon/pull/19531) — etl: limit SortAndFlushInBackground feature to only 1 goroutine per collector - to prevent system overloading  
  <sub>2026-02-28 · merged · authored · score 2 · collector, flush</sub>
- [`erigontech/erigon#19023`](https://github.com/erigontech/erigon/pull/19023) — rpc: increase TestSendRawTransactionSync timeout in race tests  
  <sub>2026-02-07 · merged · reviewed · score 2 · sync, transaction</sub>
- [`erigontech/erigon#18966`](https://github.com/erigontech/erigon/pull/18966) — rpc: fix timeout param in eth_sendRawTransactionSync  
  <sub>2026-02-04 · merged · reviewed · score 2 · sync, transaction</sub>
- [`erigontech/erigon#18945`](https://github.com/erigontech/erigon/pull/18945) — rpc: fix options for eth_sendRawTransactionSync  
  <sub>2026-02-03 · merged · reviewed · score 2 · sync, transaction</sub>
- [`erigontech/erigon#18548`](https://github.com/erigontech/erigon/pull/18548) — Performance: do not allow async disk flushes on cold paths.  
  <sub>2026-01-03 · merged · reviewed · score 2 · flush, sync</sub>
- [`erigontech/erigon#17173`](https://github.com/erigontech/erigon/pull/17173) — erigon-lib/event: snapshot observers in Notify/NotifySync to prevent deadlock  
  <sub>2025-09-20 · merged · reviewed · score 2 · snapshot, sync</sub>
- [`erigontech/erigon#17015`](https://github.com/erigontech/erigon/pull/17015) — txnprovider/shutter: fix synctest issues with go1.25 (#16965)  
  <sub>2025-09-04 · merged · reviewed · score 2 · sync, txn</sub>
- [`erigontech/erigon#16965`](https://github.com/erigontech/erigon/pull/16965) — txnprovider/shutter: fix synctest issues with go1.25  
  <sub>2025-09-02 · merged · reviewed · score 2 · sync, txn</sub>
- [`erigontech/erigon#15682`](https://github.com/erigontech/erigon/pull/15682) — dir improvements: move stagesync to `execution`  
  <sub>2025-06-20 · merged · reviewed · score 2 · stage, sync</sub>
- [`erigontech/erigon#15186`](https://github.com/erigontech/erigon/pull/15186) — Add apply/async operations for transactions  
  <sub>2025-05-20 · merged · reviewed · score 2 · sync, transaction</sub>
- [`erigontech/erigon#12051`](https://github.com/erigontech/erigon/pull/12051) — Remove `--sync.loop.prune.limit` flag  
  <sub>2024-09-20 · merged · authored · score 2 · prune, sync</sub>
- [`erigontech/erigon#11449`](https://github.com/erigontech/erigon/pull/11449) — `downloader --seedbox` to support OtterSync  
  <sub>2024-08-02 · merged · authored · score 2 · downloader, sync</sub>
- [`erigontech/erigon#11308`](https://github.com/erigontech/erigon/pull/11308) — Add downloader hash, flush and complete metrics  
  <sub>2024-07-24 · merged · reviewed · score 2 · downloader, flush</sub>
- [`erigontech/erigon#11059`](https://github.com/erigontech/erigon/pull/11059) — Fix torrent connection sync issues  
  <sub>2024-07-06 · merged · reviewed · score 2 · sync, torrent</sub>
- [`erigontech/erigon#10674`](https://github.com/erigontech/erigon/pull/10674) — stateDiff: 1 overflow page per entry   
  <sub>2024-06-09 · merged · authored · score 2 · page, state</sub>
- [`erigontech/erigon#10467`](https://github.com/erigontech/erigon/pull/10467) — polygon/sync: blockdownloader to use common.Sleep  
  <sub>2024-05-24 · merged · reviewed · score 2 · downloader, sync</sub>
- [`erigontech/erigon#10362`](https://github.com/erigontech/erigon/pull/10362) — Fix collector only calling forkchoice after 1000 blocks instead of sync limit  
  <sub>2024-05-15 · merged · reviewed · score 2 · collector, sync</sub>
- [`erigontech/erigon#10060`](https://github.com/erigontech/erigon/pull/10060) — Revert "StageSenders: `--sync.loop.block.limit` support"  
  <sub>2024-04-25 · merged · authored · score 2 · stage, sync</sub>
- [`erigontech/erigon#10010`](https://github.com/erigontech/erigon/pull/10010) — downloader: more durable db mode   
  <sub>2024-04-22 · merged · authored · score 2 · downloader, durable</sub>
- [`erigontech/erigon#9984`](https://github.com/erigontech/erigon/pull/9984) — downloader: RecalcStat to not expect that something downloading on synced node   
  <sub>2024-04-18 · merged · authored · score 2 · downloader, sync</sub>
- [`erigontech/erigon#9982`](https://github.com/erigontech/erigon/pull/9982) — StageSenders: `--sync.loop.block.limit` support  
  <sub>2024-04-18 · merged · authored · score 2 · stage, sync</sub>
- [`erigontech/erigon#9320`](https://github.com/erigontech/erigon/pull/9320) — Mapmutation.Flush to use less ram and close collectors earlier  
  <sub>2024-01-26 · merged · authored · score 2 · collector, flush</sub>
- [`erigontech/erigon#8597`](https://github.com/erigontech/erigon/pull/8597) — batch flush can without read tx  
  <sub>2023-10-27 · merged · reviewed · score 2 · flush, tx </sub>
- [`erigontech/erigon#7561`](https://github.com/erigontech/erigon/pull/7561) — e2: reduce StageSyncStep interface size  
  <sub>2023-05-23 · merged · authored · score 2 · stage, sync</sub>
- [`erigontech/erigon#6676`](https://github.com/erigontech/erigon/pull/6676) — e3: storageRangeAt fix NextPage value  
  <sub>2023-01-24 · merged · authored · score 2 · page, storage</sub>
- [`erigontech/erigon#5935`](https://github.com/erigontech/erigon/pull/5935) — e3: build files sequentially, flush indices in-advance before commit  
  <sub>2022-11-02 · merged · authored · score 2 · commit, flush</sub>
- [`erigontech/erigon#5889`](https://github.com/erigontech/erigon/pull/5889) — e3: parallel exec, rotate and partial-flush of indices wal - while main thread is idle  
  <sub>2022-10-28 · merged · authored · score 2 · flush, parallel</sub>
- [`erigontech/erigon#5018`](https://github.com/erigontech/erigon/pull/5018) — fix stage sync hang at a mined block  
  <sub>2022-08-12 · merged · reviewed · score 2 · stage, sync</sub>
- [`erigontech/erigon#3174`](https://github.com/erigontech/erigon/pull/3174) — Support for syncing on mergemock  
  <sub>2021-12-26 · merged · reviewed · score 2 · merge, sync</sub>
- [`erigontech/erigon#2353`](https://github.com/erigontech/erigon/pull/2353) — RPC: return all stages progress inside eth_syncing  
  <sub>2021-07-12 · merged · authored · score 2 · stage, sync</sub>
- [`erigontech/erigon#1772`](https://github.com/erigontech/erigon/pull/1772) — Notify RPCDaemon after sync cycle commit  
  <sub>2021-04-21 · merged · authored · score 2 · commit, sync</sub>
- [`erigontech/erigon#1017`](https://github.com/erigontech/erigon/pull/1017) — Use Finish stage for eth_syncing  
  <sub>2020-08-30 · merged · reviewed · score 2 · stage, sync</sub>
- [`ledgerwatch/erigon-lib#708`](https://github.com/ledgerwatch/erigon-lib/pull/708) — e3: parallel exec, rotate and partial-flush of indices wal - while main thread is idle  
  <sub>2022-10-28 · merged · authored · score 2 · flush, parallel</sub>

## Isolation & transactions  (428)

- [`erigontech/erigon#20308`](https://github.com/erigontech/erigon/pull/20308) — commitment: remove TxNum() from PatriciaContext interface  
  <sub>2026-04-03 · merged · reviewed · score 11 · commit, commitment, patricia, txn, txnum</sub>
- [`erigontech/erigon#21538`](https://github.com/erigontech/erigon/pull/21538) — [r3.4] db/state: prune TemporalMemBatch overlay entries past unwindToTxNum (#20625)  
  <sub>2026-05-31 · merged · reviewed · score 10 · prune, state, trie, txn, txnum, unwind</sub>
- [`erigontech/erigon#20625`](https://github.com/erigontech/erigon/pull/20625) — db/state: prune TemporalMemBatch overlay entries past unwindToTxNum  
  <sub>2026-04-17 · merged · reviewed · score 10 · prune, state, trie, txn, txnum, unwind</sub>
- [`erigontech/erigon#20443`](https://github.com/erigontech/erigon/pull/20443) — cmd/integration: show commitment domain progress(txnum) in print_stages  
  <sub>2026-04-09 · merged · reviewed · score 10 · commit, commitment, domain, stage, txn, txnum</sub>
- [`erigontech/erigon#18882`](https://github.com/erigontech/erigon/pull/18882) — [r3.4] execution: fix commitment state key txNum when last block tx is at step boundary  
  <sub>2026-01-30 · merged · reviewed · score 10 · commit, commitment, state, tx , txn, txnum</sub>
- [`erigontech/erigon#11696`](https://github.com/erigontech/erigon/pull/11696) — enable keys compression for commitment.kv > 64steps  
  <sub>2024-08-20 · merged · authored · score 10 · commit, commitment, compress, compression</sub>
- [`erigontech/erigon#20287`](https://github.com/erigontech/erigon/pull/20287) — commitment: add TrieReader — stateless read-only Patricia trie navigation  
  <sub>2026-04-02 · merged · reviewed · score 9 · commit, commitment, patricia, state, trie</sub>
- [`erigontech/erigon#20203`](https://github.com/erigontech/erigon/pull/20203) — commitment: remove dead ctx field from ConcurrentPatriciaHashed, each subtrie gets own context from factory  
  <sub>2026-03-27 · merged · reviewed · score 9 · commit, commitment, patricia, trie, tx </sub>
- [`erigontech/erigon#18236`](https://github.com/erigontech/erigon/pull/18236) — db/integrity: add more info to err when extracting trie state root in commitment hist  
  <sub>2025-12-10 · merged · reviewed · score 9 · commit, commitment, state, state root, trie</sub>
- [`erigontech/erigon#17024`](https://github.com/erigontech/erigon/pull/17024) — Revert "move commitment and changeset db format outside of `db/state` package"  
  <sub>2025-09-05 · closed · authored · score 9 · commit, commitment, db format, format, state</sub>
- [`erigontech/erigon#17019`](https://github.com/erigontech/erigon/pull/17019) — move commitment and changeset db format outside of `db/state` package  
  <sub>2025-09-05 · merged · authored · score 9 · commit, commitment, db format, format, state</sub>
- [`erigontech/erigon#10004`](https://github.com/erigontech/erigon/pull/10004) — Downloader: atomic-fs to be less smart. if app called - Create() - don't check .lock. Otherwise can't create .torrent for existing .seg files.  
  <sub>2024-04-20 · merged · authored · score 9 · .seg, atomic, downloader, seg file, torrent</sub>
- [`erigontech/erigon#21892`](https://github.com/erigontech/erigon/pull/21892) — execution/commitment: materialize collapse-sibling branch in toWitnessTrie  
  <sub>2026-06-19 · merged · reviewed · score 8 · commit, commitment, trie, witness</sub>
- [`erigontech/erigon#21854`](https://github.com/erigontech/erigon/pull/21854) — execution/commitment: include exclusion proofs for absent storage slots in execution witness  
  <sub>2026-06-16 · merged · reviewed · score 8 · commit, commitment, storage, witness</sub>
- [`erigontech/erigon#20272`](https://github.com/erigontech/erigon/pull/20272) — commitment: per-goroutine ETL collectors for concurrent rebuild  
  <sub>2026-04-01 · merged · reviewed · score 8 · collector, commit, commitment, etl </sub>
- [`erigontech/erigon#20126`](https://github.com/erigontech/erigon/pull/20126) — commitment: expand witness trie unit tests for eth_getWitness edge cases  
  <sub>2026-03-24 · merged · reviewed · score 8 · commit, commitment, trie, witness</sub>
- [`erigontech/erigon#10549`](https://github.com/erigontech/erigon/pull/10549) — fix `history invalid txNum: 2426041281 != 2425301475` error during unwind/prune  
  <sub>2024-05-29 · merged · reviewed · score 8 · prune, txn, txnum, unwind</sub>
- [`erigontech/erigon#21791`](https://github.com/erigontech/erigon/pull/21791) — commitment: remove unused bin_patricia_hashed implementation  
  <sub>2026-06-13 · merged · reviewed · score 7 · commit, commitment, patricia</sub>
- [`erigontech/erigon#20839`](https://github.com/erigontech/erigon/pull/20839) — cp: skip commitment history integrity checks when disabled  
  <sub>2026-04-27 · merged · reviewed · score 7 · commit, commitment, integrity check</sub>
- [`erigontech/erigon#20835`](https://github.com/erigontech/erigon/pull/20835) — cmd/utils/app: skip commitment history integrity checks when disabled  
  <sub>2026-04-27 · merged · reviewed · score 7 · commit, commitment, integrity check</sub>
- [`erigontech/erigon#20635`](https://github.com/erigontech/erigon/pull/20635) — [r3.4] db/state: fix MaxStep using MinTxNum in DomainRoTx.prune  
  <sub>2026-04-18 · merged · authored · score 7 · domain, prune, state, txn, txnum</sub>
- [`erigontech/erigon#19597`](https://github.com/erigontech/erigon/pull/19597) — `erigon snapshots check-commitment-hist-at-blk-range`: prevent check blocks beyond state  
  <sub>2026-03-04 · merged · authored · score 7 · commit, commitment, snapshot, snapshots, state</sub>
- [`erigontech/erigon#19258`](https://github.com/erigontech/erigon/pull/19258) — fix: add warmuper.Wait() to prevent txNum race in HexPatriciaHashed.Process  
  <sub>2026-02-17 · merged · reviewed · score 7 · patricia, txn, txnum</sub>
- [`erigontech/erigon#18331`](https://github.com/erigontech/erigon/pull/18331) — make CommitmentHistory integrity check non-default  
  <sub>2025-12-16 · merged · reviewed · score 7 · commit, commitment, integrity check</sub>
- [`erigontech/erigon#17625`](https://github.com/erigontech/erigon/pull/17625) — Test_BtreeIndex_Seek2 and TestSharedDomain_CommitmentKeyReplacement speedup  
  <sub>2025-10-24 · merged · authored · score 7 · btree, commit, commitment, domain, index</sub>
- [`erigontech/erigon#15777`](https://github.com/erigontech/erigon/pull/15777) — [r30] pick body rlp only txNum  
  <sub>2025-06-27 · closed · authored · score 7 · rlp , txn, txnum</sub>
- [`erigontech/erigon#14608`](https://github.com/erigontech/erigon/pull/14608) — history: set special compress params for commitment compress  
  <sub>2025-04-15 · merged · authored · score 7 · commit, commitment, compress</sub>
- [`erigontech/erigon#10300`](https://github.com/erigontech/erigon/pull/10300) — add metrics about unwind and commitment  
  <sub>2024-05-13 · merged · reviewed · score 7 · commit, commitment, unwind</sub>
- [`erigontech/erigon#8855`](https://github.com/erigontech/erigon/pull/8855) — e35: .UnwindTo - only move to blocks with commitment  
  <sub>2023-11-29 · merged · authored · score 7 · commit, commitment, unwind</sub>
- [`erigontech/erigon#8849`](https://github.com/erigontech/erigon/pull/8849) — e35: .UnwindTo - only move to blocks with commitment - step3  
  <sub>2023-11-29 · merged · authored · score 7 · commit, commitment, unwind</sub>
- [`erigontech/erigon#8843`](https://github.com/erigontech/erigon/pull/8843) — e35: .UnwindTo - only move to blocks with commitment - step2   
  <sub>2023-11-28 · merged · authored · score 7 · commit, commitment, unwind</sub>
- [`erigontech/erigon#8836`](https://github.com/erigontech/erigon/pull/8836) — [wip] e35: .UnwindTo - only move to blocks with commitment - step5  
  <sub>2023-11-27 · closed · authored · score 7 · commit, commitment, unwind</sub>
- [`erigontech/erigon#7465`](https://github.com/erigontech/erigon/pull/7465) — made KZGCommitment constant and SSZ compatiable  
  <sub>2023-05-08 · merged · reviewed · score 7 · commit, commitment, ssz</sub>
- [`erigontech/erigon#5176`](https://github.com/erigontech/erigon/pull/5176) — Erigon22: basic txNum forward/unwind  
  <sub>2022-08-25 · merged · authored · score 7 · txn, txnum, unwind</sub>
- [`erigontech/erigon#1660`](https://github.com/erigontech/erigon/pull/1660) — etl to use rwtx  
  <sub>2021-04-02 · merged · authored · score 7 · etl , rwtx, tx </sub>
- [`erigontech/erigon#21780`](https://github.com/erigontech/erigon/pull/21780) — db/state/statecfg: bump commitment domain kv/kvi to v2.1  
  <sub>2026-06-13 · merged · authored · score 6 · commit, commitment, domain, state</sub>
- [`erigontech/erigon#21146`](https://github.com/erigontech/erigon/pull/21146) — commitment/nibbles: add V2 key encoder/decoder  
  <sub>2026-05-12 · open · reviewed · score 6 · commit, commitment, decode, encode</sub>
- [`erigontech/erigon#21105`](https://github.com/erigontech/erigon/pull/21105) — cmd/integration/commands: force unbounded domain merge for commitment rebuild  
  <sub>2026-05-11 · merged · reviewed · score 6 · commit, commitment, domain, merge</sub>
- [`erigontech/erigon#20958`](https://github.com/erigontech/erigon/pull/20958) — db/state: take commitment.domain existence filter in-mem  
  <sub>2026-05-03 · merged · authored · score 6 · commit, commitment, domain, state</sub>
- [`erigontech/erigon#20836`](https://github.com/erigontech/erigon/pull/20836) — db/state, db/kv: extract calculateMergeStartTxNum helper  
  <sub>2026-04-27 · merged · reviewed · score 6 · merge, state, txn, txnum</sub>
- [`erigontech/erigon#20622`](https://github.com/erigontech/erigon/pull/20622) — commitment: parallelize deref domain calculation  
  <sub>2026-04-17 · merged · reviewed · score 6 · commit, commitment, domain, parallel</sub>
- [`erigontech/erigon#20548`](https://github.com/erigontech/erigon/pull/20548) — commitment: eliminate BranchMerger from fold→encode→write hot path  
  <sub>2026-04-14 · open · reviewed · score 6 · commit, commitment, encode, merge</sub>
- [`erigontech/erigon#19224`](https://github.com/erigontech/erigon/pull/19224) — fix: make SharedDomains.txNum atomic to fix data race  
  <sub>2026-02-17 · closed · reviewed · score 6 · atomic, domain, txn, txnum</sub>
- [`erigontech/erigon#17861`](https://github.com/erigontech/erigon/pull/17861) — Remove duplicate commitment domain entry in state compaction command  
  <sub>2025-11-11 · merged · reviewed · score 6 · commit, commitment, domain, state</sub>
- [`erigontech/erigon#17531`](https://github.com/erigontech/erigon/pull/17531) — commitment: extract StateReader interface in SharedDomainsCommitmentContext  
  <sub>2025-10-17 · merged · reviewed · score 6 · commit, commitment, domain, state</sub>
- [`erigontech/erigon#17380`](https://github.com/erigontech/erigon/pull/17380) — domain compaction: protect StateRoot key in commitment.kv  
  <sub>2025-10-07 · merged · reviewed · score 6 · commit, commitment, domain, state</sub>
- [`erigontech/erigon#15533`](https://github.com/erigontech/erigon/pull/15533) — print_stages: print min/max step (or txnum) per each domain  
  <sub>2025-06-11 · merged · reviewed · score 6 · domain, stage, txn, txnum</sub>
- [`erigontech/erigon#15154`](https://github.com/erigontech/erigon/pull/15154) — split `SharedDomains` s2: concentrate commitment methods in sdctx  
  <sub>2025-05-19 · merged · reviewed · score 6 · commit, commitment, domain, tx </sub>
- [`erigontech/erigon#13696`](https://github.com/erigontech/erigon/pull/13696) — Commitment: parallel subtrie computation  
  <sub>2025-02-05 · merged · reviewed · score 6 · commit, commitment, parallel, trie</sub>
- [`erigontech/erigon#13654`](https://github.com/erigontech/erigon/pull/13654) — TxLookup stage: allow TxNum=0  
  <sub>2025-02-01 · merged · authored · score 6 · lookup, stage, txn, txnum</sub>
- [`erigontech/erigon#13276`](https://github.com/erigontech/erigon/pull/13276) — commitment domain: make `.kvi` default index  
  <sub>2024-12-30 · merged · authored · score 6 · commit, commitment, domain, index</sub>
- [`erigontech/erigon#13273`](https://github.com/erigontech/erigon/pull/13273) —  [wip] commitment domain: use MPH index   
  <sub>2024-12-30 · closed · authored · score 6 · commit, commitment, domain, index</sub>
- [`erigontech/erigon#11011`](https://github.com/erigontech/erigon/pull/11011) — Allow to merge commitment separately of other domains  
  <sub>2024-07-03 · merged · reviewed · score 6 · commit, commitment, domain, merge</sub>
- [`erigontech/erigon#10620`](https://github.com/erigontech/erigon/pull/10620) — protect stage_headers/bodies/senders/txnlookup from unwind behind files  
  <sub>2024-06-05 · merged · authored · score 6 · lookup, stage, txn, unwind</sub>
- [`erigontech/erigon#10510`](https://github.com/erigontech/erigon/pull/10510) — do not remove state files bigger than `maximin(domainsTxNum)`  
  <sub>2024-05-27 · merged · reviewed · score 6 · domain, state, txn, txnum</sub>
- [`erigontech/erigon#7607`](https://github.com/erigontech/erigon/pull/7607) —  snapshots: DumpBodies - break dependency on body.BaseTxNum value in db  
  <sub>2023-05-31 · merged · authored · score 6 · snapshot, snapshots, txn, txnum</sub>
- [`erigontech/erigon#1727`](https://github.com/erigontech/erigon/pull/1727) — [merge after release] Move history stage to rwtx  
  <sub>2021-04-15 · merged · authored · score 6 · merge, rwtx, stage, tx </sub>
- [`erigontech/erigon#1726`](https://github.com/erigontech/erigon/pull/1726) — [merge after release] move ih stage to rwtx  
  <sub>2021-04-15 · merged · authored · score 6 · merge, rwtx, stage, tx </sub>
- [`erigontech/erigon#1692`](https://github.com/erigontech/erigon/pull/1692) — [merge after release] remove etl onLoadCommit hook, because etl doesn't manage transactions anymore (it's low-level code)  
  <sub>2021-04-08 · merged · authored · score 6 · commit, etl , merge, transaction</sub>
- [`erigontech/erigon#21859`](https://github.com/erigontech/erigon/pull/21859) — execution/commitment: route trie trace through an io.Writer  
  <sub>2026-06-17 · open · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#21798`](https://github.com/erigontech/erigon/pull/21798) — [r3.5] execution/commitment: skip prev lookup for new branch nodes  
  <sub>2026-06-14 · merged · authored · score 5 · commit, commitment, lookup</sub>
- [`erigontech/erigon#21740`](https://github.com/erigontech/erigon/pull/21740) — [3.6] db: commitment domain to take existance filter to RAM  
  <sub>2026-06-11 · merged · authored · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#21738`](https://github.com/erigontech/erigon/pull/21738) — [main] db: commitment domain to take existance filter to RAM  
  <sub>2026-06-11 · merged · authored · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#21737`](https://github.com/erigontech/erigon/pull/21737) — [3.5] db: commitment domain to take existance filter to RAM  
  <sub>2026-06-11 · merged · authored · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#21618`](https://github.com/erigontech/erigon/pull/21618) — commitment: rebind concurrent-trie metrics, harden CSV/warmup config  
  <sub>2026-06-04 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#21452`](https://github.com/erigontech/erigon/pull/21452) — db/state, db/config3: erigondb.toml as source of truth for commitment branch referencing  
  <sub>2026-05-27 · open · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#21407`](https://github.com/erigontech/erigon/pull/21407) — db/integrity: check txnum lookup misses  
  <sub>2026-05-26 · merged · reviewed · score 5 · lookup, txn, txnum</sub>
- [`erigontech/erigon#21283`](https://github.com/erigontech/erigon/pull/21283) — cmd/integration, db/state: add --continue flag for commitment convert  
  <sub>2026-05-19 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#21147`](https://github.com/erigontech/erigon/pull/21147) — [r3.4] db/state, cmd/integration: 4x larger commitment rebuild shard, squeeze flag transparent  
  <sub>2026-05-12 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#21143`](https://github.com/erigontech/erigon/pull/21143) — [r3.4] db/state, db/integrity: FilesOnlyStateReader for commitment rebuild and CommitmentRoot  
  <sub>2026-05-12 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#21116`](https://github.com/erigontech/erigon/pull/21116) — [r3.4] [1/3] cmd: improve commitment snapshot removal output (cherry-pick #20202)  
  <sub>2026-05-11 · merged · reviewed · score 5 · commit, commitment, snapshot</sub>
- [`erigontech/erigon#21071`](https://github.com/erigontech/erigon/pull/21071) — execution/commitmentdb: copy branch slice returned by TrieContext.Branch (#21034)  
  <sub>2026-05-08 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#21044`](https://github.com/erigontech/erigon/pull/21044) — [r3.4] execution/commitment/commitmentdb: own branch slice returned by TrieContext.Branch  
  <sub>2026-05-07 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#21034`](https://github.com/erigontech/erigon/pull/21034) — execution/commitmentdb: copy branch slice returned by `TrieContext.Branch` before sending via channel  
  <sub>2026-05-07 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#21026`](https://github.com/erigontech/erigon/pull/21026) — db/state, db/integrity: FilesOnlyStateReader for commitment rebuild and CommitmentRoot  
  <sub>2026-05-07 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#20963`](https://github.com/erigontech/erigon/pull/20963) — db/state: unify commitment-branch referencing predicate  
  <sub>2026-05-04 · merged · authored · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#20959`](https://github.com/erigontech/erigon/pull/20959) — commitment: remove WarmupCache.enabled atomic.Bool  
  <sub>2026-05-03 · merged · authored · score 5 · atomic, commit, commitment</sub>
- [`erigontech/erigon#20848`](https://github.com/erigontech/erigon/pull/20848) — cmd/utils: check txnum block lookups  
  <sub>2026-04-28 · merged · reviewed · score 5 · lookup, txn, txnum</sub>
- [`erigontech/erigon#20805`](https://github.com/erigontech/erigon/pull/20805) — parallel commitment calculations implemented  
  <sub>2026-04-25 · merged · reviewed · score 5 · commit, commitment, parallel</sub>
- [`erigontech/erigon#20481`](https://github.com/erigontech/erigon/pull/20481) — db/state: use --experimental.concurrent-commitment flag for rebuild  
  <sub>2026-04-10 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#20360`](https://github.com/erigontech/erigon/pull/20360) — db/state: RangeAsOf DB iterator starts from files.EndTxNum()  
  <sub>2026-04-06 · merged · reviewed · score 5 · state, txn, txnum</sub>
- [`erigontech/erigon#20306`](https://github.com/erigontech/erigon/pull/20306) — commitment: eliminate CellGetter callback — hashRow + pure EncodeBranch  
  <sub>2026-04-03 · merged · reviewed · score 5 · commit, commitment, encode</sub>
- [`erigontech/erigon#20265`](https://github.com/erigontech/erigon/pull/20265) — execution/cache: fix StateCache dropping deleted storage keys, causing stale reads  
  <sub>2026-04-01 · merged · reviewed · score 5 · stale read, state, storage</sub>
- [`erigontech/erigon#20207`](https://github.com/erigontech/erigon/pull/20207) — commitment: add context cancellation and remove dead mountedTries field  
  <sub>2026-03-27 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#20204`](https://github.com/erigontech/erigon/pull/20204) — db/state: disable ReplaceKeysInValues during RebuildCommitmentFiles  
  <sub>2026-03-27 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#20202`](https://github.com/erigontech/erigon/pull/20202) — cmd: improve commitment snapshot removal output  
  <sub>2026-03-27 · merged · reviewed · score 5 · commit, commitment, snapshot</sub>
- [`erigontech/erigon#20107`](https://github.com/erigontech/erigon/pull/20107) — commitment: trie trace recording for offline debugging  
  <sub>2026-03-23 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#20019`](https://github.com/erigontech/erigon/pull/20019) — [SharovBot] fix(rpc): use outer-DB tx fallback in eth_simulateV1 commitment reader (release/3.4)  
  <sub>2026-03-20 · merged · reviewed · score 5 · commit, commitment, tx </sub>
- [`erigontech/erigon#19999`](https://github.com/erigontech/erigon/pull/19999) — db/state: add HistoryKeyTxNumRange API  
  <sub>2026-03-19 · merged · reviewed · score 5 · state, txn, txnum</sub>
- [`erigontech/erigon#19966`](https://github.com/erigontech/erigon/pull/19966) — [wip] experiment: non-dupsort tables for commitment domain and history  
  <sub>2026-03-18 · closed · authored · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#19802`](https://github.com/erigontech/erigon/pull/19802) — commitmentdb: fix CommitmentReplayStateReader.Clone propagating wrong  
  <sub>2026-03-11 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#19610`](https://github.com/erigontech/erigon/pull/19610) — `erigon seg check-commitment-hist-at-blk-range`: use `madv_random` because it's highly-parallel cli command  
  <sub>2026-03-04 · merged · authored · score 5 · commit, commitment, parallel</sub>
- [`erigontech/erigon#19402`](https://github.com/erigontech/erigon/pull/19402) — SharedDomains: step4 towards eliminating txNum field   
  <sub>2026-02-22 · merged · authored · score 5 · domain, txn, txnum</sub>
- [`erigontech/erigon#19380`](https://github.com/erigontech/erigon/pull/19380) — SharedDomains: step3 towards eliminating txNum field   
  <sub>2026-02-21 · merged · authored · score 5 · domain, txn, txnum</sub>
- [`erigontech/erigon#19279`](https://github.com/erigontech/erigon/pull/19279) — SharedDomains: step2 towards eliminating txNum field  
  <sub>2026-02-18 · merged · authored · score 5 · domain, txn, txnum</sub>
- [`erigontech/erigon#19253`](https://github.com/erigontech/erigon/pull/19253) — fix: add bounds check in TransactionsSSZ.DecodeSSZ for malformed SSZ  
  <sub>2026-02-17 · merged · reviewed · score 5 · decode, ssz, transaction</sub>
- [`erigontech/erigon#19247`](https://github.com/erigontech/erigon/pull/19247) — SharedDomains: step1 towards eliminating txNum field  
  <sub>2026-02-17 · merged · authored · score 5 · domain, txn, txnum</sub>
- [`erigontech/erigon#19180`](https://github.com/erigontech/erigon/pull/19180) — check-commitment-hist-at-blk-range: parallel, add blockNum to error  
  <sub>2026-02-14 · merged · authored · score 5 · commit, commitment, parallel</sub>
- [`erigontech/erigon#18982`](https://github.com/erigontech/erigon/pull/18982) — SharedDomains: run CI on removed `SeekCommitment` from construtor  
  <sub>2026-02-05 · closed · authored · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#18617`](https://github.com/erigontech/erigon/pull/18617) — Commitment: parallel commitment updating  
  <sub>2026-01-10 · merged · reviewed · score 5 · commit, commitment, parallel</sub>
- [`erigontech/erigon#18609`](https://github.com/erigontech/erigon/pull/18609) — Add commitment lookup benchmarking  
  <sub>2026-01-09 · merged · reviewed · score 5 · commit, commitment, lookup</sub>
- [`erigontech/erigon#18600`](https://github.com/erigontech/erigon/pull/18600) — commitment/backtester: fix issues preventing para trie runs  
  <sub>2026-01-09 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#18597`](https://github.com/erigontech/erigon/pull/18597) — Add RangeLatest support for commitment domain  
  <sub>2026-01-08 · merged · reviewed · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#18339`](https://github.com/erigontech/erigon/pull/18339) — cp: rm-state: fix rm commitment decision (#18075)  
  <sub>2025-12-16 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#18075`](https://github.com/erigontech/erigon/pull/18075) — rm-state: fix rm commitment decision  
  <sub>2025-11-27 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#18011`](https://github.com/erigontech/erigon/pull/18011) — [3.3] remove experimental tag for historical commitments trie  
  <sub>2025-11-21 · merged · authored · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#18006`](https://github.com/erigontech/erigon/pull/18006) — Erigon: remove experimental tag for historical commitments trie  
  <sub>2025-11-20 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#17413`](https://github.com/erigontech/erigon/pull/17413) — Fix historical state queries from commitment  
  <sub>2025-10-10 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#16860`](https://github.com/erigontech/erigon/pull/16860) — cp: avoid extraneous commitment logs in rm-state  
  <sub>2025-08-27 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#16858`](https://github.com/erigontech/erigon/pull/16858) — Rely on schema for key referencing in commitment branches  
  <sub>2025-08-27 · merged · reviewed · score 5 · commit, commitment, schema</sub>
- [`erigontech/erigon#16771`](https://github.com/erigontech/erigon/pull/16771) — [r31] avoid extraneous commitment logs in rm-state  
  <sub>2025-08-22 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#16640`](https://github.com/erigontech/erigon/pull/16640) — [r31] fix wrong `hasRoot=true` during check on commitment state key  
  <sub>2025-08-14 · merged · reviewed · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#15317`](https://github.com/erigontech/erigon/pull/15317) — SD: remove `txNum` param from `IteratePrefix` (because it's `LatestState` method)  
  <sub>2025-05-29 · merged · authored · score 5 · state, txn, txnum</sub>
- [`erigontech/erigon#15197`](https://github.com/erigontech/erigon/pull/15197) — temporal.DomainPut: add txNum param  
  <sub>2025-05-21 · merged · authored · score 5 · domain, txn, txnum</sub>
- [`erigontech/erigon#15143`](https://github.com/erigontech/erigon/pull/15143) — refactor `sharedDomains.SeekCommitment` [step1]  
  <sub>2025-05-19 · merged · reviewed · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#14618`](https://github.com/erigontech/erigon/pull/14618) — no greedy prune of commitment hist on chain-tip  
  <sub>2025-04-16 · merged · authored+reviewed · score 5 · commit, commitment, prune</sub>
- [`erigontech/erigon#14221`](https://github.com/erigontech/erigon/pull/14221) — `blockReader.txnLookup` to not increment `txNum` before return  
  <sub>2025-03-19 · merged · authored · score 5 · lookup, txn, txnum</sub>
- [`erigontech/erigon#14165`](https://github.com/erigontech/erigon/pull/14165) — tx_lookup: use txNumReader with files  
  <sub>2025-03-15 · merged · authored · score 5 · lookup, txn, txnum</sub>
- [`erigontech/erigon#14009`](https://github.com/erigontech/erigon/pull/14009) — "less direct agg use": remove `sd.aggTx.d[kv.CommitmentDomain].Files()` add API `Files(domain)`  
  <sub>2025-02-28 · merged · authored+reviewed · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#12916`](https://github.com/erigontech/erigon/pull/12916) — commitment.EncodeBranch: rely on external copy  
  <sub>2024-11-29 · merged · authored · score 5 · commit, commitment, encode</sub>
- [`erigontech/erigon#12820`](https://github.com/erigontech/erigon/pull/12820) — [wip] experiment: d_lru for commitment domain  
  <sub>2024-11-21 · closed · authored · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#12752`](https://github.com/erigontech/erigon/pull/12752) — antiquate: close rotx before long (compressing/indexing) operations   
  <sub>2024-11-18 · merged · authored · score 5 · compress, index, tx </sub>
- [`erigontech/erigon#12470`](https://github.com/erigontech/erigon/pull/12470) — Parallel receipts root to `ComputeCommitment`  
  <sub>2024-10-24 · closed · reviewed · score 5 · commit, commitment, parallel</sub>
- [`erigontech/erigon#11664`](https://github.com/erigontech/erigon/pull/11664) — Prune `MaxTxNums` table  
  <sub>2024-08-18 · merged · reviewed · score 5 · prune, txn, txnum</sub>
- [`erigontech/erigon#11445`](https://github.com/erigontech/erigon/pull/11445) — commitment: use Update for domain IO  
  <sub>2024-08-01 · merged · reviewed · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#11438`](https://github.com/erigontech/erigon/pull/11438) — `commitment`: do not sort trie branch updates  
  <sub>2024-08-01 · merged · reviewed · score 5 · commit, commitment, trie</sub>
- [`erigontech/erigon#10871`](https://github.com/erigontech/erigon/pull/10871) — handle case when account.kv is ahead of commitment.kv and we do `rm -rf chaindata`  
  <sub>2024-06-24 · merged · authored · score 5 · account, commit, commitment</sub>
- [`erigontech/erigon#10698`](https://github.com/erigontech/erigon/pull/10698) — e3: call `DiscardHistory(kv.CommitmentDomain)` before `h.newWriter()`  
  <sub>2024-06-11 · merged · authored · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#10677`](https://github.com/erigontech/erigon/pull/10677) — state diff: disable commitment history write on chain tip  
  <sub>2024-06-09 · merged · authored · score 5 · commit, commitment, state</sub>
- [`erigontech/erigon#10612`](https://github.com/erigontech/erigon/pull/10612) — move file lock inside SD.ComputeCommitment to prevent un-decodable commit branch during merge  
  <sub>2024-06-04 · merged · reviewed · score 5 · commit, commitment, merge</sub>
- [`erigontech/erigon#10363`](https://github.com/erigontech/erigon/pull/10363) — Skip FCU altogether if domains cannot be opened due to commitment being behind  
  <sub>2024-05-15 · merged · reviewed · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#10012`](https://github.com/erigontech/erigon/pull/10012) — e35: avoid using `dirtyFilesMinimaxTxNum` in prune/build methods  
  <sub>2024-04-22 · merged · authored · score 5 · prune, txn, txnum</sub>
- [`erigontech/erigon#9727`](https://github.com/erigontech/erigon/pull/9727) — snapshots: fix system tx hash in transactions indexes  
  <sub>2024-03-16 · merged · reviewed · score 5 · index, snapshot, snapshots, transaction, tx </sub>
- [`erigontech/erigon#9249`](https://github.com/erigontech/erigon/pull/9249) — e35: prune correct 'to tx num'  
  <sub>2024-01-17 · closed · authored · score 5 · prune, tx , tx num</sub>
- [`erigontech/erigon#9022`](https://github.com/erigontech/erigon/pull/9022) — e35: use SharedDomains as RwTx interface   
  <sub>2023-12-19 · merged · authored · score 5 · domain, rwtx, tx </sub>
- [`erigontech/erigon#8977`](https://github.com/erigontech/erigon/pull/8977) — e35 commitment updates to domain wal  
  <sub>2023-12-13 · merged · reviewed · score 5 · commit, commitment, domain</sub>
- [`erigontech/erigon#8805`](https://github.com/erigontech/erigon/pull/8805) — e35: force reopen aggctx at stage_snapshots - otherwise next stages will not see just-indexed-files  
  <sub>2023-11-21 · merged · authored · score 5 · index, snapshot, snapshots, stage, tx </sub>
- [`erigontech/erigon#8732`](https://github.com/erigontech/erigon/pull/8732) — e35: "integration stage_exec --reset" call seek once, calc commitment AFTER reset.  
  <sub>2023-11-15 · merged · authored · score 5 · commit, commitment, stage</sub>
- [`erigontech/erigon#8666`](https://github.com/erigontech/erigon/pull/8666) — e35: don't rely on "txnum" index as on "execution progress"  
  <sub>2023-11-07 · merged · authored · score 5 · index, txn, txnum</sub>
- [`erigontech/erigon#7914`](https://github.com/erigontech/erigon/pull/7914) — e35: commitment before prune  
  <sub>2023-07-21 · merged · authored · score 5 · commit, commitment, prune</sub>
- [`erigontech/erigon#5860`](https://github.com/erigontech/erigon/pull/5860) — e3: better prune logs, apply thread can work without rwTx  
  <sub>2022-10-25 · merged · authored · score 5 · prune, rwtx, tx </sub>
- [`erigontech/erigon#4731`](https://github.com/erigontech/erigon/pull/4731) — commitment: generic btree  
  <sub>2022-07-18 · merged · authored · score 5 · btree, commit, commitment</sub>
- [`erigontech/erigon#1734`](https://github.com/erigontech/erigon/pull/1734) — Move TxPool stage to rwtx  
  <sub>2021-04-16 · merged · authored · score 5 · rwtx, stage, tx </sub>
- [`erigontech/erigon#1677`](https://github.com/erigontech/erigon/pull/1677) — Move reset state functions to RwTX  
  <sub>2021-04-05 · merged · authored · score 5 · rwtx, state, tx </sub>
- [`erigontech/erigon#1670`](https://github.com/erigontech/erigon/pull/1670) — Mutation: implement StatelessRwTx  
  <sub>2021-04-03 · merged · reviewed · score 5 · rwtx, state, tx </sub>
- [`erigontech/erigon#1661`](https://github.com/erigontech/erigon/pull/1661) — bitmapdb to use rwtx  
  <sub>2021-04-02 · merged · authored · score 5 · bitmap, rwtx, tx </sub>
- [`erigontech/silkworm#105`](https://github.com/erigontech/silkworm/pull/105) — Guard against db migration to store transactions individually  
  <sub>2020-11-19 · merged · reviewed · score 5 · db migration, migration, transaction</sub>
- [`ledgerwatch/erigon-lib#525`](https://github.com/ledgerwatch/erigon-lib/pull/525) — commitment: generic btree, part2  
  <sub>2022-07-18 · merged · authored · score 5 · btree, commit, commitment</sub>
- [`ledgerwatch/erigon-lib#523`](https://github.com/ledgerwatch/erigon-lib/pull/523) — commitment: generic btree  
  <sub>2022-07-18 · merged · authored · score 5 · btree, commit, commitment</sub>
- [`erigontech/erigon#21790`](https://github.com/erigontech/erigon/pull/21790) — [wip] [3.6] commitment: skip `GetLatest` for keys creation  
  <sub>2026-06-13 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#21789`](https://github.com/erigontech/erigon/pull/21789) — [bloatnet] commitment: for new branch nodes to skip `GetLatest` call   
  <sub>2026-06-13 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#21721`](https://github.com/erigontech/erigon/pull/21721) — [r3.5] commitment: fix warmuper arena data race in HashSort  
  <sub>2026-06-10 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#21432`](https://github.com/erigontech/erigon/pull/21432) — commitment: fix warmuper arena data race in HashSort  
  <sub>2026-05-26 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#21375`](https://github.com/erigontech/erigon/pull/21375) — [performance] Disable referenced keys in commitment files, bump version  
  <sub>2026-05-23 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#21141`](https://github.com/erigontech/erigon/pull/21141) — [r3.4] commitment: nibbles consolidation (#20407)  
  <sub>2026-05-12 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#21095`](https://github.com/erigontech/erigon/pull/21095) — [performance] cp commitment rebuild relevant PRs  
  <sub>2026-05-11 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#21029`](https://github.com/erigontech/erigon/pull/21029) — db/integrity: enable CommitmentRoot check on all .kv files  
  <sub>2026-05-07 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20939`](https://github.com/erigontech/erigon/pull/20939) — cmd/integration: allow resume of commitment rebuild (no history case)  
  <sub>2026-05-01 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20918`](https://github.com/erigontech/erigon/pull/20918) — commitment: compare deferred and eager roots  
  <sub>2026-04-30 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20813`](https://github.com/erigontech/erigon/pull/20813) — bloatnet: disable `CheckCommitmentKvDeref`   
  <sub>2026-04-25 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20803`](https://github.com/erigontech/erigon/pull/20803) — db/integrity: use injected logger in CheckCommitmentRoot  
  <sub>2026-04-24 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20796`](https://github.com/erigontech/erigon/pull/20796) — execution/commitmentdb: test branch data ownership  
  <sub>2026-04-24 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20555`](https://github.com/erigontech/erigon/pull/20555) — [r3.4] commitment, execctx: fix InsertBlocks failure during block catch-up  
  <sub>2026-04-14 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20546`](https://github.com/erigontech/erigon/pull/20546) — commitment, execctx: fix InsertBlocks failure during block catch-up  
  <sub>2026-04-14 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20411`](https://github.com/erigontech/erigon/pull/20411) — cmd/utils/app: make --from optional in check-commitment-hist-at-blk-range  
  <sub>2026-04-08 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20388`](https://github.com/erigontech/erigon/pull/20388) — commitment: simplify unfold if branch  
  <sub>2026-04-07 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20347`](https://github.com/erigontech/erigon/pull/20347) — db/integrity: check-commitment-hist-at-blk to consider DB data  
  <sub>2026-04-06 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20295`](https://github.com/erigontech/erigon/pull/20295) — cmd/integration: enable historical commitment config during rebuild  
  <sub>2026-04-02 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20291`](https://github.com/erigontech/erigon/pull/20291) — integration: add --yes to skip interactive prompts in commitment rebuild  
  <sub>2026-04-02 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20286`](https://github.com/erigontech/erigon/pull/20286) — [wip] `HistoryKeyTxNumIterFiles`: less copy/append  
  <sub>2026-04-02 · open · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#20266`](https://github.com/erigontech/erigon/pull/20266) — cp: commitment history rebuild and associated commits  
  <sub>2026-04-01 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20242`](https://github.com/erigontech/erigon/pull/20242) — integrity: faster CheckCommitmentHistAtBlk   
  <sub>2026-03-31 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#20073`](https://github.com/erigontech/erigon/pull/20073) — commitment rebuild: `--yes` to bypass prompt for background run  
  <sub>2026-03-23 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19945`](https://github.com/erigontech/erigon/pull/19945) — HistoryKeyTxNumIterFiles: re-use multi-seq reader and iterator  
  <sub>2026-03-17 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#19941`](https://github.com/erigontech/erigon/pull/19941) — d_lru: disable for commitment (it's useful for re-exec from 0, but i didn't test impact on chaintip)  
  <sub>2026-03-17 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19925`](https://github.com/erigontech/erigon/pull/19925) — db/integrity: add aggregate progress logs for CommitmentHistVal  
  <sub>2026-03-16 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19899`](https://github.com/erigontech/erigon/pull/19899) — [wip] commitment: lazy hashing  
  <sub>2026-03-15 · closed · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19887`](https://github.com/erigontech/erigon/pull/19887) — commitment: add warmup cache hit/miss metrics  
  <sub>2026-03-14 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19832`](https://github.com/erigontech/erigon/pull/19832) — Add commitment internals panels to Grafana dashboard  
  <sub>2026-03-12 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19774`](https://github.com/erigontech/erigon/pull/19774) — mark `commitment history` feature as non-experimental  
  <sub>2026-03-10 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19757`](https://github.com/erigontech/erigon/pull/19757) — txpool: replace custom RLP parsing with standard transaction types  
  <sub>2026-03-09 · merged · reviewed · score 4 · rlp , transaction</sub>
- [`erigontech/erigon#19676`](https://github.com/erigontech/erigon/pull/19676) — integrity: enable CheckCommitmentHistAtBlkRange by default   
  <sub>2026-03-06 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19651`](https://github.com/erigontech/erigon/pull/19651) — commitment: reduce HashSort allocations with arena+slab  
  <sub>2026-03-05 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19642`](https://github.com/erigontech/erigon/pull/19642) — `check-commitment-hist-at-blk-range`: support empty blocks, sampling logic extraction  
  <sub>2026-03-05 · merged · authored+reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19625`](https://github.com/erigontech/erigon/pull/19625) — commitment: span-based lazy copy for ReplacePlainKeys + benchmark suite  
  <sub>2026-03-04 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19613`](https://github.com/erigontech/erigon/pull/19613) — `erigon seg check-commitment-hist-at-blk-range`: friendly logging   
  <sub>2026-03-04 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19609`](https://github.com/erigontech/erigon/pull/19609) — `erigon seg check-commitment-hist-at-blk-range`: reproducible sampling  
  <sub>2026-03-04 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19508`](https://github.com/erigontech/erigon/pull/19508) — Revert "[wip] sd: removing txNum field "  
  <sub>2026-02-26 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#19489`](https://github.com/erigontech/erigon/pull/19489) — [wip] sd: removing txNum field   
  <sub>2026-02-25 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#19481`](https://github.com/erigontech/erigon/pull/19481) — sd: txnum remove step4  
  <sub>2026-02-25 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#19432`](https://github.com/erigontech/erigon/pull/19432) — add file-integrity-cache for commitment checks  
  <sub>2026-02-23 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19099`](https://github.com/erigontech/erigon/pull/19099) — CommitmentHistory: dedup   
  <sub>2026-02-11 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#19081`](https://github.com/erigontech/erigon/pull/19081) — add HistoryKeyTxNumRange and MultisetKV  
  <sub>2026-02-10 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#19016`](https://github.com/erigontech/erigon/pull/19016) — cmd/integration: commitment rebuild with history support  
  <sub>2026-02-06 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18960`](https://github.com/erigontech/erigon/pull/18960) — handle edge case for genesis block in SeekCommitment  
  <sub>2026-02-04 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18917`](https://github.com/erigontech/erigon/pull/18917) —  execution: restore commitment deferred updates hook mechanism  
  <sub>2026-02-01 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18879`](https://github.com/erigontech/erigon/pull/18879) — execution/eth1: fix flake in TestValidateChainWithLastTxNumOfBlockAtStepBoundary  
  <sub>2026-01-30 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#18850`](https://github.com/erigontech/erigon/pull/18850) — perf(cl/utils): optimize KzgCommitmentToVersionedHash to eliminate redundant allocations  
  <sub>2026-01-28 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18816`](https://github.com/erigontech/erigon/pull/18816) — Add missing tx.Commit() in stage_snapshots  
  <sub>2026-01-26 · merged · reviewed · score 4 · commit, snapshot, snapshots, stage</sub>
- [`erigontech/erigon#18774`](https://github.com/erigontech/erigon/pull/18774) — fix for some commitment.kv using more plainkeys than references  
  <sub>2026-01-23 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18750`](https://github.com/erigontech/erigon/pull/18750) — [performance] cherry-pick: handle rcache and commitment files in publishable (#18735)  
  <sub>2026-01-21 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18735`](https://github.com/erigontech/erigon/pull/18735) — handle rcache and commitment files in publishable  
  <sub>2026-01-21 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18626`](https://github.com/erigontech/erigon/pull/18626) — execution/commitment: fix race regression  
  <sub>2026-01-12 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18561`](https://github.com/erigontech/erigon/pull/18561) — Erigon: fix the disgusting commitment value transformer  
  <sub>2026-01-06 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18543`](https://github.com/erigontech/erigon/pull/18543) — Performance: fixed allocs in commitment's value transformer.  
  <sub>2026-01-03 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18487`](https://github.com/erigontech/erigon/pull/18487) — fix use of `ReplaceKeysInValues` feature in commitment_rebuild  
  <sub>2025-12-28 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18400`](https://github.com/erigontech/erigon/pull/18400) — commitment/backtester: add initial branch load metrics  
  <sub>2025-12-21 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18254`](https://github.com/erigontech/erigon/pull/18254) — db/integrity: add missed .kv filter in CheckCommitmentRoot  
  <sub>2025-12-11 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18176`](https://github.com/erigontech/erigon/pull/18176) — db/integrity: tidy unused integrityErr variable in some commitment checks  
  <sub>2025-12-05 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#18096`](https://github.com/erigontech/erigon/pull/18096) — cmd: remove duplicate cmd for printing block tx nums  
  <sub>2025-11-28 · merged · reviewed · score 4 · tx , tx num</sub>
- [`erigontech/erigon#17535`](https://github.com/erigontech/erigon/pull/17535) — Refactor txNum ranges -> step ranges logic  
  <sub>2025-10-19 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#17530`](https://github.com/erigontech/erigon/pull/17530) — Commitment: renamings and movements  
  <sub>2025-10-17 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#16939`](https://github.com/erigontech/erigon/pull/16939) — less calls of `doms.TxNum()`/`doms.BlockNum()`  
  <sub>2025-09-02 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#16779`](https://github.com/erigontech/erigon/pull/16779) — fix rebuilding commitment by smaller shards  
  <sub>2025-08-22 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#16726`](https://github.com/erigontech/erigon/pull/16726) — `integration commitment_rebuild` clarifications and fixes  
  <sub>2025-08-19 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#16697`](https://github.com/erigontech/erigon/pull/16697) — [wip] commitment: to use `etl.OldestEnryBuffer` instead of `map`  
  <sub>2025-08-18 · closed · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#16696`](https://github.com/erigontech/erigon/pull/16696) — [r32] rebuild_commitment: add `--squeeze=false`, improve logs  
  <sub>2025-08-18 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#16393`](https://github.com/erigontech/erigon/pull/16393) — adds debug tool seg txnum tool for block <-> txNum conversions  
  <sub>2025-07-31 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#16392`](https://github.com/erigontech/erigon/pull/16392) — adds debug tool `seg txnum` tool for block <-> txNum conversions  
  <sub>2025-07-31 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#16373`](https://github.com/erigontech/erigon/pull/16373) — cp: add runtime check when DumpBlocks erroneously uses lastTxNum=0  
  <sub>2025-07-30 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#16342`](https://github.com/erigontech/erigon/pull/16342) — [r31] add runtime check when DumpBlocks erroneously uses lastTxNum=0  
  <sub>2025-07-29 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#16054`](https://github.com/erigontech/erigon/pull/16054) — disable rcache integrity check for system tx  
  <sub>2025-07-11 · merged · reviewed · score 4 · integrity check, tx </sub>
- [`erigontech/erigon#15815`](https://github.com/erigontech/erigon/pull/15815) — [r30] pick `txNum+2` elimination  
  <sub>2025-06-28 · closed · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15787`](https://github.com/erigontech/erigon/pull/15787) — Backward-compatible `--experimental.commitment-history` flag  
  <sub>2025-06-27 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#15782`](https://github.com/erigontech/erigon/pull/15782) — cp: rpc: use pre-configured txNumReader (it's thread-safe)  
  <sub>2025-06-27 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15658`](https://github.com/erigontech/erigon/pull/15658) — Concurrent warmup for Commitment  
  <sub>2025-06-19 · closed · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#15645`](https://github.com/erigontech/erigon/pull/15645) — share and use txnumreader cache via blockreader (#15597)  
  <sub>2025-06-19 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15626`](https://github.com/erigontech/erigon/pull/15626) — use rlp StreamPool for tx decoding  
  <sub>2025-06-18 · merged · reviewed · score 4 · rlp , tx </sub>
- [`erigontech/erigon#15625`](https://github.com/erigontech/erigon/pull/15625) — integration commitment_rebuild: re-visit command, add docs    
  <sub>2025-06-18 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#15617`](https://github.com/erigontech/erigon/pull/15617) — remote BlockForTxNum  
  <sub>2025-06-17 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15611`](https://github.com/erigontech/erigon/pull/15611) — agg: revert `AggregatorSqueezeCommitmentValues`  
  <sub>2025-06-17 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#15597`](https://github.com/erigontech/erigon/pull/15597) — share and use txnumreader cache via blockreader  
  <sub>2025-06-16 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15489`](https://github.com/erigontech/erigon/pull/15489) — [r30] pick PR about txNum of receipt  
  <sub>2025-06-06 · closed · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15376`](https://github.com/erigontech/erigon/pull/15376) — rpcd: pass global _txNumReader   
  <sub>2025-05-31 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15297`](https://github.com/erigontech/erigon/pull/15297) — sd: step towards removing txNum  
  <sub>2025-05-28 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15192`](https://github.com/erigontech/erigon/pull/15192) — [r30] adjust txnum fro current env   
  <sub>2025-05-21 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15191`](https://github.com/erigontech/erigon/pull/15191) — [r30] adjust txnum fro current env  
  <sub>2025-05-21 · closed · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15189`](https://github.com/erigontech/erigon/pull/15189) — [r30] --latest and --step file removal with purified commitment protection   
  <sub>2025-05-21 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#15103`](https://github.com/erigontech/erigon/pull/15103) — [r30] persistent receipts in eth_getLogs used wrong txNum  
  <sub>2025-05-17 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#15102`](https://github.com/erigontech/erigon/pull/15102) — [r31] persistent receipts in eth_getLogs used wrong txNum  
  <sub>2025-05-17 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#14774`](https://github.com/erigontech/erigon/pull/14774) — commitment.v version  
  <sub>2025-04-27 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#14751`](https://github.com/erigontech/erigon/pull/14751) — Moved tx rlp resolve out of mutex lock context  
  <sub>2025-04-25 · merged · reviewed · score 4 · rlp , tx </sub>
- [`erigontech/erigon#14733`](https://github.com/erigontech/erigon/pull/14733) — measure chain-tip impact of removing `txnum` field from buffered writers  
  <sub>2025-04-24 · merged · authored+reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#14707`](https://github.com/erigontech/erigon/pull/14707) — Reuse internal _txNumReader  
  <sub>2025-04-23 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#14684`](https://github.com/erigontech/erigon/pull/14684) — Add internal_ namespace + internal_getTxNumInfo method  
  <sub>2025-04-22 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#14665`](https://github.com/erigontech/erigon/pull/14665) — purify: return meaningful error when have commitment.kv files but they all purified  
  <sub>2025-04-18 · closed · authored+reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#14603`](https://github.com/erigontech/erigon/pull/14603) — integration: support commitment history experiment  
  <sub>2025-04-15 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#14575`](https://github.com/erigontech/erigon/pull/14575) — rpc: use pre-configured txNumReader (it's thread-safe)  
  <sub>2025-04-12 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#14536`](https://github.com/erigontech/erigon/pull/14536) — Commitment: rehash code only with asserts  
  <sub>2025-04-10 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#14535`](https://github.com/erigontech/erigon/pull/14535) — kv: streams to be safe with RwTx possible update/delete  
  <sub>2025-04-10 · merged · authored · score 4 · rwtx, tx </sub>
- [`erigontech/erigon#14490`](https://github.com/erigontech/erigon/pull/14490) — collect commitment processing data  
  <sub>2025-04-08 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#14483`](https://github.com/erigontech/erigon/pull/14483) — Commitment: get rid of branch cache inside commitment context  
  <sub>2025-04-07 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#14481`](https://github.com/erigontech/erigon/pull/14481) — Commitment: remove unused parameter tempdir  
  <sub>2025-04-07 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#14098`](https://github.com/erigontech/erigon/pull/14098) — txnum eradication in rpc  
  <sub>2025-03-06 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#13521`](https://github.com/erigontech/erigon/pull/13521) — In-memory hashsort for commitment keys  
  <sub>2025-01-21 · closed · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#13509`](https://github.com/erigontech/erigon/pull/13509) — Commitment: do not use cell getter function to fold the row  
  <sub>2025-01-20 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#13348`](https://github.com/erigontech/erigon/pull/13348) — commitment: clarify update kind based on `afterMap`  
  <sub>2025-01-08 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#13183`](https://github.com/erigontech/erigon/pull/13183) — [DNM] adds --commitment.history flag to produce proof history  
  <sub>2024-12-19 · closed · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#12994`](https://github.com/erigontech/erigon/pull/12994) — `DISCARD_COMMITMENT=true` produce commitment for genesis  
  <sub>2024-12-04 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#12966`](https://github.com/erigontech/erigon/pull/12966) — commitment.Update: use `string` key for less conversions  
  <sub>2024-12-03 · closed · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#12914`](https://github.com/erigontech/erigon/pull/12914) — commitment: reuse pre-allocated buffer for hash computation, step2  
  <sub>2024-11-29 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#12912`](https://github.com/erigontech/erigon/pull/12912) — commitment: avoid binary.Wirte   
  <sub>2024-11-29 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#12835`](https://github.com/erigontech/erigon/pull/12835) — commitment: collect skip ratios when `ERIGON_KV_READ_METRICS=true`  
  <sub>2024-11-21 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#12812`](https://github.com/erigontech/erigon/pull/12812) — commitment: reuse pre-allocated buffer for hash computation  
  <sub>2024-11-20 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#12497`](https://github.com/erigontech/erigon/pull/12497) — update for SqueezeCommitment  
  <sub>2024-10-25 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#12234`](https://github.com/erigontech/erigon/pull/12234) — [wip] TxNums asserts + ForcedWrite revise  
  <sub>2024-10-07 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#12099`](https://github.com/erigontech/erigon/pull/12099) — commitment: disable bloom filter  
  <sub>2024-09-26 · closed · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#11717`](https://github.com/erigontech/erigon/pull/11717) — Commitment: finish clarify names  
  <sub>2024-08-22 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#11528`](https://github.com/erigontech/erigon/pull/11528) — `Commitment`: remove keys from `Update`  
  <sub>2024-08-08 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#11517`](https://github.com/erigontech/erigon/pull/11517) — Commitment code cleanup  
  <sub>2024-08-07 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#11440`](https://github.com/erigontech/erigon/pull/11440) — `Commitment`: sort hashed keys at first seen  
  <sub>2024-08-01 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#10980`](https://github.com/erigontech/erigon/pull/10980) — cache readers for merging commitment range  
  <sub>2024-07-02 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#10924`](https://github.com/erigontech/erigon/pull/10924) — remove `frozed` parameter from maxTxNumInFiles  
  <sub>2024-06-27 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#10703`](https://github.com/erigontech/erigon/pull/10703) — skip commitment updates if its equal to predecessor  
  <sub>2024-06-11 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#10517`](https://github.com/erigontech/erigon/pull/10517) — store less commitment history on chain-tip  
  <sub>2024-05-28 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#10416`](https://github.com/erigontech/erigon/pull/10416) — e3 commitment history backpressure  
  <sub>2024-05-20 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#10290`](https://github.com/erigontech/erigon/pull/10290) — Refactor maxTxNumInFiles logic; rename cold param to clarify its meaning  
  <sub>2024-05-12 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#10109`](https://github.com/erigontech/erigon/pull/10109) — nodedb: UpdateNode method to create 1 rwtx instead of 2  
  <sub>2024-04-28 · merged · authored+reviewed · score 4 · rwtx, tx </sub>
- [`erigontech/erigon#10049`](https://github.com/erigontech/erigon/pull/10049) — E3 commitment tweaks  
  <sub>2024-04-24 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#9965`](https://github.com/erigontech/erigon/pull/9965) — e35: if finish < block_snaps then process this blocks without global rwtx   
  <sub>2024-04-17 · merged · authored · score 4 · rwtx, tx </sub>
- [`erigontech/erigon#9862`](https://github.com/erigontech/erigon/pull/9862) — e35: discard commitment history flag  
  <sub>2024-04-04 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#9802`](https://github.com/erigontech/erigon/pull/9802) — retry make canonical bodies in case of txnums  append gap  
  <sub>2024-03-25 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/erigon#9533`](https://github.com/erigontech/erigon/pull/9533) — E35 replace values in commitment  
  <sub>2024-02-28 · merged · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#9447`](https://github.com/erigontech/erigon/pull/9447) — e35: don't produce commitment.v files - attempt 2   
  <sub>2024-02-15 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#9376`](https://github.com/erigontech/erigon/pull/9376) — [wip] e35: txnum truncate - in forkchoice - v2  
  <sub>2024-02-05 · closed · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#9172`](https://github.com/erigontech/erigon/pull/9172) — [dbg] e35: commitment read ahead  
  <sub>2024-01-09 · closed · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#9171`](https://github.com/erigontech/erigon/pull/9171) — e35: don't produce commitment.v and .ef files   
  <sub>2024-01-09 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#9081`](https://github.com/erigontech/erigon/pull/9081) — e35: sys tx history integrity check  
  <sub>2023-12-26 · merged · authored · score 4 · integrity check, tx </sub>
- [`erigontech/erigon#9078`](https://github.com/erigontech/erigon/pull/9078) — e35: set txNum before exec  
  <sub>2023-12-25 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#8994`](https://github.com/erigontech/erigon/pull/8994) — e35: iter - .kv files txNum must be smaller than db txNum  
  <sub>2023-12-15 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#8770`](https://github.com/erigontech/erigon/pull/8770) — e35: SeekCommitment - when no commitment.ef and .v files -> fallback to .kv  
  <sub>2023-11-18 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#8749`](https://github.com/erigontech/erigon/pull/8749) —  e3 commitment seek/restore  
  <sub>2023-11-16 · closed · reviewed · score 4 · commit, commitment</sub>
- [`erigontech/erigon#8737`](https://github.com/erigontech/erigon/pull/8737) — e35: SeekCommitment - doesn't see history of commitment  
  <sub>2023-11-16 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#8696`](https://github.com/erigontech/erigon/pull/8696) — e35: commitment.historyLargeValues=false  
  <sub>2023-11-11 · merged · authored · score 4 · commit, commitment</sub>
- [`erigontech/erigon#7028`](https://github.com/erigontech/erigon/pull/7028) — e3: don't loose last txnum  
  <sub>2023-03-06 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#6663`](https://github.com/erigontech/erigon/pull/6663) — e3: move txnum to erigon-lib  
  <sub>2023-01-22 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#6540`](https://github.com/erigontech/erigon/pull/6540) — e3: invalid txnum table  
  <sub>2023-01-10 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#6026`](https://github.com/erigontech/erigon/pull/6026) — Allow bigger jumps in 1 RwTx - for consistency  
  <sub>2022-11-11 · merged · authored · score 4 · rwtx, tx </sub>
- [`erigontech/erigon#5676`](https://github.com/erigontech/erigon/pull/5676) — e3: getLogsV3 fix history txnum  
  <sub>2022-10-09 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#5465`](https://github.com/erigontech/erigon/pull/5465) — erigon22: "max txNum of a block N" semantic   
  <sub>2022-09-22 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#5211`](https://github.com/erigontech/erigon/pull/5211) — erigon22: MakeCanonical must update txNums  
  <sub>2022-08-29 · merged · authored · score 4 · txn, txnum</sub>
- [`erigontech/erigon#4802`](https://github.com/erigontech/erigon/pull/4802) — Pool: parse rlp chain id for non-legacy transactions   
  <sub>2022-07-23 · merged · authored · score 4 · rlp , transaction</sub>
- [`erigontech/erigon#4799`](https://github.com/erigontech/erigon/pull/4799) — Pool: parse rlp chain id for non-legacy transactions   
  <sub>2022-07-23 · merged · authored · score 4 · rlp , transaction</sub>
- [`erigontech/erigon#3827`](https://github.com/erigontech/erigon/pull/3827) — Prohibit EIP-2718 txn wrapped as RLP strings  
  <sub>2022-04-05 · merged · reviewed · score 4 · rlp , txn</sub>
- [`erigontech/erigon#3745`](https://github.com/erigontech/erigon/pull/3745) — Snapshots: script to auto-commit torrent hashes  
  <sub>2022-03-21 · merged · authored · score 4 · commit, snapshot, snapshots, torrent</sub>
- [`erigontech/erigon#3637`](https://github.com/erigontech/erigon/pull/3637) — rpcdaemon: limit amount of read transactions   
  <sub>2022-03-03 · merged · authored · score 4 · read transaction, transaction</sub>
- [`erigontech/erigon#3214`](https://github.com/erigontech/erigon/pull/3214) — Snapshots: tx lookup in RPC from snapshots  
  <sub>2022-01-07 · merged · authored · score 4 · lookup, snapshot, snapshots, tx </sub>
- [`erigontech/erigon#2969`](https://github.com/erigontech/erigon/pull/2969) — [wip] Canonical Transaction ID's (delete txs on unwind)  
  <sub>2021-11-16 · closed · authored · score 4 · transaction, unwind</sub>
- [`erigontech/erigon#2967`](https://github.com/erigontech/erigon/pull/2967) — P2p pooled tx rlp stable  
  <sub>2021-11-16 · merged · authored · score 4 · rlp , tx </sub>
- [`erigontech/erigon#2966`](https://github.com/erigontech/erigon/pull/2966) — P2p pooled tx rlp stable  
  <sub>2021-11-16 · closed · authored · score 4 · rlp , tx </sub>
- [`erigontech/erigon#2965`](https://github.com/erigontech/erigon/pull/2965) — Pool: PooledTransactions to produce correct rlp for non-legacy txs   
  <sub>2021-11-16 · merged · authored · score 4 · rlp , transaction</sub>
- [`erigontech/erigon#2902`](https://github.com/erigontech/erigon/pull/2902) — Recsplit: add first byte of hash to txn payload  
  <sub>2021-11-02 · merged · authored · score 4 · recsplit, txn</sub>
- [`erigontech/erigon#2366`](https://github.com/erigontech/erigon/pull/2366) — Increase read transactions limit to 32K  
  <sub>2021-07-14 · merged · authored · score 4 · read transaction, transaction</sub>
- [`erigontech/erigon#1722`](https://github.com/erigontech/erigon/pull/1722) — Continue move to rwtx  
  <sub>2021-04-15 · merged · authored · score 4 · rwtx, tx </sub>
- [`erigontech/erigon#1287`](https://github.com/erigontech/erigon/pull/1287) — Allow start read transactions from ethdb.Database interface  
  <sub>2020-10-24 · merged · authored · score 4 · read transaction, transaction</sub>
- [`erigontech/interfaces#257`](https://github.com/erigontech/interfaces/pull/257) — BlockForTxNum in ethbackend  
  <sub>2025-06-17 · merged · reviewed · score 4 · txn, txnum</sub>
- [`erigontech/interfaces#240`](https://github.com/erigontech/interfaces/pull/240) — added new method for finding txNum by its hash  
  <sub>2024-10-23 · merged · reviewed · score 4 · txn, txnum</sub>
- [`ledgerwatch/erigon-lib#847`](https://github.com/ledgerwatch/erigon-lib/pull/847) — e3: move txnum to erigon-lib  
  <sub>2023-01-22 · merged · authored · score 4 · txn, txnum</sub>
- [`ledgerwatch/erigon-lib#828`](https://github.com/ledgerwatch/erigon-lib/pull/828) — e3: invalid txnum table  
  <sub>2023-01-10 · merged · authored · score 4 · txn, txnum</sub>
- [`ledgerwatch/erigon-lib#542`](https://github.com/ledgerwatch/erigon-lib/pull/542) — Pool: parse rlp chain id for non-legacy transactions  
  <sub>2022-07-22 · merged · authored+reviewed · score 4 · rlp , transaction</sub>
- [`ledgerwatch/erigon-lib#167`](https://github.com/ledgerwatch/erigon-lib/pull/167) — P2p pooled tx rlp stable  
  <sub>2021-11-16 · merged · authored · score 4 · rlp , tx </sub>
- [`erigontech/erigon#21353`](https://github.com/erigontech/erigon/pull/21353) — shutdown: propagate ctx in FillDBFromSnapshots  
  <sub>2026-05-22 · merged · authored · score 3 · snapshot, snapshots, tx </sub>
- [`erigontech/erigon#19699`](https://github.com/erigontech/erigon/pull/19699) — Deduplicate zero-copy helpers, RPC state reader boilerplate, and Bor tx lookup  
  <sub>2026-03-06 · merged · reviewed · score 3 · lookup, state, tx </sub>
- [`erigontech/erigon#19470`](https://github.com/erigontech/erigon/pull/19470) — stream on `rwtx`: to use `.Current()` instead of storing pointers in stream object (`rwtx` may change data under pointers)  
  <sub>2026-02-25 · merged · authored · score 3 · rwtx</sub>
- [`erigontech/erigon#18094`](https://github.com/erigontech/erigon/pull/18094) — cmd: add rollback-snapshots-to-block  
  <sub>2025-11-28 · merged · reviewed · score 3 · rollback, snapshot, snapshots</sub>
- [`erigontech/erigon#15162`](https://github.com/erigontech/erigon/pull/15162) — split `SharedDomains` s4: extract usage of sd with sdctx used per trie  
  <sub>2025-05-19 · merged · reviewed · score 3 · domain, trie, tx </sub>
- [`erigontech/erigon#14046`](https://github.com/erigontech/erigon/pull/14046) — RoSnapshots: atomic workers field  
  <sub>2025-03-04 · merged · authored · score 3 · atomic, snapshot, snapshots</sub>
- [`erigontech/erigon#12540`](https://github.com/erigontech/erigon/pull/12540) — prune: txn_lookup more aggressive on non-chain-tip  
  <sub>2024-10-30 · merged · authored · score 3 · lookup, prune, txn</sub>
- [`erigontech/erigon#12535`](https://github.com/erigontech/erigon/pull/12535) — Prune: determenistic TxnLookup prune time  
  <sub>2024-10-30 · merged · authored · score 3 · lookup, prune, txn</sub>
- [`erigontech/erigon#12424`](https://github.com/erigontech/erigon/pull/12424) — TxLookup index per-txn-granularity  
  <sub>2024-10-23 · merged · reviewed · score 3 · index, lookup, txn</sub>
- [`erigontech/erigon#11895`](https://github.com/erigontech/erigon/pull/11895) — Use `transactions` snapshots as `baseSegType`  
  <sub>2024-09-05 · merged · reviewed · score 3 · snapshot, snapshots, transaction</sub>
- [`erigontech/erigon#9121`](https://github.com/erigontech/erigon/pull/9121) — erigon snapshots integrity: add check for body.BaseTxnID  
  <sub>2024-01-03 · merged · authored+reviewed · score 3 · snapshot, snapshots, txn</sub>
- [`erigontech/erigon#4110`](https://github.com/erigontech/erigon/pull/4110) — RPCDaemon: open snapshots on startup (because now snapshots dir is atomic), even if no Erigon available  
  <sub>2022-05-10 · merged · authored · score 3 · atomic, snapshot, snapshots</sub>
- [`erigontech/erigon#4103`](https://github.com/erigontech/erigon/pull/4103) — Snapshots: atomic dir, step 3  
  <sub>2022-05-09 · merged · authored · score 3 · atomic, snapshot, snapshots</sub>
- [`erigontech/erigon#4085`](https://github.com/erigontech/erigon/pull/4085) — Downloader atomic snapshot dir, step 1  
  <sub>2022-05-06 · merged · authored · score 3 · atomic, downloader, snapshot</sub>
- [`erigontech/erigon#3746`](https://github.com/erigontech/erigon/pull/3746) — Snapshots: script to commit hashes  
  <sub>2022-03-21 · merged · authored · score 3 · commit, snapshot, snapshots</sub>
- [`erigontech/erigon#3213`](https://github.com/erigontech/erigon/pull/3213) — Snapshots: txnHash2BlockNum idx  
  <sub>2022-01-06 · merged · authored · score 3 · snapshot, snapshots, txn</sub>
- [`erigontech/erigon#2216`](https://github.com/erigontech/erigon/pull/2216) — Do log tables size, db metrics - avoid concurrency, check stale readers hourly   
  <sub>2021-06-22 · merged · authored · score 3 · stale read</sub>
- [`erigontech/erigon#981`](https://github.com/erigontech/erigon/pull/981) — Add tx pool stage to transaction  
  <sub>2020-08-27 · merged · authored · score 3 · stage, transaction, tx </sub>
- [`erigontech/interfaces#57`](https://github.com/erigontech/interfaces/pull/57) — add withStorage and withTransactions option to StateChanges method  
  <sub>2021-08-07 · merged · authored · score 3 · state, storage, transaction</sub>
- [`ledgerwatch/erigon-lib#224`](https://github.com/ledgerwatch/erigon-lib/pull/224) — Snapshot: Txn lookup  
  <sub>2022-01-07 · merged · authored · score 3 · lookup, snapshot, txn</sub>
- [`erigontech/erigon#21262`](https://github.com/erigontech/erigon/pull/21262) — [r3.4] rawdb: ignore invalid receipt cache transaction indexes  
  <sub>2026-05-19 · merged · authored · score 2 · index, transaction</sub>
- [`erigontech/erigon#21249`](https://github.com/erigontech/erigon/pull/21249) — rawdb: ignore invalid receipt cache transaction indexes  
  <sub>2026-05-18 · merged · reviewed · score 2 · index, transaction</sub>
- [`erigontech/erigon#21214`](https://github.com/erigontech/erigon/pull/21214) — cp #21192: prune chaindata in CommitCycle  
  <sub>2026-05-15 · merged · reviewed · score 2 · commit, prune</sub>
- [`erigontech/erigon#20503`](https://github.com/erigontech/erigon/pull/20503) — db: atomic per-key prune deletion, prune consistency assertion  
  <sub>2026-04-12 · closed · reviewed · score 2 · atomic, prune</sub>
- [`erigontech/erigon#20489`](https://github.com/erigontech/erigon/pull/20489) — [r3.4] txpool: use poolDB tx for getCachedBlobTxnLocked  
  <sub>2026-04-11 · merged · authored · score 2 · tx , txn</sub>
- [`erigontech/erigon#20359`](https://github.com/erigontech/erigon/pull/20359) — db/state: fix remaining unsafe dirtyFiles access in RoTx  
  <sub>2026-04-06 · merged · reviewed · score 2 · state, tx </sub>
- [`erigontech/erigon#20211`](https://github.com/erigontech/erigon/pull/20211) — rpc: fix debug_traceTransaction() in case of tx not found  
  <sub>2026-03-28 · merged · reviewed · score 2 · transaction, tx </sub>
- [`erigontech/erigon#19882`](https://github.com/erigontech/erigon/pull/19882) — execmodule: cross-call overlay with RO tx pipeline execution  
  <sub>2026-03-14 · merged · reviewed · score 2 · pipeline, tx </sub>
- [`erigontech/erigon#19250`](https://github.com/erigontech/erigon/pull/19250) — execution: fix lastCommittedBlockNum double-counting in parallel executor  
  <sub>2026-02-17 · merged · reviewed · score 2 · commit, parallel</sub>
- [`erigontech/erigon#19177`](https://github.com/erigontech/erigon/pull/19177) — rpc: trace_reaplyBlockTransaction() avoid ibs reset if no stateDiff is requested  
  <sub>2026-02-14 · merged · reviewed · score 2 · state, transaction</sub>
- [`erigontech/erigon#18951`](https://github.com/erigontech/erigon/pull/18951) — txnprovider/shutter: fix decryption keys processing when keys do not follow txnIndex order  
  <sub>2026-02-04 · merged · reviewed · score 2 · index, txn</sub>
- [`erigontech/erigon#18913`](https://github.com/erigontech/erigon/pull/18913) — Performance: parallel tx hashes warm  
  <sub>2026-02-01 · merged · reviewed · score 2 · parallel, tx </sub>
- [`erigontech/erigon#18629`](https://github.com/erigontech/erigon/pull/18629) — rpc/jsonrpc: refactor RPC tx formatter  
  <sub>2026-01-12 · merged · reviewed · score 2 · format, tx </sub>
- [`erigontech/erigon#18612`](https://github.com/erigontech/erigon/pull/18612) — cmd/evm/t8ntool: remove unused commonTx variable in getTransaction  
  <sub>2026-01-09 · merged · reviewed · score 2 · transaction, tx </sub>
- [`erigontech/erigon#18519`](https://github.com/erigontech/erigon/pull/18519) — persist domain cache across multiple domain_rotx  
  <sub>2025-12-30 · closed · reviewed · score 2 · domain, tx </sub>
- [`erigontech/erigon#17964`](https://github.com/erigontech/erigon/pull/17964) — rpcdaemon: re-enable Commit on StateOverride for some API  
  <sub>2025-11-19 · merged · reviewed · score 2 · commit, state</sub>
- [`erigontech/erigon#17808`](https://github.com/erigontech/erigon/pull/17808) — rpcdaemon: fix prestate with DiffMode with tx failed   
  <sub>2025-11-07 · merged · reviewed · score 2 · state, tx </sub>
- [`erigontech/erigon#17602`](https://github.com/erigontech/erigon/pull/17602) — more logs and versioning support to block tx index  
  <sub>2025-10-22 · merged · reviewed · score 2 · index, tx </sub>
- [`erigontech/erigon#17479`](https://github.com/erigontech/erigon/pull/17479) — rpcdaemon:  pre-byzantium tx calculate postState  
  <sub>2025-10-15 · merged · reviewed · score 2 · state, tx </sub>
- [`erigontech/erigon#17362`](https://github.com/erigontech/erigon/pull/17362) — persist domain cache across domain_rotx  
  <sub>2025-10-07 · closed · reviewed · score 2 · domain, tx </sub>
- [`erigontech/erigon#17311`](https://github.com/erigontech/erigon/pull/17311) — fix error in stage_exec with --no-commit  
  <sub>2025-10-01 · merged · reviewed · score 2 · commit, stage</sub>
- [`erigontech/erigon#17086`](https://github.com/erigontech/erigon/pull/17086) — rpcdaemon: prestate tracer with code hash eth get transaction receipt with block timetsamp  
  <sub>2025-09-11 · merged · reviewed · score 2 · state, transaction</sub>
- [`erigontech/erigon#16866`](https://github.com/erigontech/erigon/pull/16866) — Partial torrentfiles ignoring + more ctx to logs [cp from 3.1]  
  <sub>2025-08-27 · merged · reviewed · score 2 · torrent, tx </sub>
- [`erigontech/erigon#16474`](https://github.com/erigontech/erigon/pull/16474) — Partial torrentfiles ignoring + more ctx to logs  
  <sub>2025-08-06 · merged · reviewed · score 2 · torrent, tx </sub>
- [`erigontech/erigon#15528`](https://github.com/erigontech/erigon/pull/15528) — ReceiptDomain: miss final txn   
  <sub>2025-06-11 · merged · authored · score 2 · domain, txn</sub>
- [`erigontech/erigon#15527`](https://github.com/erigontech/erigon/pull/15527) — [e30] ReceiptDomain: miss final txn   
  <sub>2025-06-11 · merged · authored · score 2 · domain, txn</sub>
- [`erigontech/erigon#15025`](https://github.com/erigontech/erigon/pull/15025) — bugfix #15024, do not reset ibs before each tx exec and StateOverrides  
  <sub>2025-05-13 · merged · reviewed · score 2 · state, tx </sub>
- [`erigontech/erigon#14951`](https://github.com/erigontech/erigon/pull/14951) — Cherry-pick polygon snapshot related commits from main(#14946)  
  <sub>2025-05-08 · merged · reviewed · score 2 · commit, snapshot</sub>
- [`erigontech/erigon#14887`](https://github.com/erigontech/erigon/pull/14887) — Eastorski/polygon snapshot commits  
  <sub>2025-05-05 · merged · reviewed · score 2 · commit, snapshot</sub>
- [`erigontech/erigon#14739`](https://github.com/erigontech/erigon/pull/14739) — kv: add HasPrefix to TemporalTx and SharedDomains  
  <sub>2025-04-24 · merged · reviewed · score 2 · domain, tx </sub>
- [`erigontech/erigon#14480`](https://github.com/erigontech/erigon/pull/14480) — Fixed snapshot checker again (need differentiation beetwen transaction and transaction-to-block idx)  
  <sub>2025-04-07 · merged · reviewed · score 2 · snapshot, transaction</sub>
- [`erigontech/erigon#14411`](https://github.com/erigontech/erigon/pull/14411) — tests: rollback txn  
  <sub>2025-04-03 · merged · authored · score 2 · rollback, txn</sub>
- [`erigontech/erigon#13559`](https://github.com/erigontech/erigon/pull/13559) — Nil Pointer Dereference Panics in encodePayload() of Blob Tx  
  <sub>2025-01-25 · merged · reviewed · score 2 · encode, tx </sub>
- [`erigontech/erigon#13294`](https://github.com/erigontech/erigon/pull/13294) — trace to set txnIndex and blockHash  
  <sub>2025-01-01 · merged · authored · score 2 · index, txn</sub>
- [`erigontech/erigon#13211`](https://github.com/erigontech/erigon/pull/13211) — Rollback snapshot lib  
  <sub>2024-12-23 · merged · reviewed · score 2 · rollback, snapshot</sub>
- [`erigontech/erigon#12567`](https://github.com/erigontech/erigon/pull/12567) — trace API: commit state changes from InitializeBlockExecution  
  <sub>2024-10-31 · merged · reviewed · score 2 · commit, state</sub>
- [`erigontech/erigon#12408`](https://github.com/erigontech/erigon/pull/12408) — rpcdaemon: Set correct tx index when generating Bor receipts  
  <sub>2024-10-22 · merged · reviewed · score 2 · index, tx </sub>
- [`erigontech/erigon#12396`](https://github.com/erigontech/erigon/pull/12396) — seg: make prune run as an rotx reader  
  <sub>2024-10-21 · merged · reviewed · score 2 · prune, tx </sub>
- [`erigontech/erigon#12097`](https://github.com/erigontech/erigon/pull/12097) — stage_bor_heimdall commits partial progress  
  <sub>2024-09-26 · merged · reviewed · score 2 · commit, stage</sub>
- [`erigontech/erigon#12060`](https://github.com/erigontech/erigon/pull/12060) — E3: fixed `transactions-to-block` indexes download  
  <sub>2024-09-21 · merged · reviewed · score 2 · index, transaction</sub>
- [`erigontech/erigon#11287`](https://github.com/erigontech/erigon/pull/11287) — on chain-tip: if batch is full - stop execution stage - to allow commit and reduce db size  
  <sub>2024-07-23 · merged · authored · score 2 · commit, stage</sub>
- [`erigontech/erigon#10652`](https://github.com/erigontech/erigon/pull/10652) — COMMIT_EACH_STAGE: env flag  
  <sub>2024-06-07 · merged · authored · score 2 · commit, stage</sub>
- [`erigontech/erigon#10561`](https://github.com/erigontech/erigon/pull/10561) — prune tx if something available  
  <sub>2024-05-30 · merged · reviewed · score 2 · prune, tx </sub>
- [`erigontech/erigon#10482`](https://github.com/erigontech/erigon/pull/10482) — prune: less atomics in loops  
  <sub>2024-05-26 · merged · authored · score 2 · atomic, prune</sub>
- [`erigontech/erigon#10274`](https://github.com/erigontech/erigon/pull/10274) — make prune each batch in new tx  
  <sub>2024-05-10 · merged · reviewed · score 2 · prune, tx </sub>
- [`erigontech/erigon#10273`](https://github.com/erigontech/erigon/pull/10273) — e3: SharedDomains.SetTx also must set aggCtx field  
  <sub>2024-05-10 · merged · authored · score 2 · domain, tx </sub>
- [`erigontech/erigon#9992`](https://github.com/erigontech/erigon/pull/9992) — downloader: step towards atomic fs  
  <sub>2024-04-19 · merged · authored · score 2 · atomic, downloader</sub>
- [`erigontech/erigon#9608`](https://github.com/erigontech/erigon/pull/9608) — EngineBlockDownloader to not pass http-request-ctx in unbounded goroutines   
  <sub>2024-03-06 · merged · authored · score 2 · downloader, tx </sub>
- [`erigontech/erigon#9607`](https://github.com/erigontech/erigon/pull/9607) — e35: EngineBlockDownloader to not pass http-request-ctx in unbounded goroutines   
  <sub>2024-03-06 · merged · authored · score 2 · downloader, tx </sub>
- [`erigontech/erigon#9371`](https://github.com/erigontech/erigon/pull/9371) — ethstats: Fix Issue with Unreported Pending Transaction Information  
  <sub>2024-02-04 · merged · reviewed · score 2 · format, transaction</sub>
- [`erigontech/erigon#9043`](https://github.com/erigontech/erigon/pull/9043) — atomic CRUD for .torrent files   
  <sub>2023-12-21 · merged · authored · score 2 · atomic, torrent</sub>
- [`erigontech/erigon#7851`](https://github.com/erigontech/erigon/pull/7851) — integration stage_exec: add flag --no-commit  
  <sub>2023-07-06 · merged · authored · score 2 · commit, stage</sub>
- [`erigontech/erigon#7616`](https://github.com/erigontech/erigon/pull/7616) — stageLoop: unbound canRunCycleInOneTransaction logic from initialCycle variable   
  <sub>2023-06-01 · merged · authored · score 2 · stage, transaction</sub>
- [`erigontech/erigon#6850`](https://github.com/erigontech/erigon/pull/6850) — e3: reduce buildIndex ctx scope  
  <sub>2023-02-12 · merged · authored · score 2 · index, tx </sub>
- [`erigontech/erigon#6738`](https://github.com/erigontech/erigon/pull/6738) — e3: last reader to close/remove merged files (marked as `canDelete`) inside tx.Rollback()   
  <sub>2023-01-29 · merged · authored · score 2 · merge, rollback</sub>
- [`erigontech/erigon#6212`](https://github.com/erigontech/erigon/pull/6212) — e3: use fact that lifecycle of readList smaller than State22 and RoTx   
  <sub>2022-12-05 · merged · authored · score 2 · state, tx </sub>
- [`erigontech/erigon#5879`](https://github.com/erigontech/erigon/pull/5879) — E3: parallel exec, apply on roTx  
  <sub>2022-10-27 · merged · authored · score 2 · parallel, tx </sub>
- [`erigontech/erigon#5693`](https://github.com/erigontech/erigon/pull/5693) — e3: prune limited amount before commit #675  
  <sub>2022-10-11 · merged · authored · score 2 · commit, prune</sub>
- [`erigontech/erigon#5614`](https://github.com/erigontech/erigon/pull/5614) — erigon3: allow commit in parallel exec    
  <sub>2022-10-04 · merged · authored · score 2 · commit, parallel</sub>
- [`erigontech/erigon#5613`](https://github.com/erigontech/erigon/pull/5613) — erigon3: no overlap parallel tx  
  <sub>2022-10-04 · merged · authored · score 2 · parallel, tx </sub>
- [`erigontech/erigon#5601`](https://github.com/erigontech/erigon/pull/5601) — erigon3: overlap tx on parallel exec fix  
  <sub>2022-10-03 · merged · authored · score 2 · parallel, tx </sub>
- [`erigontech/erigon#5518`](https://github.com/erigontech/erigon/pull/5518) — erigon3: fix conflict with innner_tx in stage_bodies  
  <sub>2022-09-26 · merged · authored · score 2 · stage, tx </sub>
- [`erigontech/erigon#4093`](https://github.com/erigontech/erigon/pull/4093) — atomic snapshot dir, step 2  
  <sub>2022-05-07 · merged · authored · score 2 · atomic, snapshot</sub>
- [`erigontech/erigon#3464`](https://github.com/erigontech/erigon/pull/3464) — eth_GetTransactionByHash: to return nil pending txn by hash  
  <sub>2022-02-10 · merged · authored · score 2 · transaction, txn</sub>
- [`erigontech/erigon#3440`](https://github.com/erigontech/erigon/pull/3440) — Snapshot: don't drop on ctx cancel  
  <sub>2022-02-07 · merged · authored · score 2 · snapshot, tx </sub>
- [`erigontech/erigon#3001`](https://github.com/erigontech/erigon/pull/3001) — eth_getTransactionReceipt not to return unrelated different tx receipts  
  <sub>2021-11-21 · merged · reviewed · score 2 · transaction, tx </sub>
- [`erigontech/erigon#2302`](https://github.com/erigontech/erigon/pull/2302) — remove ctx from state writer interface  
  <sub>2021-07-05 · merged · authored · score 2 · state, tx </sub>
- [`erigontech/erigon#2238`](https://github.com/erigontech/erigon/pull/2238) — RPC: trace_replayTransaction and trace_replayBlockTransactions methods (stateDiff only)  
  <sub>2021-06-26 · merged · authored · score 2 · state, transaction</sub>
- [`erigontech/erigon#1909`](https://github.com/erigontech/erigon/pull/1909) — KV and RemoteKV: to reuse stateless cursors during transaction  
  <sub>2021-05-10 · merged · authored · score 2 · state, transaction</sub>
- [`erigontech/erigon#1888`](https://github.com/erigontech/erigon/pull/1888) — update stage progress before commit - to keep db always consistent  
  <sub>2021-05-06 · merged · authored · score 2 · commit, stage</sub>
- [`erigontech/erigon#1872`](https://github.com/erigontech/erigon/pull/1872) — Add kv to stage settings (because it doesn't change in runtime, tx will be passed as Stage func argument)  
  <sub>2021-05-04 · merged · authored · score 2 · stage, tx </sub>
- [`erigontech/erigon#1667`](https://github.com/erigontech/erigon/pull/1667) — Stateless Tx interface  
  <sub>2021-04-03 · merged · reviewed · score 2 · state, tx </sub>
- [`erigontech/erigon#1580`](https://github.com/erigontech/erigon/pull/1580) — RPCDaemon: increase throughput by allowing more parallel grpc streams and not lockthread for read tx  
  <sub>2021-03-22 · merged · authored · score 2 · parallel, tx </sub>
- [`erigontech/erigon#1368`](https://github.com/erigontech/erigon/pull/1368) — State cache switching writes to reads during commit  
  <sub>2020-11-21 · merged · reviewed · score 2 · commit, state</sub>
- [`erigontech/erigon#1079`](https://github.com/erigontech/erigon/pull/1079) — transactional migrations  
  <sub>2020-09-08 · merged · authored · score 2 · migration, transaction</sub>
- [`erigontech/erigon#902`](https://github.com/erigontech/erigon/pull/902) — Migrations validation: duplicate names and commit call  
  <sub>2020-08-11 · merged · authored · score 2 · commit, migration</sub>
- [`erigontech/erigon#751`](https://github.com/erigontech/erigon/pull/751) — remove atomic from stage4  
  <sub>2020-07-16 · merged · authored · score 2 · atomic, stage</sub>
- [`erigontech/erigon#418`](https://github.com/erigontech/erigon/pull/418) — don't pass common ctx to blochain.Commit  
  <sub>2020-03-31 · merged · authored · score 2 · commit, tx </sub>
- [`erigontech/erigon#349`](https://github.com/erigontech/erigon/pull/349) — 335 tx lookup  
  <sub>2020-02-01 · closed · reviewed · score 2 · lookup, tx </sub>
- [`erigontech/interfaces#89`](https://github.com/erigontech/interfaces/pull/89) — TxnLookup  
  <sub>2022-01-07 · merged · authored · score 2 · lookup, txn</sub>
- [`erigontech/interfaces#65`](https://github.com/erigontech/interfaces/pull/65) — Tx id in state diff  
  <sub>2021-09-15 · merged · authored · score 2 · state, tx </sub>
- [`erigontech/interfaces#64`](https://github.com/erigontech/interfaces/pull/64) — kv server to send txnID after tx open  
  <sub>2021-09-15 · merged · authored · score 2 · tx , txn</sub>
- [`ledgerwatch/erigon-lib#889`](https://github.com/ledgerwatch/erigon-lib/pull/889) — e3: reduce buildIndex ctx scope  
  <sub>2023-02-12 · merged · authored · score 2 · index, tx </sub>
- [`ledgerwatch/erigon-lib#869`](https://github.com/ledgerwatch/erigon-lib/pull/869) — e3: last reader to close/remove merged files (marked as `canDelete`) inside tx.Rollback()   
  <sub>2023-01-29 · merged · authored · score 2 · merge, rollback</sub>
- [`ledgerwatch/erigon-lib#707`](https://github.com/ledgerwatch/erigon-lib/pull/707) — E3: parallel exec, apply on roTx  
  <sub>2022-10-27 · merged · authored · score 2 · parallel, tx </sub>
- [`ledgerwatch/erigon-lib#675`](https://github.com/ledgerwatch/erigon-lib/pull/675) — e3: prune limited amount before commit  
  <sub>2022-10-11 · merged · authored · score 2 · commit, prune</sub>
- [`ledgerwatch/erigon-lib#59`](https://github.com/ledgerwatch/erigon-lib/pull/59) — Pool: state diff direct client, tx parse fuzzing  
  <sub>2021-09-06 · merged · authored · score 2 · state, tx </sub>

## State / domains / commitment  (243)

- [`erigontech/erigon#21625`](https://github.com/erigontech/erigon/pull/21625) — [wip] seg: 2-3x faster domain merge compression via Aho-Corasick matcher and cover-DP optimizations  
  <sub>2026-06-04 · open · reviewed · score 8 · compress, compression, domain, merge</sub>
- [`erigontech/erigon#20770`](https://github.com/erigontech/erigon/pull/20770) — [performance] recsplit: off-heap EliasFano + Sharded Fuse fix + domain merge limit CLI  
  <sub>2026-04-24 · closed · authored · score 8 · domain, eliasfano, merge, recsplit</sub>
- [`erigontech/erigon#10397`](https://github.com/erigontech/erigon/pull/10397) — erigon-lib/state: inverted index to use elias fano reverse iterator seek  
  <sub>2024-05-17 · merged · reviewed · score 8 · elias fano, index, inverted index, state</sub>
- [`erigontech/erigon#21537`](https://github.com/erigontech/erigon/pull/21537) — rpc/jsonrpc: encode executionWitness headers as RLP  
  <sub>2026-05-31 · merged · reviewed · score 7 · encode, rlp , witness</sub>
- [`erigontech/erigon#11712`](https://github.com/erigontech/erigon/pull/11712) — compression of storage.kv  
  <sub>2024-08-22 · merged · authored · score 7 · compress, compression, storage</sub>
- [`erigontech/erigon#11296`](https://github.com/erigontech/erigon/pull/11296) — refactor: rename fields in hex patricia trie  
  <sub>2024-07-23 · merged · reviewed · score 7 · hex patricia, patricia, trie</sub>
- [`erigontech/erigon#5051`](https://github.com/erigontech/erigon/pull/5051) — erigon22: working PlainState unwind  
  <sub>2022-08-14 · merged · authored · score 7 · plainstate, state, unwind</sub>
- [`erigontech/erigon#759`](https://github.com/erigontech/erigon/pull/759) — [Just to discuss] Prefix compression of State buckets (based on DupSort feature)  
  <sub>2020-07-20 · closed · authored · score 7 · compress, compression, state</sub>
- [`erigontech/erigon#21183`](https://github.com/erigontech/erigon/pull/21183) — [wip] db/state: fix readyForCollation when block snapshots exist but state files do not  
  <sub>2026-05-14 · open · authored · score 6 · block snapshots, snapshot, snapshots, state</sub>
- [`erigontech/erigon#20701`](https://github.com/erigontech/erigon/pull/20701) — cp: cap state collation at block snapshots progress  
  <sub>2026-04-21 · merged · reviewed · score 6 · block snapshots, snapshot, snapshots, state</sub>
- [`erigontech/erigon#723`](https://github.com/erigontech/erigon/pull/723) — TxLookup unwind: Remove entries for blocks between unwindPoint+1 and stage.BlockNumber  
  <sub>2020-07-08 · merged · authored · score 6 · lookup, stage, trie, unwind</sub>
- [`erigontech/erigon#21622`](https://github.com/erigontech/erigon/pull/21622) — db/recsplit: make IndexReader stateless  
  <sub>2026-06-04 · merged · reviewed · score 5 · index, recsplit, state</sub>
- [`erigontech/erigon#21331`](https://github.com/erigontech/erigon/pull/21331) — cmd/utils/app: skip .tmp files in state snapshot integrity check  
  <sub>2026-05-21 · merged · reviewed · score 5 · integrity check, snapshot, state</sub>
- [`erigontech/erigon#21328`](https://github.com/erigontech/erigon/pull/21328) — cmd/utils/app: skip .tmp files in state snapshot integrity check  
  <sub>2026-05-21 · merged · reviewed · score 5 · integrity check, snapshot, state</sub>
- [`erigontech/erigon#21149`](https://github.com/erigontech/erigon/pull/21149) — [r3.4] wire `--erigondb.domain.steps-in-frozen-file` for `stage_exec` and `seg retire`  
  <sub>2026-05-12 · merged · reviewed · score 5 · domain, retire, stage</sub>
- [`erigontech/erigon#21025`](https://github.com/erigontech/erigon/pull/21025) — wire --erigondb.domain.steps-in-frozen-file for stage_exec and seg retire  
  <sub>2026-05-07 · merged · reviewed · score 5 · domain, retire, stage</sub>
- [`erigontech/erigon#20596`](https://github.com/erigontech/erigon/pull/20596) — db/state: fix collation/pruning race and unwind visibility in BuildFilesInBackground  
  <sub>2026-04-16 · closed · authored · score 5 · pruning, state, unwind</sub>
- [`erigontech/erigon#20594`](https://github.com/erigontech/erigon/pull/20594) — [r3.4] db/state: fix collation/pruning race and unwind visibility in BuildFilesInBackground  
  <sub>2026-04-16 · merged · authored · score 5 · pruning, state, unwind</sub>
- [`erigontech/erigon#20445`](https://github.com/erigontech/erigon/pull/20445) — db/state: fix collation/pruning race and unwind visibility in BuildFilesInBackground  
  <sub>2026-04-09 · merged · reviewed · score 5 · pruning, state, unwind</sub>
- [`erigontech/erigon#20396`](https://github.com/erigontech/erigon/pull/20396) — state: convert standalone inverted index slices to fixed-size arrays  
  <sub>2026-04-08 · merged · authored · score 5 · index, inverted index, state</sub>
- [`erigontech/erigon#20302`](https://github.com/erigontech/erigon/pull/20302) — integrity: blk-range chk to pre-build "changed keys" index before calc state root  
  <sub>2026-04-03 · merged · authored · score 5 · index, state, state root</sub>
- [`erigontech/erigon#19878`](https://github.com/erigontech/erigon/pull/19878) — [r3.4] cmd/utils/app: retrofit tests for state snapshot integrity checks  
  <sub>2026-03-13 · merged · reviewed · score 5 · integrity check, snapshot, state</sub>
- [`erigontech/erigon#19867`](https://github.com/erigontech/erigon/pull/19867) — cmd/utils/app: retrofit tests for state snapshot integrity checks  
  <sub>2026-03-13 · merged · reviewed · score 5 · integrity check, snapshot, state</sub>
- [`erigontech/erigon#18988`](https://github.com/erigontech/erigon/pull/18988) — witness: Fix storage proofs for accounts with no storage  
  <sub>2026-02-05 · merged · reviewed · score 5 · account, storage, witness</sub>
- [`erigontech/erigon#18586`](https://github.com/erigontech/erigon/pull/18586) — db/state: remove unused decomp from inverted index dedup  
  <sub>2026-01-07 · merged · reviewed · score 5 · index, inverted index, state</sub>
- [`erigontech/erigon#12508`](https://github.com/erigontech/erigon/pull/12508) — Caplin: Automatic retirement of state tables to their own snapshot files   
  <sub>2024-10-27 · merged · reviewed · score 5 · retire, snapshot, state</sub>
- [`erigontech/erigon#10863`](https://github.com/erigontech/erigon/pull/10863) — remove hashStateStage/IHStage from defaultSages and unwindOrder  
  <sub>2024-06-23 · merged · authored+reviewed · score 5 · stage, state, unwind</sub>
- [`erigontech/erigon#8992`](https://github.com/erigontech/erigon/pull/8992) — e35: del storage in "plain state writer" style  
  <sub>2023-12-15 · merged · authored · score 5 · plain state, state, storage</sub>
- [`erigontech/erigon#3860`](https://github.com/erigontech/erigon/pull/3860) — Execution : Remove unneeded Plainstate lookups for EOAs  
  <sub>2022-04-09 · merged · reviewed · score 5 · lookup, plainstate, state</sub>
- [`erigontech/erigon#1500`](https://github.com/erigontech/erigon/pull/1500) — New Trie db layout - store trie structure info and multiple hashes per record  
  <sub>2021-02-18 · merged · authored · score 5 · db layout, layout, trie</sub>
- [`erigontech/erigon#913`](https://github.com/erigontech/erigon/pull/913) — [merge after release] dupsort of plain state  
  <sub>2020-08-13 · merged · authored · score 5 · merge, plain state, state</sub>
- [`erigontech/erigon#722`](https://github.com/erigontech/erigon/pull/722) — Add commands "compare_states", add command "stage9", fix unwind of stage9 (it walked over whole db)  
  <sub>2020-07-07 · merged · authored · score 5 · stage, state, unwind</sub>
- [`erigontech/erigon#21539`](https://github.com/erigontech/erigon/pull/21539) — rpc/jsonrpc: drop pre-state code already created in-block from witness  
  <sub>2026-05-31 · merged · reviewed · score 4 · state, witness</sub>
- [`erigontech/erigon#21527`](https://github.com/erigontech/erigon/pull/21527) — db/state: log reorg-safe block and step in BuildFilesInBackground  
  <sub>2026-05-30 · merged · reviewed · score 4 · reorg, state</sub>
- [`erigontech/erigon#21518`](https://github.com/erigontech/erigon/pull/21518) — rpc/jsonrpc: source executionWitness codes from pre-state reads  
  <sub>2026-05-30 · merged · reviewed · score 4 · state, witness</sub>
- [`erigontech/erigon#20886`](https://github.com/erigontech/erigon/pull/20886) — db/state: reset reader on recsplit collision retry in SimpleAccessorBuilder  
  <sub>2026-04-28 · merged · reviewed · score 4 · recsplit, state</sub>
- [`erigontech/erigon#20681`](https://github.com/erigontech/erigon/pull/20681) — db/state: propagate tx.Unwind error up  
  <sub>2026-04-20 · merged · reviewed · score 4 · state, unwind</sub>
- [`erigontech/erigon#20636`](https://github.com/erigontech/erigon/pull/20636) — db/state: restore empty tombstones on unwind (cherry-pick #20627 to release/3.4)  
  <sub>2026-04-18 · merged · authored · score 4 · state, unwind</sub>
- [`erigontech/erigon#20627`](https://github.com/erigontech/erigon/pull/20627) — db/state: restore empty tombstones on unwind and honor them in getLatestFromDb  
  <sub>2026-04-17 · merged · reviewed · score 4 · state, unwind</sub>
- [`erigontech/erigon#20524`](https://github.com/erigontech/erigon/pull/20524) — Revert "[r3.4] db/state: fix stale slot resurrection after unwind and deletion (#20494)"  
  <sub>2026-04-13 · merged · reviewed · score 4 · state, unwind</sub>
- [`erigontech/erigon#20509`](https://github.com/erigontech/erigon/pull/20509) — revert "db/state: fix stale slot resurrection after unwind and deletion (#20483)"  
  <sub>2026-04-13 · merged · reviewed · score 4 · state, unwind</sub>
- [`erigontech/erigon#20494`](https://github.com/erigontech/erigon/pull/20494) — [r3.4] db/state: fix stale slot resurrection after unwind and deletion  
  <sub>2026-04-11 · merged · authored · score 4 · state, unwind</sub>
- [`erigontech/erigon#20483`](https://github.com/erigontech/erigon/pull/20483) — db/state: fix stale slot resurrection after unwind and deletion  
  <sub>2026-04-10 · merged · reviewed · score 4 · state, unwind</sub>
- [`erigontech/erigon#20313`](https://github.com/erigontech/erigon/pull/20313) — Bug 1: Fix integrity check at domain <-> history boundary (cherry-pick to 3.4)  
  <sub>2026-04-03 · merged · reviewed · score 4 · domain, integrity check</sub>
- [`erigontech/erigon#20311`](https://github.com/erigontech/erigon/pull/20311) — Bug 1: Fix integrity check at domain <-> history boundary  
  <sub>2026-04-03 · merged · reviewed · score 4 · domain, integrity check</sub>
- [`erigontech/erigon#20256`](https://github.com/erigontech/erigon/pull/20256) — [3.4] cherry-pick fix state root on eth_simulateV1 (#20062)  
  <sub>2026-03-31 · merged · reviewed · score 4 · state, state root</sub>
- [`erigontech/erigon#20136`](https://github.com/erigontech/erigon/pull/20136) — db/seg: arena-based MatchFinder (patricia trie)  
  <sub>2026-03-24 · merged · authored · score 4 · patricia, trie</sub>
- [`erigontech/erigon#19789`](https://github.com/erigontech/erigon/pull/19789) — integrity: state root check - to support `--failFast`  
  <sub>2026-03-11 · merged · authored · score 4 · state, state root</sub>
- [`erigontech/erigon#19752`](https://github.com/erigontech/erigon/pull/19752) — fix(accessor): reset keyPos/valPos on recsplit collision retry in domain.go  
  <sub>2026-03-09 · merged · reviewed · score 4 · domain, recsplit</sub>
- [`erigontech/erigon#19472`](https://github.com/erigontech/erigon/pull/19472) — Test_HexPatriciaHashed_ProcessWithDozensOfStorageKeys flaky fix  
  <sub>2026-02-25 · merged · authored · score 4 · patricia, storage</sub>
- [`erigontech/erigon#19401`](https://github.com/erigontech/erigon/pull/19401) — seg, state: reuse bufio buffers in Compressor to optimise tests  
  <sub>2026-02-22 · merged · reviewed · score 4 · compress, state</sub>
- [`erigontech/erigon#19251`](https://github.com/erigontech/erigon/pull/19251) — fix: remove prevStep from DomainDiff/unwind cycle  
  <sub>2026-02-17 · merged · reviewed · score 4 · domain, unwind</sub>
- [`erigontech/erigon#18002`](https://github.com/erigontech/erigon/pull/18002) — cp Integrity check: compare state progress and block progress  
  <sub>2025-11-20 · merged · reviewed · score 4 · integrity check, state</sub>
- [`erigontech/erigon#17913`](https://github.com/erigontech/erigon/pull/17913) — integrity check: compare state progress and block progress  
  <sub>2025-11-15 · merged · reviewed · score 4 · integrity check, state</sub>
- [`erigontech/erigon#17825`](https://github.com/erigontech/erigon/pull/17825) — db/rawdb: fix incorrect log message in ReadStorageBodyRLP  
  <sub>2025-11-09 · merged · reviewed · score 4 · rlp , storage</sub>
- [`erigontech/erigon#16639`](https://github.com/erigontech/erigon/pull/16639) — [r31] rm-state: fix state root check  
  <sub>2025-08-14 · closed · authored · score 4 · state, state root</sub>
- [`erigontech/erigon#16407`](https://github.com/erigontech/erigon/pull/16407) — integrity check: consider that rcache might be atmost 1 ahead of account progress  
  <sub>2025-08-01 · merged · reviewed · score 4 · account, integrity check</sub>
- [`erigontech/erigon#16406`](https://github.com/erigontech/erigon/pull/16406) — integrity check: consider that rcache might be atmost 1 ahead of account progress  
  <sub>2025-08-01 · merged · reviewed · score 4 · account, integrity check</sub>
- [`erigontech/erigon#15196`](https://github.com/erigontech/erigon/pull/15196) — getWitness to use less direc api of trie  
  <sub>2025-05-21 · merged · reviewed · score 4 · trie, witness</sub>
- [`erigontech/erigon#14771`](https://github.com/erigontech/erigon/pull/14771) — [r30] `erigon seg retire`: to remove garbage state files  
  <sub>2025-04-26 · merged · authored · score 4 · retire, state</sub>
- [`erigontech/erigon#14727`](https://github.com/erigontech/erigon/pull/14727) — `erigon seg retire`: to remove garbage state files   
  <sub>2025-04-24 · merged · authored+reviewed · score 4 · retire, state</sub>
- [`erigontech/erigon#12783`](https://github.com/erigontech/erigon/pull/12783) — DO NOT MERGE: witness for Erigon 3  
  <sub>2024-11-19 · closed · reviewed · score 4 · merge, witness</sub>
- [`erigontech/erigon#12025`](https://github.com/erigontech/erigon/pull/12025) — domain lru: support compressed vals  
  <sub>2024-09-18 · merged · authored · score 4 · compress, domain</sub>
- [`erigontech/erigon#10752`](https://github.com/erigontech/erigon/pull/10752) — moved units from PlainState to e3 primitives  
  <sub>2024-06-14 · merged · reviewed · score 4 · plainstate, state</sub>
- [`erigontech/erigon#10368`](https://github.com/erigontech/erigon/pull/10368) — tweak(plainstate): add close func to close cursors  
  <sub>2024-05-16 · merged · reviewed · score 4 · plainstate, state</sub>
- [`erigontech/erigon#10058`](https://github.com/erigontech/erigon/pull/10058) — [wip] e35: if requested unwind is in the future (after current state) - then just allow it - don't need re-org state  
  <sub>2024-04-25 · closed · authored · score 4 · state, unwind</sub>
- [`erigontech/erigon#9523`](https://github.com/erigontech/erigon/pull/9523) — return error when PlainState has empty value   
  <sub>2024-02-27 · merged · authored · score 4 · plainstate, state</sub>
- [`erigontech/erigon#9511`](https://github.com/erigontech/erigon/pull/9511) — e35: domain/history/ii - add own func to create recsplit idx. step 1 towards less false-positives  
  <sub>2024-02-26 · merged · authored · score 4 · domain, recsplit</sub>
- [`erigontech/erigon#9051`](https://github.com/erigontech/erigon/pull/9051) — webseed: remove dependency on db state  
  <sub>2023-12-22 · merged · authored · score 4 · state, webseed</sub>
- [`erigontech/erigon#8712`](https://github.com/erigontech/erigon/pull/8712) — e35: unskip TestLargeReorgTrieGC  
  <sub>2023-11-12 · merged · authored · score 4 · reorg, trie</sub>
- [`erigontech/erigon#7470`](https://github.com/erigontech/erigon/pull/7470) — e4: chain_makers to not work on PlainState  
  <sub>2023-05-09 · merged · authored · score 4 · plainstate, state</sub>
- [`erigontech/erigon#5159`](https://github.com/erigontech/erigon/pull/5159) — erigon22: unwind trie support  
  <sub>2022-08-24 · merged · authored · score 4 · trie, unwind</sub>
- [`erigontech/erigon#5132`](https://github.com/erigontech/erigon/pull/5132) — erigon22: incremental state root calcc  
  <sub>2022-08-22 · merged · authored · score 4 · state, state root</sub>
- [`erigontech/erigon#5088`](https://github.com/erigontech/erigon/pull/5088) — erigon22: fix storage cleanup on unwind  
  <sub>2022-08-17 · merged · authored · score 4 · storage, unwind</sub>
- [`erigontech/erigon#3601`](https://github.com/erigontech/erigon/pull/3601) — [stable] Auto detect latest block for optimal use of plain state and cache  
  <sub>2022-02-23 · merged · reviewed · score 4 · plain state, state</sub>
- [`erigontech/erigon#1799`](https://github.com/erigontech/erigon/pull/1799) — add hashstate, trie, history, logIndex stages  
  <sub>2021-04-25 · merged · authored · score 4 · index, stage, state, trie</sub>
- [`erigontech/erigon#1283`](https://github.com/erigontech/erigon/pull/1283) — Integration crush on unwind inside state.LogPrefix() method   
  <sub>2020-10-23 · merged · authored · score 4 · state, unwind</sub>
- [`erigontech/erigon#742`](https://github.com/erigontech/erigon/pull/742) — [wip] State root sometimes corrupt after interrupt  
  <sub>2020-07-14 · closed · authored · score 4 · state, state root</sub>
- [`erigontech/erigon#402`](https://github.com/erigontech/erigon/pull/402) — Make AccountCreation do determined amount of operations and Move .Put out of .View   
  <sub>2020-03-23 · merged · authored · score 4 · .vi, account</sub>
- [`ledgerwatch/erigon-lib#586`](https://github.com/ledgerwatch/erigon-lib/pull/586) — state22.Unwind()  
  <sub>2022-08-14 · merged · authored · score 4 · state, unwind</sub>
- [`ledgerwatch/erigon-lib#180`](https://github.com/ledgerwatch/erigon-lib/pull/180) — RecSplit: store BaseDataID in .idx file (helps to navigate over non blockNum-based entries)  
  <sub>2021-11-21 · merged · authored · score 4 · recsplit, trie</sub>
- [`erigontech/erigon#21917`](https://github.com/erigontech/erigon/pull/21917) — db/seg: caller-managed SAIS scratch buffer; drop legacy patricia MatchFinder  
  <sub>2026-06-20 · open · authored · score 3 · patricia</sub>
- [`erigontech/erigon#21627`](https://github.com/erigontech/erigon/pull/21627) — db/state: persist domain file cache across rotxs, survive merges  
  <sub>2026-06-04 · open · reviewed · score 3 · domain, merge, state</sub>
- [`erigontech/erigon#21532`](https://github.com/erigontech/erigon/pull/21532) — rpc/jsonrpc: omit empty keys and order witness headers ascending  
  <sub>2026-05-30 · merged · reviewed · score 3 · witness</sub>
- [`erigontech/erigon#21484`](https://github.com/erigontech/erigon/pull/21484) — rpc/jsonrpc: filter redundant collapse-sibling nodes from debug_executionWitness  
  <sub>2026-05-28 · closed · reviewed · score 3 · witness</sub>
- [`erigontech/erigon#21268`](https://github.com/erigontech/erigon/pull/21268) — Revert "db/state: remove CheckSnapshotsCompatibility (pre-3.1 compat check) (#20746)"  
  <sub>2026-05-19 · merged · authored · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#21261`](https://github.com/erigontech/erigon/pull/21261) — rpc/jsonrpc: split debug_executionWitness into phase helpers (on top of lupin012 codes fix)  
  <sub>2026-05-18 · merged · reviewed · score 3 · witness</sub>
- [`erigontech/erigon#21148`](https://github.com/erigontech/erigon/pull/21148) — [r3.4] db/state, ethconfig: bound domain merge; add --erigondb.domain.steps-in-frozen-file  
  <sub>2026-05-12 · merged · reviewed · score 3 · domain, merge, state</sub>
- [`erigontech/erigon#20938`](https://github.com/erigontech/erigon/pull/20938) — eest: add EIP-8025 execution witness test suite (93 zkevm fixtures)  
  <sub>2026-05-01 · closed · reviewed · score 3 · witness</sub>
- [`erigontech/erigon#20859`](https://github.com/erigontech/erigon/pull/20859) — cmd/utils: clarify --snap.skip-state-snapshot-download vs --prune.mode=blocks  
  <sub>2026-04-28 · merged · authored · score 3 · prune, snapshot, state</sub>
- [`erigontech/erigon#20785`](https://github.com/erigontech/erigon/pull/20785) — [r3.4] db/state: skip DB entries within file range in DomainLatestIterFile  
  <sub>2026-04-24 · closed · authored · score 3 · domain, state, trie</sub>
- [`erigontech/erigon#20746`](https://github.com/erigontech/erigon/pull/20746) — db/state: remove CheckSnapshotsCompatibility (pre-3.1 compat check)  
  <sub>2026-04-23 · merged · authored · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#20597`](https://github.com/erigontech/erigon/pull/20597) — db/state: inv_index merge remove 1 intermediate buffer to reduce peak memory  
  <sub>2026-04-16 · merged · authored+reviewed · score 3 · index, merge, state</sub>
- [`erigontech/erigon#20345`](https://github.com/erigontech/erigon/pull/20345) — debug_executionWitness: follow up  
  <sub>2026-04-06 · merged · authored · score 3 · witness</sub>
- [`erigontech/erigon#20051`](https://github.com/erigontech/erigon/pull/20051) — [SharovBot] [r3.4] execution/state: fix WriteAccountStorage skip using stale blockOriginStorage  
  <sub>2026-03-21 · merged · reviewed · score 3 · account, state, storage</sub>
- [`erigontech/erigon#20005`](https://github.com/erigontech/erigon/pull/20005) — cmd/utils/app: refactor DeleteStateSnapshots to use args struct  
  <sub>2026-03-19 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#19917`](https://github.com/erigontech/erigon/pull/19917) — db/state: fix unsafe dirtyFiles access in merge file lookups  
  <sub>2026-03-16 · merged · reviewed · score 3 · lookup, merge, state</sub>
- [`erigontech/erigon#19506`](https://github.com/erigontech/erigon/pull/19506) — db/state: skip Benchmark_BtreeIndex_Search when data file is absent  
  <sub>2026-02-26 · merged · reviewed · score 3 · btree, index, state</sub>
- [`erigontech/erigon#19467`](https://github.com/erigontech/erigon/pull/19467) — Test optimisation: pool resources allocated in the HexPatriciaHashed  
  <sub>2026-02-24 · merged · reviewed · score 3 · patricia</sub>
- [`erigontech/erigon#19208`](https://github.com/erigontech/erigon/pull/19208) — add alias to `erigon seg rm-all-state-snapshots`  
  <sub>2026-02-16 · merged · authored · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#18665`](https://github.com/erigontech/erigon/pull/18665) — [r3.3] not needed collector erased in prune domains  
  <sub>2026-01-14 · merged · reviewed · score 3 · collector, domain, prune</sub>
- [`erigontech/erigon#16848`](https://github.com/erigontech/erigon/pull/16848) — agg: move `iiCfg`/`Schema`/`RegisterDomain calls` to `statecfg`  
  <sub>2025-08-27 · merged · authored · score 3 · domain, schema, state</sub>
- [`erigontech/erigon#16010`](https://github.com/erigontech/erigon/pull/16010) — relax state prune calculation in snapshot download  
  <sub>2025-07-09 · merged · reviewed · score 3 · prune, snapshot, state</sub>
- [`erigontech/erigon#15949`](https://github.com/erigontech/erigon/pull/15949) — rm state snapshots flag mixer  
  <sub>2025-07-05 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#15223`](https://github.com/erigontech/erigon/pull/15223) — don't delete state-salt file on rm-all-state-snapshots  
  <sub>2025-05-23 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#15214`](https://github.com/erigontech/erigon/pull/15214) — don't delete state-salt file on rm-all-state-snapshots.  
  <sub>2025-05-22 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#15167`](https://github.com/erigontech/erigon/pull/15167) — [r30] Prune: protect each domain from pruning ahead of it's visible files   
  <sub>2025-05-20 · merged · authored · score 3 · domain, prune, pruning</sub>
- [`erigontech/erigon#15166`](https://github.com/erigontech/erigon/pull/15166) — Prune: protect each domain from pruning ahead of it's visible files  
  <sub>2025-05-20 · merged · authored · score 3 · domain, prune, pruning</sub>
- [`erigontech/erigon#14851`](https://github.com/erigontech/erigon/pull/14851) — docs: updated redirection to `witness_operators.go`  
  <sub>2025-05-02 · merged · reviewed · score 3 · witness</sub>
- [`erigontech/erigon#14746`](https://github.com/erigontech/erigon/pull/14746) — [pick r3.0] merge: look only at state domains when canceling merge  
  <sub>2025-04-25 · merged · authored · score 3 · domain, merge, state</sub>
- [`erigontech/erigon#14745`](https://github.com/erigontech/erigon/pull/14745) — merge: look only at state domains when canceling merge  
  <sub>2025-04-25 · closed · authored · score 3 · domain, merge, state</sub>
- [`erigontech/erigon#13497`](https://github.com/erigontech/erigon/pull/13497) — Erigon 3: Fix state snapshots skipping  
  <sub>2025-01-18 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#13107`](https://github.com/erigontech/erigon/pull/13107) — E3: make state snapshots download optional  
  <sub>2024-12-13 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#12847`](https://github.com/erigontech/erigon/pull/12847) — experimental: MPT block witness for Erigon 3  
  <sub>2024-11-22 · merged · reviewed · score 3 · witness</sub>
- [`erigontech/erigon#12687`](https://github.com/erigontech/erigon/pull/12687) — Caplin: fixed validators refill for empty state snapshots  
  <sub>2024-11-08 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#10742`](https://github.com/erigontech/erigon/pull/10742) — `snapshots rm-state-snapshots --latest` command  
  <sub>2024-06-13 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#10339`](https://github.com/erigontech/erigon/pull/10339) — Fix situation where progress in domain files is higher than progress in blocks snapshots  
  <sub>2024-05-14 · merged · reviewed · score 3 · domain, snapshot, snapshots</sub>
- [`erigontech/erigon#9985`](https://github.com/erigontech/erigon/pull/9985) — downloader: RecalcStates double-accounting fix  
  <sub>2024-04-18 · merged · authored · score 3 · account, downloader, state</sub>
- [`erigontech/erigon#9305`](https://github.com/erigontech/erigon/pull/9305) — e35:  remove salt.txt while deleting state snapshots  
  <sub>2024-01-24 · merged · reviewed · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#3193`](https://github.com/erigontech/erigon/pull/3193) — Snapshots: remove old state generator  
  <sub>2022-01-03 · merged · authored · score 3 · snapshot, snapshots, state</sub>
- [`erigontech/erigon#1563`](https://github.com/erigontech/erigon/pull/1563) — Simple test for layout of TrieOfAccountsBucket   
  <sub>2021-03-19 · merged · reviewed · score 3 · account, layout, trie</sub>
- [`erigontech/erigon#504`](https://github.com/erigontech/erigon/pull/504) — Merge account and storage resolvers  
  <sub>2020-05-01 · merged · authored · score 3 · account, merge, storage</sub>
- [`erigontech/erigon#21528`](https://github.com/erigontech/erigon/pull/21528) — db/state: fix Aggregator & ForkableAgg Close vs background MergeLoop WaitGroup race  
  <sub>2026-05-30 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#21398`](https://github.com/erigontech/erigon/pull/21398) — simplify state aggregation and pruning logic  
  <sub>2026-05-25 · merged · reviewed · score 2 · pruning, state</sub>
- [`erigontech/erigon#21280`](https://github.com/erigontech/erigon/pull/21280) — db/kv, db/migrations, cmd: drop pre-E3 plain/hashed state and history tables  
  <sub>2026-05-19 · merged · reviewed · score 2 · migration, state</sub>
- [`erigontech/erigon#21218`](https://github.com/erigontech/erigon/pull/21218) — cp #21209: prune: fix stranded old-step dups in dupsort domains  
  <sub>2026-05-15 · merged · reviewed · score 2 · domain, prune</sub>
- [`erigontech/erigon#21058`](https://github.com/erigontech/erigon/pull/21058) — cmd/evm: parallel workers in evm statetest and blocktest  
  <sub>2026-05-08 · merged · reviewed · score 2 · parallel, state</sub>
- [`erigontech/erigon#20974`](https://github.com/erigontech/erigon/pull/20974) — db/state: clip merge windows that straddle existing files  
  <sub>2026-05-04 · merged · authored · score 2 · merge, state</sub>
- [`erigontech/erigon#20973`](https://github.com/erigontech/erigon/pull/20973) — db/state: clip merge windows that straddle existing files  
  <sub>2026-05-04 · closed · authored · score 2 · merge, state</sub>
- [`erigontech/erigon#20909`](https://github.com/erigontech/erigon/pull/20909) — db/state: clip merge windows that straddle existing files  
  <sub>2026-04-29 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#20882`](https://github.com/erigontech/erigon/pull/20882) — db/state: add unit tests for findMergeRangeInFiles  
  <sub>2026-04-28 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#20871`](https://github.com/erigontech/erigon/pull/20871) — db/state: extract findMergeRangeInFiles helper  
  <sub>2026-04-28 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#20837`](https://github.com/erigontech/erigon/pull/20837) — [performance] [cherry-pick] Bound domain merge limit; add CLI override (#20705)  
  <sub>2026-04-27 · merged · reviewed · score 2 · domain, merge</sub>
- [`erigontech/erigon#20817`](https://github.com/erigontech/erigon/pull/20817) — db/state: simplify DomainLatestIterFile  
  <sub>2026-04-26 · merged · authored · score 2 · domain, state</sub>
- [`erigontech/erigon#20807`](https://github.com/erigontech/erigon/pull/20807) — rpc: fix prestateTracer diff mode missing deleted accounts  
  <sub>2026-04-25 · merged · reviewed · score 2 · account, state</sub>
- [`erigontech/erigon#20771`](https://github.com/erigontech/erigon/pull/20771) — [performance] fix issue #20169: StateCache + collation/pruning race fixes  
  <sub>2026-04-24 · closed · authored · score 2 · pruning, state</sub>
- [`erigontech/erigon#20745`](https://github.com/erigontech/erigon/pull/20745) — db/state: replace Walk callbacks with btree Iter in dirty_files.go  
  <sub>2026-04-23 · merged · authored · score 2 · btree, state</sub>
- [`erigontech/erigon#20712`](https://github.com/erigontech/erigon/pull/20712) — execution/trie: enhance trie hashing flow and correct key encoding  
  <sub>2026-04-21 · merged · reviewed · score 2 · encoding, trie</sub>
- [`erigontech/erigon#20705`](https://github.com/erigontech/erigon/pull/20705) — Bound domain merge limit; add CLI override  
  <sub>2026-04-21 · merged · reviewed · score 2 · domain, merge</sub>
- [`erigontech/erigon#20527`](https://github.com/erigontech/erigon/pull/20527) — node/components/storage/snapshot: add file inventory, trust model, range arithmetic  
  <sub>2026-04-13 · merged · reviewed · score 2 · snapshot, storage</sub>
- [`erigontech/erigon#20488`](https://github.com/erigontech/erigon/pull/20488) — [r3.4] db/state: fix btree cursor leak in debugIteratePrefixLatest  
  <sub>2026-04-11 · merged · authored · score 2 · btree, state</sub>
- [`erigontech/erigon#20486`](https://github.com/erigontech/erigon/pull/20486) — db/state: add optional throttle to MergeLoop to reduce disk I/O pressure  
  <sub>2026-04-10 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#20468`](https://github.com/erigontech/erigon/pull/20468) — db/state: fix btree cursor leak in debugIteratePrefixLatest  
  <sub>2026-04-10 · merged · reviewed · score 2 · btree, state</sub>
- [`erigontech/erigon#20444`](https://github.com/erigontech/erigon/pull/20444) — db/state: skip DB entries within file range in debugIteratePrefixLatest  
  <sub>2026-04-09 · merged · reviewed · score 2 · state, trie</sub>
- [`erigontech/erigon#20389`](https://github.com/erigontech/erigon/pull/20389) — graphql: fix block.account and account.storage resolvers (#11662)  
  <sub>2026-04-07 · merged · reviewed · score 2 · account, storage</sub>
- [`erigontech/erigon#20372`](https://github.com/erigontech/erigon/pull/20372) — [r3.4] execution/state: use index-based range over log topics to avoid copy  
  <sub>2026-04-07 · merged · authored · score 2 · index, state</sub>
- [`erigontech/erigon#20118`](https://github.com/erigontech/erigon/pull/20118) — merge: prioritize Domain over II. part2  
  <sub>2026-03-24 · merged · authored · score 2 · domain, merge</sub>
- [`erigontech/erigon#20077`](https://github.com/erigontech/erigon/pull/20077) — [SharovBot] [main] db/state: fix spurious accessor rebuild for post-merge subset files  
  <sub>2026-03-23 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#20065`](https://github.com/erigontech/erigon/pull/20065) — merge: prioritize `Domain` merge over `StandeloneInvIdx`  
  <sub>2026-03-22 · merged · authored · score 2 · domain, merge</sub>
- [`erigontech/erigon#20031`](https://github.com/erigontech/erigon/pull/20031) — rm-state: add subset file cleanup when removing merged files  
  <sub>2026-03-20 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#20001`](https://github.com/erigontech/erigon/pull/20001) — db/state: add doMerge param to BuildFiles2  
  <sub>2026-03-19 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#20000`](https://github.com/erigontech/erigon/pull/20000) — db/state: add DisableInterDomainDependencies for selective integrity bypass  
  <sub>2026-03-19 · merged · reviewed · score 2 · domain, state</sub>
- [`erigontech/erigon#19987`](https://github.com/erigontech/erigon/pull/19987) — db/state: fix spurious accessor rebuild for post-merge subset files  
  <sub>2026-03-19 · merged · authored · score 2 · merge, state</sub>
- [`erigontech/erigon#19965`](https://github.com/erigontech/erigon/pull/19965) — db/state: fix spurious accessor rebuild for post-merge subset files  
  <sub>2026-03-18 · closed · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#19884`](https://github.com/erigontech/erigon/pull/19884) — etl, state: reduce allocation pressure in parallel executor  
  <sub>2026-03-14 · merged · reviewed · score 2 · parallel, state</sub>
- [`erigontech/erigon#19587`](https://github.com/erigontech/erigon/pull/19587) — db/state, snapcfg: download erigondb.toml via torrent; move settings resolution out of Open()  
  <sub>2026-03-03 · merged · reviewed · score 2 · state, torrent</sub>
- [`erigontech/erigon#19549`](https://github.com/erigontech/erigon/pull/19549) — seg rm-state: delete .tmp files from snapshot directories  
  <sub>2026-03-01 · merged · reviewed · score 2 · snapshot, state</sub>
- [`erigontech/erigon#19464`](https://github.com/erigontech/erigon/pull/19464) — move btindex from `db/state` pkg to `db/datastruct/btindex`  
  <sub>2026-02-24 · merged · authored · score 2 · index, state</sub>
- [`erigontech/erigon#19441`](https://github.com/erigontech/erigon/pull/19441) — merge: prioritize Domain merge over History  
  <sub>2026-02-24 · merged · authored · score 2 · domain, merge</sub>
- [`erigontech/erigon#19438`](https://github.com/erigontech/erigon/pull/19438) — evn flag to: don't merge Hist/II but still merge Domains  
  <sub>2026-02-24 · merged · authored · score 2 · domain, merge</sub>
- [`erigontech/erigon#19437`](https://github.com/erigontech/erigon/pull/19437) — evn flag to: don't merge Hist/II but still merge Domains  
  <sub>2026-02-24 · closed · authored · score 2 · domain, merge</sub>
- [`erigontech/erigon#18863`](https://github.com/erigontech/erigon/pull/18863) — reducing prune state t/o and small fix  
  <sub>2026-01-29 · merged · reviewed · score 2 · prune, state</sub>
- [`erigontech/erigon#18515`](https://github.com/erigontech/erigon/pull/18515) — Revert "Revert "Performance: do not rehash the trie storage that is memoized""  
  <sub>2025-12-30 · merged · reviewed · score 2 · storage, trie</sub>
- [`erigontech/erigon#18495`](https://github.com/erigontech/erigon/pull/18495) — Shared domain merge  
  <sub>2025-12-29 · merged · reviewed · score 2 · domain, merge</sub>
- [`erigontech/erigon#18460`](https://github.com/erigontech/erigon/pull/18460) — Revert "Performance: do not rehash the trie storage that is memoized"  
  <sub>2025-12-24 · merged · reviewed · score 2 · storage, trie</sub>
- [`erigontech/erigon#18422`](https://github.com/erigontech/erigon/pull/18422) — Performance: do not rehash the trie storage that is memoized  
  <sub>2025-12-23 · merged · reviewed · score 2 · storage, trie</sub>
- [`erigontech/erigon#18321`](https://github.com/erigontech/erigon/pull/18321) — add caplin state to "seg index" command  
  <sub>2025-12-15 · merged · reviewed · score 2 · index, state</sub>
- [`erigontech/erigon#18087`](https://github.com/erigontech/erigon/pull/18087) — Refactor StorageSize formatting to eliminate duplication  
  <sub>2025-11-27 · merged · reviewed · score 2 · format, storage</sub>
- [`erigontech/erigon#18058`](https://github.com/erigontech/erigon/pull/18058) — Added benchmark test for random access history state of accounts  
  <sub>2025-11-26 · merged · reviewed · score 2 · account, state</sub>
- [`erigontech/erigon#17676`](https://github.com/erigontech/erigon/pull/17676) — Added hint to run `stage_exec --reset` after rm-state commands  
  <sub>2025-10-27 · merged · reviewed · score 2 · stage, state</sub>
- [`erigontech/erigon#17546`](https://github.com/erigontech/erigon/pull/17546) — state/merge: use iit.files instead of dirtyFiles in staticFilesInRange  
  <sub>2025-10-20 · merged · reviewed · score 2 · merge, state</sub>
- [`erigontech/erigon#17533`](https://github.com/erigontech/erigon/pull/17533) — rpcdaemon: move allocation to sharedDomain only in case calcPostState  
  <sub>2025-10-18 · merged · reviewed · score 2 · domain, state</sub>
- [`erigontech/erigon#16769`](https://github.com/erigontech/erigon/pull/16769) — agg: move high-level shared domains tests (rebuild/sqeeze) outside of state package  
  <sub>2025-08-22 · merged · authored · score 2 · domain, state</sub>
- [`erigontech/erigon#16667`](https://github.com/erigontech/erigon/pull/16667) — [main] Domain Schema should remain unchanged  
  <sub>2025-08-15 · merged · reviewed · score 2 · domain, schema</sub>
- [`erigontech/erigon#16609`](https://github.com/erigontech/erigon/pull/16609) — Call downloader.Delete() for state files  
  <sub>2025-08-13 · merged · authored · score 2 · downloader, state</sub>
- [`erigontech/erigon#16603`](https://github.com/erigontech/erigon/pull/16603) — [r3.1] schema of domains should be unchanged  
  <sub>2025-08-13 · merged · reviewed · score 2 · domain, schema</sub>
- [`erigontech/erigon#16058`](https://github.com/erigontech/erigon/pull/16058) — [r30] reduce prune state batch size - to make it more time-determenistic  
  <sub>2025-07-11 · merged · authored · score 2 · prune, state</sub>
- [`erigontech/erigon#16027`](https://github.com/erigontech/erigon/pull/16027) — cp: relax state prune [r30]  
  <sub>2025-07-10 · merged · reviewed · score 2 · prune, state</sub>
- [`erigontech/erigon#15413`](https://github.com/erigontech/erigon/pull/15413) — Parallel State Transition  
  <sub>2025-06-02 · merged · reviewed · score 2 · parallel, state</sub>
- [`erigontech/erigon#15394`](https://github.com/erigontech/erigon/pull/15394) — domain.findMergeRange: unit-tests  
  <sub>2025-06-02 · merged · authored · score 2 · domain, merge</sub>
- [`erigontech/erigon#15371`](https://github.com/erigontech/erigon/pull/15371) — Make ReadAccountStorage return uint256 not []byte  
  <sub>2025-05-30 · merged · reviewed · score 2 · account, storage</sub>
- [`erigontech/erigon#15298`](https://github.com/erigontech/erigon/pull/15298) — purify_domain to use agg and build indexes after done  
  <sub>2025-05-28 · merged · reviewed · score 2 · domain, index</sub>
- [`erigontech/erigon#14929`](https://github.com/erigontech/erigon/pull/14929) — rpcdaemon: merge PR 14869 on 3.0 (re-use getReceipt() on logs retrieval)  
  <sub>2025-05-07 · merged · reviewed · score 2 · merge, trie</sub>
- [`erigontech/erigon#12933`](https://github.com/erigontech/erigon/pull/12933) — sdc.Account: separate reads by domain on pprof  
  <sub>2024-12-01 · merged · authored · score 2 · account, domain</sub>
- [`erigontech/erigon#12879`](https://github.com/erigontech/erigon/pull/12879) — Move `turbo/trie` and `core/types/accounts` to `erigon-lib`  
  <sub>2024-11-26 · merged · reviewed · score 2 · account, trie</sub>
- [`erigontech/erigon#12848`](https://github.com/erigontech/erigon/pull/12848) — erigondb: domain/history/index configurations  
  <sub>2024-11-22 · merged · reviewed · score 2 · domain, index</sub>
- [`erigontech/erigon#12046`](https://github.com/erigontech/erigon/pull/12046) — erigon-lib/state: parallel tests  
  <sub>2024-09-20 · merged · authored · score 2 · parallel, state</sub>
- [`erigontech/erigon#12016`](https://github.com/erigontech/erigon/pull/12016) — `erigon seg rm-state --domain=receipt` support  
  <sub>2024-09-17 · merged · authored · score 2 · domain, state</sub>
- [`erigontech/erigon#11739`](https://github.com/erigontech/erigon/pull/11739) — Fix duplicate borevent snapshot entries  
  <sub>2024-08-25 · merged · reviewed · score 2 · snapshot, trie</sub>
- [`erigontech/erigon#11684`](https://github.com/erigontech/erigon/pull/11684) — fix: debug_accountRange(): increase block_number on storage walk (e3)  
  <sub>2024-08-19 · merged · reviewed · score 2 · account, storage</sub>
- [`erigontech/erigon#11669`](https://github.com/erigontech/erigon/pull/11669) — fix: debug_accountRange(): increase block_number on storage walk (e2)  
  <sub>2024-08-19 · merged · reviewed · score 2 · account, storage</sub>
- [`erigontech/erigon#11581`](https://github.com/erigontech/erigon/pull/11581) — Simplify `StateReaderV3` by extracting `StateReaderParallelV3`  
  <sub>2024-08-13 · merged · authored · score 2 · parallel, state</sub>
- [`erigontech/erigon#11577`](https://github.com/erigontech/erigon/pull/11577) — Build and merge domains in separated directory   
  <sub>2024-08-12 · closed · reviewed · score 2 · domain, merge</sub>
- [`erigontech/erigon#11362`](https://github.com/erigontech/erigon/pull/11362) — compatibility with geth - of stateDiff encoding   
  <sub>2024-07-27 · merged · authored · score 2 · encoding, state</sub>
- [`erigontech/erigon#11063`](https://github.com/erigontech/erigon/pull/11063) — debug_accountRange: to limit storage fetch prefix  
  <sub>2024-07-08 · merged · authored · score 2 · account, storage</sub>
- [`erigontech/erigon#11021`](https://github.com/erigontech/erigon/pull/11021) — incorporate `MergeRange` into `DomainRanges`  
  <sub>2024-07-04 · merged · reviewed · score 2 · domain, merge</sub>
- [`erigontech/erigon#10879`](https://github.com/erigontech/erigon/pull/10879) — remove: stage_hash_state and stage_intermediate_hashes  
  <sub>2024-06-24 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#10830`](https://github.com/erigontech/erigon/pull/10830) — remove stage_hash_state test  
  <sub>2024-06-21 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#10753`](https://github.com/erigontech/erigon/pull/10753) — Raise the limit of debug_accountRange to 8192 (if storage not requested)  
  <sub>2024-06-14 · merged · reviewed · score 2 · account, storage</sub>
- [`erigontech/erigon#10746`](https://github.com/erigontech/erigon/pull/10746) — trace_block: to change reader's state for each txIndex  
  <sub>2024-06-14 · merged · authored · score 2 · index, state</sub>
- [`erigontech/erigon#10356`](https://github.com/erigontech/erigon/pull/10356) — integration stage_exec --reset: ready for "state files are ahead of blocks files" case  
  <sub>2024-05-15 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#10231`](https://github.com/erigontech/erigon/pull/10231) — remove batch limit heuristic for prunes>5h, added stateful prune cursors  
  <sub>2024-05-07 · merged · reviewed · score 2 · prune, state</sub>
- [`erigontech/erigon#9351`](https://github.com/erigontech/erigon/pull/9351) — e35: map-reduce re-exec, "custom_tracing" stage for it. Change kv.Domain type from string to int.  
  <sub>2024-01-31 · merged · authored · score 2 · domain, stage</sub>
- [`erigontech/erigon#8929`](https://github.com/erigontech/erigon/pull/8929) — e35: rely on SharedDomains.deleteAccount logic  
  <sub>2023-12-07 · merged · authored · score 2 · account, domain</sub>
- [`erigontech/erigon#8920`](https://github.com/erigontech/erigon/pull/8920) — e35: stateReader storage key buf  
  <sub>2023-12-07 · merged · authored · score 2 · state, storage</sub>
- [`erigontech/erigon#8826`](https://github.com/erigontech/erigon/pull/8826) — e35: rely only on domain progress (history may be pruned and it's fine).   
  <sub>2023-11-24 · merged · authored · score 2 · domain, prune</sub>
- [`erigontech/erigon#8769`](https://github.com/erigontech/erigon/pull/8769) — e35: protect from "index ahead of domain" case (by removing idx files)  
  <sub>2023-11-18 · merged · authored · score 2 · domain, index</sub>
- [`erigontech/erigon#7460`](https://github.com/erigontech/erigon/pull/7460) — history_reader_v3: must always return accounts encoded as v3  
  <sub>2023-05-08 · merged · authored · score 2 · account, encode</sub>
- [`erigontech/erigon#7102`](https://github.com/erigontech/erigon/pull/7102) — torrent: don't cancel storage, because lib can't handle such error and can graceful-shutdown anyway  
  <sub>2023-03-14 · merged · authored · score 2 · storage, torrent</sub>
- [`erigontech/erigon#6550`](https://github.com/erigontech/erigon/pull/6550) — e3: locality index, correct metadata size accounting  
  <sub>2023-01-11 · merged · authored · score 2 · account, index</sub>
- [`erigontech/erigon#6512`](https://github.com/erigontech/erigon/pull/6512) — HashState: parallel promote cleanly  
  <sub>2023-01-06 · merged · authored · score 2 · parallel, state</sub>
- [`erigontech/erigon#6473`](https://github.com/erigontech/erigon/pull/6473) — coherent state cache: change btree type  
  <sub>2022-12-30 · merged · authored · score 2 · btree, state</sub>
- [`erigontech/erigon#5713`](https://github.com/erigontech/erigon/pull/5713) — Recon parallel: split ReconState to 2 objects to avoid lock contention between .Done() and .Get(), less ram in beginning  
  <sub>2022-10-12 · merged · authored · score 2 · parallel, state</sub>
- [`erigontech/erigon#5321`](https://github.com/erigontech/erigon/pull/5321) — Erigon22: add state reconstitution to stage_exec  
  <sub>2022-09-09 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#5296`](https://github.com/erigontech/erigon/pull/5296) — Fix IH when state contains addresses < 1st key in AccTrie  
  <sub>2022-09-06 · merged · reviewed · score 2 · state, trie</sub>
- [`erigontech/erigon#5116`](https://github.com/erigontech/erigon/pull/5116) — erigon22: incremental stage trie  
  <sub>2022-08-19 · merged · authored · score 2 · stage, trie</sub>
- [`erigontech/erigon#5111`](https://github.com/erigontech/erigon/pull/5111) — erigon22: incremental hash state stage  
  <sub>2022-08-19 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#5102`](https://github.com/erigontech/erigon/pull/5102) — erigon22: incremental hash state stage  
  <sub>2022-08-18 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#5033`](https://github.com/erigontech/erigon/pull/5033) — erigon2.2: save stage progress to chainDB, can run "integration stage_exec" and "state erigon22" on same datadir  
  <sub>2022-08-13 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#4751`](https://github.com/erigontech/erigon/pull/4751) — Still fixing index out of range in (*Accumulator) ChangeStorage  
  <sub>2022-07-19 · merged · reviewed · score 2 · index, storage</sub>
- [`erigontech/erigon#4537`](https://github.com/erigontech/erigon/pull/4537) — pass context around hased state stage  
  <sub>2022-06-25 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#4295`](https://github.com/erigontech/erigon/pull/4295) — stage trie: nil check  
  <sub>2022-05-29 · merged · authored · score 2 · stage, trie</sub>
- [`erigontech/erigon#3271`](https://github.com/erigontech/erigon/pull/3271) — [stable] Implement parity_listStorageKeys for current state  
  <sub>2022-01-16 · merged · reviewed · score 2 · state, storage</sub>
- [`erigontech/erigon#3033`](https://github.com/erigontech/erigon/pull/3033) — Snapshot: exec and trie to support snapshot files  
  <sub>2021-11-25 · merged · authored · score 2 · snapshot, trie</sub>
- [`erigontech/erigon#2722`](https://github.com/erigontech/erigon/pull/2722) — fix account encode bench  
  <sub>2021-09-23 · merged · authored · score 2 · account, encode</sub>
- [`erigontech/erigon#2441`](https://github.com/erigontech/erigon/pull/2441) — less alloc at hash state key transformation  
  <sub>2021-07-24 · merged · authored · score 2 · format, state</sub>
- [`erigontech/erigon#1549`](https://github.com/erigontech/erigon/pull/1549) — Trie: use APPEND when re-generating trie. Also including db-migration for PR#1535  
  <sub>2021-03-12 · merged · authored+reviewed · score 2 · migration, trie</sub>
- [`erigontech/erigon#1522`](https://github.com/erigontech/erigon/pull/1522) — Trie: add invariant - first level of trie must be in DB (to ensure having 100% trie structure in trie_account table)  
  <sub>2021-03-01 · merged · authored · score 2 · account, trie</sub>
- [`erigontech/erigon#1445`](https://github.com/erigontech/erigon/pull/1445) — [to add cache] store IH as branch node and with trie meta info, split Hashed state buckets  
  <sub>2021-01-19 · closed · authored · score 2 · state, trie</sub>
- [`erigontech/erigon#922`](https://github.com/erigontech/erigon/pull/922) — Swap IH and HashState stages  
  <sub>2020-08-15 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#903`](https://github.com/erigontech/erigon/pull/903) — recover_from_hashstate_stage_interruption  
  <sub>2020-08-11 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#728`](https://github.com/erigontech/erigon/pull/728) — Integration add checkChangeSet into state_stages command  
  <sub>2020-07-09 · merged · authored · score 2 · stage, state</sub>
- [`erigontech/erigon#709`](https://github.com/erigontech/erigon/pull/709) — Experiments: state in DupSort layout and speed of large DupSort key deletion  
  <sub>2020-07-04 · merged · authored · score 2 · layout, state</sub>
- [`erigontech/erigon#471`](https://github.com/erigontech/erigon/pull/471) — Merge cached resolvers to stateful resolver  
  <sub>2020-04-20 · merged · authored · score 2 · merge, state</sub>
- [`erigontech/erigon#355`](https://github.com/erigontech/erigon/pull/355) — Trie: store self-destructed accounts  
  <sub>2020-02-06 · merged · authored+reviewed · score 2 · account, trie</sub>
- [`erigontech/silkworm#443`](https://github.com/erigontech/silkworm/pull/443) — Fix AccountTrieCursor traversal  
  <sub>2021-09-30 · merged · reviewed · score 2 · account, trie</sub>
- [`erigontech/silkworm#160`](https://github.com/erigontech/silkworm/pull/160) — Optimization: Remove storage_root from Account  
  <sub>2021-02-13 · merged · reviewed · score 2 · account, storage</sub>
- [`ledgerwatch/erigon-lib#938`](https://github.com/ledgerwatch/erigon-lib/pull/938) — torrent: don't cancel storage, because lib can't handle such error and can graceful-shutdown anyway  
  <sub>2023-03-14 · merged · authored · score 2 · storage, torrent</sub>
- [`ledgerwatch/erigon-lib#937`](https://github.com/ledgerwatch/erigon-lib/pull/937) — torrent: don't cancel storage, because lib can't handle such error and can graceful-shutdown anyway  
  <sub>2023-03-14 · merged · authored · score 2 · storage, torrent</sub>
- [`ledgerwatch/erigon-lib#813`](https://github.com/ledgerwatch/erigon-lib/pull/813) — coherent state cache: change btree type  
  <sub>2022-12-30 · merged · authored · score 2 · btree, state</sub>
- [`ledgerwatch/erigon-lib#596`](https://github.com/ledgerwatch/erigon-lib/pull/596) — get code/acc/storage index from aggregator  
  <sub>2022-08-19 · merged · authored · score 2 · index, storage</sub>
- [`ledgerwatch/erigon-lib#595`](https://github.com/ledgerwatch/erigon-lib/pull/595) — domain: docs of tables format  
  <sub>2022-08-18 · merged · authored · score 2 · domain, format</sub>
- [`ledgerwatch/erigon-lib#526`](https://github.com/ledgerwatch/erigon-lib/pull/526) — domain: files generic btree  
  <sub>2022-07-18 · merged · authored · score 2 · btree, domain</sub>

## Snapshots / freezer / segments  (473)

- [`erigontech/erigon#3265`](https://github.com/erigontech/erigon/pull/3265) — Snapshots: ParallelCompressor class, DecompressedFile class  
  <sub>2022-01-15 · merged · authored · score 9 · compress, decompress, parallel, snapshot, snapshots</sub>
- [`erigontech/erigon#8892`](https://github.com/erigontech/erigon/pull/8892) — caplin: to use 1 worker for snapshots compression   
  <sub>2023-12-04 · merged · authored · score 8 · compress, compression, snapshot, snapshots</sub>
- [`erigontech/erigon#8853`](https://github.com/erigontech/erigon/pull/8853) — e35: by default - minimize background impact: 1 goroutine for collate and build, 1 goroutine for merge, no parallel compression  
  <sub>2023-11-29 · merged · authored · score 8 · compress, compression, merge, parallel</sub>
- [`erigontech/erigon#4403`](https://github.com/erigontech/erigon/pull/4403) — Snapshots: allow delete .seg files  
  <sub>2022-06-08 · merged · authored · score 8 · .seg, seg file, snapshot, snapshots</sub>
- [`erigontech/erigon#3724`](https://github.com/erigontech/erigon/pull/3724) — Snapshots: start seed new large .seg files  
  <sub>2022-03-17 · merged · authored · score 8 · .seg, seg file, snapshot, snapshots</sub>
- [`erigontech/erigon#3571`](https://github.com/erigontech/erigon/pull/3571) — "erigon snapshots recompress" to apply new compression rules without db access  
  <sub>2022-02-22 · merged · authored · score 8 · compress, compression, snapshot, snapshots</sub>
- [`erigontech/erigon#3445`](https://github.com/erigontech/erigon/pull/3445) — snapshots: funcs to fast decompress all segments  
  <sub>2022-02-08 · merged · authored · score 8 · compress, decompress, snapshot, snapshots</sub>
- [`erigontech/erigon#3223`](https://github.com/erigontech/erigon/pull/3223) — Snapshots: create .seg and huffman_codes.txt in tmpdir  
  <sub>2022-01-09 · merged · authored · score 8 · .seg, huffman, snapshot, snapshots</sub>
- [`erigontech/erigon#3211`](https://github.com/erigontech/erigon/pull/3211) — Snapshot: move parallel compression to erigon-lib  
  <sub>2022-01-06 · merged · authored · score 8 · compress, compression, parallel, snapshot</sub>
- [`erigontech/erigon#3140`](https://github.com/erigontech/erigon/pull/3140) — add words count in .seg (breaking change in snapshot format)  
  <sub>2021-12-17 · merged · authored · score 8 · .seg, format, snapshot, snapshot format</sub>
- [`erigontech/erigon#21781`](https://github.com/erigontech/erigon/pull/21781) — merge: less ram usage in .bt build and compression  
  <sub>2026-06-13 · merged · authored · score 7 · compress, compression, merge</sub>
- [`erigontech/erigon#9036`](https://github.com/erigontech/erigon/pull/9036) — db migration: if stage_snapshots > 0, then create prohibit_new_downloads.lock file  
  <sub>2023-12-20 · merged · authored · score 7 · db migration, migration, snapshot, snapshots, stage</sub>
- [`ledgerwatch/erigon-lib#355`](https://github.com/ledgerwatch/erigon-lib/pull/355) — add emptyWordsCount field to .seg file header (breaking .seg format)  
  <sub>2022-03-07 · merged · authored · score 7 · .seg, format, seg file</sub>
- [`erigontech/erigon#20965`](https://github.com/erigontech/erigon/pull/20965) — [performance] change block retire's "keep in db" value to MaxReorgDepth  
  <sub>2026-05-04 · merged · reviewed · score 6 · reorg, retire</sub>
- [`erigontech/erigon#20964`](https://github.com/erigontech/erigon/pull/20964) — change block retire's "keep in db" value to MaxReorgDepth  
  <sub>2026-05-04 · merged · reviewed · score 6 · reorg, retire</sub>
- [`erigontech/erigon#20943`](https://github.com/erigontech/erigon/pull/20943) — change block retire's "keep in db" value to MaxReorgDepth  
  <sub>2026-05-01 · merged · reviewed · score 6 · reorg, retire</sub>
- [`erigontech/erigon#18825`](https://github.com/erigontech/erigon/pull/18825) — Fixed index building for v0 snapshot format  
  <sub>2026-01-27 · merged · reviewed · score 6 · format, index, snapshot, snapshot format</sub>
- [`erigontech/erigon#18746`](https://github.com/erigontech/erigon/pull/18746) — Forward compatible snapshots format  
  <sub>2026-01-21 · merged · reviewed · score 6 · format, forward compat, snapshot, snapshots</sub>
- [`erigontech/erigon#14768`](https://github.com/erigontech/erigon/pull/14768) — blocks retire: to use core rlp package instead of txpool's one  
  <sub>2025-04-26 · merged · authored · score 6 · retire, rlp </sub>
- [`erigontech/erigon#14763`](https://github.com/erigontech/erigon/pull/14763) — [r30] blocks retire: to use core rlp package instead of txpool's one  
  <sub>2025-04-26 · merged · authored · score 6 · retire, rlp </sub>
- [`erigontech/erigon#8606`](https://github.com/erigontech/erigon/pull/8606) — "erigon snapshots retire": prune, then retire, then prune  
  <sub>2023-10-28 · merged · authored · score 6 · prune, retire, snapshot, snapshots</sub>
- [`erigontech/erigon#3971`](https://github.com/erigontech/erigon/pull/3971) — Snapshots: allow stage_headers --unwind behind available snapshots  
  <sub>2022-04-26 · merged · authored · score 6 · snapshot, snapshots, stage, unwind</sub>
- [`erigontech/erigon#3558`](https://github.com/erigontech/erigon/pull/3558) — block snapshots merge  
  <sub>2022-02-21 · merged · authored · score 6 · block snapshots, merge, snapshot, snapshots</sub>
- [`erigontech/erigon#3286`](https://github.com/erigontech/erigon/pull/3286) — Snapshots: parallel compressor to allow empty words  
  <sub>2022-01-18 · merged · authored · score 6 · compress, parallel, snapshot, snapshots</sub>
- [`erigontech/erigon#21330`](https://github.com/erigontech/erigon/pull/21330) — `FillDBFromSnapshots`: to use etl pool  
  <sub>2026-05-21 · merged · authored · score 5 · etl , snapshot, snapshots</sub>
- [`erigontech/erigon#20517`](https://github.com/erigontech/erigon/pull/20517) — teach: `Unwind` beyond data in snapshots not allowed  
  <sub>2026-04-13 · merged · authored · score 5 · snapshot, snapshots, unwind</sub>
- [`erigontech/erigon#20490`](https://github.com/erigontech/erigon/pull/20490) — RoSnapshots: lock-free .View method  
  <sub>2026-04-11 · merged · authored+reviewed · score 5 · .vi, snapshot, snapshots</sub>
- [`erigontech/erigon#16198`](https://github.com/erigontech/erigon/pull/16198) — Improved consistency in bor block snapshots retiring process  
  <sub>2025-07-21 · merged · reviewed · score 5 · block snapshots, snapshot, snapshots</sub>
- [`erigontech/erigon#14947`](https://github.com/erigontech/erigon/pull/14947) — Revert commented seg retire for bor snapshots  
  <sub>2025-05-08 · merged · reviewed · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#14946`](https://github.com/erigontech/erigon/pull/14946) — Fix seg retire cmd for to not skip bor snapshots  
  <sub>2025-05-08 · merged · reviewed · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#13872`](https://github.com/erigontech/erigon/pull/13872) — fix use of `erigon snapshots retire --from/to` flags  
  <sub>2025-02-19 · merged · reviewed · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#12124`](https://github.com/erigontech/erigon/pull/12124) — Fixing new caplin snapshots interval retirement  
  <sub>2024-09-28 · merged · reviewed · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#10802`](https://github.com/erigontech/erigon/pull/10802) — `erigon snapshots retire` lock datadir  
  <sub>2024-06-19 · merged · authored · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#10393`](https://github.com/erigontech/erigon/pull/10393) — Snapshot's webseeds not added correctly in Downloader when doing 2 rounds of downloading  
  <sub>2024-05-17 · closed · reviewed · score 5 · downloader, snapshot, webseed</sub>
- [`erigontech/erigon#9752`](https://github.com/erigontech/erigon/pull/9752) — downloader: don't skip webseed if .torrent file exists (because download maybe not completed yet)  
  <sub>2024-03-19 · merged · authored · score 5 · downloader, torrent, webseed</sub>
- [`erigontech/erigon#9512`](https://github.com/erigontech/erigon/pull/9512) — snapshots: compress package renames  
  <sub>2024-02-26 · merged · reviewed · score 5 · compress, snapshot, snapshots</sub>
- [`erigontech/erigon#9295`](https://github.com/erigontech/erigon/pull/9295) — downloader: prohibit_new_downloads.lock check missed download .torrent from WebSeed  
  <sub>2024-01-24 · merged · authored · score 5 · downloader, torrent, webseed</sub>
- [`erigontech/erigon#9163`](https://github.com/erigontech/erigon/pull/9163) — "erigon snapshots retire" - doesn't see any files because version is 0 - fix  
  <sub>2024-01-08 · merged · authored · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#9101`](https://github.com/erigontech/erigon/pull/9101) — e35: etl remove merge collector  
  <sub>2023-12-29 · merged · authored · score 5 · collector, etl , merge</sub>
- [`erigontech/erigon#9053`](https://github.com/erigontech/erigon/pull/9053) — mode to produce block snapshots  
  <sub>2023-12-22 · merged · authored · score 5 · block snapshots, snapshot, snapshots</sub>
- [`erigontech/erigon#8912`](https://github.com/erigontech/erigon/pull/8912) — bor snaps: "erigon snapshots retire" to build bor files    
  <sub>2023-12-06 · merged · authored · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#8729`](https://github.com/erigontech/erigon/pull/8729) — downloader: whitelist only .seg.torrent files.   
  <sub>2023-11-15 · merged · authored · score 5 · .seg, downloader, torrent</sub>
- [`erigontech/erigon#8346`](https://github.com/erigontech/erigon/pull/8346) — downloader: download .torrent files from webseeds provider  
  <sub>2023-10-03 · merged · authored · score 5 · downloader, torrent, webseed</sub>
- [`erigontech/erigon#7662`](https://github.com/erigontech/erigon/pull/7662) — mainnet: more block snapshots  
  <sub>2023-06-05 · merged · authored · score 5 · block snapshots, snapshot, snapshots</sub>
- [`erigontech/erigon#6486`](https://github.com/erigontech/erigon/pull/6486) — "erigon snapshots retire" save progress  
  <sub>2023-01-02 · merged · authored · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#6485`](https://github.com/erigontech/erigon/pull/6485) — "erigon snapshots retire" to save progress   
  <sub>2023-01-02 · merged · authored · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#4272`](https://github.com/erigontech/erigon/pull/4272) — Use ETL to fill kv.HeaderNumber from snapshots  
  <sub>2022-05-26 · merged · authored · score 5 · etl , snapshot, snapshots</sub>
- [`erigontech/erigon#3845`](https://github.com/erigontech/erigon/pull/3845) — Snapshots: recompress.sh  
  <sub>2022-04-07 · merged · authored · score 5 · compress, snapshot, snapshots</sub>
- [`erigontech/erigon#3731`](https://github.com/erigontech/erigon/pull/3731) — Snapshots: corner cases when .seg exists and .idx doesn't  
  <sub>2022-03-18 · merged · authored · score 5 · .seg, snapshot, snapshots</sub>
- [`erigontech/erigon#3707`](https://github.com/erigontech/erigon/pull/3707) — Snapshots: retire blocks by default   
  <sub>2022-03-16 · merged · authored · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#3684`](https://github.com/erigontech/erigon/pull/3684) — Snapshots: retire testing tool  
  <sub>2022-03-12 · merged · authored · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#3603`](https://github.com/erigontech/erigon/pull/3603) — snapshots: command to debug retire blocks  
  <sub>2022-02-24 · merged · authored · score 5 · retire, snapshot, snapshots</sub>
- [`erigontech/erigon#3573`](https://github.com/erigontech/erigon/pull/3573) — "erigon snapshots recompress" add test  
  <sub>2022-02-22 · merged · authored · score 5 · compress, snapshot, snapshots</sub>
- [`erigontech/erigon#3557`](https://github.com/erigontech/erigon/pull/3557) — Erigon2: support block snapshots  
  <sub>2022-02-21 · merged · authored · score 5 · block snapshots, snapshot, snapshots</sub>
- [`erigontech/erigon#3198`](https://github.com/erigontech/erigon/pull/3198) — Snapshot: add hash first byte to headers.seg, serve p2p blocks from snapshots  
  <sub>2022-01-03 · merged · authored · score 5 · .seg, snapshot, snapshots</sub>
- [`erigontech/erigon#21700`](https://github.com/erigontech/erigon/pull/21700) — [r3.5] db/downloader: lock torrentsByName read in allActiveSnapshots  
  <sub>2026-06-09 · merged · reviewed · score 4 · downloader, snapshot, snapshots, torrent</sub>
- [`erigontech/erigon#21696`](https://github.com/erigontech/erigon/pull/21696) — db/downloader: lock torrentsByName read in allActiveSnapshots  
  <sub>2026-06-09 · merged · reviewed · score 4 · downloader, snapshot, snapshots, torrent</sub>
- [`erigontech/erigon#21089`](https://github.com/erigontech/erigon/pull/21089) — db/snapcfg: vendor erigon-snapshot/webseed inline  
  <sub>2026-05-10 · merged · reviewed · score 4 · snapshot, webseed</sub>
- [`erigontech/erigon#21023`](https://github.com/erigontech/erigon/pull/21023) — cmd/utils/app: wait for background build/merge before MergeLoop in seg retire  
  <sub>2026-05-07 · merged · reviewed · score 4 · merge, retire</sub>
- [`erigontech/erigon#20464`](https://github.com/erigontech/erigon/pull/20464) — p2p/sentry: event-driven StatusData cache, merge dual db.View  
  <sub>2026-04-10 · merged · reviewed · score 4 · .vi, merge</sub>
- [`erigontech/erigon#19190`](https://github.com/erigontech/erigon/pull/19190) — merge: add env variables to change merge workers and compress workers  
  <sub>2026-02-15 · merged · authored · score 4 · compress, merge</sub>
- [`erigontech/erigon#18995`](https://github.com/erigontech/erigon/pull/18995) — Reduce impact of background merge/compress to ChainTip  
  <sub>2026-02-06 · merged · authored · score 4 · compress, merge</sub>
- [`erigontech/erigon#18994`](https://github.com/erigontech/erigon/pull/18994) — Reduce impact of background merge/compress to ChainTip  
  <sub>2026-02-06 · merged · authored · score 4 · compress, merge</sub>
- [`erigontech/erigon#17439`](https://github.com/erigontech/erigon/pull/17439) — db/downloader: remove dead WebSeeds fields and accessors  
  <sub>2025-10-13 · merged · reviewed · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#16903`](https://github.com/erigontech/erigon/pull/16903) — Fixed calculation of start block number in snapshot retirement (#16902)  
  <sub>2025-08-29 · merged · reviewed · score 4 · retire, snapshot</sub>
- [`erigontech/erigon#16879`](https://github.com/erigontech/erigon/pull/16879) — Pull torrent fix for webseed cancellation and webseedUniqueRequestKey panic  
  <sub>2025-08-28 · merged · reviewed · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#15896`](https://github.com/erigontech/erigon/pull/15896) — Pull finishing webseed tweaks from anacrolix/torrent  
  <sub>2025-07-02 · merged · reviewed · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#15873`](https://github.com/erigontech/erigon/pull/15873) — Fixed bor events snapshot retirement  
  <sub>2025-07-01 · merged · reviewed · score 4 · retire, snapshot</sub>
- [`erigontech/erigon#15377`](https://github.com/erigontech/erigon/pull/15377) — retire: more merge threads  
  <sub>2025-05-31 · merged · authored · score 4 · merge, retire</sub>
- [`erigontech/erigon#15003`](https://github.com/erigontech/erigon/pull/15003) — cherry-pick: fix erigon seg retire to handle incomplete merges  
  <sub>2025-05-12 · merged · reviewed · score 4 · merge, retire</sub>
- [`erigontech/erigon#14973`](https://github.com/erigontech/erigon/pull/14973) — fix erigon seg retire to handle incomplete merges  
  <sub>2025-05-09 · merged · reviewed · score 4 · merge, retire</sub>
- [`erigontech/erigon#10715`](https://github.com/erigontech/erigon/pull/10715) — Improved downloader webseed performance  
  <sub>2024-06-12 · merged · reviewed · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#10177`](https://github.com/erigontech/erigon/pull/10177) — Set existing torrent webseeds after download  
  <sub>2024-05-02 · merged · reviewed · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#10149`](https://github.com/erigontech/erigon/pull/10149) — Set existing torrent webseeds after download  
  <sub>2024-04-30 · merged · reviewed · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#9643`](https://github.com/erigontech/erigon/pull/9643) — [E3] Compute infohash before creating .torrent file from webseeds  
  <sub>2024-03-08 · closed · reviewed · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#9642`](https://github.com/erigontech/erigon/pull/9642) — Compute infohash before creating .torrent file from webseeds  
  <sub>2024-03-08 · merged · reviewed · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#9586`](https://github.com/erigontech/erigon/pull/9586) — downloader: move webseed discover to mainLoop #9583  
  <sub>2024-03-05 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#9583`](https://github.com/erigontech/erigon/pull/9583) — downloader: move webseed discover to mainLoop  
  <sub>2024-03-05 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#9068`](https://github.com/erigontech/erigon/pull/9068) — block retire: merge all possible files (even bor) even if nothing to retire  
  <sub>2023-12-24 · merged · authored · score 4 · merge, retire</sub>
- [`erigontech/erigon#9052`](https://github.com/erigontech/erigon/pull/9052) — allow erigon download .torrent from webseed by default  
  <sub>2023-12-22 · merged · authored · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#9045`](https://github.com/erigontech/erigon/pull/9045) — downloader: handle race between adding magnet link and files from webseed  
  <sub>2023-12-21 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#8901`](https://github.com/erigontech/erigon/pull/8901) — e35: torrent lib with webseeds methods  
  <sub>2023-12-05 · merged · authored · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#8879`](https://github.com/erigontech/erigon/pull/8879) — downloader: download rates per peer with webseeds  
  <sub>2023-12-01 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#8820`](https://github.com/erigontech/erigon/pull/8820) — webseed: .torrent file validation must check - fileName and hash   
  <sub>2023-11-23 · merged · authored · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#8662`](https://github.com/erigontech/erigon/pull/8662) — downloader: demote webseed request errors  
  <sub>2023-11-06 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#8629`](https://github.com/erigontech/erigon/pull/8629) — webseed: don't download .torrent files   
  <sub>2023-10-31 · merged · authored · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#8611`](https://github.com/erigontech/erigon/pull/8611) — downloader: webseed better error messages  
  <sub>2023-10-30 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#8607`](https://github.com/erigontech/erigon/pull/8607) — downloader: less webseed logs (#8586)  
  <sub>2023-10-29 · merged · reviewed · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#8586`](https://github.com/erigontech/erigon/pull/8586) — downloader: less webseed logs  
  <sub>2023-10-25 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#8512`](https://github.com/erigontech/erigon/pull/8512) — downloader: default webseed token for e2   
  <sub>2023-10-18 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#8510`](https://github.com/erigontech/erigon/pull/8510) — downloader: less webseed logs  
  <sub>2023-10-18 · merged · authored · score 4 · downloader, webseed</sub>
- [`erigontech/erigon#8176`](https://github.com/erigontech/erigon/pull/8176) — torrent: add --webseeds cli arg  
  <sub>2023-09-12 · merged · authored · score 4 · torrent, webseed</sub>
- [`erigontech/erigon#8170`](https://github.com/erigontech/erigon/pull/8170) — Downloader: don't fail when see unusual file, skip it (backward/forward compatibility)  
  <sub>2023-09-10 · merged · authored · score 4 · downloader, forward compat</sub>
- [`erigontech/erigon#6300`](https://github.com/erigontech/erigon/pull/6300) — e3: cli command to retire/prune history  
  <sub>2022-12-14 · merged · authored · score 4 · prune, retire</sub>
- [`erigontech/erigon#5561`](https://github.com/erigontech/erigon/pull/5561) — erigon3: agg to use workers for compress and merge  
  <sub>2022-09-28 · merged · authored · score 4 · compress, merge</sub>
- [`erigontech/erigon#4229`](https://github.com/erigontech/erigon/pull/4229) — torrent and roaring libs version up  
  <sub>2022-05-22 · merged · authored · score 4 · roaring, torrent</sub>
- [`erigontech/erigon#3925`](https://github.com/erigontech/erigon/pull/3925) — Snapshots: Max index parallelism to 4  
  <sub>2022-04-21 · merged · authored · score 4 · index, parallel, snapshot, snapshots</sub>
- [`erigontech/erigon#3794`](https://github.com/erigontech/erigon/pull/3794) — snapshots: prune txlookup  
  <sub>2022-03-30 · merged · authored · score 4 · lookup, prune, snapshot, snapshots</sub>
- [`erigontech/erigon#3607`](https://github.com/erigontech/erigon/pull/3607) — snapshots: indexing of recently merged range   
  <sub>2022-02-24 · merged · authored · score 4 · index, merge, snapshot, snapshots</sub>
- [`erigontech/erigon#3606`](https://github.com/erigontech/erigon/pull/3606) — snapshots: indexing of recently merged range  
  <sub>2022-02-24 · merged · authored · score 4 · index, merge, snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#42`](https://github.com/erigontech/erigon-snapshot/pull/42) — Downloader webseed token  
  <sub>2023-10-18 · merged · authored · score 4 · downloader, webseed</sub>
- [`ledgerwatch/erigon-lib#1122`](https://github.com/ledgerwatch/erigon-lib/pull/1122) — torrent: add --webseeds cli arg  
  <sub>2023-09-12 · merged · authored · score 4 · torrent, webseed</sub>
- [`ledgerwatch/erigon-lib#1117`](https://github.com/ledgerwatch/erigon-lib/pull/1117) — Downloader: don't fail when see unusual file, skip it (backward/forward compatibility)  
  <sub>2023-09-10 · merged · authored · score 4 · downloader, forward compat</sub>
- [`ledgerwatch/erigon-lib#657`](https://github.com/ledgerwatch/erigon-lib/pull/657) — erigon3: allow set workers amount for history compress and merge  
  <sub>2022-09-28 · merged · authored · score 4 · compress, merge</sub>
- [`erigontech/erigon#19727`](https://github.com/erigontech/erigon/pull/19727) — [cherry-pick] [r34] snapcfg: lazy-parse EmbeddedWebseeds, only parse the chain in use  
  <sub>2026-03-08 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#19722`](https://github.com/erigontech/erigon/pull/19722) — snapcfg: lazy-parse EmbeddedWebseeds, only parse the chain in use  
  <sub>2026-03-07 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#19036`](https://github.com/erigontech/erigon/pull/19036) — Caplin: to not insert frozen blocks  
  <sub>2026-02-08 · merged · reviewed · score 3 · frozen blocks</sub>
- [`erigontech/erigon#19001`](https://github.com/erigontech/erigon/pull/19001) — integrations stage_exec: restore deleted `stageExecProgress` recovery based on snapshots data  
  <sub>2026-02-06 · merged · authored · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon#18943`](https://github.com/erigontech/erigon/pull/18943) — Teach claude skills for building erigon and seg retire  
  <sub>2026-02-03 · merged · reviewed · score 3 · retire</sub>
- [`erigontech/erigon#18710`](https://github.com/erigontech/erigon/pull/18710) — Tighten warnings and logging around webseed and HTTP metainfo handling  
  <sub>2026-01-19 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#16919`](https://github.com/erigontech/erigon/pull/16919) — Pull another fix for unique webseed request panic  
  <sub>2025-08-31 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#16690`](https://github.com/erigontech/erigon/pull/16690) — [r31] dl.Del call from `pruneBlockSnapshots`  
  <sub>2025-08-16 · merged · authored · score 3 · prune, snapshot, snapshots</sub>
- [`erigontech/erigon#16598`](https://github.com/erigontech/erigon/pull/16598) — Support overriding remote preverified hashes and clobbering webseeds  
  <sub>2025-08-13 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#16551`](https://github.com/erigontech/erigon/pull/16551) — ensure bor dbs are opened in seg retire (#16515)  
  <sub>2025-08-11 · merged · reviewed · score 3 · retire</sub>
- [`erigontech/erigon#16515`](https://github.com/erigontech/erigon/pull/16515) — ensure bor dbs are opened in seg retire  
  <sub>2025-08-08 · merged · reviewed · score 3 · retire</sub>
- [`erigontech/erigon#16507`](https://github.com/erigontech/erigon/pull/16507) — snapshots reset, torrent logging and upgrade docs  
  <sub>2025-08-08 · merged · reviewed · score 3 · snapshot, snapshots, torrent</sub>
- [`erigontech/erigon#16087`](https://github.com/erigontech/erigon/pull/16087) — Fix a few misc mux and webseed issues spotted by Alex  
  <sub>2025-07-14 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#15981`](https://github.com/erigontech/erigon/pull/15981) — `seg retire`: remove external misleading check  
  <sub>2025-07-07 · merged · reviewed · score 3 · retire</sub>
- [`erigontech/erigon#15914`](https://github.com/erigontech/erigon/pull/15914) — Cherry-pick: Fixed milestone pruning and fixed BorEvents snapshots  
  <sub>2025-07-03 · merged · reviewed · score 3 · pruning, snapshot, snapshots</sub>
- [`erigontech/erigon#15912`](https://github.com/erigontech/erigon/pull/15912) — Add WebSeed download rate flag  
  <sub>2025-07-03 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#15765`](https://github.com/erigontech/erigon/pull/15765) — Pull latest webseed performance improvements WIP  
  <sub>2025-06-26 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#15053`](https://github.com/erigontech/erigon/pull/15053) — retire: high-level MadvNormal  
  <sub>2025-05-15 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#14896`](https://github.com/erigontech/erigon/pull/14896) — workarount "retire" for bormilestone files  
  <sub>2025-05-06 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#14362`](https://github.com/erigontech/erigon/pull/14362) — exclude manifest.txt from webseed check  
  <sub>2025-03-29 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#12332`](https://github.com/erigontech/erigon/pull/12332) — RPCDaemon and Erigon: don't open files at startup if download is not finished (StageSnapshots == 0)  
  <sub>2024-10-16 · merged · authored+reviewed · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon#11761`](https://github.com/erigontech/erigon/pull/11761) — dl: check if webseed exists by `HEAD` request with small deadline  
  <sub>2024-08-27 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#11539`](https://github.com/erigontech/erigon/pull/11539) — Erigon: Added verification for whether snapshots are publishable or not and added clearIndexing command  
  <sub>2024-08-08 · merged · reviewed · score 3 · index, snapshot, snapshots</sub>
- [`erigontech/erigon#11329`](https://github.com/erigontech/erigon/pull/11329) — Erigon 3: Added `--all` flag to `downloader` to generate downloader for non-seedable snapshots  
  <sub>2024-07-25 · merged · reviewed · score 3 · downloader, snapshot, snapshots</sub>
- [`erigontech/erigon#11037`](https://github.com/erigontech/erigon/pull/11037) — dl: discover webseeds even if this file type is prohibited by .lock  
  <sub>2024-07-05 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#10922`](https://github.com/erigontech/erigon/pull/10922) — mandatory `verbosity=debug` for `print_stages` and `snapshots stat`  
  <sub>2024-06-26 · merged · reviewed · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon#10876`](https://github.com/erigontech/erigon/pull/10876) — retire bor files: don't stop after first iteration  
  <sub>2024-06-24 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#10858`](https://github.com/erigontech/erigon/pull/10858) — dl: nable CI webseeds chk  
  <sub>2024-06-22 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#10856`](https://github.com/erigontech/erigon/pull/10856) — dl: WebseedActiveTrips counters  
  <sub>2024-06-22 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#10815`](https://github.com/erigontech/erigon/pull/10815) — webseed docs  
  <sub>2024-06-20 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#10634`](https://github.com/erigontech/erigon/pull/10634) — erigon retire: infinity loop at bor chains  
  <sub>2024-06-06 · merged · reviewed · score 3 · retire</sub>
- [`erigontech/erigon#10598`](https://github.com/erigontech/erigon/pull/10598) — e3: bor blocks retire: infinity loop fix  
  <sub>2024-06-03 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#10596`](https://github.com/erigontech/erigon/pull/10596) — bor blocks retire: infinity loop fix  
  <sub>2024-06-03 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#10361`](https://github.com/erigontech/erigon/pull/10361) — retry on some errors to fetch data from webseed `manifest-verify`  
  <sub>2024-05-15 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#10243`](https://github.com/erigontech/erigon/pull/10243) — e2: bor-mainnet fix broken v1-054600-054700-borspans.seg   
  <sub>2024-05-08 · merged · authored · score 3 · .seg</sub>
- [`erigontech/erigon#10242`](https://github.com/erigontech/erigon/pull/10242) — e3: bor-mainnet fix broken v1-054600-054700-borspans.seg  
  <sub>2024-05-08 · merged · authored · score 3 · .seg</sub>
- [`erigontech/erigon#10021`](https://github.com/erigontech/erigon/pull/10021) — E35 skip frozen blocks processing during mock test  
  <sub>2024-04-22 · merged · reviewed · score 3 · frozen blocks</sub>
- [`erigontech/erigon#9996`](https://github.com/erigontech/erigon/pull/9996) — `erigon snapshots index: support caplin's files  
  <sub>2024-04-19 · merged · authored · score 3 · index, snapshot, snapshots</sub>
- [`erigontech/erigon#9980`](https://github.com/erigontech/erigon/pull/9980) — "erigon snapsots retire": to build all files   
  <sub>2024-04-18 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#9979`](https://github.com/erigontech/erigon/pull/9979) — "erigon snapsots retire": to build all files  
  <sub>2024-04-18 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#9941`](https://github.com/erigontech/erigon/pull/9941) — manifest-verify: if --webseed parameter is not empty, don't add default buckets  
  <sub>2024-04-15 · closed · authored · score 3 · webseed</sub>
- [`erigontech/erigon#9857`](https://github.com/erigontech/erigon/pull/9857) — exitCode 1 when got webseed errs, added report overview in the end  
  <sub>2024-04-03 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#9853`](https://github.com/erigontech/erigon/pull/9853) —  check webseeds has files declared in manifest  
  <sub>2024-04-02 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#9762`](https://github.com/erigontech/erigon/pull/9762) — added command to verify remote manifests from webseeds  
  <sub>2024-03-19 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon#9740`](https://github.com/erigontech/erigon/pull/9740) — e35: restore lost webseeds urls  
  <sub>2024-03-18 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#9638`](https://github.com/erigontech/erigon/pull/9638) — retire blocks: pre-check if db has enough data to build files  
  <sub>2024-03-08 · merged · authored+reviewed · score 3 · retire</sub>
- [`erigontech/erigon#9623`](https://github.com/erigontech/erigon/pull/9623) — better retire logs  
  <sub>2024-03-07 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#9622`](https://github.com/erigontech/erigon/pull/9622) — better retire logs  
  <sub>2024-03-07 · closed · authored · score 3 · retire</sub>
- [`erigontech/erigon#9350`](https://github.com/erigontech/erigon/pull/9350) — Remove private S3 buckets webseed feature (and was sdk dependency)    
  <sub>2024-01-31 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#9318`](https://github.com/erigontech/erigon/pull/9318) — RpcDaemon doesn't see recently retired blocks   
  <sub>2024-01-26 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#9268`](https://github.com/erigontech/erigon/pull/9268) — fix potential nil ptr in bor sn retirement  
  <sub>2024-01-19 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#9153`](https://github.com/erigontech/erigon/pull/9153) — Change retire progress log level to debug  
  <sub>2024-01-07 · merged · reviewed · score 3 · retire</sub>
- [`erigontech/erigon#9083`](https://github.com/erigontech/erigon/pull/9083) — return deleted caplin-v2 webseed  
  <sub>2023-12-26 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#9072`](https://github.com/erigontech/erigon/pull/9072) — fix typo in snap webseed server names  
  <sub>2023-12-24 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#9061`](https://github.com/erigontech/erigon/pull/9061) — retire: handle case when bor snaps are behind block snaps  
  <sub>2023-12-23 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#9009`](https://github.com/erigontech/erigon/pull/9009) — erigon snapshots index: build bor indices  
  <sub>2023-12-18 · merged · authored · score 3 · index, snapshot, snapshots</sub>
- [`erigontech/erigon#8908`](https://github.com/erigontech/erigon/pull/8908) — Fix snap initialization from frozen blocks  
  <sub>2023-12-05 · merged · reviewed · score 3 · frozen blocks</sub>
- [`erigontech/erigon#8862`](https://github.com/erigontech/erigon/pull/8862) — prnt_stages: to show value of --snapshots flag  
  <sub>2023-11-30 · merged · authored · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon#8614`](https://github.com/erigontech/erigon/pull/8614) — snapshots: reduce merge limit of blocks to 100K  
  <sub>2023-10-30 · merged · authored · score 3 · merge, snapshot, snapshots</sub>
- [`erigontech/erigon#8466`](https://github.com/erigontech/erigon/pull/8466) — better webseed support  
  <sub>2023-10-13 · merged · authored · score 3 · webseed</sub>
- [`erigontech/erigon#8375`](https://github.com/erigontech/erigon/pull/8375) — downloader: move from `snapshots/db` to `snapshots/downloader`  
  <sub>2023-10-05 · merged · authored · score 3 · downloader, snapshot, snapshots</sub>
- [`erigontech/erigon#7614`](https://github.com/erigontech/erigon/pull/7614) — blocks retire: fix baseID logic  
  <sub>2023-06-01 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#6846`](https://github.com/erigontech/erigon/pull/6846) — Snapshots Indexing: avoid loop with semaphore locking before logging   
  <sub>2023-02-12 · merged · authored · score 3 · index, snapshot, snapshots</sub>
- [`erigontech/erigon#6845`](https://github.com/erigontech/erigon/pull/6845) — Snapshots Indexing: avoid loop with semaphore locking before logging  
  <sub>2023-02-12 · merged · authored · score 3 · index, snapshot, snapshots</sub>
- [`erigontech/erigon#6484`](https://github.com/erigontech/erigon/pull/6484) — e3: force merge snapshots before reconst  
  <sub>2023-01-02 · merged · authored · score 3 · merge, snapshot, snapshots</sub>
- [`erigontech/erigon#6431`](https://github.com/erigontech/erigon/pull/6431) — stage_snapshots: clean table before initial write  
  <sub>2022-12-24 · merged · authored · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon#5680`](https://github.com/erigontech/erigon/pull/5680) — erigon3: cli command to force merge snapshots  
  <sub>2022-10-10 · merged · authored · score 3 · merge, snapshot, snapshots</sub>
- [`erigontech/erigon#5261`](https://github.com/erigontech/erigon/pull/5261) — Adding a new stage for snapshots download and creation  
  <sub>2022-09-01 · merged · reviewed · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon#5174`](https://github.com/erigontech/erigon/pull/5174) — snapshots: check gap between snapshots and db at Erigon startup (after download confirmation from Downloader)  
  <sub>2022-08-25 · merged · authored · score 3 · downloader, snapshot, snapshots</sub>
- [`erigontech/erigon#5150`](https://github.com/erigontech/erigon/pull/5150) — Snapshots: Erigon update list in db only after Downloader confirmation, rpcdaemon read list from db   
  <sub>2022-08-23 · merged · authored · score 3 · downloader, snapshot, snapshots</sub>
- [`erigontech/erigon#4803`](https://github.com/erigontech/erigon/pull/4803) — RetireBlocks: encapsulate delete logic  
  <sub>2022-07-23 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#4785`](https://github.com/erigontech/erigon/pull/4785) — RetireBlocks: less arguments  
  <sub>2022-07-22 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#4501`](https://github.com/erigontech/erigon/pull/4501) — "torrent_hashes --verify" to detect "snapshots/tmp" dir  
  <sub>2022-06-20 · merged · authored · score 3 · snapshot, snapshots, torrent</sub>
- [`erigontech/erigon#3983`](https://github.com/erigontech/erigon/pull/3983) — Snapshots: TxLookup empty block body   
  <sub>2022-04-27 · merged · authored · score 3 · lookup, snapshot, snapshots</sub>
- [`erigontech/erigon#3969`](https://github.com/erigontech/erigon/pull/3969) — Snapshots: open bittorrent udp port in docker  
  <sub>2022-04-26 · merged · authored · score 3 · snapshot, snapshots, torrent</sub>
- [`erigontech/erigon#3869`](https://github.com/erigontech/erigon/pull/3869) — RetireBlocks: preserve genesis  
  <sub>2022-04-11 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#3823`](https://github.com/erigontech/erigon/pull/3823) — Snapsthos: build indices on retire blocks  
  <sub>2022-04-05 · merged · authored · score 3 · retire</sub>
- [`erigontech/erigon#3822`](https://github.com/erigontech/erigon/pull/3822) — Snapshots: reopen after merge  
  <sub>2022-04-05 · merged · authored · score 3 · merge, snapshot, snapshots</sub>
- [`erigontech/erigon#3761`](https://github.com/erigontech/erigon/pull/3761) — Snapshots: gen .torrent file only for big segments  
  <sub>2022-03-24 · merged · authored · score 3 · snapshot, snapshots, torrent</sub>
- [`erigontech/erigon#3733`](https://github.com/erigontech/erigon/pull/3733) — Snapshots: do indexing for older ranges if need   
  <sub>2022-03-18 · merged · authored · score 3 · index, snapshot, snapshots</sub>
- [`erigontech/erigon#3645`](https://github.com/erigontech/erigon/pull/3645) — snapshots: merge segments strategy   
  <sub>2022-03-04 · merged · authored · score 3 · merge, snapshot, snapshots</sub>
- [`erigontech/erigon#3619`](https://github.com/erigontech/erigon/pull/3619) — snapshots: delete .idx after merge  
  <sub>2022-02-25 · merged · authored · score 3 · merge, snapshot, snapshots</sub>
- [`erigontech/erigon#3518`](https://github.com/erigontech/erigon/pull/3518) — snapshots: header stage fixes  
  <sub>2022-02-16 · merged · authored · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon#3506`](https://github.com/erigontech/erigon/pull/3506) — snapshots: use blockReader in IH stage  
  <sub>2022-02-13 · merged · authored · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon#3259`](https://github.com/erigontech/erigon/pull/3259) — Snapshots: watch the burn stage  
  <sub>2022-01-14 · merged · authored · score 3 · snapshot, snapshots, stage</sub>
- [`erigontech/erigon-snapshot#1287`](https://github.com/erigontech/erigon-snapshot/pull/1287) — Remove unused webseed/ directory  
  <sub>2026-05-22 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon-snapshot#1282`](https://github.com/erigontech/erigon-snapshot/pull/1282) — webseed: point mainnet/sepolia/chiado/gnosis/hoodi at erigon36-v1 buckets  
  <sub>2026-05-22 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon-snapshot#160`](https://github.com/erigontech/erigon-snapshot/pull/160) — e2: bor-mainnet fix broken v1-054600-054700-borspans.seg   
  <sub>2024-05-08 · merged · authored · score 3 · .seg</sub>
- [`erigontech/erigon-snapshot#159`](https://github.com/erigontech/erigon-snapshot/pull/159) — e3: bor-mainnet fix broken v1-054600-054700-borspans.seg   
  <sub>2024-05-08 · merged · authored · score 3 · .seg</sub>
- [`erigontech/erigon-snapshot#158`](https://github.com/erigontech/erigon-snapshot/pull/158) — e3: bor-mainnet fix broken v1-054600-054700-borspans.seg  
  <sub>2024-05-08 · closed · authored · score 3 · .seg</sub>
- [`erigontech/erigon-snapshot#123`](https://github.com/erigontech/erigon-snapshot/pull/123) — e35 webseeds update  
  <sub>2024-02-19 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon-snapshot#122`](https://github.com/erigontech/erigon-snapshot/pull/122) — Updated all webseeds (E2)  
  <sub>2024-02-16 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon-snapshot#98`](https://github.com/erigontech/erigon-snapshot/pull/98) — Correct caplin webseeds for mainnet  
  <sub>2023-12-31 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon-snapshot#97`](https://github.com/erigontech/erigon-snapshot/pull/97) — Added correct sepolia webseed for Caplin  
  <sub>2023-12-31 · merged · reviewed · score 3 · webseed</sub>
- [`erigontech/erigon-snapshot#93`](https://github.com/erigontech/erigon-snapshot/pull/93) — return deleted caplin-v2 webseed  
  <sub>2023-12-26 · merged · authored · score 3 · webseed</sub>
- [`ledgerwatch/erigon-lib#818`](https://github.com/ledgerwatch/erigon-lib/pull/818) — e3: force merge snapshots before reconst  
  <sub>2023-01-02 · merged · authored · score 3 · merge, snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#672`](https://github.com/ledgerwatch/erigon-lib/pull/672) — erigon3: cli command to force merge snapshots  
  <sub>2022-10-10 · merged · authored · score 3 · merge, snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#212`](https://github.com/ledgerwatch/erigon-lib/pull/212) — add words count in .seg  
  <sub>2021-12-17 · merged · authored · score 3 · .seg</sub>
- [`erigontech/erigon#21766`](https://github.com/erigontech/erigon/pull/21766) — docs: warn that `snapshots reset` is destructive (upgrading guide)  
  <sub>2026-06-12 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#21594`](https://github.com/erigontech/erigon/pull/21594) — cl/antiquary: batch beacon snapshot indexing  
  <sub>2026-06-03 · merged · reviewed · score 2 · index, snapshot</sub>
- [`erigontech/erigon#21079`](https://github.com/erigontech/erigon/pull/21079) — db/snapcfg: internalize SnapshotSource enum, drop stale TODOs  
  <sub>2026-05-09 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#20900`](https://github.com/erigontech/erigon/pull/20900) — enforce block-snapshots cap inside aggregator collation  
  <sub>2026-04-29 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#20852`](https://github.com/erigontech/erigon/pull/20852) — enforce block-snapshots cap inside aggregator collation  
  <sub>2026-04-28 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#20570`](https://github.com/erigontech/erigon/pull/20570) — downloader: torrent_hashes --diff flag  
  <sub>2026-04-15 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#20569`](https://github.com/erigontech/erigon/pull/20569) — `downloader torrent_hashes --diff`  
  <sub>2026-04-15 · closed · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#20565`](https://github.com/erigontech/erigon/pull/20565) — merge: set `merge workers` to 1. because all components already support own parallel-bulding  
  <sub>2026-04-15 · merged · authored · score 2 · merge, parallel</sub>
- [`erigontech/erigon#20526`](https://github.com/erigontech/erigon/pull/20526) — downloader: decentralized snapshot distribution via chain.toml P2P discovery  
  <sub>2026-04-13 · merged · reviewed · score 2 · downloader, snapshot</sub>
- [`erigontech/erigon#20071`](https://github.com/erigontech/erigon/pull/20071) — [r3.4] downloader: update anacrolix/torrent to latest master  
  <sub>2026-03-22 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#19674`](https://github.com/erigontech/erigon/pull/19674) — downloader: update anacrolix/torrent to latest master  
  <sub>2026-03-06 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#19365`](https://github.com/erigontech/erigon/pull/19365) — merge: lookupByShortenedKey: reuse buffer  
  <sub>2026-02-20 · merged · authored · score 2 · lookup, merge</sub>
- [`erigontech/erigon#19355`](https://github.com/erigontech/erigon/pull/19355) — merge: findShortenedKey: reuse shortenedKeyOffset encoding buffer   
  <sub>2026-02-20 · merged · authored+reviewed · score 2 · encoding, merge</sub>
- [`erigontech/erigon#19207`](https://github.com/erigontech/erigon/pull/19207) — stage_exec: allow more workers for build/collate/merge  
  <sub>2026-02-16 · merged · reviewed · score 2 · merge, stage</sub>
- [`erigontech/erigon#19090`](https://github.com/erigontech/erigon/pull/19090) — Improvements for history snapshot benchmark test + useful cmd to print distribution of the keys in snapshots  
  <sub>2026-02-10 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#18585`](https://github.com/erigontech/erigon/pull/18585) — fix block reader to read genesis from db and not snapshots  
  <sub>2026-01-07 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#18360`](https://github.com/erigontech/erigon/pull/18360) — fix seed call of merged files to downloader  
  <sub>2025-12-17 · merged · reviewed · score 2 · downloader, merge</sub>
- [`erigontech/erigon#18255`](https://github.com/erigontech/erigon/pull/18255) — Buffer downloader/torrentClientStatus  
  <sub>2025-12-11 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#18146`](https://github.com/erigontech/erigon/pull/18146) — Remove extra --chain flag to snapshots reset  
  <sub>2025-12-03 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#17961`](https://github.com/erigontech/erigon/pull/17961) — Implemented rebuild cmd for history snapshots  
  <sub>2025-11-18 · closed · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#17958`](https://github.com/erigontech/erigon/pull/17958) — Added dedup mechanism in history snapshots  
  <sub>2025-11-18 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#17893`](https://github.com/erigontech/erigon/pull/17893) — db/services: move over BlockSnapshots and DownloadRequest  
  <sub>2025-11-14 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#17864`](https://github.com/erigontech/erigon/pull/17864) — Dump tool to print history snapshots content  
  <sub>2025-11-12 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#17399`](https://github.com/erigontech/erigon/pull/17399) — db/downloader: make FilesTotal reflect torrent count; remove dead accumulation  
  <sub>2025-10-09 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#16943`](https://github.com/erigontech/erigon/pull/16943) — agg: move `CheckSnapshotsCompatibility` outside of `NewAgg`  as test's bottleneck  
  <sub>2025-09-02 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16930`](https://github.com/erigontech/erigon/pull/16930) — cp: snapshots_cmd related PRs from main  
  <sub>2025-09-01 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16867`](https://github.com/erigontech/erigon/pull/16867) — warn for using old snapshots (cp from 3.1)  
  <sub>2025-08-27 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16794`](https://github.com/erigontech/erigon/pull/16794) — Cherry pick downloader and torrent fixes from 3.1  
  <sub>2025-08-25 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#16792`](https://github.com/erigontech/erigon/pull/16792) — Improve snapshots reset action  
  <sub>2025-08-25 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16758`](https://github.com/erigontech/erigon/pull/16758) — Fix regression in hashing file holes in snapshots  
  <sub>2025-08-21 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16756`](https://github.com/erigontech/erigon/pull/16756) — `erigon snapshots meta`: to print keys_size/vals_size  
  <sub>2025-08-21 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16662`](https://github.com/erigontech/erigon/pull/16662) — Cherry pick snapshot overriding and downloader.verify fixes from 3.1  
  <sub>2025-08-15 · merged · reviewed · score 2 · downloader, snapshot</sub>
- [`erigontech/erigon#16655`](https://github.com/erigontech/erigon/pull/16655) — Require torrents added from disk to complete on `downloader.verify`  
  <sub>2025-08-15 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#16487`](https://github.com/erigontech/erigon/pull/16487) — Revert "Added timeout for bor snapshots if data is not ready"  
  <sub>2025-08-07 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16435`](https://github.com/erigontech/erigon/pull/16435) — [r3.1] warn for using old snapshots  
  <sub>2025-08-04 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16359`](https://github.com/erigontech/erigon/pull/16359) — Added timeout for bor snapshots if data is not ready  
  <sub>2025-07-30 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16357`](https://github.com/erigontech/erigon/pull/16357) — Clarify snapshots reset before file naming update  
  <sub>2025-07-30 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16348`](https://github.com/erigontech/erigon/pull/16348) — downloader: avoid loading snapshot hashes for unsupported networks  
  <sub>2025-07-29 · merged · reviewed · score 2 · downloader, snapshot</sub>
- [`erigontech/erigon#16346`](https://github.com/erigontech/erigon/pull/16346) — [r3.1] v1.1zation of e3.1 snapshots  
  <sub>2025-07-29 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16345`](https://github.com/erigontech/erigon/pull/16345) — Added timeout for bor snapshots if data is not ready  
  <sub>2025-07-29 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16338`](https://github.com/erigontech/erigon/pull/16338) — Fix the snapshots reset command usage  
  <sub>2025-07-29 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#16328`](https://github.com/erigontech/erigon/pull/16328) — Torrent performance and misc downloader tweaks  
  <sub>2025-07-28 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#16288`](https://github.com/erigontech/erigon/pull/16288) — [r3.1] auto upgrade snapshots  
  <sub>2025-07-25 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#15692`](https://github.com/erigontech/erigon/pull/15692) — [30] Fixed issue with gaps in checkpoint snapshots when heimdall publish them too late  
  <sub>2025-06-21 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#15641`](https://github.com/erigontech/erigon/pull/15641) — Fixed issue with gaps in checkpoint snapshots when heimdall publish t…  
  <sub>2025-06-18 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#15473`](https://github.com/erigontech/erigon/pull/15473) — Fixed snapshot downloader inconsistency for minimal mode node (#15429)  
  <sub>2025-06-05 · merged · reviewed · score 2 · downloader, snapshot</sub>
- [`erigontech/erigon#15429`](https://github.com/erigontech/erigon/pull/15429) — Fixed snapshot downloader inconsistency for minimal mode node  
  <sub>2025-06-03 · merged · reviewed · score 2 · downloader, snapshot</sub>
- [`erigontech/erigon#15283`](https://github.com/erigontech/erigon/pull/15283) — [e31] dl: remove .torrent after merge  
  <sub>2025-05-27 · merged · authored · score 2 · merge, torrent</sub>
- [`erigontech/erigon#15282`](https://github.com/erigontech/erigon/pull/15282) — dl: remove .torrent after merge   
  <sub>2025-05-27 · merged · authored · score 2 · merge, torrent</sub>
- [`erigontech/erigon#14906`](https://github.com/erigontech/erigon/pull/14906) — cmd/utils: Remove unnecessary `LoadSnapshotsHashes` invocation  
  <sub>2025-05-06 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#14828`](https://github.com/erigontech/erigon/pull/14828) — Expose downloader torrent client status to HTTP (#14639)  
  <sub>2025-05-01 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#14779`](https://github.com/erigontech/erigon/pull/14779) — `downloader torrent_create`: enable `--all` by default  
  <sub>2025-04-27 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#14760`](https://github.com/erigontech/erigon/pull/14760) — reload salt file post snapshots download  
  <sub>2025-04-25 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#14639`](https://github.com/erigontech/erigon/pull/14639) — Expose downloader torrent client status to HTTP  
  <sub>2025-04-17 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#14441`](https://github.com/erigontech/erigon/pull/14441) — snapshot repo and filename schema  
  <sub>2025-04-04 · merged · reviewed · score 2 · schema, snapshot</sub>
- [`erigontech/erigon#14387`](https://github.com/erigontech/erigon/pull/14387) — [DO NOT MERGE] add file name parser/gen to SnapshotConfig  
  <sub>2025-04-01 · closed · reviewed · score 2 · merge, snapshot</sub>
- [`erigontech/erigon#13442`](https://github.com/erigontech/erigon/pull/13442) — [DO NOT MERGE] make IndexRange agnostic of business logic  
  <sub>2025-01-15 · closed · reviewed · score 2 · index, merge</sub>
- [`erigontech/erigon#13355`](https://github.com/erigontech/erigon/pull/13355) — allSnapshots should not panic regardlessly  
  <sub>2025-01-09 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#13253`](https://github.com/erigontech/erigon/pull/13253) — remove agg from SnapshotsCfg  
  <sub>2024-12-27 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#13018`](https://github.com/erigontech/erigon/pull/13018) — Empty ChainName in snapshots   
  <sub>2024-12-06 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#12954`](https://github.com/erigontech/erigon/pull/12954) — Caplin: fix broken snapshots  
  <sub>2024-12-02 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#12534`](https://github.com/erigontech/erigon/pull/12534) — Fixing blob snapshots not being opened correctly  
  <sub>2024-10-29 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#12529`](https://github.com/erigontech/erigon/pull/12529) — downloader: check chainID before torrent_create  
  <sub>2024-10-29 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#11957`](https://github.com/erigontech/erigon/pull/11957) — polygon/bor: fix panic in BorRoSnapshots checkpoint funcs when waypoint snapshots disabled  
  <sub>2024-09-11 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#11850`](https://github.com/erigontech/erigon/pull/11850) — downloader: added downloaded torrents notifier  
  <sub>2024-09-03 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#11714`](https://github.com/erigontech/erigon/pull/11714) — `erigon snapshots meta` command  
  <sub>2024-08-22 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#11416`](https://github.com/erigontech/erigon/pull/11416) — don't close `roSnapshots` objects while files download  
  <sub>2024-07-31 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#11331`](https://github.com/erigontech/erigon/pull/11331) — diagnostics: refactor snapshot indexing  
  <sub>2024-07-25 · merged · reviewed · score 2 · index, snapshot</sub>
- [`erigontech/erigon#11313`](https://github.com/erigontech/erigon/pull/11313) — E3: Fixed and simplified block snapshot pruning  
  <sub>2024-07-24 · merged · reviewed · score 2 · pruning, snapshot</sub>
- [`erigontech/erigon#11250`](https://github.com/erigontech/erigon/pull/11250) — Caplin: Add support for beacon snapshots (also stops relying on Engine API)  
  <sub>2024-07-20 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#11105`](https://github.com/erigontech/erigon/pull/11105) — Diagnostics: snapshot stage info gathering  
  <sub>2024-07-10 · merged · reviewed · score 2 · snapshot, stage</sub>
- [`erigontech/erigon#11086`](https://github.com/erigontech/erigon/pull/11086) — `erigon snapshots`: clean func  
  <sub>2024-07-09 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#11084`](https://github.com/erigontech/erigon/pull/11084) — `erigon snapshots ls` command  
  <sub>2024-07-09 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10945`](https://github.com/erigontech/erigon/pull/10945) — snapshots updated for amoy, holesky, sepolia and gnosis  
  <sub>2024-06-28 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10936`](https://github.com/erigontech/erigon/pull/10936) — diagnostics: finished with snapshot substages  
  <sub>2024-06-27 · merged · reviewed · score 2 · snapshot, stage</sub>
- [`erigontech/erigon#10906`](https://github.com/erigontech/erigon/pull/10906) — `erigon snapshots stats` command to print status of snapshots  
  <sub>2024-06-25 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10885`](https://github.com/erigontech/erigon/pull/10885) — `capcli check-snapshots` fix panic after optimistic read  
  <sub>2024-06-24 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10852`](https://github.com/erigontech/erigon/pull/10852) — FillDBFromSnapshots: allow background sort  
  <sub>2024-06-22 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10850`](https://github.com/erigontech/erigon/pull/10850) — Caplin: Self-recover snapshots gap  
  <sub>2024-06-21 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10797`](https://github.com/erigontech/erigon/pull/10797) — `erigon snapshots integrity --fromStep` flag added  
  <sub>2024-06-19 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10795`](https://github.com/erigontech/erigon/pull/10795) — `erigon snapshots integrity --failFast` flag  
  <sub>2024-06-19 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10595`](https://github.com/erigontech/erigon/pull/10595) — stageLoop: keep headerDownloader in `initialCycle` mode while doing big jumps  
  <sub>2024-06-03 · merged · authored · score 2 · downloader, stage</sub>
- [`erigontech/erigon#10475`](https://github.com/erigontech/erigon/pull/10475) — Added Caplin snapshots for Gnosis Chain  
  <sub>2024-05-25 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#10161`](https://github.com/erigontech/erigon/pull/10161) — Added support for Lock for E3 snapshots  
  <sub>2024-05-01 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9983`](https://github.com/erigontech/erigon/pull/9983) — downloader torrent_create: print logs line about created amount  
  <sub>2024-04-18 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#9867`](https://github.com/erigontech/erigon/pull/9867) — downloader: calling wrong url to download .torrent  
  <sub>2024-04-05 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#9804`](https://github.com/erigontech/erigon/pull/9804) — downloader: when torrent added to lib and metadata resolved - already too late checking for whitelist. need check before adding to lib  
  <sub>2024-03-26 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#9782`](https://github.com/erigontech/erigon/pull/9782) — downloader: manual .lock remove may lead to race and creation of data files without .torrent  
  <sub>2024-03-22 · merged · authored+reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#9766`](https://github.com/erigontech/erigon/pull/9766) — Added blob sidecars snapshots for sepolia  
  <sub>2024-03-19 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9724`](https://github.com/erigontech/erigon/pull/9724) — Add torrentDownload to default downloader case  
  <sub>2024-03-15 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#9700`](https://github.com/erigontech/erigon/pull/9700) — downloader: faster `addTorrentFilesFromDisk`  
  <sub>2024-03-13 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#9663`](https://github.com/erigontech/erigon/pull/9663) — downloader: dont delete torrent files  
  <sub>2024-03-10 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#9554`](https://github.com/erigontech/erigon/pull/9554) — e35: print in debug logs if gap in snapshots detected  
  <sub>2024-03-01 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9540`](https://github.com/erigontech/erigon/pull/9540) — bor: BorStartEventID support snapshots  
  <sub>2024-02-29 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9509`](https://github.com/erigontech/erigon/pull/9509) — snaps: use hardcoded list of types - to protect borSnapshots impact on block snaps   
  <sub>2024-02-25 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9508`](https://github.com/erigontech/erigon/pull/9508) — e35: protect borSnapshots from interacting with block snaps  
  <sub>2024-02-25 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9488`](https://github.com/erigontech/erigon/pull/9488) — snapshots: fix filesByRange (#9472)  
  <sub>2024-02-22 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9372`](https://github.com/erigontech/erigon/pull/9372) — Fixed small hiccup in BeaconBlocks snapshots  
  <sub>2024-02-04 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9235`](https://github.com/erigontech/erigon/pull/9235) — e35: "erigon snapshots meta" for .bt  
  <sub>2024-01-15 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9111`](https://github.com/erigontech/erigon/pull/9111) — Updated erigon-snapshots  
  <sub>2024-01-01 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9085`](https://github.com/erigontech/erigon/pull/9085) — e35 semaphore for building snapshots  
  <sub>2023-12-26 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#9079`](https://github.com/erigontech/erigon/pull/9079) — e35: "erigon snapshots debug" add .ef files trace  
  <sub>2023-12-25 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8990`](https://github.com/erigontech/erigon/pull/8990) — snapshots: --metrics must not affect logs about peers rate  
  <sub>2023-12-15 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8987`](https://github.com/erigontech/erigon/pull/8987) — added collecting info about snapshot indexing, renamed downloading prop  
  <sub>2023-12-14 · merged · reviewed · score 2 · index, snapshot</sub>
- [`erigontech/erigon#8942`](https://github.com/erigontech/erigon/pull/8942) — e35: "erigon snapshots debug" step 2  
  <sub>2023-12-10 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8938`](https://github.com/erigontech/erigon/pull/8938) — e35: "erigon snapshots debug" command  
  <sub>2023-12-09 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8935`](https://github.com/erigontech/erigon/pull/8935) — dvovk/snapshotsstats  
  <sub>2023-12-08 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8922`](https://github.com/erigontech/erigon/pull/8922) — e35: env DOWNLOADER_ONLY_BLOCKS, STAGES_ONLY_BLOCKS  
  <sub>2023-12-07 · merged · authored · score 2 · downloader, stage</sub>
- [`erigontech/erigon#8897`](https://github.com/erigontech/erigon/pull/8897) — e35: header reader, handle absence of snapshots  
  <sub>2023-12-04 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8834`](https://github.com/erigontech/erigon/pull/8834) — "erigon snapshots diff": setup logger  
  <sub>2023-11-27 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8824`](https://github.com/erigontech/erigon/pull/8824) — add command "downloader torrent_cat"  
  <sub>2023-11-24 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#8785`](https://github.com/erigontech/erigon/pull/8785) — downloader: don't create .torrent for too small files  
  <sub>2023-11-20 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#8691`](https://github.com/erigontech/erigon/pull/8691) — e35: fix start from existing snapshots corner cases  
  <sub>2023-11-10 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8665`](https://github.com/erigontech/erigon/pull/8665) — Add full support to beacon snapshots  
  <sub>2023-11-06 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8612`](https://github.com/erigontech/erigon/pull/8612) — downloader: preparations for reducing blocks merge limit  
  <sub>2023-10-30 · merged · authored · score 2 · downloader, merge</sub>
- [`erigontech/erigon#8570`](https://github.com/erigontech/erigon/pull/8570) — Added functional beacon snapshots reader and generator to Caplin  
  <sub>2023-10-24 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8488`](https://github.com/erigontech/erigon/pull/8488) — bor initFrozenSnapshot: parallel erecover  
  <sub>2023-10-16 · merged · authored · score 2 · parallel, snapshot</sub>
- [`erigontech/erigon#8472`](https://github.com/erigontech/erigon/pull/8472) — fix sepolia snapshots hashes  
  <sub>2023-10-14 · closed · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8461`](https://github.com/erigontech/erigon/pull/8461) — mumbai snapshots - 41m  
  <sub>2023-10-13 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8436`](https://github.com/erigontech/erigon/pull/8436) — mainnet 18 snapshots  
  <sub>2023-10-11 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8358`](https://github.com/erigontech/erigon/pull/8358) — downloader: don't drop torrents after download (performance problem there solved)  
  <sub>2023-10-04 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#8326`](https://github.com/erigontech/erigon/pull/8326) — snapshots: remove concept of separated hist .toml file  
  <sub>2023-09-29 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8253`](https://github.com/erigontech/erigon/pull/8253) — torrent: allow --downloader.verify use all CPU's  
  <sub>2023-09-21 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#8182`](https://github.com/erigontech/erigon/pull/8182) — Downloader: correct logging when create .torrent files  
  <sub>2023-09-13 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#8165`](https://github.com/erigontech/erigon/pull/8165) — more sepolia snapshots  
  <sub>2023-09-09 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#8158`](https://github.com/erigontech/erigon/pull/8158) — remove small snapshots from polygons .toml  
  <sub>2023-09-08 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#7991`](https://github.com/erigontech/erigon/pull/7991) — e3: remove history snapshots  
  <sub>2023-08-10 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#7757`](https://github.com/erigontech/erigon/pull/7757) — faster opening of snapshots and indices  
  <sub>2023-06-19 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#7631`](https://github.com/erigontech/erigon/pull/7631) — sepolia new snapshots  
  <sub>2023-06-02 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#7619`](https://github.com/erigontech/erigon/pull/7619) — add "erigon snapshots diff" sub-command to find difference between 2 snapshots  
  <sub>2023-06-01 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#7584`](https://github.com/erigontech/erigon/pull/7584) — use blockReader as service-provider of RoSnapshots  
  <sub>2023-05-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#7579`](https://github.com/erigontech/erigon/pull/7579) — tests for blocks snapshots creation data producer   
  <sub>2023-05-25 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#7543`](https://github.com/erigontech/erigon/pull/7543) — move e2 snapshots management closer to e3: step 1  
  <sub>2023-05-19 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#7321`](https://github.com/erigontech/erigon/pull/7321) — e3: in-general merge must not see "overlaps/deleted" files, but merge of history need access to corresponding index files (even if they marked as deleted or already merged - before kill -9)  
  <sub>2023-04-17 · merged · authored · score 2 · index, merge</sub>
- [`erigontech/erigon#6942`](https://github.com/erigontech/erigon/pull/6942) — e3: more mainnet snapshots  
  <sub>2023-02-24 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6847`](https://github.com/erigontech/erigon/pull/6847) — Sepolia: enable blocks snapshots by default  
  <sub>2023-02-12 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6839`](https://github.com/erigontech/erigon/pull/6839) — e3: more mainnet snapshots  
  <sub>2023-02-11 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6765`](https://github.com/erigontech/erigon/pull/6765) — e3: more mergeFiles tests, refcnt for LocalityIndex  
  <sub>2023-02-02 · merged · authored · score 2 · index, merge</sub>
- [`erigontech/erigon#6623`](https://github.com/erigontech/erigon/pull/6623) — e3: more bsc snapshots  
  <sub>2023-01-19 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6596`](https://github.com/erigontech/erigon/pull/6596) — e3: new goerli snapshots  
  <sub>2023-01-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6411`](https://github.com/erigontech/erigon/pull/6411) — e3: correct bsc snapshots  
  <sub>2022-12-23 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6387`](https://github.com/erigontech/erigon/pull/6387) — e3: verified mainnet snapshots  
  <sub>2022-12-20 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6075`](https://github.com/erigontech/erigon/pull/6075) — bsc: new blocks snapshots  
  <sub>2022-11-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6070`](https://github.com/erigontech/erigon/pull/6070) — e3: more mainnet snapshots  
  <sub>2022-11-17 · closed · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6069`](https://github.com/erigontech/erigon/pull/6069) — Revert "e3: more mainnet snapshots"  
  <sub>2022-11-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#6068`](https://github.com/erigontech/erigon/pull/6068) — e3: more mainnet snapshots  
  <sub>2022-11-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5895`](https://github.com/erigontech/erigon/pull/5895) — e3: less small merges, parallel merge  
  <sub>2022-10-29 · merged · authored · score 2 · merge, parallel</sub>
- [`erigontech/erigon#5868`](https://github.com/erigontech/erigon/pull/5868) — don't stop stageLoop if error happen during background blocks snapshot creation  
  <sub>2022-10-26 · merged · authored · score 2 · snapshot, stage</sub>
- [`erigontech/erigon#5867`](https://github.com/erigontech/erigon/pull/5867) — e3: more mainnet snapshots  
  <sub>2022-10-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5858`](https://github.com/erigontech/erigon/pull/5858) — e3: goerli snapshots  
  <sub>2022-10-25 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5842`](https://github.com/erigontech/erigon/pull/5842) — snapshots: new blocks snapshot for mainnet  
  <sub>2022-10-23 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5829`](https://github.com/erigontech/erigon/pull/5829) — e3: remove some mainnet snapshots  
  <sub>2022-10-22 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5806`](https://github.com/erigontech/erigon/pull/5806) — e3: more snapshots   
  <sub>2022-10-20 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5726`](https://github.com/erigontech/erigon/pull/5726) — e3: history mainnet,bsc snapshots  
  <sub>2022-10-13 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5725`](https://github.com/erigontech/erigon/pull/5725) — e3: history bsc and mainnet snapshots  
  <sub>2022-10-13 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5714`](https://github.com/erigontech/erigon/pull/5714) — goerli snapshots: blocks and history  
  <sub>2022-10-12 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5681`](https://github.com/erigontech/erigon/pull/5681) — new bsc blocks snapshots  
  <sub>2022-10-10 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5594`](https://github.com/erigontech/erigon/pull/5594) — remote rpcdaemon to create snapshots/history dir at startup  
  <sub>2022-10-02 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5588`](https://github.com/erigontech/erigon/pull/5588) — erigon3: step toward background snapshots build  
  <sub>2022-10-01 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5524`](https://github.com/erigontech/erigon/pull/5524) — snapshot index workers amount - based on available RAM and CPU  
  <sub>2022-09-26 · merged · authored+reviewed · score 2 · index, snapshot</sub>
- [`erigontech/erigon#5449`](https://github.com/erigontech/erigon/pull/5449) — "erigon snapshots ram" command  
  <sub>2022-09-21 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5369`](https://github.com/erigontech/erigon/pull/5369) — bor/consensus: Only write Snapshots to DB for checkpoints  
  <sub>2022-09-15 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5351`](https://github.com/erigontech/erigon/pull/5351) — erigon22: folder snapshots/history   
  <sub>2022-09-13 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5348`](https://github.com/erigontech/erigon/pull/5348) — erigon22: snapshots/history dir instead of agg22  
  <sub>2022-09-13 · closed · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5338`](https://github.com/erigontech/erigon/pull/5338) — erigon22: to use datadir/snapshots, instead of datadir/agg22  
  <sub>2022-09-12 · closed · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#5290`](https://github.com/erigontech/erigon/pull/5290) — moved retiring of blocks from senders into snapshot stage  
  <sub>2022-09-06 · merged · reviewed · score 2 · snapshot, stage</sub>
- [`erigontech/erigon#5043`](https://github.com/erigontech/erigon/pull/5043) — rpcdaemon: start without panic when --snapshots=false  
  <sub>2022-08-13 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4829`](https://github.com/erigontech/erigon/pull/4829) — kv.Snapshots() server implementation  
  <sub>2022-07-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4825`](https://github.com/erigontech/erigon/pull/4825) — kv.Snapshots() grpc method  
  <sub>2022-07-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4786`](https://github.com/erigontech/erigon/pull/4786) — snapshot merger: smaller interface  
  <sub>2022-07-22 · merged · authored · score 2 · merge, snapshot</sub>
- [`erigontech/erigon#4777`](https://github.com/erigontech/erigon/pull/4777) — save list of snapshots in db  
  <sub>2022-07-21 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4748`](https://github.com/erigontech/erigon/pull/4748) — Add --snapdir to specify independent snapshots folder for some commands  
  <sub>2022-07-19 · closed · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4733`](https://github.com/erigontech/erigon/pull/4733) — snapshots: mainnet to 15m  
  <sub>2022-07-18 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4729`](https://github.com/erigontech/erigon/pull/4729) — Auto download snapshots  
  <sub>2022-07-17 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4625`](https://github.com/erigontech/erigon/pull/4625) — Snapshots: save initial list to db, to avoid future snapshots downloading   
  <sub>2022-07-04 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4624`](https://github.com/erigontech/erigon/pull/4624) — snapshots table  
  <sub>2022-07-04 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4578`](https://github.com/erigontech/erigon/pull/4578) — Snapshots: new bsc hash  
  <sub>2022-06-29 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4558`](https://github.com/erigontech/erigon/pull/4558) — Snapshots: don't panic after too far reset  
  <sub>2022-06-28 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4556`](https://github.com/erigontech/erigon/pull/4556) — eth_estimateGas to use snapshots and blocksLRU  
  <sub>2022-06-28 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4404`](https://github.com/erigontech/erigon/pull/4404) — reset blocks migration: to delete .torrent files also  
  <sub>2022-06-08 · merged · authored · score 2 · migration, torrent</sub>
- [`erigontech/erigon#4393`](https://github.com/erigontech/erigon/pull/4393) — Snapshots: optimisticaly open at app startup  
  <sub>2022-06-07 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4392`](https://github.com/erigontech/erigon/pull/4392) — don't open snapshots at startup  
  <sub>2022-06-07 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4386`](https://github.com/erigontech/erigon/pull/4386) — downloader torrent_hashes --verify: 1 error line per file  
  <sub>2022-06-07 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#4350`](https://github.com/erigontech/erigon/pull/4350) — Snapshots: more runtime invariants check   
  <sub>2022-06-03 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4283`](https://github.com/erigontech/erigon/pull/4283) — Torrent: verify is more informative  
  <sub>2022-05-27 · merged · authored · score 2 · format, torrent</sub>
- [`erigontech/erigon#4245`](https://github.com/erigontech/erigon/pull/4245) — SnapshotIndex: Add more context to panic  
  <sub>2022-05-24 · merged · authored · score 2 · index, snapshot</sub>
- [`erigontech/erigon#4216`](https://github.com/erigontech/erigon/pull/4216) — It's safe now to open snapshots at app start  
  <sub>2022-05-20 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4178`](https://github.com/erigontech/erigon/pull/4178) — HeadersPOS: to use snapshots  
  <sub>2022-05-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4135`](https://github.com/erigontech/erigon/pull/4135) — it's ok to not have snapshots dir  
  <sub>2022-05-12 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4098`](https://github.com/erigontech/erigon/pull/4098) — Snapshots: restore logInterval   
  <sub>2022-05-07 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#4063`](https://github.com/erigontech/erigon/pull/4063) — RPCDaemon - open snapshots only when they are ready (and indices ready).  
  <sub>2022-05-04 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3986`](https://github.com/erigontech/erigon/pull/3986) — Downloader: calc stat inside, add --torrent.download.slots and limit downloads inside  
  <sub>2022-04-27 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#3958`](https://github.com/erigontech/erigon/pull/3958) — Snapshots: rare nil pointer at fresh start  
  <sub>2022-04-25 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3957`](https://github.com/erigontech/erigon/pull/3957) — Snapshots: support empty buf case  
  <sub>2022-04-25 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3909`](https://github.com/erigontech/erigon/pull/3909) — Snapshots: use kv.ReadAhead helper  
  <sub>2022-04-18 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3906`](https://github.com/erigontech/erigon/pull/3906) — integration: check that snapshots are nil  
  <sub>2022-04-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3905`](https://github.com/erigontech/erigon/pull/3905) — integration: senders check that snapshots are not nil  
  <sub>2022-04-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3885`](https://github.com/erigontech/erigon/pull/3885) — Snapshots: notify before remove  
  <sub>2022-04-14 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3857`](https://github.com/erigontech/erigon/pull/3857) — wait for snapshots not only for POW  
  <sub>2022-04-09 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3834`](https://github.com/erigontech/erigon/pull/3834) — Snapshots: nat support  
  <sub>2022-04-06 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3833`](https://github.com/erigontech/erigon/pull/3833) — Snapshots: open rwdir once  
  <sub>2022-04-05 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3784`](https://github.com/erigontech/erigon/pull/3784) — Snapshots: write hashes to file only if amount of them growth  
  <sub>2022-03-28 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3772`](https://github.com/erigontech/erigon/pull/3772) — Snapshots: nil indices on p2p fix  
  <sub>2022-03-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3762`](https://github.com/erigontech/erigon/pull/3762) — Snapshots: handle well gaps in idx files  
  <sub>2022-03-24 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3760`](https://github.com/erigontech/erigon/pull/3760) — Snapshots: remove "experimental" prefix from cli flag  
  <sub>2022-03-24 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3755`](https://github.com/erigontech/erigon/pull/3755) — Snapshots: notify rpcdaemon about new snapshot  
  <sub>2022-03-23 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3749`](https://github.com/erigontech/erigon/pull/3749) — Snapshots: better support of p2p  
  <sub>2022-03-21 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3744`](https://github.com/erigontech/erigon/pull/3744) — Snapshots: fix partial .idx detection   
  <sub>2022-03-21 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3732`](https://github.com/erigontech/erigon/pull/3732) — Snapshots: grpc event   
  <sub>2022-03-18 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3723`](https://github.com/erigontech/erigon/pull/3723) — Integration: fix nil snapshots case  
  <sub>2022-03-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3683`](https://github.com/erigontech/erigon/pull/3683) — snapshots: enum file types  
  <sub>2022-03-12 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3670`](https://github.com/erigontech/erigon/pull/3670) — open snapshots in embedded rpcdaemon  
  <sub>2022-03-10 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3623`](https://github.com/erigontech/erigon/pull/3623) — snapshots: speedup slow test  
  <sub>2022-02-25 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3611`](https://github.com/erigontech/erigon/pull/3611) — snapshots: better logging  
  <sub>2022-02-24 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3602`](https://github.com/erigontech/erigon/pull/3602) — snapshots: ensure tmpdir exists  
  <sub>2022-02-24 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3583`](https://github.com/erigontech/erigon/pull/3583) — Snapshots: more filename fixes  
  <sub>2022-02-23 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3582`](https://github.com/erigontech/erigon/pull/3582) — snapshots: better files sort and filter  
  <sub>2022-02-23 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3439`](https://github.com/erigontech/erigon/pull/3439) — Snapshots: Add verify command, fix mainnet hashes  
  <sub>2022-02-07 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3382`](https://github.com/erigontech/erigon/pull/3382) — snapshots: bsc  
  <sub>2022-01-31 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3356`](https://github.com/erigontech/erigon/pull/3356) — Snapshots: use default config   
  <sub>2022-01-27 · closed · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3328`](https://github.com/erigontech/erigon/pull/3328) — Snapshots: fill kv.HeaderNumber table  
  <sub>2022-01-23 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3296`](https://github.com/erigontech/erigon/pull/3296) — Snapshots: prepare to re-use some funcs  
  <sub>2022-01-19 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3264`](https://github.com/erigontech/erigon/pull/3264) — Snapshots: files list  
  <sub>2022-01-15 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3224`](https://github.com/erigontech/erigon/pull/3224) — Snapshots: fix pprof cli flags support in sub-commands  
  <sub>2022-01-09 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3222`](https://github.com/erigontech/erigon/pull/3222) — Snapshots: create .dat in tmpdir   
  <sub>2022-01-09 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3221`](https://github.com/erigontech/erigon/pull/3221) — Snapshot: indexing to print logs with clear progress  
  <sub>2022-01-09 · merged · authored · score 2 · index, snapshot</sub>
- [`erigontech/erigon#3194`](https://github.com/erigontech/erigon/pull/3194) — Snapshots: add --to parameter to "erigon snapshots create"  
  <sub>2022-01-03 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3191`](https://github.com/erigontech/erigon/pull/3191) — Snapshot: describe idx schema  
  <sub>2021-12-31 · merged · authored · score 2 · schema, snapshot</sub>
- [`erigontech/erigon#3150`](https://github.com/erigontech/erigon/pull/3150) — Snapshots hashes for mainnet   
  <sub>2021-12-21 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#3117`](https://github.com/erigontech/erigon/pull/3117) — Snapshots download and seed  
  <sub>2021-12-13 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#2999`](https://github.com/erigontech/erigon/pull/2999) — Snapshot: common indexing func  
  <sub>2021-11-21 · merged · authored · score 2 · index, snapshot</sub>
- [`erigontech/erigon#2996`](https://github.com/erigontech/erigon/pull/2996) — snapshots: read block from snapshots, add sender to txs file   
  <sub>2021-11-20 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#2957`](https://github.com/erigontech/erigon/pull/2957) — Open blocks snapshots  
  <sub>2021-11-14 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon#2929`](https://github.com/erigontech/erigon/pull/2929) — Small step towards torrent downloader  
  <sub>2021-11-08 · merged · authored · score 2 · downloader, torrent</sub>
- [`erigontech/erigon#2908`](https://github.com/erigontech/erigon/pull/2908) — Remove --snapshot.layout flag  
  <sub>2021-11-03 · merged · authored · score 2 · layout, snapshot</sub>
- [`erigontech/erigon#1788`](https://github.com/erigontech/erigon/pull/1788) — Add stage exec to downloader  
  <sub>2021-04-23 · merged · authored · score 2 · downloader, stage</sub>
- [`erigontech/erigon#1787`](https://github.com/erigontech/erigon/pull/1787) — Use Config struct for headers/body/senders stages. Add StageSenders to new downloader.   
  <sub>2021-04-23 · merged · authored · score 2 · downloader, stage</sub>
- [`erigontech/erigon#1749`](https://github.com/erigontech/erigon/pull/1749) — add --datadir parameter to integration, snapshot generator, header downloader  
  <sub>2021-04-19 · merged · authored · score 2 · downloader, snapshot</sub>
- [`erigontech/erigon-qa#226`](https://github.com/erigontech/erigon-qa/pull/226) — Extract and update downloader torrent client status endpoint path  
  <sub>2025-07-28 · merged · reviewed · score 2 · downloader, torrent</sub>
- [`erigontech/erigon-snapshot#795`](https://github.com/erigontech/erigon-snapshot/pull/795) — Introduce arbitrum snapshots  
  <sub>2025-07-31 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#469`](https://github.com/erigontech/erigon-snapshot/pull/469) — Pass branch explicitly to LoadSnapshots  
  <sub>2025-03-17 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#168`](https://github.com/erigontech/erigon-snapshot/pull/168) — Added Gnosis snapshots to Caplin  
  <sub>2024-05-25 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#114`](https://github.com/erigontech/erigon-snapshot/pull/114) — Updated beacon snapshots for sepolia/mainnet  
  <sub>2024-01-30 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#95`](https://github.com/erigontech/erigon-snapshot/pull/95) — Introduce new public buckets for the snapshots  
  <sub>2023-12-28 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#36`](https://github.com/erigontech/erigon-snapshot/pull/36) — remove history snapshots  
  <sub>2023-08-10 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#31`](https://github.com/erigontech/erigon-snapshot/pull/31) — new sepolia snapshots  
  <sub>2023-06-02 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#25`](https://github.com/erigontech/erigon-snapshot/pull/25) — e3: more mainnet snapshots  
  <sub>2023-02-22 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#23`](https://github.com/erigontech/erigon-snapshot/pull/23) — e3: more mainnet snapshots  
  <sub>2023-02-11 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#19`](https://github.com/erigontech/erigon-snapshot/pull/19) — e3: more mainnet snapshots  
  <sub>2023-01-19 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#17`](https://github.com/erigontech/erigon-snapshot/pull/17) — e3: new goerli snapshots  
  <sub>2023-01-17 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#16`](https://github.com/erigontech/erigon-snapshot/pull/16) — e3: new snapshots  
  <sub>2023-01-12 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshot#5`](https://github.com/erigontech/erigon-snapshot/pull/5) — Snapshots: bsc   
  <sub>2022-06-29 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshots-automation#45`](https://github.com/erigontech/erigon-snapshots-automation/pull/45) — snapshots_automation: drop arb-sepolia / Arbitrum support  
  <sub>2026-05-26 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/erigon-snapshots-automation#36`](https://github.com/erigontech/erigon-snapshots-automation/pull/36) — Increase timeout for snapshots_release workflow to 1 day  
  <sub>2026-03-18 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`erigontech/interfaces#158`](https://github.com/erigontech/interfaces/pull/158) — e3 snapshots   
  <sub>2023-02-10 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/interfaces#120`](https://github.com/erigontech/interfaces/pull/120) — kv.Snapshots() method  
  <sub>2022-07-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/interfaces#119`](https://github.com/erigontech/interfaces/pull/119) — kv.Snapshots() method  
  <sub>2022-07-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`erigontech/scripts#21`](https://github.com/erigontech/scripts/pull/21) — [snapshots automation] Separation of touches to increase performance  
  <sub>2025-09-05 · merged · reviewed · score 2 · snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#1123`](https://github.com/ledgerwatch/erigon-lib/pull/1123) — Downloader: correct logging when create .torrent files  
  <sub>2023-09-13 · merged · authored · score 2 · downloader, torrent</sub>
- [`ledgerwatch/erigon-lib#1025`](https://github.com/ledgerwatch/erigon-lib/pull/1025) — faster opening of snapshots and indices  
  <sub>2023-06-19 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#972`](https://github.com/ledgerwatch/erigon-lib/pull/972) — e3: in-general merge must not see "overlaps/deleted" files, but merge of history need access to corresponding index files (even if they marked as deleted or already merged - before `kill -9`)   
  <sub>2023-04-17 · merged · authored · score 2 · index, merge</sub>
- [`ledgerwatch/erigon-lib#878`](https://github.com/ledgerwatch/erigon-lib/pull/878) — e3: more mergeFiles tests, refcnt for LocalityIndex  
  <sub>2023-02-02 · merged · authored · score 2 · index, merge</sub>
- [`ledgerwatch/erigon-lib#710`](https://github.com/ledgerwatch/erigon-lib/pull/710) — e3: less small merges, parallel merge  
  <sub>2022-10-29 · merged · authored · score 2 · merge, parallel</sub>
- [`ledgerwatch/erigon-lib#663`](https://github.com/ledgerwatch/erigon-lib/pull/663) — erigon3: step toward background snapshots build  
  <sub>2022-10-01 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#551`](https://github.com/ledgerwatch/erigon-lib/pull/551) — kv.Snapshots() implementation  
  <sub>2022-07-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#549`](https://github.com/ledgerwatch/erigon-lib/pull/549) — kv.Snapshots() grpc method  
  <sub>2022-07-26 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#510`](https://github.com/ledgerwatch/erigon-lib/pull/510) — Snapshots table  
  <sub>2022-07-04 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#432`](https://github.com/ledgerwatch/erigon-lib/pull/432) — Downloader: calc stat inside, add --torrent.download.slots and limit downloads inside  
  <sub>2022-04-27 · merged · authored · score 2 · downloader, torrent</sub>
- [`ledgerwatch/erigon-lib#346`](https://github.com/ledgerwatch/erigon-lib/pull/346) — snapshots: ensure tmpdir exists  
  <sub>2022-02-24 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#233`](https://github.com/ledgerwatch/erigon-lib/pull/233) — snapshots: same workers amount  
  <sub>2022-01-15 · merged · authored · score 2 · snapshot, snapshots</sub>
- [`ledgerwatch/erigon-lib#225`](https://github.com/ledgerwatch/erigon-lib/pull/225) — Snapshots: create .dat in tmpdir   
  <sub>2022-01-09 · merged · authored · score 2 · snapshot, snapshots</sub>

## Indexing & perfect hashing  (144)

- [`erigontech/erigon#20567`](https://github.com/erigontech/erigon/pull/20567) — btindex: WarmUp: read key-only, skip value to avoid unnecessary decompression  
  <sub>2026-04-15 · merged · authored · score 10 · compress, compression, decompress, index</sub>
- [`erigontech/erigon#21871`](https://github.com/erigontech/erigon/pull/21871) — db/recsplit: use SmallSortableBuffers for bucket collector ETL (#21830)  
  <sub>2026-06-18 · merged · authored · score 7 · collector, etl , recsplit</sub>
- [`erigontech/erigon#21830`](https://github.com/erigontech/erigon/pull/21830) — db/recsplit: use SmallSortableBuffers for bucket collector ETL  
  <sub>2026-06-16 · merged · authored · score 7 · collector, etl , recsplit</sub>
- [`erigontech/erigon#21877`](https://github.com/erigontech/erigon/pull/21877) — db/recsplit/eliasfano16, db/recsplit/eliasfano32: don't mutate fuzzer input  
  <sub>2026-06-18 · merged · reviewed · score 6 · eliasfano, recsplit</sub>
- [`erigontech/erigon#20640`](https://github.com/erigontech/erigon/pull/20640) — recsplit: off-heap EliasFano build  
  <sub>2026-04-18 · merged · authored · score 6 · eliasfano, recsplit</sub>
- [`erigontech/erigon#20566`](https://github.com/erigontech/erigon/pull/20566) — db/recsplit/eliasfano32: fix searchUpperReverse off-by-one on no-solution fast path  
  <sub>2026-04-15 · merged · authored · score 6 · eliasfano, recsplit</sub>
- [`erigontech/erigon#20323`](https://github.com/erigontech/erigon/pull/20323) — recsplit: use same etl pool with other system  
  <sub>2026-04-04 · merged · authored · score 6 · etl , recsplit</sub>
- [`erigontech/erigon#19924`](https://github.com/erigontech/erigon/pull/19924) — recsplit: use same etl pool with other system  
  <sub>2026-03-16 · merged · authored · score 6 · etl , recsplit</sub>
- [`erigontech/erigon#19196`](https://github.com/erigontech/erigon/pull/19196) — compressor and recsplit: native timings support  
  <sub>2026-02-15 · merged · authored · score 6 · compress, recsplit</sub>
- [`erigontech/erigon#19195`](https://github.com/erigontech/erigon/pull/19195) — [wip] compressor and recsplit: global workers limit  
  <sub>2026-02-15 · merged · authored · score 6 · compress, recsplit</sub>
- [`erigontech/erigon#16282`](https://github.com/erigontech/erigon/pull/16282) — [r32] recsplit: backward compatibility   
  <sub>2025-07-25 · merged · authored · score 6 · backward compat, recsplit</sub>
- [`erigontech/erigon#16281`](https://github.com/erigontech/erigon/pull/16281) — [r3.1] recsplit: backward compatibility fix  
  <sub>2025-07-25 · merged · authored · score 6 · backward compat, recsplit</sub>
- [`erigontech/erigon#16280`](https://github.com/erigontech/erigon/pull/16280) — recsplit: backward compatible fix  
  <sub>2025-07-25 · closed · authored · score 6 · backward compat, recsplit</sub>
- [`erigontech/erigon#15986`](https://github.com/erigontech/erigon/pull/15986) — recsplit: fix smal idx backward compatibility  
  <sub>2025-07-08 · merged · authored · score 6 · backward compat, recsplit</sub>
- [`erigontech/erigon#15960`](https://github.com/erigontech/erigon/pull/15960) — recsplit: internal existence filter based on `fuse_filter`. only `.efi` and `.kvi` files  
  <sub>2025-07-07 · merged · authored+reviewed · score 6 · .efi, recsplit</sub>
- [`ledgerwatch/erigon-lib#474`](https://github.com/ledgerwatch/erigon-lib/pull/474) — recsplit: configurable etl limit  
  <sub>2022-05-30 · merged · authored · score 6 · etl , recsplit</sub>
- [`ledgerwatch/erigon-lib#307`](https://github.com/ledgerwatch/erigon-lib/pull/307) — Less alloc etl recsplit  
  <sub>2022-02-09 · merged · authored · score 6 · etl , recsplit</sub>
- [`erigontech/erigon#21619`](https://github.com/erigontech/erigon/pull/21619) — db/recsplit: speed up index lookups  
  <sub>2026-06-04 · open · reviewed · score 5 · index, lookup, recsplit</sub>
- [`erigontech/erigon#17486`](https://github.com/erigontech/erigon/pull/17486) — Improved BTree index benchmark tests and added new ones  
  <sub>2025-10-15 · merged · reviewed · score 5 · btree, btree index, index</sub>
- [`erigontech/erigon#10276`](https://github.com/erigontech/erigon/pull/10276) — fix inverted index pruning  
  <sub>2024-05-10 · merged · reviewed · score 5 · index, inverted index, pruning</sub>
- [`erigontech/erigon#21800`](https://github.com/erigontech/erigon/pull/21800) — btindex: use off-heap EliasFano during build  
  <sub>2026-06-14 · closed · authored · score 4 · eliasfano, index</sub>
- [`erigontech/erigon#21777`](https://github.com/erigontech/erigon/pull/21777) — btindex: use off-heap EliasFano during build  
  <sub>2026-06-13 · merged · authored · score 4 · eliasfano, index</sub>
- [`erigontech/erigon#19538`](https://github.com/erigontech/erigon/pull/19538) — recsplit: parallel  
  <sub>2026-03-01 · merged · authored · score 4 · parallel, recsplit</sub>
- [`erigontech/erigon#19515`](https://github.com/erigontech/erigon/pull/19515) — [wip] recsplit: parallelism  
  <sub>2026-02-27 · closed · authored · score 4 · parallel, recsplit</sub>
- [`erigontech/erigon#19514`](https://github.com/erigontech/erigon/pull/19514) — recsplit: prepare for parallelism  
  <sub>2026-02-27 · merged · authored · score 4 · parallel, recsplit</sub>
- [`erigontech/erigon#17587`](https://github.com/erigontech/erigon/pull/17587) — roaring bitmap version up  
  <sub>2025-10-22 · merged · authored · score 4 · bitmap, roaring</sub>
- [`erigontech/erigon#11530`](https://github.com/erigontech/erigon/pull/11530) — inverted index: lru  
  <sub>2024-08-08 · merged · authored · score 4 · index, inverted index</sub>
- [`erigontech/erigon#10402`](https://github.com/erigontech/erigon/pull/10402) — Refactor inverted indexes instances  
  <sub>2024-05-18 · merged · reviewed · score 4 · index, inverted index</sub>
- [`erigontech/erigon#10292`](https://github.com/erigontech/erigon/pull/10292) — buildIndex: reset buf on recsplit collision  
  <sub>2024-05-13 · merged · authored · score 4 · index, recsplit</sub>
- [`erigontech/erigon#10146`](https://github.com/erigontech/erigon/pull/10146) — e3 etl on index collation  
  <sub>2024-04-30 · merged · reviewed · score 4 · etl , index</sub>
- [`erigontech/erigon#8238`](https://github.com/erigontech/erigon/pull/8238) — Add util to test native recsplit index creation  
  <sub>2023-09-19 · merged · reviewed · score 4 · index, recsplit</sub>
- [`erigontech/erigon#2895`](https://github.com/erigontech/erigon/pull/2895) — Recsplit: add hack recsplitLookup for test  
  <sub>2021-10-31 · merged · authored · score 4 · lookup, recsplit</sub>
- [`erigontech/erigon#2606`](https://github.com/erigontech/erigon/pull/2606) — Roaring bitmap lib version up  
  <sub>2021-09-01 · merged · authored · score 4 · bitmap, roaring</sub>
- [`erigontech/erigon#2413`](https://github.com/erigontech/erigon/pull/2413) — add stop point of tx_lookup unwind  
  <sub>2021-07-21 · merged · authored · score 4 · lookup, unwind</sub>
- [`erigontech/erigon#2399`](https://github.com/erigontech/erigon/pull/2399) — Pruning for: exec, log_index, tx_lookup, history stages  
  <sub>2021-07-19 · merged · authored · score 4 · index, lookup, pruning, stage</sub>
- [`erigontech/erigon#1227`](https://github.com/erigontech/erigon/pull/1227) — Bitmap etl  
  <sub>2020-10-12 · merged · authored · score 4 · bitmap, etl </sub>
- [`erigontech/erigon#1165`](https://github.com/erigontech/erigon/pull/1165) — switch to go implementation of roaring bitmaps for alpine support  
  <sub>2020-10-01 · merged · authored · score 4 · bitmap, roaring</sub>
- [`ledgerwatch/erigon-lib#50`](https://github.com/ledgerwatch/erigon-lib/pull/50) — Roaring bitmap lib version up   
  <sub>2021-09-01 · merged · authored · score 4 · bitmap, roaring</sub>
- [`erigontech/erigon#21797`](https://github.com/erigontech/erigon/pull/21797) — [bloatnet] recsplit: enable sharded ShardedFuse by default  
  <sub>2026-06-14 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#21796`](https://github.com/erigontech/erigon/pull/21796) — [r3.5] db/recsplit: enable sharded FuseFilter by default  
  <sub>2026-06-14 · closed · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#21793`](https://github.com/erigontech/erigon/pull/21793) — [3.6] recsplit: enable ShardedFuse by default  
  <sub>2026-06-13 · merged · reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#21385`](https://github.com/erigontech/erigon/pull/21385) — eliasfano32: Seek returns position alongside value  
  <sub>2026-05-24 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#21164`](https://github.com/erigontech/erigon/pull/21164) — db/recsplit: set ExistenceFilterVersion to 1  
  <sub>2026-05-13 · merged · reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#21144`](https://github.com/erigontech/erigon/pull/21144) — recsplit: sharded FuseFilter (cherry-pick #20644)  
  <sub>2026-05-12 · merged · reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#20644`](https://github.com/erigontech/erigon/pull/20644) — recsplit: sharded FuseFilter  
  <sub>2026-04-18 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#19788`](https://github.com/erigontech/erigon/pull/19788) — db: EliasFano: Seek perf on big sequences  
  <sub>2026-03-11 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#19773`](https://github.com/erigontech/erigon/pull/19773) — recsplit: keyPos reset on retry  
  <sub>2026-03-10 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#19582`](https://github.com/erigontech/erigon/pull/19582) — EliasFano: setBits simplify  
  <sub>2026-03-03 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#19556`](https://github.com/erigontech/erigon/pull/19556) — EliasFano.Build: less iterations in upperBits loop  
  <sub>2026-03-02 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#19555`](https://github.com/erigontech/erigon/pull/19555) — EliasFano: Build() optimize  
  <sub>2026-03-02 · closed · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#19536`](https://github.com/erigontech/erigon/pull/19536) — recsplit: support progress reporting  
  <sub>2026-03-01 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#19535`](https://github.com/erigontech/erigon/pull/19535) — recsplit: use `uint32` for bucketIdx - to reduce amount of intermediate data  
  <sub>2026-02-28 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#19194`](https://github.com/erigontech/erigon/pull/19194) — recsplit: speedup `findBijection`  
  <sub>2026-02-15 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#19043`](https://github.com/erigontech/erigon/pull/19043) — recsplit: optimize `findSplit` and `findBijection`  
  <sub>2026-02-09 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#19041`](https://github.com/erigontech/erigon/pull/19041) — recsplit: basic benches and extract hot parts to funcs (for future optimizations)  
  <sub>2026-02-09 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#19040`](https://github.com/erigontech/erigon/pull/19040) — recsplit: don't use `etl` for offsets because they are already sorted  
  <sub>2026-02-09 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#19039`](https://github.com/erigontech/erigon/pull/19039) — recsplit: Build allocs reduce  
  <sub>2026-02-09 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#16864`](https://github.com/erigontech/erigon/pull/16864) — recsplit inner version 1 incompatible fix (cp from 3.1)  
  <sub>2025-08-27 · merged · reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#16543`](https://github.com/erigontech/erigon/pull/16543) — recsplit inner version 1 incompatible fix  
  <sub>2025-08-11 · merged · reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#16511`](https://github.com/erigontech/erigon/pull/16511) — dir improvements: move `recsplit` & `etl` from `erigon-lib` to `db`  
  <sub>2025-08-08 · merged · reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#15959`](https://github.com/erigontech/erigon/pull/15959) — recsplit: add version inside file header  
  <sub>2025-07-06 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#15071`](https://github.com/erigontech/erigon/pull/15071) — fill in recsplit.close() at different places  
  <sub>2025-05-15 · merged · reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#14726`](https://github.com/erigontech/erigon/pull/14726) — build .vi: fix cnt in logs  
  <sub>2025-04-24 · merged · authored · score 3 · .vi</sub>
- [`erigontech/erigon#14682`](https://github.com/erigontech/erigon/pull/14682) — history: dedup code of build `.vi` file  
  <sub>2025-04-21 · merged · authored · score 3 · .vi</sub>
- [`erigontech/erigon#14625`](https://github.com/erigontech/erigon/pull/14625) — historical re-exec: re-used EliasFano object  
  <sub>2025-04-16 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#13272`](https://github.com/erigontech/erigon/pull/13272) — recsplit: change default BucketSize  
  <sub>2024-12-30 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#12970`](https://github.com/erigontech/erigon/pull/12970) — recsplit: compact Enum=true representation  
  <sub>2024-12-03 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#12836`](https://github.com/erigontech/erigon/pull/12836) — Design decision of `.efi` `Enum=true and LessFalsePositives=true`  
  <sub>2024-11-22 · merged · authored · score 3 · .efi</sub>
- [`erigontech/erigon#12817`](https://github.com/erigontech/erigon/pull/12817) — [wip] experiment: .efi no enum  
  <sub>2024-11-21 · closed · authored · score 3 · .efi</sub>
- [`erigontech/erigon#12520`](https://github.com/erigontech/erigon/pull/12520) — Fix panic: runtime error: negative shift amount on eliasfano reverse iterator seek  
  <sub>2024-10-28 · merged · reviewed · score 3 · eliasfano</sub>
- [`erigontech/erigon#10395`](https://github.com/erigontech/erigon/pull/10395) — eliasfano32: optimise reverse iterator  
  <sub>2024-05-17 · merged · reviewed · score 3 · eliasfano</sub>
- [`erigontech/erigon#9913`](https://github.com/erigontech/erigon/pull/9913) — Add kv.log pruning alongside logIndex prune  
  <sub>2024-04-11 · merged · reviewed · score 3 · index, prune, pruning</sub>
- [`erigontech/erigon#9515`](https://github.com/erigontech/erigon/pull/9515) — e35: recsplit: less false positives  
  <sub>2024-02-26 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#9514`](https://github.com/erigontech/erigon/pull/9514) — e35: recsplit: allow empty enum  
  <sub>2024-02-26 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#9513`](https://github.com/erigontech/erigon/pull/9513) — recsplit: allow empty enum  
  <sub>2024-02-26 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#9501`](https://github.com/erigontech/erigon/pull/9501) — recsplit: support feature flags   
  <sub>2024-02-23 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#9218`](https://github.com/erigontech/erigon/pull/9218) — recsplit: reduce ram pressure  
  <sub>2024-01-12 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#7994`](https://github.com/erigontech/erigon/pull/7994) — Recsplit: cancelable build  
  <sub>2023-08-11 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#6944`](https://github.com/erigontech/erigon/pull/6944) — e3: eliasfano iterator.seek()  
  <sub>2023-02-24 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#6904`](https://github.com/erigontech/erigon/pull/6904) — EliasFano: Search to touch only UpperBits array  
  <sub>2023-02-20 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#5831`](https://github.com/erigontech/erigon/pull/5831) — eliasfano: To fix checkptr fatal error   
  <sub>2022-10-22 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#5603`](https://github.com/erigontech/erigon/pull/5603) — eliasfano32.Max() method on serialized bytes   
  <sub>2022-10-03 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#5568`](https://github.com/erigontech/erigon/pull/5568) — erigon3: build .vi after download  
  <sub>2022-09-29 · merged · authored · score 3 · .vi</sub>
- [`erigontech/erigon#5523`](https://github.com/erigontech/erigon/pull/5523) — erigon3: build .efi after download #654  
  <sub>2022-09-26 · merged · authored · score 3 · .efi</sub>
- [`erigontech/erigon#4492`](https://github.com/erigontech/erigon/pull/4492) — Roaring version up  
  <sub>2022-06-19 · merged · authored · score 3 · roaring</sub>
- [`erigontech/erigon#4427`](https://github.com/erigontech/erigon/pull/4427) — roaring: up version   
  <sub>2022-06-10 · merged · authored · score 3 · roaring</sub>
- [`erigontech/erigon#2993`](https://github.com/erigontech/erigon/pull/2993) — Recsplit: move files read/write helpers to erigon-lib  
  <sub>2021-11-19 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#2928`](https://github.com/erigontech/erigon/pull/2928) — recsplit: single offset bucket  
  <sub>2021-11-08 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#2926`](https://github.com/erigontech/erigon/pull/2926) — Recsplit: preserve immutability threshold  
  <sub>2021-11-07 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#2925`](https://github.com/erigontech/erigon/pull/2925) — Recsplit: collision typed error  
  <sub>2021-11-07 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#2912`](https://github.com/erigontech/erigon/pull/2912) — EliasFano: fix jump calculation, fuzzing to trigger jump logic  
  <sub>2021-11-04 · merged · authored · score 3 · eliasfano</sub>
- [`erigontech/erigon#2897`](https://github.com/erigontech/erigon/pull/2897) — Recsplit: call ef.Build and set ef.prevOffset   
  <sub>2021-11-01 · merged · authored · score 3 · recsplit</sub>
- [`erigontech/erigon#2867`](https://github.com/erigontech/erigon/pull/2867) — recsplit: bigger bufio buffers  
  <sub>2021-10-25 · merged · authored+reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#2848`](https://github.com/erigontech/erigon/pull/2848) — [wip] To use roaring IsEmpty method  
  <sub>2021-10-20 · closed · authored · score 3 · roaring</sub>
- [`erigontech/erigon#1865`](https://github.com/erigontech/erigon/pull/1865) — switch to roaring release version  
  <sub>2021-05-03 · merged · authored · score 3 · roaring</sub>
- [`ledgerwatch/erigon-lib#1073`](https://github.com/ledgerwatch/erigon-lib/pull/1073) — Recsplit: cancelable build  
  <sub>2023-08-11 · merged · authored · score 3 · recsplit</sub>
- [`ledgerwatch/erigon-lib#905`](https://github.com/ledgerwatch/erigon-lib/pull/905) — eliasfano better seek  
  <sub>2023-02-24 · merged · authored · score 3 · eliasfano</sub>
- [`ledgerwatch/erigon-lib#904`](https://github.com/ledgerwatch/erigon-lib/pull/904) — eliasfano iterator.Seek()  
  <sub>2023-02-24 · merged · authored · score 3 · eliasfano</sub>
- [`ledgerwatch/erigon-lib#895`](https://github.com/ledgerwatch/erigon-lib/pull/895) — EliasFano: Search to touch only UpperBits array  
  <sub>2023-02-20 · merged · authored · score 3 · eliasfano</sub>
- [`ledgerwatch/erigon-lib#697`](https://github.com/ledgerwatch/erigon-lib/pull/697) — eliasfano: To fix checkptr fatal error   
  <sub>2022-10-22 · merged · authored · score 3 · eliasfano</sub>
- [`ledgerwatch/erigon-lib#682`](https://github.com/ledgerwatch/erigon-lib/pull/682) — feat: implement eliasfano32.Min()  
  <sub>2022-10-13 · merged · reviewed · score 3 · eliasfano</sub>
- [`ledgerwatch/erigon-lib#664`](https://github.com/ledgerwatch/erigon-lib/pull/664) — eliasfano32.Max() method on serialized bytes   
  <sub>2022-10-03 · merged · authored · score 3 · eliasfano</sub>
- [`ledgerwatch/erigon-lib#659`](https://github.com/ledgerwatch/erigon-lib/pull/659) — erigon3: build .vi after downloading  
  <sub>2022-09-29 · merged · authored · score 3 · .vi</sub>
- [`ledgerwatch/erigon-lib#654`](https://github.com/ledgerwatch/erigon-lib/pull/654) — erigon3: build .efi after download  
  <sub>2022-09-26 · merged · authored · score 3 · .efi</sub>
- [`ledgerwatch/erigon-lib#499`](https://github.com/ledgerwatch/erigon-lib/pull/499) — Roaring version up  
  <sub>2022-06-19 · merged · authored · score 3 · roaring</sub>
- [`ledgerwatch/erigon-lib#475`](https://github.com/ledgerwatch/erigon-lib/pull/475) — match roaring version with erigon  
  <sub>2022-05-30 · merged · authored · score 3 · roaring</sub>
- [`ledgerwatch/erigon-lib#325`](https://github.com/ledgerwatch/erigon-lib/pull/325) — Recsplit: use crypto rand seed if user not set  
  <sub>2022-02-13 · merged · authored · score 3 · recsplit</sub>
- [`ledgerwatch/erigon-lib#176`](https://github.com/ledgerwatch/erigon-lib/pull/176) — Recsplit: move files read/write helpers to erigon-lib   
  <sub>2021-11-19 · merged · authored · score 3 · recsplit</sub>
- [`ledgerwatch/erigon-lib#152`](https://github.com/ledgerwatch/erigon-lib/pull/152) — Recsplit: single offset bucket  
  <sub>2021-11-08 · merged · authored · score 3 · recsplit</sub>
- [`ledgerwatch/erigon-lib#150`](https://github.com/ledgerwatch/erigon-lib/pull/150) — Recsplit: collision typed error  
  <sub>2021-11-07 · merged · authored · score 3 · recsplit</sub>
- [`ledgerwatch/erigon-lib#145`](https://github.com/ledgerwatch/erigon-lib/pull/145) — EliasFano: fix jump calculation, fuzzing to trigger jump logic  
  <sub>2021-11-04 · merged · authored · score 3 · eliasfano</sub>
- [`ledgerwatch/erigon-lib#140`](https://github.com/ledgerwatch/erigon-lib/pull/140) — Recsplit: call ef.Build and set ef.prevOffset  
  <sub>2021-11-01 · merged · authored · score 3 · recsplit</sub>
- [`ledgerwatch/erigon-lib#138`](https://github.com/ledgerwatch/erigon-lib/pull/138) — recsplit add MustOpen method  
  <sub>2021-10-31 · merged · authored · score 3 · recsplit</sub>
- [`ledgerwatch/erigon-lib#129`](https://github.com/ledgerwatch/erigon-lib/pull/129) — recsplit: bigger bufio buffer  
  <sub>2021-10-25 · merged · authored · score 3 · recsplit</sub>
- [`ledgerwatch/erigon-lib#67`](https://github.com/ledgerwatch/erigon-lib/pull/67) — Initial recsplit  
  <sub>2021-09-12 · merged · reviewed · score 3 · recsplit</sub>
- [`erigontech/erigon#21893`](https://github.com/erigontech/erigon/pull/21893) — db/datastruct/btindex: EF-encode .bt pivot offsets   
  <sub>2026-06-19 · merged · reviewed · score 2 · encode, index</sub>
- [`erigontech/erigon#21813`](https://github.com/erigontech/erigon/pull/21813) — db/datastruct/btindex: interpolation search in BTree leaf  
  <sub>2026-06-15 · merged · reviewed · score 2 · btree, index</sub>
- [`erigontech/erigon#21794`](https://github.com/erigontech/erigon/pull/21794) — btindex: interpolation search in BTree leaf  
  <sub>2026-06-13 · merged · reviewed · score 2 · btree, index</sub>
- [`erigontech/erigon#19231`](https://github.com/erigontech/erigon/pull/19231) — Test_BtreeIndex_Seek2: fix speed  
  <sub>2026-02-17 · merged · authored · score 2 · btree, index</sub>
- [`erigontech/erigon#19179`](https://github.com/erigontech/erigon/pull/19179) — prune unification (TxLookup)  
  <sub>2026-02-14 · merged · reviewed · score 2 · lookup, prune</sub>
- [`erigontech/erigon#16591`](https://github.com/erigontech/erigon/pull/16591) — [r3.0] catchinn panic in index lookup  
  <sub>2025-08-12 · merged · reviewed · score 2 · index, lookup</sub>
- [`erigontech/erigon#16399`](https://github.com/erigontech/erigon/pull/16399) — [r31] add inverted_index in printStages (#16394)  
  <sub>2025-08-01 · merged · reviewed · score 2 · index, stage</sub>
- [`erigontech/erigon#16394`](https://github.com/erigontech/erigon/pull/16394) — [r31] add inverted_index in printStages  
  <sub>2025-07-31 · merged · reviewed · score 2 · index, stage</sub>
- [`erigontech/erigon#16051`](https://github.com/erigontech/erigon/pull/16051) — [r30] reduce immutability limit - to speedup TxLookup table prune  
  <sub>2025-07-11 · merged · authored · score 2 · lookup, prune</sub>
- [`erigontech/erigon#15918`](https://github.com/erigontech/erigon/pull/15918) — change format of receipt files to fix "duplicated log_index"  
  <sub>2025-07-03 · merged · reviewed · score 2 · format, index</sub>
- [`erigontech/erigon#15895`](https://github.com/erigontech/erigon/pull/15895) — IntegrityInvertedIndexAllValuesAreInRange make parallel   
  <sub>2025-07-02 · merged · reviewed · score 2 · index, parallel</sub>
- [`erigontech/erigon#14784`](https://github.com/erigontech/erigon/pull/14784) — `stage_custom_trace`: to produce logindex, traceindex  
  <sub>2025-04-28 · merged · authored · score 2 · index, stage</sub>
- [`erigontech/erigon#13005`](https://github.com/erigontech/erigon/pull/13005) — speedup files open: by parallel index open  
  <sub>2024-12-05 · merged · authored · score 2 · index, parallel</sub>
- [`erigontech/erigon#11305`](https://github.com/erigontech/erigon/pull/11305) — remove stage_call_trace, stage_index, stage_log_index  
  <sub>2024-07-24 · merged · authored · score 2 · index, stage</sub>
- [`erigontech/erigon#10894`](https://github.com/erigontech/erigon/pull/10894) — remove log_index_stage from default_stages.go  
  <sub>2024-06-25 · merged · authored · score 2 · index, stage</sub>
- [`erigontech/erigon#10392`](https://github.com/erigontech/erigon/pull/10392) — reuse same cursor during prune of `InvertedIndex`  
  <sub>2024-05-17 · merged · reviewed · score 2 · index, prune</sub>
- [`erigontech/erigon#10294`](https://github.com/erigontech/erigon/pull/10294) — Fix potential index out of bounds in decodeBlobVersionedHashes  
  <sub>2024-05-13 · merged · reviewed · score 2 · decode, index</sub>
- [`erigontech/erigon#9733`](https://github.com/erigontech/erigon/pull/9733) — Fix LogIndex Prune  
  <sub>2024-03-17 · merged · reviewed · score 2 · index, prune</sub>
- [`erigontech/erigon#6086`](https://github.com/erigontech/erigon/pull/6086) — TxLookup: limit incremental prune range  
  <sub>2022-11-20 · merged · authored · score 2 · lookup, prune</sub>
- [`erigontech/erigon#5957`](https://github.com/erigontech/erigon/pull/5957) — e3: disable txlookup stage  
  <sub>2022-11-04 · merged · authored · score 2 · lookup, stage</sub>
- [`erigontech/erigon#5181`](https://github.com/erigontech/erigon/pull/5181) — erigon22: disable logIndex, historyIndex, callTracesIndex stages in --history.v2=true mode  
  <sub>2022-08-25 · merged · authored · score 2 · index, stage</sub>
- [`erigontech/erigon#4925`](https://github.com/erigontech/erigon/pull/4925) — Sn: parallel files indexing progress logs  
  <sub>2022-08-04 · merged · authored · score 2 · index, parallel</sub>
- [`erigontech/erigon#4740`](https://github.com/erigontech/erigon/pull/4740) — Support block parameter for integration stage_log_index  
  <sub>2022-07-19 · merged · reviewed · score 2 · index, stage</sub>
- [`erigontech/erigon#4335`](https://github.com/erigontech/erigon/pull/4335) — --snap.stop: to prevent indexing on stage_header  
  <sub>2022-06-02 · merged · authored · score 2 · index, stage</sub>
- [`erigontech/erigon#4246`](https://github.com/erigontech/erigon/pull/4246) — use casting to bytes array in txlookup stage  
  <sub>2022-05-24 · merged · authored · score 2 · lookup, stage</sub>
- [`erigontech/erigon#3921`](https://github.com/erigontech/erigon/pull/3921) — Parallel indexing  
  <sub>2022-04-20 · merged · authored · score 2 · index, parallel</sub>
- [`erigontech/erigon#3858`](https://github.com/erigontech/erigon/pull/3858) — Fix for slow LogIndex prune  
  <sub>2022-04-09 · merged · authored · score 2 · index, prune</sub>
- [`erigontech/erigon#3314`](https://github.com/erigontech/erigon/pull/3314) — Cumulative index stage  
  <sub>2022-01-21 · merged · reviewed · score 2 · index, stage</sub>
- [`erigontech/erigon#2434`](https://github.com/erigontech/erigon/pull/2434) — fix prune log index by wrong distance  
  <sub>2021-07-24 · merged · authored · score 2 · index, prune</sub>

## Compression / encoding  (150)

- [`erigontech/erigon#18485`](https://github.com/erigontech/erigon/pull/18485) — Optimized the Huffman decoding hot paths in the decompression routines  
  <sub>2025-12-28 · merged · reviewed · score 12 · compress, compression, decompress, huffman</sub>
- [`erigontech/erigon#5464`](https://github.com/erigontech/erigon/pull/5464) — erigon method to test decompression speed  
  <sub>2022-09-22 · merged · authored · score 9 · compress, compression, decompress</sub>
- [`ledgerwatch/erigon-lib#452`](https://github.com/ledgerwatch/erigon-lib/pull/452) — reduce memory footprint during decompression  
  <sub>2022-05-17 · merged · reviewed · score 9 · compress, compression, decompress</sub>
- [`erigontech/erigon#3427`](https://github.com/erigontech/erigon/pull/3427) — ParallelCompressor: Remove intermediate ETL collectors   
  <sub>2022-02-04 · merged · authored · score 8 · collector, compress, etl , parallel</sub>
- [`ledgerwatch/erigon-lib#302`](https://github.com/ledgerwatch/erigon-lib/pull/302) — ParallelCompressor: Remove intermediate ETL collectors  
  <sub>2022-02-04 · merged · authored · score 8 · collector, compress, etl , parallel</sub>
- [`erigontech/erigon#925`](https://github.com/erigontech/erigon/pull/925) — add support of blocks compression to txpool stage  
  <sub>2020-08-15 · merged · authored+reviewed · score 7 · compress, compression, stage</sub>
- [`erigontech/erigon#859`](https://github.com/erigontech/erigon/pull/859) — stage3 block compression support  
  <sub>2020-08-02 · merged · authored · score 7 · compress, compression, stage</sub>
- [`ledgerwatch/erigon-lib#234`](https://github.com/ledgerwatch/erigon-lib/pull/234) — ParallelCompressor class, DecompressedFile class   
  <sub>2022-01-15 · merged · authored · score 7 · compress, decompress, parallel</sub>
- [`ledgerwatch/erigon-lib#223`](https://github.com/ledgerwatch/erigon-lib/pull/223) — Parallel compression  
  <sub>2022-01-06 · merged · authored · score 7 · compress, compression, parallel</sub>
- [`erigontech/erigon#20665`](https://github.com/erigontech/erigon/pull/20665) — rpc: compression with libdeflate  
  <sub>2026-04-19 · merged · reviewed · score 6 · compress, compression</sub>
- [`erigontech/erigon#20074`](https://github.com/erigontech/erigon/pull/20074) — [wip] seg: add word-level compression enum into data-file header  
  <sub>2026-03-23 · open · authored+reviewed · score 6 · compress, compression</sub>
- [`erigontech/erigon#19537`](https://github.com/erigontech/erigon/pull/19537) — [wip] seg: add word-level compression enum into data-file header  
  <sub>2026-03-01 · closed · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#19443`](https://github.com/erigontech/erigon/pull/19443) — seg: if word-level compression disabled. don't create `.idt` file  
  <sub>2026-02-24 · merged · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#19191`](https://github.com/erigontech/erigon/pull/19191) — compression: replace C `sais` lib by Golang stdlib's one  
  <sub>2026-02-15 · merged · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#18813`](https://github.com/erigontech/erigon/pull/18813) — Disabled compression in collate function  
  <sub>2026-01-26 · merged · reviewed · score 6 · compress, compression</sub>
- [`erigontech/erigon#18752`](https://github.com/erigontech/erigon/pull/18752) — Hist.Collate: disable compression to speedup Collate+Build  
  <sub>2026-01-22 · closed · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#18490`](https://github.com/erigontech/erigon/pull/18490) — rm `condense` feature from decompressor  
  <sub>2025-12-29 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#17542`](https://github.com/erigontech/erigon/pull/17542) — bench: decompressor heap-alloc vs buf-reuse  
  <sub>2025-10-20 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#16812`](https://github.com/erigontech/erigon/pull/16812) — [wip] decompress: arena allocator  
  <sub>2025-08-26 · open · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#15858`](https://github.com/erigontech/erigon/pull/15858) — BenchmarkDecompress: on 0.5mb words  
  <sub>2025-07-01 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#15583`](https://github.com/erigontech/erigon/pull/15583) — rpcdaemon/erigon modify compression default config  
  <sub>2025-06-15 · merged · reviewed · score 6 · compress, compression</sub>
- [`erigontech/erigon#14604`](https://github.com/erigontech/erigon/pull/14604) — hist: values snappy compression  
  <sub>2025-04-15 · merged · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#13281`](https://github.com/erigontech/erigon/pull/13281) — [wip] allow disable compression in future  
  <sub>2024-12-31 · closed · authored+reviewed · score 6 · compress, compression</sub>
- [`erigontech/erigon#12951`](https://github.com/erigontech/erigon/pull/12951) — d_lru: to store decompressed values  
  <sub>2024-12-02 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#12087`](https://github.com/erigontech/erigon/pull/12087) — compression: additional limit for effective dict  
  <sub>2024-09-25 · closed · reviewed · score 6 · compress, compression</sub>
- [`erigontech/erigon#11688`](https://github.com/erigontech/erigon/pull/11688) — missed compression flags   
  <sub>2024-08-20 · merged · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#10558`](https://github.com/erigontech/erigon/pull/10558) — buildVI: nil decompressor passed fix  
  <sub>2024-05-30 · merged · reviewed · score 6 · compress, decompress</sub>
- [`erigontech/erigon#9948`](https://github.com/erigontech/erigon/pull/9948) — Clarify decompressor opening errors  
  <sub>2024-04-15 · merged · reviewed · score 6 · compress, decompress</sub>
- [`erigontech/erigon#7228`](https://github.com/erigontech/erigon/pull/7228) — stricter protection against bad dict in decompressor  
  <sub>2023-03-31 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#6812`](https://github.com/erigontech/erigon/pull/6812) — less logs about compression  
  <sub>2023-02-09 · merged · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#5853`](https://github.com/erigontech/erigon/pull/5853) — add DECOMPRESS_CONDENSITY env variable  
  <sub>2022-10-24 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#5804`](https://github.com/erigontech/erigon/pull/5804) — add fileName to decompressor panic  
  <sub>2022-10-20 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#5130`](https://github.com/erigontech/erigon/pull/5130) — compress: implemented consensed huffman pattern tables #536  
  <sub>2022-08-22 · merged · authored · score 6 · compress, huffman</sub>
- [`erigontech/erigon#4882`](https://github.com/erigontech/erigon/pull/4882) — decompress: catch maxDepth underflow  
  <sub>2022-08-01 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#4536`](https://github.com/erigontech/erigon/pull/4536) — Compress: reduce etl buffers to save RAM #4535  
  <sub>2022-06-25 · merged · authored · score 6 · compress, etl </sub>
- [`erigontech/erigon#4535`](https://github.com/erigontech/erigon/pull/4535) — Compress and snap indices: reduce etl buffers to save RAM  
  <sub>2022-06-25 · closed · authored · score 6 · compress, etl </sub>
- [`erigontech/erigon#4176`](https://github.com/erigontech/erigon/pull/4176) — Decompress: to use less ram  
  <sub>2022-05-17 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#3395`](https://github.com/erigontech/erigon/pull/3395) — Decompressor.WithReadAhead  
  <sub>2022-02-01 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#3225`](https://github.com/erigontech/erigon/pull/3225) — Decompressor: fast Count() method  
  <sub>2022-01-09 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#2066`](https://github.com/erigontech/erigon/pull/2066) — rpcdaemon: --http.compression flag (default: true)  
  <sub>2021-05-31 · merged · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#1453`](https://github.com/erigontech/erigon/pull/1453) — remove blocks compression  
  <sub>2021-01-24 · merged · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#1178`](https://github.com/erigontech/erigon/pull/1178) — [wip] Receipts compression  
  <sub>2020-10-03 · closed · authored · score 6 · compress, compression</sub>
- [`erigontech/erigon#380`](https://github.com/erigontech/erigon/pull/380) — Run CI on bolt with prefix_compression_without_allocation (fixes)  
  <sub>2020-02-22 · merged · authored · score 6 · compress, compression</sub>
- [`ledgerwatch/bolt#16`](https://github.com/ledgerwatch/bolt/pull/16) — [WIP] Reduce amount of allocations in PrefixCompression feature  
  <sub>2020-02-21 · closed · authored · score 6 · compress, compression</sub>
- [`ledgerwatch/bolt#11`](https://github.com/ledgerwatch/bolt/pull/11) — invert logic of keyPrefixCompression flag  
  <sub>2020-01-10 · merged · authored · score 6 · compress, compression</sub>
- [`ledgerwatch/bolt#2`](https://github.com/ledgerwatch/bolt/pull/2) — Optional key prefix compression  
  <sub>2019-12-24 · merged · authored · score 6 · compress, compression</sub>
- [`ledgerwatch/erigon-lib#1056`](https://github.com/ledgerwatch/erigon-lib/pull/1056) — [WIP] decompress::Match   
  <sub>2023-07-24 · merged · reviewed · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#1042`](https://github.com/ledgerwatch/erigon-lib/pull/1042) — [WIP] compress/decompress.go::Match modified  
  <sub>2023-07-10 · closed · reviewed · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#962`](https://github.com/ledgerwatch/erigon-lib/pull/962) — stricter protection against bad dict in decompressor  
  <sub>2023-03-31 · merged · authored · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#882`](https://github.com/ledgerwatch/erigon-lib/pull/882) — less logs about compression  
  <sub>2023-02-09 · merged · authored · score 6 · compress, compression</sub>
- [`ledgerwatch/erigon-lib#701`](https://github.com/ledgerwatch/erigon-lib/pull/701) — add DECOMPRESS_CONDENSITY env variable  
  <sub>2022-10-24 · merged · authored · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#689`](https://github.com/ledgerwatch/erigon-lib/pull/689) — add fileName to decompressor panic  
  <sub>2022-10-20 · merged · authored · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#562`](https://github.com/ledgerwatch/erigon-lib/pull/562) — decompress: catch maxDepth underflow  
  <sub>2022-08-01 · merged · authored · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#536`](https://github.com/ledgerwatch/erigon-lib/pull/536) — compress: implemented consensed huffman pattern tables  
  <sub>2022-07-20 · merged · reviewed · score 6 · compress, huffman</sub>
- [`ledgerwatch/erigon-lib#502`](https://github.com/ledgerwatch/erigon-lib/pull/502) — Compress: reduce etl buffers to save RAM  
  <sub>2022-06-25 · merged · authored · score 6 · compress, etl </sub>
- [`ledgerwatch/erigon-lib#468`](https://github.com/ledgerwatch/erigon-lib/pull/468) — added print of decompressed file at panic  
  <sub>2022-05-25 · merged · reviewed · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#290`](https://github.com/ledgerwatch/erigon-lib/pull/290) — Decompressor.WithReadAhead  
  <sub>2022-02-01 · merged · authored · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#226`](https://github.com/ledgerwatch/erigon-lib/pull/226) — Decompressor: fast .Count method  
  <sub>2022-01-09 · merged · authored · score 6 · compress, decompress</sub>
- [`ledgerwatch/erigon-lib#220`](https://github.com/ledgerwatch/erigon-lib/pull/220) — Decompressor internal file path getter  
  <sub>2021-12-31 · merged · authored · score 6 · compress, decompress</sub>
- [`erigontech/erigon#19892`](https://github.com/erigontech/erigon/pull/19892) — rlp: optimize RLP encode/decode to reduce allocations  
  <sub>2026-03-14 · merged · reviewed · score 5 · decode, encode, rlp </sub>
- [`erigontech/erigon#17794`](https://github.com/erigontech/erigon/pull/17794) — fix: add nil checks in CBOR encoder/decoder pool operations  
  <sub>2025-11-05 · merged · reviewed · score 5 · cbor, decode, encode</sub>
- [`erigontech/erigon#9691`](https://github.com/erigontech/erigon/pull/9691) — Shortening body encode/decode RLP code  
  <sub>2024-03-12 · merged · reviewed · score 5 · decode, encode, rlp </sub>
- [`erigontech/erigon#21287`](https://github.com/erigontech/erigon/pull/21287) — execution/rlp, execution/types: cut RLP header-decode allocations  
  <sub>2026-05-19 · merged · reviewed · score 4 · decode, rlp </sub>
- [`erigontech/erigon#18203`](https://github.com/erigontech/erigon/pull/18203) — fix(compress): correct zstd decode error prefix  
  <sub>2025-12-07 · merged · reviewed · score 4 · compress, decode</sub>
- [`erigontech/erigon#16036`](https://github.com/erigontech/erigon/pull/16036) — rip: Log.DecodeRLP method  
  <sub>2025-07-10 · merged · authored · score 4 · decode, rlp </sub>
- [`erigontech/erigon#16030`](https://github.com/erigontech/erigon/pull/16030) — hand-crafted Log.DecodeRLP  
  <sub>2025-07-10 · closed · authored · score 4 · decode, rlp </sub>
- [`erigontech/erigon#15210`](https://github.com/erigontech/erigon/pull/15210) — BlockReader: use cheaper rlp decode method  
  <sub>2025-05-22 · merged · authored · score 4 · decode, rlp </sub>
- [`erigontech/erigon#13341`](https://github.com/erigontech/erigon/pull/13341) — RLP encoding and decoding generator for simple structures  
  <sub>2025-01-08 · merged · reviewed · score 4 · encoding, rlp </sub>
- [`erigontech/erigon#11114`](https://github.com/erigontech/erigon/pull/11114) — gencodec version up  
  <sub>2024-07-11 · closed · authored · score 4 · codec, encode</sub>
- [`erigontech/erigon#7116`](https://github.com/erigontech/erigon/pull/7116) — simplify DecodeRLP for some types  
  <sub>2023-03-15 · closed · reviewed · score 4 · decode, rlp </sub>
- [`erigontech/erigon#7053`](https://github.com/erigontech/erigon/pull/7053) — [wip] e3: history db format without auto-increment  
  <sub>2023-03-08 · closed · authored · score 4 · db format, format</sub>
- [`erigontech/erigon#3361`](https://github.com/erigontech/erigon/pull/3361) — parallel compressor: less read of dat file  
  <sub>2022-01-27 · merged · authored · score 4 · compress, parallel</sub>
- [`erigontech/erigon#3358`](https://github.com/erigontech/erigon/pull/3358) — parallel compressor: don't save dict  
  <sub>2022-01-27 · merged · authored · score 4 · compress, parallel</sub>
- [`erigontech/erigon#1242`](https://github.com/erigontech/erigon/pull/1242) — Disable cbor migration with fallback to support release  
  <sub>2020-10-15 · closed · authored · score 4 · cbor, migration</sub>
- [`ledgerwatch/bolt#22`](https://github.com/ledgerwatch/bolt/pull/22) — [uncompatible db format] Fix unsafe pointer conversions caught by Go 1.14 checkptr  
  <sub>2020-04-02 · merged · authored · score 4 · db format, format</sub>
- [`ledgerwatch/erigon-lib#924`](https://github.com/ledgerwatch/erigon-lib/pull/924) — [wip] e3: history db format without auto-increment  
  <sub>2023-03-08 · closed · authored · score 4 · db format, format</sub>
- [`ledgerwatch/erigon-lib#284`](https://github.com/ledgerwatch/erigon-lib/pull/284) — parallel compress: less read of dat file  
  <sub>2022-01-27 · merged · authored · score 4 · compress, parallel</sub>
- [`ledgerwatch/erigon-lib#283`](https://github.com/ledgerwatch/erigon-lib/pull/283) — parallel compressor: don't save dict  
  <sub>2022-01-27 · merged · authored · score 4 · compress, parallel</sub>
- [`ledgerwatch/erigon-lib#245`](https://github.com/ledgerwatch/erigon-lib/pull/245) — Parallel compressor - allow empty words  
  <sub>2022-01-18 · merged · authored · score 4 · compress, parallel</sub>
- [`ledgerwatch/erigon-lib#244`](https://github.com/ledgerwatch/erigon-lib/pull/244) — Switch to parallel compressor  
  <sub>2022-01-18 · merged · authored · score 4 · compress, parallel</sub>
- [`erigontech/erigon#21742`](https://github.com/erigontech/erigon/pull/21742) — bloatnet: reduce word-level compress sampling  
  <sub>2026-06-11 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#20815`](https://github.com/erigontech/erigon/pull/20815) — QA: enable test also on http-compressed and websockets for historical mainnet  
  <sub>2026-04-25 · merged · reviewed · score 3 · compress</sub>
- [`erigontech/erigon#20790`](https://github.com/erigontech/erigon/pull/20790) — `erigon seg ls`: show dictionary size on disk and in mem  
  <sub>2026-04-24 · merged · authored · score 3 · dictionary</sub>
- [`erigontech/erigon#20715`](https://github.com/erigontech/erigon/pull/20715) — ci: speedup hive eest consume-rlp by removing unnecessary NAT discovery  
  <sub>2026-04-21 · merged · reviewed · score 3 · rlp </sub>
- [`erigontech/erigon#20053`](https://github.com/erigontech/erigon/pull/20053) — rpc/jsonrpc: fix debug_getBadBlocks swapped block/rlp fields  
  <sub>2026-03-21 · merged · reviewed · score 3 · rlp </sub>
- [`erigontech/erigon#19192`](https://github.com/erigontech/erigon/pull/19192) — erigon seg compress: support flag `--from` as input file instead of `stdin`  
  <sub>2026-02-15 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#17872`](https://github.com/erigontech/erigon/pull/17872) — db/seg: fix MatchPrefixUncompressed empty prefix/word semantics  
  <sub>2025-11-12 · open · reviewed · score 3 · compress</sub>
- [`erigontech/erigon#17495`](https://github.com/erigontech/erigon/pull/17495) — fix bug in EpochData ssz marshalling  
  <sub>2025-10-16 · merged · reviewed · score 3 · ssz</sub>
- [`erigontech/erigon#17441`](https://github.com/erigontech/erigon/pull/17441) — db/seg: fix MatchPrefixUncompressed/MatchCmpUncompressed empty-input semantics  
  <sub>2025-10-13 · open · reviewed · score 3 · compress</sub>
- [`erigontech/erigon#12895`](https://github.com/erigontech/erigon/pull/12895) — Remove rlp and bitutil from lint exclude-rules  
  <sub>2024-11-27 · merged · reviewed · score 3 · rlp </sub>
- [`erigontech/erigon#11876`](https://github.com/erigontech/erigon/pull/11876) — code.kv: compress values  
  <sub>2024-09-05 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#11875`](https://github.com/erigontech/erigon/pull/11875) — `erigon seg compress` - support OnlyVals option  
  <sub>2024-09-05 · closed · authored · score 3 · compress</sub>
- [`erigontech/erigon#11711`](https://github.com/erigontech/erigon/pull/11711) — compress: enforce hard dict limit  
  <sub>2024-08-22 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#11672`](https://github.com/erigontech/erigon/pull/11672) — comp: DictionaryBuilder - separate soft/hard limits  
  <sub>2024-08-19 · merged · authored · score 3 · dictionary</sub>
- [`erigontech/erigon#11666`](https://github.com/erigontech/erigon/pull/11666) — compress: extract cfg object  
  <sub>2024-08-19 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#11222`](https://github.com/erigontech/erigon/pull/11222) — block files: don't compress 1k and 10k files  
  <sub>2024-07-18 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#11082`](https://github.com/erigontech/erigon/pull/11082) — up `x` deps and cbor version  
  <sub>2024-07-09 · merged · authored · score 3 · cbor</sub>
- [`erigontech/erigon#10291`](https://github.com/erigontech/erigon/pull/10291) — Receipts: remove old rlp types  
  <sub>2024-05-13 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#10105`](https://github.com/erigontech/erigon/pull/10105) — core/types: disable go:generate codecgen for receipts and logs  
  <sub>2024-04-28 · merged · reviewed · score 3 · codec</sub>
- [`erigontech/erigon#9460`](https://github.com/erigontech/erigon/pull/9460) — seg compress: fix LCP initialization  
  <sub>2024-02-16 · merged · reviewed · score 3 · compress</sub>
- [`erigontech/erigon#9453`](https://github.com/erigontech/erigon/pull/9453) — silkworm: seg compressor fuzz test  
  <sub>2024-02-15 · merged · reviewed · score 3 · compress</sub>
- [`erigontech/erigon#8143`](https://github.com/erigontech/erigon/pull/8143) — compress.Next: return empty byte slice instead of nil when wordLen == 0  
  <sub>2023-09-06 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#8098`](https://github.com/erigontech/erigon/pull/8098) — Compress: graceful shutdown support  
  <sub>2023-08-30 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#8072`](https://github.com/erigontech/erigon/pull/8072) — [wip]: test non-nil compress.Next  
  <sub>2023-08-25 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#7542`](https://github.com/erigontech/erigon/pull/7542) — Caplin: Adding SSZ generics  
  <sub>2023-05-18 · merged · reviewed · score 3 · ssz</sub>
- [`erigontech/erigon#7454`](https://github.com/erigontech/erigon/pull/7454) — [caplin] ssz byteobjects  
  <sub>2023-05-07 · merged · reviewed · score 3 · ssz</sub>
- [`erigontech/erigon#5631`](https://github.com/erigontech/erigon/pull/5631) — Compress params change   
  <sub>2022-10-05 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#5131`](https://github.com/erigontech/erigon/pull/5131) — Compress: limit patternMaxDepth  
  <sub>2022-08-22 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#4734`](https://github.com/erigontech/erigon/pull/4734) — compressor: generic sort  
  <sub>2022-07-18 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#4214`](https://github.com/erigontech/erigon/pull/4214) — Snap: reduced memory footprint on building huffman table  
  <sub>2022-05-20 · merged · authored · score 3 · huffman</sub>
- [`erigontech/erigon#3891`](https://github.com/erigontech/erigon/pull/3891) — Compress: reduce maxlen to 512  
  <sub>2022-04-15 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#3807`](https://github.com/erigontech/erigon/pull/3807) — compressor: log lvl  
  <sub>2022-04-01 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#3798`](https://github.com/erigontech/erigon/pull/3798) — compress and uncompress cli methods  
  <sub>2022-03-31 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#3396`](https://github.com/erigontech/erigon/pull/3396) — penalize peer for invalid rlp  
  <sub>2022-02-01 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#3315`](https://github.com/erigontech/erigon/pull/3315) — Penalize for invalid rlp   
  <sub>2022-01-21 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#3242`](https://github.com/erigontech/erigon/pull/3242) — Penalize for invalid rlp   
  <sub>2022-01-12 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#3232`](https://github.com/erigontech/erigon/pull/3232) — [wip] penalize peer for invalid rlp  
  <sub>2022-01-11 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#3176`](https://github.com/erigontech/erigon/pull/3176) — RLP base error, part2  
  <sub>2021-12-27 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#3175`](https://github.com/erigontech/erigon/pull/3175) — RLP base error, part2  
  <sub>2021-12-27 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#2943`](https://github.com/erigontech/erigon/pull/2943) — Compress: add maxPatternLen=64  
  <sub>2021-11-10 · merged · authored · score 3 · compress</sub>
- [`erigontech/erigon#2640`](https://github.com/erigontech/erigon/pull/2640) — Pool: rlp fuzzing fixes  
  <sub>2021-09-07 · closed · authored · score 3 · rlp </sub>
- [`erigontech/erigon#2124`](https://github.com/erigontech/erigon/pull/2124) — More correct rlp of Sokol headers  
  <sub>2021-06-09 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#2109`](https://github.com/erigontech/erigon/pull/2109) — revert receipt codec version  
  <sub>2021-06-06 · merged · authored · score 3 · codec</sub>
- [`erigontech/erigon#1172`](https://github.com/erigontech/erigon/pull/1172) — Switch to cbor  
  <sub>2020-10-02 · merged · authored · score 3 · cbor</sub>
- [`erigontech/erigon#1163`](https://github.com/erigontech/erigon/pull/1163) — Better cbor support  
  <sub>2020-10-01 · merged · authored · score 3 · cbor</sub>
- [`erigontech/erigon-snapshot#7`](https://github.com/erigontech/erigon-snapshot/pull/7) — Change compress params and new bsc files  
  <sub>2022-10-10 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#1090`](https://github.com/ledgerwatch/erigon-lib/pull/1090) — Compress: graceful shutdown support  
  <sub>2023-08-30 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#1085`](https://github.com/ledgerwatch/erigon-lib/pull/1085) — compress.Next: return empty byte slice instead of nil when wordLen == 0  
  <sub>2023-08-25 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#991`](https://github.com/ledgerwatch/erigon-lib/pull/991) — update ssz.go with latest changes  
  <sub>2023-05-09 · merged · reviewed · score 3 · ssz</sub>
- [`ledgerwatch/erigon-lib#691`](https://github.com/ledgerwatch/erigon-lib/pull/691) — compress: to use less ram  
  <sub>2022-10-20 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#651`](https://github.com/ledgerwatch/erigon-lib/pull/651) — Compress params change  
  <sub>2022-09-24 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#648`](https://github.com/ledgerwatch/erigon-lib/pull/648) — remove sequential compressor  
  <sub>2022-09-22 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#598`](https://github.com/ledgerwatch/erigon-lib/pull/598) — Compress: limit patternMaxDepth  
  <sub>2022-08-22 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#524`](https://github.com/ledgerwatch/erigon-lib/pull/524) — compressor: generic sort  
  <sub>2022-07-18 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#478`](https://github.com/ledgerwatch/erigon-lib/pull/478) — compress.Count() method  
  <sub>2022-06-03 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#459`](https://github.com/ledgerwatch/erigon-lib/pull/459) — [erigon2] reduced memory footprint on building huffman table  
  <sub>2022-05-19 · merged · reviewed · score 3 · huffman</sub>
- [`ledgerwatch/erigon-lib#416`](https://github.com/ledgerwatch/erigon-lib/pull/416) — Compress: reduce maxlen to 512  
  <sub>2022-04-15 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#408`](https://github.com/ledgerwatch/erigon-lib/pull/408) — compressor: log lvl  
  <sub>2022-04-01 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#362`](https://github.com/ledgerwatch/erigon-lib/pull/362) — cancel compress  
  <sub>2022-03-12 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#361`](https://github.com/ledgerwatch/erigon-lib/pull/361) — compress: less allocs   
  <sub>2022-03-12 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#260`](https://github.com/ledgerwatch/erigon-lib/pull/260) — Fixes in compress  
  <sub>2022-01-21 · merged · reviewed · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#222`](https://github.com/ledgerwatch/erigon-lib/pull/222) — Rlp base err2   
  <sub>2022-01-05 · merged · authored · score 3 · rlp </sub>
- [`ledgerwatch/erigon-lib#221`](https://github.com/ledgerwatch/erigon-lib/pull/221) — Rlp base err2  
  <sub>2022-01-05 · merged · authored · score 3 · rlp </sub>
- [`ledgerwatch/erigon-lib#155`](https://github.com/ledgerwatch/erigon-lib/pull/155) — Compress: add maxPatternLen=64  
  <sub>2021-11-10 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#154`](https://github.com/ledgerwatch/erigon-lib/pull/154) — Compress: fix compress bytes share  
  <sub>2021-11-10 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#151`](https://github.com/ledgerwatch/erigon-lib/pull/151) — Use bufio limit in compressor  
  <sub>2021-11-07 · merged · authored · score 3 · compress</sub>
- [`ledgerwatch/erigon-lib#106`](https://github.com/ledgerwatch/erigon-lib/pull/106) — rlp uint fix  
  <sub>2021-10-10 · merged · authored · score 3 · rlp </sub>
- [`ledgerwatch/erigon-lib#60`](https://github.com/ledgerwatch/erigon-lib/pull/60) — Pool: rlp fuzzing fixes  
  <sub>2021-09-07 · merged · authored · score 3 · rlp </sub>
- [`ledgerwatch/erigon-lib#4`](https://github.com/ledgerwatch/erigon-lib/pull/4) — Rlp first look  
  <sub>2021-07-27 · merged · authored · score 3 · rlp </sub>
- [`erigontech/erigon#18980`](https://github.com/erigontech/erigon/pull/18980) — perf(cl/block_collector): optimize encodeBlock buffer allocation  
  <sub>2026-02-05 · merged · reviewed · score 2 · collector, encode</sub>

## ETL / staged sync / pruning  (125)

- [`erigontech/erigon#1806`](https://github.com/erigontech/erigon/pull/1806) — exec unwind etl  
  <sub>2021-04-26 · merged · authored · score 6 · etl , unwind</sub>
- [`erigontech/erigon#17783`](https://github.com/erigontech/erigon/pull/17783) — Fix unwinds for parallel processing  
  <sub>2025-11-04 · merged · reviewed · score 4 · parallel, unwind</sub>
- [`erigontech/erigon#16974`](https://github.com/erigontech/erigon/pull/16974) — agg: writers to not create etl collectors if `discard = true`   
  <sub>2025-09-03 · merged · authored · score 4 · collector, etl </sub>
- [`erigontech/erigon#15551`](https://github.com/erigontech/erigon/pull/15551) — unwind and prune on forkable agg  
  <sub>2025-06-12 · merged · reviewed · score 4 · prune, unwind</sub>
- [`erigontech/erigon#12695`](https://github.com/erigontech/erigon/pull/12695) — E3: Reduced allocs due to ETL during pruning  
  <sub>2024-11-09 · merged · reviewed · score 4 · etl , pruning</sub>
- [`erigontech/erigon#10673`](https://github.com/erigontech/erigon/pull/10673) — cl: etl collector does copy under the hood  
  <sub>2024-06-09 · merged · authored · score 4 · collector, etl </sub>
- [`erigontech/erigon#10633`](https://github.com/erigontech/erigon/pull/10633) — protect stage_bor_heimdal: from unwind behind files  
  <sub>2024-06-06 · merged · authored · score 4 · stage, unwind</sub>
- [`erigontech/erigon#6757`](https://github.com/erigontech/erigon/pull/6757) — e3: indices wal - to reuse etl collector  
  <sub>2023-02-01 · merged · authored · score 4 · collector, etl </sub>
- [`erigontech/erigon#3813`](https://github.com/erigontech/erigon/pull/3813) — Delete blocks on integration stage_header --unwind  
  <sub>2022-04-02 · merged · authored · score 4 · stage, unwind</sub>
- [`erigontech/erigon#2592`](https://github.com/erigontech/erigon/pull/2592) — CallTraces prune to use ETL  
  <sub>2021-08-29 · merged · authored · score 4 · etl , prune</sub>
- [`erigontech/erigon#2381`](https://github.com/erigontech/erigon/pull/2381) — Remove stage builder and use ID's in unwindOrder  
  <sub>2021-07-16 · merged · authored · score 4 · stage, unwind</sub>
- [`ledgerwatch/erigon-lib#875`](https://github.com/ledgerwatch/erigon-lib/pull/875) — e3: indices wal - to reuse etl collector  
  <sub>2023-02-01 · merged · authored · score 4 · collector, etl </sub>
- [`erigontech/erigon#20906`](https://github.com/erigontech/erigon/pull/20906) — integration: guard unwind boundaries  
  <sub>2026-04-29 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#20902`](https://github.com/erigontech/erigon/pull/20902) — add ReceiptRoot integrity check  
  <sub>2026-04-29 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#20806`](https://github.com/erigontech/erigon/pull/20806) — bloatnet: allow unknown integrity checks  
  <sub>2026-04-25 · merged · authored · score 3 · integrity check</sub>
- [`erigontech/erigon#20773`](https://github.com/erigontech/erigon/pull/20773) — cmd/utils/app, db/integrity: add time budget for integrity checks  
  <sub>2026-04-24 · merged · authored · score 3 · integrity check</sub>
- [`erigontech/erigon#20714`](https://github.com/erigontech/erigon/pull/20714) — add time budget for integrity checks  
  <sub>2026-04-21 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#20516`](https://github.com/erigontech/erigon/pull/20516) — execution/cache: wire RevertWithDiffset into unwind path  
  <sub>2026-04-13 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#20296`](https://github.com/erigontech/erigon/pull/20296) — prune: clear PruningValsProgress on stage_exec --reset  
  <sub>2026-04-02 · merged · reviewed · score 3 · prune, pruning, stage</sub>
- [`erigontech/erigon#19268`](https://github.com/erigontech/erigon/pull/19268) — Fix: don't integrity check rcache if they are not being generated  
  <sub>2026-02-17 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#19063`](https://github.com/erigontech/erigon/pull/19063) — [r33] execution/execmodule: fix unwinding logic when side forks go back in height (#18993)  
  <sub>2026-02-10 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#19033`](https://github.com/erigontech/erigon/pull/19033) — Performance: skip unwind when unneded.  
  <sub>2026-02-08 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#18993`](https://github.com/erigontech/erigon/pull/18993) — execution/execmodule: fix unwinding logic when side forks go back in height  
  <sub>2026-02-06 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#18560`](https://github.com/erigontech/erigon/pull/18560) — db/integrity: remove unused ticker in RCache integrity check  
  <sub>2026-01-05 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#18544`](https://github.com/erigontech/erigon/pull/18544) — [wip]: single etl buf pool  
  <sub>2026-01-03 · closed · authored · score 3 · etl </sub>
- [`erigontech/erigon#18448`](https://github.com/erigontech/erigon/pull/18448) — skip-check option for integrity checks  
  <sub>2025-12-24 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#18244`](https://github.com/erigontech/erigon/pull/18244) — fix: avoid duplicate byte-to-string conversions in ETL buffers  
  <sub>2025-12-10 · open · reviewed · score 3 · etl </sub>
- [`erigontech/erigon#17890`](https://github.com/erigontech/erigon/pull/17890) — [3.2] prune: 500ms pruning timeout for stage_exec on ChainTiptar  
  <sub>2025-11-14 · merged · authored · score 3 · prune, pruning, stage</sub>
- [`erigontech/erigon#17889`](https://github.com/erigontech/erigon/pull/17889) — [3.3] prune: 500ms pruning timeout for stage_exec on ChainTip  
  <sub>2025-11-14 · merged · authored · score 3 · prune, pruning, stage</sub>
- [`erigontech/erigon#17700`](https://github.com/erigontech/erigon/pull/17700) — cp: comment out brittle case in integrity check  
  <sub>2025-10-29 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#17511`](https://github.com/erigontech/erigon/pull/17511) — [r32] execution: protect e3 file collation from reorgs  
  <sub>2025-10-17 · merged · reviewed · score 3 · reorg</sub>
- [`erigontech/erigon#17469`](https://github.com/erigontech/erigon/pull/17469) — execution: protect e3 file collation from reorgs  
  <sub>2025-10-15 · merged · reviewed · score 3 · reorg</sub>
- [`erigontech/erigon#17165`](https://github.com/erigontech/erigon/pull/17165) — execution: store changesets for last MaxReorgDepth blocks after initial cycle  
  <sub>2025-09-19 · merged · reviewed · score 3 · reorg</sub>
- [`erigontech/erigon#16802`](https://github.com/erigontech/erigon/pull/16802) — faster HistoryNoSystemTxs integrity check  
  <sub>2025-08-25 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16801`](https://github.com/erigontech/erigon/pull/16801) — faster HistoryNoSystemTxs integrity check  
  <sub>2025-08-25 · closed · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16701`](https://github.com/erigontech/erigon/pull/16701) — cp: reuse already prepared heimdall store in integrity check (#16634)  
  <sub>2025-08-18 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16634`](https://github.com/erigontech/erigon/pull/16634) — reuse already prepared heimdall store in integrity check  
  <sub>2025-08-14 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16536`](https://github.com/erigontech/erigon/pull/16536) — add publishable to integrity checks  
  <sub>2025-08-11 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16535`](https://github.com/erigontech/erigon/pull/16535) — [r31] add publishable to integrity checks  
  <sub>2025-08-11 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16534`](https://github.com/erigontech/erigon/pull/16534) — add publishable to integrity checks  
  <sub>2025-08-11 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16468`](https://github.com/erigontech/erigon/pull/16468) — cp: remove milestones from integrity check  
  <sub>2025-08-06 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16453`](https://github.com/erigontech/erigon/pull/16453) — remove milestones from integrity check  
  <sub>2025-08-05 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16375`](https://github.com/erigontech/erigon/pull/16375) — cp: add HeaderNoGaps to integrity check  
  <sub>2025-07-30 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16319`](https://github.com/erigontech/erigon/pull/16319) — [r31] add HeaderNoGaps to integrity check  
  <sub>2025-07-28 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#16059`](https://github.com/erigontech/erigon/pull/16059) — throw error if integrity check name is wrong  
  <sub>2025-07-11 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#15964`](https://github.com/erigontech/erigon/pull/15964) — rcache integrity check  
  <sub>2025-07-07 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#15910`](https://github.com/erigontech/erigon/pull/15910) — Updated ETL framework documentation link in README.md  
  <sub>2025-07-02 · merged · reviewed · score 3 · etl </sub>
- [`erigontech/erigon#15711`](https://github.com/erigontech/erigon/pull/15711) — higher-level unit tests for dependency integrity checker  
  <sub>2025-06-23 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#15404`](https://github.com/erigontech/erigon/pull/15404) — Cherry-pick: Fix receipts dangling from reorged blocks (#15401)  
  <sub>2025-06-02 · merged · reviewed · score 3 · reorg</sub>
- [`erigontech/erigon#15401`](https://github.com/erigontech/erigon/pull/15401) — E3: Fix receipts dangling from reorged blocks  
  <sub>2025-06-02 · merged · reviewed · score 3 · reorg</sub>
- [`erigontech/erigon#15392`](https://github.com/erigontech/erigon/pull/15392) — [e30] integrity check: less ram use  
  <sub>2025-06-02 · merged · authored · score 3 · integrity check</sub>
- [`erigontech/erigon#15391`](https://github.com/erigontech/erigon/pull/15391) — integrity check: less ram use  
  <sub>2025-06-02 · merged · authored · score 3 · integrity check</sub>
- [`erigontech/erigon#15055`](https://github.com/erigontech/erigon/pull/15055) — drop integrity check of dirty files (we have good recalcVisiblFiles func)  
  <sub>2025-05-15 · merged · authored · score 3 · integrity check</sub>
- [`erigontech/erigon#14690`](https://github.com/erigontech/erigon/pull/14690) — kv.temporal: add method Unwind  
  <sub>2025-04-22 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#14587`](https://github.com/erigontech/erigon/pull/14587) — snap_repo integrity check  
  <sub>2025-04-14 · merged · reviewed · score 3 · integrity check</sub>
- [`erigontech/erigon#14311`](https://github.com/erigontech/erigon/pull/14311) — sd: add `aggTx.Unwind` method  
  <sub>2025-03-27 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#14048`](https://github.com/erigontech/erigon/pull/14048) — added `MAX_REORG_DEPTH=512` env variable  
  <sub>2025-03-04 · merged · authored · score 3 · reorg</sub>
- [`erigontech/erigon#12738`](https://github.com/erigontech/erigon/pull/12738) — Caplin: demote reorg log  
  <sub>2024-11-15 · merged · reviewed · score 3 · reorg</sub>
- [`erigontech/erigon#10958`](https://github.com/erigontech/erigon/pull/10958) — E3: Complete Diff-oriented unwind  
  <sub>2024-07-01 · closed · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#10925`](https://github.com/erigontech/erigon/pull/10925) — unwind possibility check: simplify   
  <sub>2024-06-27 · merged · authored+reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#10903`](https://github.com/erigontech/erigon/pull/10903) — E3: Added automatic bounded unwind  
  <sub>2024-06-25 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#10824`](https://github.com/erigontech/erigon/pull/10824) — E3: No-gaps for UnwindTo minimum  
  <sub>2024-06-20 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#10807`](https://github.com/erigontech/erigon/pull/10807) — E3: Added unwind check  
  <sub>2024-06-19 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#10777`](https://github.com/erigontech/erigon/pull/10777) — allow run single integrity checker  
  <sub>2024-06-17 · merged · authored · score 3 · integrity check</sub>
- [`erigontech/erigon#10696`](https://github.com/erigontech/erigon/pull/10696) — Fixed bugs that made reorg unusable in some situations  
  <sub>2024-06-10 · merged · reviewed · score 3 · reorg</sub>
- [`erigontech/erigon#10619`](https://github.com/erigontech/erigon/pull/10619) — don't allow unwind behind files  
  <sub>2024-06-05 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#10586`](https://github.com/erigontech/erigon/pull/10586) — E35: Added changesets based unwinds  
  <sub>2024-06-01 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#10302`](https://github.com/erigontech/erigon/pull/10302) — close unwind cursors  
  <sub>2024-05-13 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#10186`](https://github.com/erigontech/erigon/pull/10186) — Fixed unwind cursor leak in E35  
  <sub>2024-05-02 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#9995`](https://github.com/erigontech/erigon/pull/9995) — [wip] e35: keep 1 step in db (for unwinds)  
  <sub>2024-04-19 · closed · authored · score 3 · unwind</sub>
- [`erigontech/erigon#9930`](https://github.com/erigontech/erigon/pull/9930) — e3 etl collate history  
  <sub>2024-04-12 · merged · reviewed · score 3 · etl </sub>
- [`erigontech/erigon#9140`](https://github.com/erigontech/erigon/pull/9140) — e35: fix "too far unwind"   
  <sub>2024-01-05 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#8919`](https://github.com/erigontech/erigon/pull/8919) — e35: remove unwind `limit` param  
  <sub>2023-12-07 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#8837`](https://github.com/erigontech/erigon/pull/8837) — e35: `CanUnwindBeforeBlockNum` to return min allowed blockNum in case of error  
  <sub>2023-11-27 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#7759`](https://github.com/erigontech/erigon/pull/7759) — e3: unwind simplify  
  <sub>2023-06-19 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#7758`](https://github.com/erigontech/erigon/pull/7758) — e3: simplify unwind  
  <sub>2023-06-19 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#7416`](https://github.com/erigontech/erigon/pull/7416) — e3: dont fetch code hash in unwind  
  <sub>2023-05-01 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#6331`](https://github.com/erigontech/erigon/pull/6331) — Reorganization the devnet subscription services  
  <sub>2022-12-15 · merged · reviewed · score 3 · reorg</sub>
- [`erigontech/erigon#6147`](https://github.com/erigontech/erigon/pull/6147) — E3: fix unwind changes visibility  
  <sub>2022-11-29 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#5988`](https://github.com/erigontech/erigon/pull/5988) — e3: integration support unwind loop  
  <sub>2022-11-07 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#5981`](https://github.com/erigontech/erigon/pull/5981) — e3: accumulator nil on unwind  
  <sub>2022-11-07 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#5947`](https://github.com/erigontech/erigon/pull/5947) — e3: fix retainList on unwind  
  <sub>2022-11-03 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#5742`](https://github.com/erigontech/erigon/pull/5742) — e3: write history and indices to etl   
  <sub>2022-10-14 · merged · authored · score 3 · etl </sub>
- [`erigontech/erigon#5090`](https://github.com/erigontech/erigon/pull/5090) — erigon22: unwind code  
  <sub>2022-08-17 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#5058`](https://github.com/erigontech/erigon/pull/5058) — erigon22: unwind code  
  <sub>2022-08-15 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#5039`](https://github.com/erigontech/erigon/pull/5039) — Aggregator22.Unwind()  
  <sub>2022-08-13 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#4529`](https://github.com/erigontech/erigon/pull/4529) — Delete bad blocks on unwind  
  <sub>2022-06-24 · merged · reviewed · score 3 · unwind</sub>
- [`erigontech/erigon#3768`](https://github.com/erigontech/erigon/pull/3768) — integration unwind sender  
  <sub>2022-03-25 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#3767`](https://github.com/erigontech/erigon/pull/3767) — integration_unwind_sender  
  <sub>2022-03-25 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#3763`](https://github.com/erigontech/erigon/pull/3763) — fix integration unwind nil pointer  
  <sub>2022-03-24 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#3322`](https://github.com/erigontech/erigon/pull/3322) — etl less allocs  
  <sub>2022-01-22 · merged · authored · score 3 · etl </sub>
- [`erigontech/erigon#2481`](https://github.com/erigontech/erigon/pull/2481) — etl call traces  
  <sub>2021-08-02 · merged · authored · score 3 · etl </sub>
- [`erigontech/erigon#2439`](https://github.com/erigontech/erigon/pull/2439) — Sokol v0: unwind support  
  <sub>2021-07-24 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#2395`](https://github.com/erigontech/erigon/pull/2395) — Make UnwindOrder variable non-inverted  
  <sub>2021-07-18 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#2388`](https://github.com/erigontech/erigon/pull/2388) — Remove "persistent unwind" concept  
  <sub>2021-07-17 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#1688`](https://github.com/erigontech/erigon/pull/1688) — delete tds.unwindTo method  
  <sub>2021-04-08 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#1494`](https://github.com/erigontech/erigon/pull/1494) — blocks exec unwind - to support graceful shutdown  
  <sub>2021-02-13 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#1068`](https://github.com/erigontech/erigon/pull/1068) — add unwind_to cmd  
  <sub>2020-09-07 · closed · authored · score 3 · unwind</sub>
- [`erigontech/erigon#972`](https://github.com/erigontech/erigon/pull/972) — After reboot unwind stack has wrong order  
  <sub>2020-08-24 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#890`](https://github.com/erigontech/erigon/pull/890) — integration: clear unwind stack command (hack)  
  <sub>2020-08-09 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#757`](https://github.com/erigontech/erigon/pull/757) — Remove load start key from etl  
  <sub>2020-07-18 · merged · authored · score 3 · etl </sub>
- [`ledgerwatch/erigon-lib#1027`](https://github.com/ledgerwatch/erigon-lib/pull/1027) — e3: simplify unwind  
  <sub>2023-06-19 · merged · authored · score 3 · unwind</sub>
- [`ledgerwatch/erigon-lib#1026`](https://github.com/ledgerwatch/erigon-lib/pull/1026) — e3: simplify unwind  
  <sub>2023-06-19 · merged · authored · score 3 · unwind</sub>
- [`ledgerwatch/erigon-lib#683`](https://github.com/ledgerwatch/erigon-lib/pull/683) — e3: write history and indices to etl   
  <sub>2022-10-14 · merged · authored · score 3 · etl </sub>
- [`ledgerwatch/erigon-lib#591`](https://github.com/ledgerwatch/erigon-lib/pull/591) — erigon22: unwind code  
  <sub>2022-08-17 · merged · authored · score 3 · unwind</sub>
- [`ledgerwatch/erigon-lib#587`](https://github.com/ledgerwatch/erigon-lib/pull/587) — erigon22: unwind code   
  <sub>2022-08-15 · merged · authored · score 3 · unwind</sub>
- [`ledgerwatch/erigon-lib#584`](https://github.com/ledgerwatch/erigon-lib/pull/584) — Aggregator22.Unwind()  
  <sub>2022-08-13 · merged · authored · score 3 · unwind</sub>
- [`ledgerwatch/erigon-lib#463`](https://github.com/ledgerwatch/erigon-lib/pull/463) — a bit more docs to etl  
  <sub>2022-05-24 · merged · authored · score 3 · etl </sub>
- [`ledgerwatch/erigon-lib#263`](https://github.com/ledgerwatch/erigon-lib/pull/263) — Etl less allocs  
  <sub>2022-01-22 · merged · authored · score 3 · etl </sub>
- [`ledgerwatch/erigon-lib#147`](https://github.com/ledgerwatch/erigon-lib/pull/147) — ETL file names revert  
  <sub>2021-11-06 · merged · authored · score 3 · etl </sub>
- [`ledgerwatch/erigon-lib#15`](https://github.com/ledgerwatch/erigon-lib/pull/15) — Pool: add onNewTxs method, mined txs must be removed before add unwinded  
  <sub>2021-08-05 · merged · authored · score 3 · unwind</sub>
- [`ledgerwatch/erigon-lib#14`](https://github.com/ledgerwatch/erigon-lib/pull/14) — Pool: handle more p2p message, pool object, more invariants, single method for unwind+forward    
  <sub>2021-08-03 · merged · authored · score 3 · unwind</sub>
- [`ledgerwatch/erigon-lib#13`](https://github.com/ledgerwatch/erigon-lib/pull/13) — Pool: basic OnNewBlock and Unwind functions  
  <sub>2021-08-01 · merged · authored · score 3 · unwind</sub>
- [`erigontech/erigon#18997`](https://github.com/erigontech/erigon/pull/18997) — integration stage_exec: call Prune  
  <sub>2026-02-06 · merged · authored · score 2 · prune, stage</sub>
- [`erigontech/erigon#15225`](https://github.com/erigontech/erigon/pull/15225) — [e30] stage_custom_trace: more aggressive prune  
  <sub>2025-05-23 · merged · authored · score 2 · prune, stage</sub>
- [`erigontech/erigon#15224`](https://github.com/erigontech/erigon/pull/15224) — stage_custom_trace: more aggressive prune  
  <sub>2025-05-23 · merged · authored · score 2 · prune, stage</sub>
- [`erigontech/erigon#10848`](https://github.com/erigontech/erigon/pull/10848) — add pruneNothing checker and fix endless pruning on Amoy  
  <sub>2024-06-21 · merged · reviewed · score 2 · prune, pruning</sub>
- [`erigontech/erigon#10258`](https://github.com/erigontech/erigon/pull/10258) — e3: reduce prune collector size - to allow background sort  
  <sub>2024-05-09 · merged · authored · score 2 · collector, prune</sub>
- [`erigontech/erigon#9902`](https://github.com/erigontech/erigon/pull/9902) — Chore: improve comments and readability with stageloop prune  
  <sub>2024-04-10 · merged · reviewed · score 2 · prune, stage</sub>
- [`erigontech/erigon#7643`](https://github.com/erigontech/erigon/pull/7643) — prune speedup. stage_senders: don't re-calc existing senders  
  <sub>2023-06-03 · merged · authored · score 2 · prune, stage</sub>
- [`erigontech/erigon#2913`](https://github.com/erigontech/erigon/pull/2913) — dont_apply_prune_migration_on_start  
  <sub>2021-11-04 · merged · authored · score 2 · migration, prune</sub>
- [`erigontech/erigon#2393`](https://github.com/erigontech/erigon/pull/2393) — Pruning stages order support  
  <sub>2021-07-18 · merged · authored · score 2 · pruning, stage</sub>
- [`erigontech/erigon#2385`](https://github.com/erigontech/erigon/pull/2385) — add pruning stage concept, but not enable yet  
  <sub>2021-07-17 · merged · authored · score 2 · pruning, stage</sub>
- [`erigontech/erigon#1257`](https://github.com/erigontech/erigon/pull/1257) — Migration idempotency: handle corner-cases of CriticalCollector  
  <sub>2020-10-19 · merged · authored+reviewed · score 2 · collector, migration</sub>
- [`erigontech/erigon#868`](https://github.com/erigontech/erigon/pull/868) — Migrations: use stage name as db key  
  <sub>2020-08-05 · merged · authored · score 2 · migration, stage</sub>

## On-disk / DB format & migration  (7)

- [`erigontech/erigon#4732`](https://github.com/erigontech/erigon/pull/4732) — db migration fix: it was able run with delay  
  <sub>2022-07-18 · merged · authored · score 4 · db migration, migration</sub>
- [`erigontech/erigon#4389`](https://github.com/erigontech/erigon/pull/4389) — db migration to reset blocks   
  <sub>2022-06-07 · merged · authored · score 4 · db migration, migration</sub>
- [`erigontech/erigon#11448`](https://github.com/erigontech/erigon/pull/11448) — E3: Better backward compatibility for evergreen (fixes headerdownload case)  
  <sub>2024-08-01 · merged · reviewed · score 3 · backward compat</sub>
- [`erigontech/erigon#10077`](https://github.com/erigontech/erigon/pull/10077) — Revert "backward compatibility of .lock" and Backward compatibility by Giulio  
  <sub>2024-04-26 · merged · reviewed · score 3 · backward compat</sub>
- [`erigontech/erigon#10006`](https://github.com/erigontech/erigon/pull/10006) — backward compatibility of .lock  
  <sub>2024-04-20 · merged · authored+reviewed · score 3 · backward compat</sub>
- [`erigontech/erigon#4702`](https://github.com/erigontech/erigon/pull/4702) — backward compatibility: use default UID=1000 GID=1000  
  <sub>2022-07-13 · merged · authored · score 3 · backward compat</sub>
- [`erigontech/erigon#4701`](https://github.com/erigontech/erigon/pull/4701) — backward compatibility: use default UID=1000 GID=1000  
  <sub>2022-07-13 · closed · authored · score 3 · backward compat</sub>
