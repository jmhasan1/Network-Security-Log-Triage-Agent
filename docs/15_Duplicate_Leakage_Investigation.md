# 15. Duplicate and Evaluation Leakage Investigation

**Status:** Phase 3A complete (September 2026)  
**Notebook:** [`14_duplicate_leakage_experiment.ipynb`](../notebooks/14_duplicate_leakage_experiment.ipynb)  
**Artifact:** [`duplicate_leakage_baseline.json`](../notebooks/evaluation/duplicate_leakage_baseline.json)

## Purpose

Measure how exact duplicate records and repeated feature vectors cross a conventional random row split, and quantify how that overlap can affect evaluation. This was a notebook experiment; it did not modify production code or the canonical dataset.

## Dataset and terminology

Canonical input: `data/raw/phisingData.csv`, 11,055 rows × 31 columns, 30 feature columns and target `Result`. SHA-256: `a4b16abbd8610e4f53fd63e8eb3da793157a961111ed5e9d9d8afa21af866995`.

Do not conflate these different counts:

- **Excess exact full-row duplicate occurrences:** 5,206 (11,055 rows minus 5,849 unique complete rows).
- **Rows participating in full-row duplicate groups:** 7,843, as calculated across all 31 columns in the Phase 3 comparison.
- **Feature duplicate groups:** 2,614 groups with repeated values across the 30 feature columns; maximum group size 25.
- **Conflicting-label feature groups:** 64 of those feature groups have more than one target label. These are examined separately in Phase 3B.

An earlier experiment JSON contains a `feature_duplicate_rows` field of 5,270 reflecting that experiment's specific counting convention. Do not treat it as interchangeable with the later, explicitly defined 7,884 rows participating in duplicate feature groups in the frozen protocol artifact.

## Random-row baseline

The baseline used an 80/20 non-stratified random row split (`random_state=42`): 8,844 training rows and 2,211 test rows.

- Shared feature groups across train and test: 1,143.
- Test rows with a duplicate in training: 1,447 (65.4455% of test rows).
- Accuracy: 0.968340.
- Precision: 0.964706.
- Recall: 0.980080.
- F1: 0.972332.
- Confusion matrix: `[[911, 45], [25, 1230]]`.

The random-row metrics are retained as a historical baseline. The high duplicate overlap means these results should not be interpreted as a duplicate-leakage-controlled estimate of generalization to unseen feature groups.

## Initial group split

The initial `GroupShuffleSplit` experiment assigned complete feature groups to one partition and reported zero shared groups, with 8,751 training and 2,304 test rows. Its F1 was 0.952774 and accuracy 0.945313. This is a historical Phase 3A result; Phase 3C later froze a canonical group-ID construction and protocol, so this initial partition is not the official frozen split.

## Decisions

1. Keep random-row results for historical comparison, with the leakage caveat.
2. Use a feature-group-aware split for the primary benchmark; see the Phase 3C freeze document.
3. Preserve the canonical dataset. Duplicate presence alone is not grounds for deleting records.
4. Keep duplicate diagnostics distinct from data validation decisions and from label adjudication.
