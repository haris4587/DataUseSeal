"""Recompute public artifact commitments; does not query live chain state."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)
def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()
def read(name):
    return json.loads((root / 'evidence' / name).read_text())

receipt = read('finalized-result.json')
claimed = receipt.pop('decision_hash')
assert digest(canonical(receipt)) == claimed, 'decision hash mismatch'
request = read('finalized-request.json')
request['attempts'] = 0
request_hash = request.pop('request_hash')
assert digest(canonical(request)) == request_hash == receipt['request_hash'], 'request hash mismatch'
policy = read('finalized-policy.json')
assert digest(canonical(policy['policy'])) == policy['policy_hash'] == receipt['policy_hash'], 'policy hash mismatch'
assert request['package'] == json.loads((root / 'examples/live-package.json').read_text())
for s in request['package']['sources']:
    body = (root / 'examples' / (s['role'] + '.txt')).read_bytes()
    assert len(body) == s['bytes'] and hashlib.sha256(body).hexdigest() == s['sha256']
source = (root / 'contracts/data_use_seal.py').read_bytes()
deployed = (root / 'evidence/deployed-source.py').read_bytes()
assert source == deployed, 'deployed source mismatch'
assert hashlib.sha256(source).hexdigest() == read('source-verification.json')['source_sha256']
assert receipt['result']['outcome'] == 'POLICY_VIOLATION'
assert [c['status'] for c in receipt['result']['checks']] == ['FAIL', 'PASS']
print('PASS: deployed source, policy, request, evidence bytes and decision hash verified.')
