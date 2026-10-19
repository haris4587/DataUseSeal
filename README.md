# DataUseSeal

A standalone GenLayer Intelligent Contract that compares a proposed dataset use with a locked technical data-usage policy. It is not a legal/privacy ruling, ownership certification, data audit, or proof that the proposed implementation actually runs as described.

## Workflow

1. `lock_policy(policy_json)` permanently records 1–6 named requirements. Anyone can define a policy; the recorded wallet is its author, not a verified data controller.
2. `submit_use(policy_id, package_json)` permanently commits a dataset/release identity, proposed-use description, and three sources in order: dataset, terms, provenance.
3. The submitter calls `review(request_id)`. Every validator independently retrieves all three documents and verifies HTTP 2xx, exact byte length, SHA-256, and UTF-8 before independent semantic assessment.
4. Consensus requires identical dataset binding and every check status. A validator also validates the leader's schema and literal quotations against its independently retrieved documents; different reasoning/quote selection is permitted.
5. `get_result(request_id, attempt)` provides an append-only receipt, request/policy hashes, previous decision hash, contract address, and SHA-256 decision hash. Read at the network's finalized state, not merely accepted state.

| Outcome | Deterministic rule |
|---|---|
| ALLOWED | Binding VERIFIED; every check PASS |
| RESTRICTED | Binding VERIFIED; at least one unmet CONDITION, no FAIL/UNKNOWN |
| POLICY_VIOLATION | Binding VERIFIED; at least one FAIL (including alongside UNKNOWN) |
| INCONCLUSIVE | Binding unknown/conflicting, retrieval/model failure, or UNKNOWN without FAIL |

A clear prohibition is FAIL; a missing prerequisite for an otherwise permitted use is CONDITION. Unknown identity/provenance overrides all check results. No conclusive result can be overwritten. Inconclusive reviews may retry the exact package at most twice; all three attempts remain available. A corrected package is a new request. Other users cannot occupy a shared candidate slot or consume another request's attempts.

## Evidence format

Use `examples/policy.json`. Package fields: `dataset_id`, `release`, `proposed_use`, `sources`. Each source contains `role`, `url`, `sha256` (64 lower-case hex), `bytes`. Only `https://raw.githubusercontent.com/OWNER/REPO/FULL_40_HEX_COMMIT/PATH` is accepted. No mutable branch refs, query strings, custom hosts, credentials or traversal. Hashes authenticate committed bytes, not the authority or truthfulness of their publisher. Use a trusted repository and independently check its author and applicability.

Per document ≤16,000 bytes; total ≤32,000; proposed use ≤6,000; package JSON ≤16,000. Documents are public UTF-8 text only, not entire datasets. Large datasets should use a versioned authenticated release manifest. The contract does not download or audit every row.

## Reproduce

Python 3.12+ and `genvm-linter==0.11.0`:

```sh
python -m unittest discover -s tests -v
genvm-lint check contracts/data_use_seal.py --json
sha256sum contracts/data_use_seal.py
```

The 37 offline tests use explicit host doubles to exercise actual contract methods, leader/validator comparisons, malformed outputs, malicious leader decisions/citations, evidence tampering, authorization, retries, immutable state and hashes. They are not real GenVM/LLM consensus tests. GenVM lint plus SDK validation separately checks the pinned v0.2.16 runner. See [deployment](docs/DEPLOYMENT.md), [security](docs/SECURITY.md), and [evidence](docs/EVIDENCE.md) for live verification.

## Official references (checked 2026-10-19)

- https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle — independent leader/validator assessments and `gl.vm.run_nondet_unsafe`.
- https://docs.genlayer.com/developers/intelligent-contracts/features/non-determinism — isolation of nondeterministic work.
- https://docs.genlayer.com/api-references/genlayer-linter — lint and exact SDK validation.
- https://sdk.genlayer.com/v0.1.3/_modules/genlayer/gl/nondet/web.html — `Response.status`/bytes API; confirmed against the actual v0.2.16 SDK and Studio runner. Some prose docs still illustrate `status_code`; that field is not used here.
