# Data Validation

The **Data Validation** component is the second stage of the Machine Learning pipeline.

Its primary responsibility is to verify that the ingested dataset satisfies the expected quality and structural requirements before it is used for feature engineering and model training.

By validating the dataset early in the pipeline, the project reduces the risk of training models on incomplete, inconsistent, or unexpected data.

The output of this stage is a **DataValidationArtifact**, which is consumed by the Data Transformation component.

---

# Purpose

The objective of Data Validation is to ensure that the dataset retrieved during Data Ingestion is suitable for Machine Learning.

The validation process confirms that:

- The dataset follows the expected schema.
- Required features are present.
- The dataset structure matches expectations.
- Data distribution has not significantly changed.
- Validation reports are generated for analysis.

Instead of allowing downstream components to discover data quality issues during preprocessing or training, validation identifies them immediately after ingestion.

---

# Responsibilities

The Data Validation component performs the following tasks:

- Read training and testing datasets
- Load the expected schema
- Validate dataset structure
- Detect dataset drift
- Generate validation reports
- Produce a DataValidationArtifact

---

# Inputs

The component receives:

## DataValidationConfig

Contains configuration information such as:

| Configuration | Description |
|--------------|-------------|
| Schema File | Expected dataset schema |
| Validation Report Path | Output validation report |
| Drift Report Path | Output drift report |
| Validation Status File | Validation status |

---

## DataIngestionArtifact

Provides the locations of datasets created during Data Ingestion.

| Artifact Field | Description |
|---------------|-------------|
| train_file_path | Training dataset |
| test_file_path | Testing dataset |
| feature_store_path | Complete raw dataset |

---

# Outputs

The component produces a **DataValidationArtifact**.

Typical outputs include:

| Artifact Field | Description |
|---------------|-------------|
| validation_status | Whether validation succeeded |
| valid_train_file_path | Validated training dataset |
| valid_test_file_path | Validated testing dataset |
| drift_report_path | Dataset drift report |

This artifact becomes the input for Data Transformation.

---

# Execution Flow

```text
Train.csv
      │
      ▼
Read Dataset
      │
      ▼
Load Schema
      │
      ▼
Schema Validation
      │
      ▼
Dataset Drift Detection
      │
      ▼
Generate Validation Reports
      │
      ▼
Create DataValidationArtifact
```

---

# Step-by-Step Workflow

## Step 1 — Read the Dataset

The component loads the training and testing datasets generated during Data Ingestion.

Both datasets are required because validation compares the statistical properties of training and testing data.

---

## Step 2 — Load Schema

The expected dataset structure is loaded from the project's schema file.

The schema defines:

- Expected columns
- Dataset structure

The validation process compares the actual dataset against this schema.

---

## Step 3 — Validate Dataset Structure

The current implementation performs schema validation by checking that the dataset structure matches the expected schema.

Current validation includes:

- Column count verification

If validation fails, the dataset is considered invalid.

> **Implementation Note:**  
> In the current implementation, schema validation primarily verifies the number of columns. Validation of column names, data types, missing required columns, and feature constraints has not yet been implemented.

---

## Step 4 — Detect Dataset Drift

After structural validation, the component checks whether the statistical distribution of the current dataset differs significantly from the reference dataset.

Dataset drift indicates that the data being used for training may no longer represent the data on which the model was originally developed.

The project uses the **Kolmogorov–Smirnov (KS) Test** for drift detection.

The process is illustrated below.

```text
Reference Dataset
        │
        ├───────────────┐
        ▼               ▼
Current Dataset     KS Test
        │               │
        └──────► p-value
                        │
                        ▼
            Drift / No Drift
```

The drift detection results are stored in a YAML report for later analysis.

---

# Dataset Drift

## What is Dataset Drift?

Dataset drift occurs when the statistical properties of incoming data differ from those of the reference dataset.

Possible causes include:

- Changes in network traffic
- New attack patterns
- Infrastructure updates
- Changes in user behavior
- Data collection issues

If significant drift exists, model performance may degrade over time.

---

## Kolmogorov–Smirnov (KS) Test

The KS Test compares the cumulative distributions of two datasets.

For each feature:

- A statistical test is performed.
- A p-value is calculated.
- The result indicates whether the feature distribution has changed significantly.

The project records these results in a drift report.

---

# Validation Report

The component generates validation reports describing:

- Schema validation results
- Drift detection results
- Overall validation status

These reports assist developers in diagnosing data quality issues.

---

# Data Flow

```text
DataIngestionArtifact
        │
        ▼
Train Dataset
Test Dataset
        │
        ▼
Schema Validation
        │
        ▼
Dataset Drift Detection
        │
        ▼
Validation Report
        │
        ▼
DataValidationArtifact
```

---

# Produced Artifact

```text
DataValidationArtifact

├── validation_status
├── valid_train_file_path
├── valid_test_file_path
└── drift_report_path
```

This artifact provides validated dataset paths for the Data Transformation component.

---

# Error Handling

Potential issues include:

- Missing datasets
- Invalid schema file
- Empty datasets
- Failed drift analysis
- File read errors

All exceptions are wrapped using the project's custom exception framework.

---

# Design Decisions

Several architectural decisions improve the robustness of the validation process.

### Independent Validation Stage

Validation is isolated from Data Ingestion.

This separation ensures that data acquisition and data quality verification remain independent responsibilities.

---

### Schema-Driven Validation

The expected dataset structure is defined externally rather than hardcoded into the validation logic.

---

### Statistical Drift Detection

The pipeline evaluates not only dataset structure but also changes in feature distributions.

This provides an additional layer of protection against silent performance degradation.

---

### Artifact-Based Communication

Validation results are encapsulated inside a DataValidationArtifact, allowing downstream components to remain loosely coupled.

---

# Software Engineering Patterns

This component demonstrates several common design patterns.

| Pattern | Purpose |
|----------|---------|
| Validation Layer | Isolates data quality checks |
| Pipeline Pattern | Second stage of the ML workflow |
| Dependency Injection | Receives configuration externally |
| Data Transfer Object (DTO) | Uses DataValidationArtifact |
| Single Responsibility Principle | Handles only validation |

---

# Implementation Notes

The current implementation includes several important characteristics.

- Reads training and testing datasets generated during Data Ingestion.
- Loads the schema from a YAML configuration file.
- Performs schema validation based primarily on column count.
- Detects dataset drift using the Kolmogorov–Smirnov (KS) Test.
- Generates a YAML drift report.
- Produces a DataValidationArtifact for the next pipeline stage.

These notes describe the current implementation and may evolve as the validation component is enhanced.

---

# Current Limitations

The current implementation has several limitations.

- Schema validation checks only the number of columns.
- Column names are not verified.
- Data types are not validated.
- Missing mandatory features are not detected.
- Feature ranges and value constraints are not validated.
- Drift detection results do not automatically stop pipeline execution.
- Validation reports provide limited diagnostic information.

These limitations are acceptable for the current implementation but should be addressed in future versions.

---

# Current vs. Production Validation

| Validation Check         | Current Implementation | Production Recommendation         |
| ------------------------ | ---------------------- | --------------------------------- |
| Column Count             | ✅ Yes                  | ✅ Yes                             |
| Column Names             | ❌ No                   | ✅ Yes                             |
| Data Types               | ❌ No                   | ✅ Yes                             |
| Missing Required Columns | ❌ No                   | ✅ Yes                             |
| Null Value Threshold     | ❌ No                   | ✅ Yes                             |
| Duplicate Detection      | ❌ No                   | ✅ Yes                             |
| Range Validation         | ❌ No                   | ✅ Yes                             |
| Dataset Drift            | ✅ KS Test              | ✅ KS Test + Additional Monitoring |

---

# Future Improvements

Potential enhancements include:

- Validate column names.
- Validate feature data types.
- Validate required and optional features.
- Check for duplicate records.
- Validate missing value thresholds.
- Detect outliers.
- Add configurable drift thresholds.
- Generate richer validation reports.
- Support data quality dashboards.
- Integrate automated validation into CI/CD pipelines.

---

# Summary

The Data Validation component ensures that datasets entering the Machine Learning pipeline satisfy the expected structural and statistical requirements.

By validating schema consistency and detecting dataset drift before preprocessing begins, the component helps maintain data quality and reduces the likelihood of training models on unreliable or unexpected data.

---

# Next Document

Continue with:

```text
07_Data_Transformation.md
```

to understand how validated datasets are converted into model-ready features for Machine Learning.