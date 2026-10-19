# Verified submission evidence

## Final contract

- Network: GenLayer Studio / StudioNet sandbox, not mainnet.
- Contract: [0xD6Ef423eE56d9d50F43F3570DD6ACCFe05A3ED67](https://explorer-studio.genlayer.com/address/0xD6Ef423eE56d9d50F43F3570DD6ACCFe05A3ED67).
- Built-in Studio account: `0x0a6a54B9e0fd10eD8E258a5955b26710f58D389f`. No external wallet.
- [Deployment transaction](https://explorer-studio.genlayer.com/tx/0xe477ea67ff200444e5362595b222ea7bf9c87a35fa8998bb73316028b4b4f082): FINALIZED, SUCCESS.
- [Policy transaction](https://explorer-studio.genlayer.com/tx/0x3052ca4d8956992a517aff294bb38c3344a8f692735b056d8250a24f94eb65e9): FINALIZED, SUCCESS; policy ID `0`.
- [Use-package transaction](https://explorer-studio.genlayer.com/tx/0xad1dc3150a8aec478757a3bba8304ea552db717c7184e704e52080bbcbaa8a98): FINALIZED, SUCCESS; request ID `0`.
- [Full Consensus review](https://explorer-studio.genlayer.com/tx/0xb1cf7327c6d367ee78f6b40831a5f49aed5521bb9d71965a2e331e8bec33c84e): FINALIZED, GenVM SUCCESS, consensus Accepted, Normal execution, 5 initial validators, 0 leader rotations. Explorer displays 3 agree votes (including leader) and 2 idle; this is majority agreement, not a claim that all five executed successfully.

## Meaningful semantic test

Synthetic Grid v1 terms permit internal academic benchmarking and explicitly prohibit commercial redistribution of raw data. Proposed use sells and redistributes raw data commercially, while including the required attribution for publishing aggregate benchmark results. Authenticated evidence has three roles and is pinned at [fixture commit 4ba139b](https://github.com/haris4587/DataUseSeal/tree/4ba139b88c868630ae33c36e4100f3309d66eff7/examples).

Finalized `get_result("0", 0)` returns binding VERIFIED, PURPOSE FAIL, ATTRIBUTION PASS, outcome **POLICY_VIOLATION**. Literal source/use quotations and reasons are preserved in [finalized-result.json](../evidence/finalized-result.json). The actual finalized policy and request are preserved alongside it.

Decision SHA-256: `edecd869878e06ed31b94d6f4fb0792caf9d07ff37b6b4a2567bd6b9bb6fb372`.
Request SHA-256: `d0d7f5d93dfa8b71adfc20258a7a8d68ff40c1593452ba887a0562c16da0978f`.
Policy SHA-256: `1b351144c0cdd8af0e86ee6a61b70dbdba2016eef1634f6ec7254a092c84f864`.

## Source and reproducibility

Exact deployed source commit: [3518971e03d636499a97158d8e330eb95552fe27](https://github.com/haris4587/DataUseSeal/commit/3518971e03d636499a97158d8e330eb95552fe27).
Source SHA-256: `df9c0178e22fc3208da3dc420d99181ce09caceda25524f2f6e7aa966b7f6ff2` (12,111 bytes).
Explorer-rendered deployed source was saved as [deployed-source.py](../evidence/deployed-source.py) and compared byte-for-byte with the committed contract. [source-verification.json](../evidence/source-verification.json) records equality. Later commits contain evidence/docs only; the source commit identifies the deployed implementation.

- [37 offline tests passed](../evidence/offline-tests.txt), using host doubles; not real GenVM consensus.
- [GenVM lint and exact SDK validation passed](../evidence/genvm-check.json): 3 lint checks; 7 public methods (4 view, 3 write), no constructor parameters; pinned v0.2.16.
- [Finalized consensus overview](../evidence/full-consensus-overview.txt), [votes](../evidence/full-consensus-votes.txt), [screenshot](../evidence/full-consensus-finalized.jpg).
- Run `python evidence/verify.py`: recomputes policy/request/decision hashes, evidence lengths/hashes and deployed source equality. [Output](../evidence/verification-results.txt).

## Transparent correction history

The initial deployment `0xDE2988D6Dc634f2018921Bf0C4462feE2a8571d9` used source commit 4ba139b. Its review [0x8a898ff7...](https://explorer-studio.genlayer.com/tx/0x8a898ff78656b79ff669782db8373c32a2c4112d48f5a4468b544d107326fc6e) returned INCONCLUSIVE after conflating noncompliant use with identity/provenance conflict. The prompt was corrected to distinguish evidence identity from usage compliance, retested, and deployed to the final address above. This initial result is not claimed as the successful final demo.

An initial malformed JSON input [0x3839af26...](https://explorer-studio.genlayer.com/tx/0x3839af26c0658469354d646e02e3c2eec2e1b33eb6d161423715360c1721766e) on the superseded deployment finalized with GenVM ERROR; corrected JSON was then submitted successfully. A transaction's consensus Accepted status alone is not evidence of successful contract execution.
