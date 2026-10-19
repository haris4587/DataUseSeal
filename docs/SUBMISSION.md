# GenLayer Intelligent Contracts submission

**Contribution type:** Builder → Intelligent Contracts

**Title:** DataUseSeal — Consensus Verification of Dataset Usage Policies

**One-line description:** Verifies proposed dataset uses against locked technical policies using independently checked, version-bound evidence and GenLayer consensus.

**Notes / Description (under 1000 characters):**

DataUseSeal is a standalone GenLayer Intelligent Contract for checking proposed dataset uses against locked usage policies. Validators independently fetch commit-pinned dataset, terms and provenance evidence, verify HTTP success, byte lengths and SHA-256 hashes, then assess every policy requirement. Consensus compares evidence binding and each check status; citations are checked against authenticated text. Deterministic rules return ALLOWED, RESTRICTED, POLICY_VIOLATION or INCONCLUSIVE. Policies and use packages are immutable, reviews are submitter-authorized, retries are bounded, and receipts preserve append-only history with decision hashes. The finalized Studio Full Consensus demo identifies prohibited commercial resale while accepting required attribution. Includes 37 passing offline tests, GenVM lint/SDK validation and byte-identical deployed/GitHub source verification. This checks technical policy compliance, not legal rights, privacy safety or actual runtime behavior.

**Repository:** https://github.com/haris4587/DataUseSeal

See [EVIDENCE.md](EVIDENCE.md) for the exact contract, transaction, source-commit and SHA-256 records, and all public evidence links. The final documentation commit is available through the repository main-branch history; the deployed source is fixed at commit 3518971e03d636499a97158d8e330eb95552fe27.
