# Data Transformation

The **Data Transformation** component is the third stage of the Machine Learning pipeline.

Its primary responsibility is to convert validated datasets into a format suitable for Machine Learning by performing preprocessing, handling missing values, separating features and labels, and generating transformed datasets for model training.

The output of this stage is a **DataTransformationArtifact**, which is consumed by the Model Training component.

---

# Purpose

Raw datasets are rarely suitable for direct use in Machine Learning models.

The objective of Data Transformation is to ensure that all input data is converted into a consistent, numerical, and model-ready format while preserving the integrity of the original dataset.

This component performs all preprocessing operations required before model training begins.

---

# Responsibilities

The Data Transformation component performs the following tasks:

- Read validated datasets
- Separate features and target labels
- Standardize missing values
- Apply preprocessing pipeline
- Generate transformed NumPy arrays
- Save preprocessing objects
- Produce a DataTransformationArtifact

---

# Inputs

The component receives two inputs.

## DataTransformationConfig

Contains configuration information including:

| Configuration | Description |
|--------------|-------------|
| Preprocessor Object Path | Location to save preprocessing pipeline |
| Train Array Path | Output transformed training data |
| Test Array Path | Output transformed testing data |

---

## DataValidationArtifact

Provides validated datasets from the previous stage.

| Artifact Field | Description |
|---------------|-------------|
| valid_train_file_path | Validated training dataset |
| valid_test_file_path | Validated testing dataset |

---

# Outputs

The component produces a **DataTransformationArtifact**.

| Artifact Field | Description |
|---------------|-------------|
| transformed_train_file_path | Transformed training NumPy array |
| transformed_test_file_path | Transformed testing NumPy array |
| transformed_object_file_path | Serialized preprocessing pipeline |

These outputs become the inputs for Model Training.

---

# Execution Flow

```text
Validated Train/Test Dataset
            │
            ▼
Read CSV Files
            │
            ▼
Separate Features & Target
            │
            ▼
Replace Invalid Values
            │
            ▼
Create Preprocessing Pipeline
            │
            ▼
Fit on Training Data
            │
            ▼
Transform Train & Test
            │
            ▼
Generate NumPy Arrays
            │
            ▼
Save Preprocessor
            │
            ▼
Create DataTransformationArtifact
```

---

# Step-by-Step Workflow

## Step 1 — Read Validated Datasets

The component loads the validated training and testing datasets produced by the Data Validation stage.

These datasets have already passed structural validation and drift analysis.

---

## Step 2 — Separate Features and Target

The dataset is divided into:

- **Features (X)** – Input variables used for prediction.
- **Target (y)** – Ground truth labels used during supervised learning.

Conceptually:

```text
Dataset

↓

Features (X)

+

Target (y)
```

Separating the target variable ensures that preprocessing operations are applied only to the input features.

---

## Step 3 — Standardize Missing Values

The current implementation replaces placeholder values (such as `-1`) with valid representations before preprocessing.

This ensures that missing information is handled consistently across the dataset.

---

## Step 4 — Build the Preprocessing Pipeline

The project uses Scikit-learn's `Pipeline` abstraction.

Current preprocessing pipeline:

```text
Features

↓

KNNImputer

↓

Processed Features
```

Using a pipeline guarantees that identical preprocessing steps are applied during both training and inference.

---

## Step 5 — Handle Missing Values

The pipeline uses **KNNImputer** to estimate missing feature values.

Rather than replacing missing values with simple statistics (such as mean or median), KNNImputer identifies similar observations and estimates missing values using neighboring samples.

Current workflow:

```text
Training Features

↓

Fit KNNImputer

↓

Learn Neighbor Relationships

↓

Transform Training Data

↓

Transform Testing Data
```

The imputer is fitted **only on the training dataset**.

The fitted preprocessing pipeline is then reused to transform the testing dataset.

This prevents **data leakage**, ensuring that information from the testing dataset does not influence the training process.

---

# Why Fit Only on Training Data?

A fundamental Machine Learning principle is that preprocessing parameters should be learned exclusively from the training dataset.

Incorrect approach:

```text
Train + Test

↓

Fit Preprocessor

↓

Train Model
```

Correct approach:

```text
Training Data

↓

Fit Preprocessor

↓

Transform Train

↓

Transform Test
```

This ensures a fair evaluation of model performance.

---

## Step 6 — Generate NumPy Arrays

After preprocessing, the transformed feature matrices are combined with their corresponding target labels.

The resulting datasets are stored as NumPy arrays.

Conceptually:

```text
Processed Features

+

Target Labels

↓

NumPy Arrays
```

NumPy arrays provide efficient storage and are well-suited for Machine Learning algorithms.

---

## Step 7 — Save the Preprocessing Pipeline

The fitted preprocessing pipeline is serialized and saved to disk.

```text
preprocessor.pkl
```

Saving the preprocessor ensures that future prediction requests receive identical preprocessing to the training data.

Without this step, the model would receive inconsistent feature representations during inference.

---

## Step 8 — Create DataTransformationArtifact

Finally, the component creates a DataTransformationArtifact containing references to:

- Transformed training data
- Transformed testing data
- Serialized preprocessing pipeline

This artifact is passed to the Model Training component.

---

# Preprocessing Pipeline

Current implementation:

```text
Input Features

↓

KNNImputer

↓

Processed Features
```

Although the current pipeline contains a single preprocessing step, Scikit-learn Pipelines are designed to support additional transformations as the project evolves.

Possible future preprocessing stages include:

- Feature Scaling
- Feature Encoding
- Feature Selection
- Dimensionality Reduction

---

# Data Flow

```text
Validated Dataset

↓

Feature / Target Separation

↓

Preprocessing Pipeline

↓

Transformed Features

↓

NumPy Arrays

↓

DataTransformationArtifact
```

---

# Produced Artifact

```text
DataTransformationArtifact

├── transformed_train_file_path
├── transformed_test_file_path
└── transformed_object_file_path
```

This artifact provides all resources required for model training.

---

# Error Handling

Potential issues include:

- Missing validated datasets
- Failed preprocessing pipeline creation
- Serialization failures
- Invalid feature columns
- NumPy conversion errors

All exceptions are handled using the project's custom exception framework.

---

# Design Decisions

Several architectural decisions improve the robustness of the transformation process.

### Separate Transformation Stage

Preprocessing is isolated from both validation and model training.

This keeps responsibilities clearly separated.

---

### Scikit-learn Pipeline

Using a Pipeline guarantees that identical preprocessing is applied during training and inference.

---

### Preventing Data Leakage

The preprocessing pipeline is fitted only on the training dataset.

Testing data is transformed using the fitted pipeline.

---

### Persisting the Preprocessor

Saving the preprocessing pipeline ensures reproducibility and consistent inference.

---

### Artifact-Based Communication

Transformation results are encapsulated inside a DataTransformationArtifact rather than returning multiple unrelated values.

---

# Software Engineering Patterns

This component demonstrates several common design patterns.

| Pattern | Purpose |
|----------|---------|
| Pipeline Pattern | Organizes preprocessing into sequential operations |
| Dependency Injection | Receives configuration externally |
| Data Transfer Object (DTO) | Uses DataTransformationArtifact |
| Single Responsibility Principle | Handles only feature preprocessing |
| Strategy Pattern | Scikit-learn Pipeline allows preprocessing steps to be modified independently |

---

# Implementation Notes

The current implementation includes the following preprocessing steps.

- Reads validated training and testing datasets.
- Separates features and target labels.
- Replaces placeholder values (`-1`) before preprocessing.
- Uses a Scikit-learn Pipeline.
- Applies KNNImputer for missing value imputation.
- Fits the preprocessing pipeline only on the training dataset.
- Transforms both training and testing datasets.
- Saves transformed datasets as NumPy arrays.
- Serializes the fitted preprocessing pipeline.
- Produces a DataTransformationArtifact.

These notes describe the current implementation and may evolve as additional preprocessing techniques are introduced.

---

# Current Limitations

The current implementation is intentionally simple.

Current limitations include:

- Only KNNImputer is applied.
- No feature scaling.
- No categorical feature encoding.
- No feature selection.
- No dimensionality reduction.
- No automated preprocessing optimization.
- No feature engineering beyond missing value handling.

These limitations are acceptable for the current implementation but leave room for future enhancements.

---

# Future Improvements

Potential enhancements include:

- StandardScaler or RobustScaler for numerical features.
- One-Hot Encoding for categorical variables.
- Feature selection techniques.
- Dimensionality reduction (e.g., PCA).
- Automated preprocessing using ColumnTransformer.
- Feature engineering based on domain knowledge.
- Configurable preprocessing pipelines.
- Data transformation versioning.
- Pipeline performance monitoring.

---

# Why Data Transformation Matters

Machine Learning models expect structured numerical inputs. However, real-world datasets often contain missing values, inconsistent formats, or features that require preprocessing before they can be used effectively.

By isolating all preprocessing logic within the Data Transformation component, the pipeline ensures that:

- Training and inference use identical preprocessing steps.
- Data leakage is prevented by fitting transformations only on the training data.
- Preprocessing logic is reusable across different models.
- Future preprocessing techniques can be added without changing downstream components.

This design improves reproducibility, maintainability, and consistency throughout the Machine Learning lifecycle.

---

# Summary

The Data Transformation component converts validated datasets into a machine learning-ready representation by applying consistent preprocessing operations, handling missing values, generating transformed NumPy arrays, and persisting the preprocessing pipeline.

By separating preprocessing from both validation and model training, the project maintains a modular architecture while ensuring that identical transformations are applied during both training and inference.

---

# Next Document

Continue with:

```text
08_Model_Training.md
```

to understand how the transformed datasets are used to train, evaluate, and package the final Machine Learning model.