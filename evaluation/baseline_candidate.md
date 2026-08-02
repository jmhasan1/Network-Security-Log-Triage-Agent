# Baseline Candidate Report

**Project:** Network Security Log Triage Agent

**Stage:** Baseline Candidate (Pre-Version 1)

**Date:** YYYY-MM-DD

---

# Purpose

This report documents the initial Machine Learning baseline before major improvements to the training pipeline.

The objective is to establish a reproducible reference point that future preprocessing, feature engineering, model selection, and evaluation improvements can be compared against.

This model should **not** be considered Version 1.0.

---

# Dataset

Dataset Name:
Network Security Phishing Dataset

Task:
Binary Classification

Target:

Result

Classes:

- Phishing
- Legitimate

Current Dataset Version:

Baseline Dataset

---

# Data Pipeline

MongoDB

↓

Data Validation

↓

KS-Test Drift Detection

↓

KNN Imputer

↓

StandardScaler

↓

Train/Test Split

↓

Random Forest

---

# Model

Algorithm:

Random Forest Classifier

Training Method:

GridSearchCV

Framework:

scikit-learn

---

# Performance

| Metric | Train | Test |
|---------|------:|------:|
| Precision | 0.9883 | 0.9862 |
| Recall | 0.9927 | 0.9927 |
| F1 Score | 0.9905 | 0.9894 |

---

# Missing Evaluation

The following metrics have not yet been incorporated.

- Accuracy
- ROC-AUC
- PR-AUC
- MCC
- Balanced Accuracy
- Confusion Matrix

These will be added during Version 1 development.

---

# MLflow

Experiment Tracking:

Enabled

Current Logged Information:

- Precision
- Recall
- F1
- Parameters

Planned Improvements:

- Training Time
- Inference Time
- Dataset Size
- Git Commit
- Python Version
- Feature Count
- Confusion Matrix
- ROC Curve

---

# Current Strengths

✓ Stable pipeline

✓ Good generalization

✓ Modular architecture

✓ MLflow integration

✓ Drift detection

✓ FastAPI deployment

---

# Current Weaknesses

- Limited evaluation metrics

- Classical models only

- GridSearchCV only

- No explainability

- No benchmark framework

- No Optuna

- No error analysis

---

# Planned Improvements

Phase 2.1

Data Validation

- Better schema validation
- Duplicate detection
- Class distribution report

---

Phase 2.2

Data Transformation

- Compare imputers
- Compare scalers
- Feature selection

---

Phase 2.3

Model Training

- XGBoost
- LightGBM
- CatBoost
- Optuna

---

Phase 2.4

Evaluation

- ROC-AUC
- MCC
- Explainability
- Confusion Matrix
- Error Analysis

---

# Version Status

Current Version:

Baseline Candidate (v0.9)

Next Milestone:

Version 1.0 Benchmark

Status:

In Progress

---

# Notes

This report serves as the reference point for future experiments.

Every future preprocessing change, feature engineering improvement, model selection decision, and evaluation enhancement should be compared against this baseline before being adopted into Version 1.0.