# Security model and limitations

## Deterministic boundaries

All web and model calls run within the nondeterministic leader/validator functions. Storage writes occur only after consensus. Immutable policy and package JSON are canonicalized with sorted keys, ASCII escapes and compact separators. SHA-256 hashes use UTF-8. Duplicate keys are rejected. Request hashes cover the initial request record (attempts=0, without request_hash); decision hashes cover the receipt without decision_hash. Each receipt also binds the deployment address and previous hash.

Input validation constrains sources to a fixed public host and exact Git commits; blocks branch refs, query strings and traversal; bounds bytes, source count, checks, strings and retries. Host retrieval may itself allocate oversized responses before Python checks the committed size; this contract cannot impose a transport streaming limit through the SDK. No payments, secrets, external wallet integration, admin upgrades or privileged reset exist.

## Semantic consensus

Validators do not accept leader formatting alone. They fetch and hash evidence independently, run their own semantic assessment, compare binding/outcome/error/every check status, and reject leader quotations absent from independently retrieved text. Canonical, deterministic aggregation avoids model-authored top-level verdicts. Literal quotations support auditability but do not prove semantic correctness. Provenance/binding judgments remain model-based; validator disagreement can leave a transaction undetermined with no state change.

Prompt instructions explicitly treat policies, use descriptions and evidence as untrusted data, prohibit embedded commands and missing-permission assumptions, and restrict the task to technical policy matching. This reduces prompt injection exposure; it cannot guarantee immunity against adversarial text or correlated model errors. Offline tests verify prompt construction and fail-closed structural gates, not universal semantic injection resistance. Review adversarial evidence before operational reliance.

## Authentication and scope

TLS origin, full Git commit, byte length and SHA-256 bind exact public documents. They do NOT establish publisher authority, ownership, consent, license validity, completeness of provenance or legal enforceability. A malicious user can commit fabricated evidence or a permissive policy: the contract reports only relative to those visible commitments. Consumers must select trusted policy authors and repository origins themselves. The recorded owner is a wallet identity, not a verified person/organization. No claim of privacy safety or lawfulness should be inferred from ALLOWED.

Policies and requests are public and append-only. Do not submit personal data, credentials, confidential terms or nonpublic datasets. Submitter-only review avoids third parties burning retries. There is no global request slot limit; spam costs/resources remain a network concern. Transient fetch/model failures become INCONCLUSIVE only if validators agree on the exact failure; persistent disagreement remains a failed/undetermined network transaction. A successful application receipt still needs protocol finality. No contract-local challenge window is asserted.

## Disclosure

Report reproducible issues through a GitHub issue without disclosing secrets. This is unaudited builder software and a Studio demonstration, not production legal infrastructure.
