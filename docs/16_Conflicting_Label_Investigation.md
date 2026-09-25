# 16. Conflicting-Label Investigation

**Status:** Phase 3B complete (September 2026)  
**Notebook:** [`15_conflicting_label_investigation.ipynb`](../notebooks/15_conflicting_label_investigation.ipynb)  
**Artifact:** [`conflicting_label_investigation.json`](../notebooks/evaluation/conflicting_label_investigation.json)

## Objective

Identify feature-identical records (same 30 feature values) with differing `Result` labels, quantify their prevalence, and evaluate sensitivity to excluding such groups without rewriting the canonical labels.

## Findings

| Measure | Result |
|---|---:|
| Dataset rows | 11,055 |
| Unique feature groups | 5,785 |
| Feature duplicate groups | 2,614 |
| Conflicting-label groups | 64 |
| Rows in conflicting groups | 357 (3.2293%) |
| Conflicting-group rate among feature groups | 1.1063% |
| Maximum feature-group size | 25 |

The canonical target distribution is 4,898 raw `-1` labels and 6,157 raw `+1` labels. The investigation found conflicts among feature-identical rows; it does not establish why those labels differ, which label is authoritative, or whether a particular record is mislabeled.

## Evaluation sensitivity

The artifact records a group-aware all-data experiment and a sensitivity experiment excluding the 357 rows in conflicting groups. The exclusion sensitivity run reported F1 0.980392 and accuracy 0.978221 on its own reduced evaluation population. These figures are not directly interchangeable with the later frozen primary benchmark because the population and split protocol differ.

The later frozen Protocol C sensitivity uses 10,698 available rows and reports F1 0.965248 and accuracy 0.962121. See [`17_Evaluation_Protocol_Freeze.md`](17_Evaluation_Protocol_Freeze.md) for the official protocol definitions and results.

## Decisions and safeguards

- Do not majority-vote, infer, or overwrite labels for conflicting groups without an external source of label authority or documented domain adjudication.
- Do not remove these records from the canonical dataset as a default cleaning step.
- Preserve the raw data and report conflicting groups as a distinct diagnostic.
- Exclusion is a sensitivity analysis only, not the official benchmark population.
- Any future label correction requires provenance, an explicit decision record, and a new versioned dataset artifact.

The investigation is not evidence of real-world SOC performance and does not determine the correct labels.
