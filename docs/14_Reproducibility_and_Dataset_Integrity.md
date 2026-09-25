# 14. Reproducibility and Dataset Integrity

**Status:** Phase 2 complete (September 2026)  
**Scope:** Notebook-led reproducibility investigation; this document records experimental findings and does not claim that the full production pipeline is already end-to-end reproducible.

## Objective

Establish a repeatable experimental baseline for the canonical phishing dataset, record dataset identity, and verify repeatability of the row-level split and preprocessing steps before hardening the production pipeline.

## Canonical dataset

- Repository path: `data/raw/phisingData.csv` (a notebook copy is also kept under `notebooks/data/raw/`).
- SHA-256: `a4b16abbd8610e4f53fd63e8eb3da793157a961111ed5e9d9d8afa21af866995`
- Shape: 11,055 rows × 31 columns; 30 features and target `Result`.
- Raw target counts: `-1`: 4,898; `+1`: 6,157.
- Model target mapping used in experiments: `-1 → 0`, `+1 → 1`.

The root and notebook dataset copies were verified to have identical SHA-256 values. The dataset is the UCI Phishing Websites tabular dataset; it is not raw network traffic or live SOC telemetry.

## Experiment

Notebook: [`13_reproducibility_experiment.ipynb`](../notebooks/13_reproducibility_experiment.ipynb)  
Machine-readable result: [`reproducibility_baseline.json`](../notebooks/evaluation/reproducibility_baseline.json)

The recorded baseline used an 80/20 non-stratified row split with `random_state=42`:

| Partition | Rows |
|---|---:|
| Train | 8,844 |
| Test | 2,211 |

Two executions produced identical train and test membership fingerprints. The experiment also repeated KNN imputation (`KNNImputer`, `n_neighbors=3`, `weights="uniform"`) and verified identical transformed train/test outputs and fingerprints.

This confirms repeatability of the specified experiment in its recorded environment. It does not establish that a random row split is leakage-safe, that all pipeline stages are deterministic across all environments, or that the benchmark represents production SOC performance.

## Environment recorded in the artifact

Python 3.11.13, Windows 10 (AMD64), NumPy 2.4.6, pandas 2.3.3, scikit-learn 1.9.0. Consult the JSON artifact for fingerprints and exact recorded values.

## Engineering conclusions

1. Dataset fingerprints and split membership fingerprints should accompany benchmark results.
2. Reproducibility and evaluation validity are separate questions. The row split was repeatable but later Phase 3 analysis found substantial duplicate-group overlap.
3. Preserve historical results as immutable evidence; later protocols should be recorded as new artifacts rather than overwriting this baseline.
4. The production pipeline still requires subsequent hardening and end-to-end reproducibility checks in the roadmap.

## Related work

- Phase 3 duplicate investigation: [`15_Duplicate_Leakage_Investigation.md`](15_Duplicate_Leakage_Investigation.md)
- Phase 3 label conflicts: [`16_Conflicting_Label_Investigation.md`](16_Conflicting_Label_Investigation.md)
- Frozen evaluation protocol: [`17_Evaluation_Protocol_Freeze.md`](17_Evaluation_Protocol_Freeze.md)
