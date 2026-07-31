# Model Training

The **Model Training** component is the fourth and final stage of the Machine Learning training pipeline.

Its primary responsibility is to train multiple Machine Learning models using the transformed datasets, compare their performance, select the best-performing model, package it for inference, and generate the final **ModelTrainerArtifact**.

Unlike earlier stages, which focus on data preparation, this component is responsible for producing the deployable Machine Learning model used during inference.

---

# Purpose

The objective of Model Training is to automate the complete model development workflow.

This includes:

- Loading transformed datasets
- Training multiple candidate models
- Performing hyperparameter optimization
- Evaluating model performance
- Selecting the best model
- Tracking experiments using MLflow
- Packaging the trained model
- Saving artifacts required for inference

This component eliminates the need for manually training and comparing individual models.

---

# Responsibilities

The Model Training component performs the following tasks:

- Load transformed datasets
- Initialize candidate Machine Learning models
- Perform hyperparameter tuning
- Evaluate model performance
- Select the best model
- Log experiments to MLflow
- Package the preprocessing pipeline and trained model
- Save the final model
- Produce a ModelTrainerArtifact

---

# Inputs

The component receives two inputs.

## ModelTrainerConfig

Contains configuration required during training.

Typical configuration includes:

| Configuration | Description |
|--------------|-------------|
| Model Output Path | Location to save trained model |
| Expected Accuracy | Minimum acceptable model performance |
| MLflow Configuration | Experiment tracking settings |
| Training Parameters | Model-specific settings |

---

## DataTransformationArtifact

Provides the transformed datasets and preprocessing object.

| Artifact Field | Description |
|---------------|-------------|
| transformed_train_file_path | Training NumPy array |
| transformed_test_file_path | Testing NumPy array |
| transformed_object_file_path | Serialized preprocessing pipeline |

---

# Outputs

The component produces a **ModelTrainerArtifact**.

Typical outputs include:

| Artifact Field | Description |
|---------------|-------------|
| trained_model_file_path | Final serialized model |
| train_metric_artifact | Training evaluation metrics |
| test_metric_artifact | Testing evaluation metrics |

The artifact represents the successful completion of the training pipeline.

---

# Execution Flow

```text
Transformed Train/Test Arrays
            │
            ▼
Load NumPy Arrays
            │
            ▼
Initialize Candidate Models
            │
            ▼
Hyperparameter Tuning
            │
            ▼
Evaluate Models
            │
            ▼
Select Best Model
            │
            ▼
Log MLflow Experiment
            │
            ▼
Package NetworkModel
            │
            ▼
Save Model
            │
            ▼
Create ModelTrainerArtifact
```

---

# Step-by-Step Workflow

## Step 1 — Load Transformed Data

The component loads the transformed training and testing datasets produced by the Data Transformation stage.

Each dataset consists of:

- Processed feature matrix
- Target labels

The transformed NumPy arrays are used directly for model training.

---

## Step 2 — Initialize Candidate Models

Rather than relying on a single algorithm, the project trains multiple candidate models.

The current implementation evaluates:

- Random Forest Classifier
- Decision Tree Classifier
- Gradient Boosting Classifier
- Logistic Regression
- AdaBoost Classifier

Training multiple models increases the likelihood of selecting the most suitable algorithm for the dataset.

---

## Step 3 — Hyperparameter Optimization

Each candidate model is trained using predefined hyperparameter search spaces.

The project uses **GridSearchCV** to identify the optimal parameter combination for every model.

Conceptually:

```text
Candidate Model

↓

Hyperparameter Grid

↓

GridSearchCV

↓

Best Parameters

↓

Optimized Model
```

Hyperparameter optimization helps improve model performance without changing the underlying algorithm.

---

## Step 4 — Model Evaluation

After training, each optimized model is evaluated using the transformed datasets.

The evaluation process compares model performance and determines which model should be selected.

Only the highest-performing model proceeds to deployment.

---

## Step 5 — Select the Best Model

The evaluation framework compares all candidate models.

```text
Random Forest
        │
Decision Tree
        │
Gradient Boosting
        │
Logistic Regression
        │
AdaBoost
        │
        ▼
Highest Performing Model
```

The selected model becomes the final production model.

---

## Step 6 — Experiment Tracking

The project integrates **MLflow** to record every training run.

Each experiment stores:

- Model parameters
- Evaluation metrics
- Trained models
- Experiment metadata

Using MLflow makes experiments reproducible and simplifies model comparison.

---

## Step 7 — Package the Model

The project combines:

```text
Preprocessor

+

Trained Model
```

into a single **NetworkModel** object.

This ensures that prediction requests automatically receive identical preprocessing before inference.

---

## Step 8 — Save the Model

The packaged NetworkModel is serialized and stored on disk.

The saved model is later loaded by the FastAPI application for prediction.

---

## Step 9 — Create ModelTrainerArtifact

Finally, the component creates the **ModelTrainerArtifact**, containing references to the trained model and evaluation metrics.

This artifact represents the successful completion of the training pipeline.

---

# Candidate Models

The current implementation evaluates multiple supervised learning algorithms.

| Model | Purpose |
|--------|---------|
| Random Forest | Ensemble tree-based classifier |
| Decision Tree | Simple interpretable classifier |
| Gradient Boosting | Sequential ensemble learning |
| Logistic Regression | Linear probabilistic classifier |
| AdaBoost | Adaptive boosting ensemble |

Each model is independently tuned and evaluated before selection.

---

# Hyperparameter Optimization

The project uses **GridSearchCV** for systematic hyperparameter tuning.

General workflow:

```text
Candidate Model
        │
        ▼
Parameter Grid
        │
        ▼
Cross Validation
        │
        ▼
Best Parameters
        │
        ▼
Optimized Model
```

This approach helps identify better-performing parameter combinations than default settings.

---

# Experiment Tracking

MLflow is used to track every training run.

Tracked information includes:

- Model parameters
- Performance metrics
- Serialized models
- Experiment metadata

Experiment tracking enables reproducibility and comparison between different training runs.

---

# NetworkModel

Rather than saving only the trained classifier, the project packages:

```text
Preprocessor

+

Classifier

↓

NetworkModel
```

The FastAPI application loads this object during inference.

This guarantees that identical preprocessing is applied to every prediction request.

---

# Data Flow

```text
Transformed Arrays

↓

Candidate Models

↓

Grid Search

↓

Evaluation

↓

Best Model

↓

NetworkModel

↓

Saved Model

↓

ModelTrainerArtifact
```

---

# Produced Artifact

```text
ModelTrainerArtifact

├── trained_model_file_path
├── train_metric_artifact
└── test_metric_artifact
```

This artifact represents the final output of the Machine Learning training pipeline.

---

# Error Handling

Potential issues include:

- Missing transformed datasets
- Model training failures
- Hyperparameter optimization failures
- MLflow connection issues
- Model serialization failures

All exceptions are handled using the project's custom exception framework.

---

# Design Decisions

Several architectural decisions improve the flexibility and maintainability of the training process.

### Multiple Candidate Models

Evaluating several algorithms reduces dependence on a single model and allows data-driven model selection.

---

### Hyperparameter Optimization

Automated parameter tuning produces stronger models than fixed default parameters.

---

### Experiment Tracking

MLflow records every experiment, improving reproducibility and simplifying model comparison.

---

### Model Packaging

Packaging the preprocessing pipeline and classifier together ensures consistent inference.

---

### Artifact-Based Communication

The training stage returns a structured ModelTrainerArtifact rather than multiple unrelated outputs.

---

# Software Engineering Patterns

This component demonstrates several software engineering patterns.

| Pattern | Purpose |
|----------|---------|
| Strategy Pattern | Multiple candidate models can be evaluated interchangeably |
| Pipeline Pattern | Final stage of the training workflow |
| Dependency Injection | Receives configuration externally |
| Data Transfer Object (DTO) | Uses ModelTrainerArtifact |
| Single Responsibility Principle | Handles only model training |

---

# Implementation Notes

The current implementation includes the following functionality.

- Loads transformed NumPy arrays.
- Trains multiple candidate models.
- Uses GridSearchCV for hyperparameter tuning.
- Compares candidate model performance.
- Logs experiments to MLflow.
- Packages the preprocessor and trained classifier into a NetworkModel.
- Saves the packaged model.
- Produces a ModelTrainerArtifact.

These notes describe the current implementation and may evolve as additional models and evaluation strategies are introduced.

---

# Current Limitations

The current implementation has several areas for improvement.

- Limited set of candidate algorithms.
- Fixed hyperparameter search spaces.
- No automated feature selection.
- No ensemble of top-performing models.
- No model explainability integration.
- No automated retraining strategy.

Additionally, during our review of the current codebase, two implementation-specific observations were identified:

- The model evaluation helper currently relies on **`r2_score`**, which is typically used for regression rather than classification. This should be reviewed to ensure that the evaluation metric aligns with the classification task.
- The current implementation constructs a `NetworkModel` wrapper but should verify that the packaged object is the one being serialized and saved for inference.

These observations reflect the current implementation and should be revisited during future improvements.

---

# Future Improvements

Potential enhancements include:

- Support additional classification algorithms.
- Bayesian or Optuna-based hyperparameter optimization.
- Automated model selection.
- Cross-validation reporting.
- Feature importance analysis.
- Explainable AI (SHAP/LIME).
- Model registry integration.
- Automated retraining pipelines.
- Continuous performance monitoring.
- Drift-aware model retraining.

---

MongoDB
    │
    ▼
Data Ingestion
    │
    ▼
Data Validation
    │
    ▼
Data Transformation
    │
    ▼
Model Training
    │
    ▼
NetworkModel
    │
    ▼
Saved Model
    │
    ▼
FastAPI Inference

# Summary

The Model Training component automates the process of training, evaluating, selecting, and packaging Machine Learning models.

By combining multiple candidate algorithms, hyperparameter optimization, experiment tracking, and model packaging into a single modular component, the project produces a reproducible and deployable Machine Learning model while maintaining a clean separation between training and inference.

---

# Next Document

Continue with:

```text
09_Training_Pipeline.md
```

to understand how all pipeline stages are orchestrated into a complete end-to-end Machine Learning workflow.