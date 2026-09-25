# 17. Evaluation Protocol Comparison and Freeze

**Status:** Phase 3C complete; primary protocol frozen (September 24, 2026)  
**Notebooks:** [`16_evaluation_protocol_comparison.ipynb`](../notebooks/16_evaluation_protocol_comparison.ipynb), [`17_evaluation_protocol_freeze.ipynb`](../notebooks/17_evaluation_protocol_freeze.ipynb)  
**Artifacts:** [`phase_3c_evaluation_protocol_comparison.json`](../notebooks/evaluation/phase_3c_evaluation_protocol_comparison.json), [`phase_3c_evaluation_protocol_comparison_freezed.json`](../notebooks/evaluation/phase_3c_evaluation_protocol_comparison_freezed.json)

> The artifact filename `freezed` is retained as committed. It is the official frozen result; the earlier comparison JSON is a historical artifact and remains unchanged.

## Dataset and fixed experiment configuration

- Dataset: `data/raw/phisingData.csv`; 11,055 rows × 31 columns; 30 features; target `Result`.
- SHA-256: `a4b16abbd8610e4f53fd63e8eb3da793157a961111ed5e9d9d8afa21af866995`.
- Target mapping: raw `-1 → 0`, `+1 → 1`.
- Test fraction: 0.20; random state: 42.
- Preprocessing: `KNNImputer(n_neighbors=3, weights="uniform")`.
- Estimator: `RandomForestClassifier(n_estimators=128, criterion="gini", bootstrap=True, max_depth=None, max_features="sqrt", random_state=42)`.

## Protocols and recorded outcomes

| Protocol | Role | Train / test | Shared feature groups | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|---:|---:|
| A — random row split | Historical baseline; leakage-permitting | 8,844 / 2,211 | 1,143 | 0.968340 | 0.964706 | 0.980080 | 0.972332 |
| B — deterministic feature-group-aware split | **Official primary frozen protocol** | 8,797 / 2,258 | 0 | 0.948184 | 0.964643 | 0.946456 | 0.955463 |
| C — group-aware, conflicting groups excluded | Sensitivity analysis only | 8,586 / 2,112 | 0 | 0.962121 | 0.967770 | 0.962738 | 0.965248 |
| D — group majority-derived labels | Not admissible as official benchmark | — | — | — | — | — | — |

Protocol A has 1,447 test rows with a duplicate in training (65.4455%). Its metrics are retained for historical context and are not the primary leakage-controlled result.

Protocol B confusion matrix: `[[886, 46], [71, 1255]]`. Protocol C confusion matrix: `[[921, 37], [43, 1111]]`.

## Canonical group identity and repeatability

Protocol B creates a complete feature tuple for each row, sorts the unique tuples lexicographically, and maps them to contiguous integer group IDs. This defines a stable encoding for the group relation before applying the seeded group-aware split.

Two repeated runs produced identical train and test membership, metrics, and zero train/test feature-group overlap. Membership fingerprints:

- Train: `8ce409452de18f284e44c132f3628b4b929af2a5967b64d4da5ab1115a191760`
- Test: `1189855d6296ad48d606e2fa10edc50f24d765ee77d3c38969f487d60b59bc35`

Different valid encodings or orderings of group IDs can produce different seeded `GroupShuffleSplit` partitions. Therefore the group-ID construction is part of the frozen protocol, not an interchangeable implementation detail.

## Decision record

1. **Primary:** Protocol B, deterministic feature-group-aware split.
2. **Historical:** Protocol A, random-row split, explicitly identified as leakage-permitting.
3. **Sensitivity:** Protocol C, conflicting groups excluded; the canonical dataset remains unchanged.
4. **Rejected for official use:** Protocol D, because deriving majority labels would rewrite ground truth without external label authority.
5. Production code and canonical dataset were not modified by the freeze experiment.

## Interpretation limits

These are benchmark results on the UCI Phishing Websites tabular dataset. They are not measurements of live network traffic, SOC alert triage, or production incident response. The protocol freeze establishes a reproducible evaluation design; it does not establish deployment readiness or real-world generalization.
