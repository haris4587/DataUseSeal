# Deployment

Runtime: GenVM v0.2.16; dependency hash is embedded in the first two source lines and matches the current Studio template. Constructor has no arguments. Use GenLayer Studio's built-in account; no MetaMask or external wallet is required.

1. Run offline tests and `genvm-lint check contracts/data_use_seal.py --json`.
2. Push source and synthetic fixtures. Build the package from commit-pinned fixture URLs and exact byte/SHA-256 values.
3. Load the exact source into Studio. Deploy, wait for finalized successful execution, and record the deployment transaction/address.
4. Call lock_policy, then submit_use for its returned ID. Select Full Consensus for review, not leader-only execution.
5. Wait for FINALIZED and successful GenVM/consensus results; read get_request/get_result and verify hashes.
6. Compare deployed source bytes with the committed source and publish receipts, result, hashes and verification evidence. StudioNet results must not be represented as production/mainnet outcomes.

The final live record is maintained in EVIDENCE.md; absent values mean unverified, not successful.
