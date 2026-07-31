# Data Ingestion

The **Data Ingestion** component is the first stage of the Machine Learning pipeline.

Its responsibility is to retrieve the dataset from the source database, create a local feature store, split the dataset into training and testing sets, and prepare the data for downstream pipeline stages.

The output of this stage is a **DataIngestionArtifact**, which is consumed by the Data Validation component.

---

# Purpose

The objective of Data Ingestion is to move data from the external storage system into the Machine Learning pipeline.

This component ensures that:

- Data is successfully retrieved from MongoDB.
- A local copy of the dataset is maintained.
- The dataset is split into training and testing sets.
- Downstream components receive standardized input paths.

Rather than allowing every component to access the database directly, only the Data Ingestion component interacts with MongoDB.

This improves modularity and separates data access from Machine Learning logic.

---

# Responsibilities

The Data Ingestion component performs the following tasks:

- Connect to MongoDB
- Retrieve the dataset
- Convert MongoDB documents into a Pandas DataFrame
- Store the raw dataset locally (Feature Store)
- Split the dataset into training and testing sets
- Save train and test datasets
- Return a DataIngestionArtifact

---

# Inputs

The component receives a **DataIngestionConfig** object.

Typical configuration values include:

| Configuration | Description |
|--------------|-------------|
| MongoDB Database | Source database |
| MongoDB Collection | Source collection |
| Feature Store Path | Local raw dataset |
| Train Dataset Path | Training CSV |
| Test Dataset Path | Testing CSV |
| Train/Test Split Ratio | Dataset split percentage |

---

# Outputs

The component produces a **DataIngestionArtifact** containing:

| Artifact Field | Description |
|---------------|-------------|
| feature_store_path | Local copy of the complete dataset |
| train_file_path | Training dataset |
| test_file_path | Testing dataset |

This artifact becomes the input for the Data Validation stage.

---

# Execution Flow

The execution process is illustrated below.

```text
MongoDB
      │
      ▼
Connect to Database
      │
      ▼
Retrieve Collection
      │
      ▼
Convert to Pandas DataFrame
      │
      ▼
Remove MongoDB _id Column
      │
      ▼
Replace Invalid Values
      │
      ▼
Save Feature Store
      │
      ▼
Train/Test Split
      │
      ▼
Save Train CSV
      │
      ▼
Save Test CSV
      │
      ▼
Create DataIngestionArtifact
```

---

# Step-by-Step Workflow

## Step 1 — Connect to MongoDB

The pipeline establishes a connection using the MongoDB connection string stored in the `.env` file.

The Data Ingestion component is the only part of the pipeline responsible for interacting with the database.

---

## Step 2 — Read the Dataset

The specified MongoDB collection is retrieved.

Each MongoDB document represents one record in the dataset.

The collection is converted into a Pandas DataFrame for subsequent processing.

---

## Step 3 — Remove MongoDB Metadata

MongoDB automatically creates an `_id` field for every document.

This field is used internally by MongoDB and is not a meaningful machine learning feature.

Therefore, it is removed before training.

```text
Before

_id
feature1
feature2
label

↓

After

feature1
feature2
label
```

---

## Step 4 — Handle Missing Values

The dataset replaces placeholder values such as `"na"` with NumPy's `NaN`.

This standardization allows downstream preprocessing components to correctly identify and impute missing values.

---

## Step 5 — Create Feature Store

The complete dataset is written to the Feature Store.

The Feature Store serves as the local snapshot of the retrieved data.

It provides:

- Reproducibility
- Easier debugging
- Local data availability
- Reduced dependency on MongoDB during later stages

---

## Step 6 — Split Dataset

The dataset is divided into training and testing subsets.

```text
Feature Store
      │
      ▼
Train/Test Split
      │
      ├────────► Train.csv
      │
      └────────► Test.csv
```

The split ratio is defined in the configuration.

This separation ensures that the model is evaluated on unseen data.

---

## Step 7 — Save Datasets

The following datasets are stored locally:

```text
Feature Store

↓

Train.csv

↓

Test.csv
```

These files become the inputs for the Data Validation component.

---

## Step 8 — Create Artifact

Finally, the component creates a DataIngestionArtifact.

```text
DataIngestionArtifact

├── feature_store_path
├── train_file_path
└── test_file_path
```

This artifact is passed to the next pipeline stage.

---

# Feature Store

The Feature Store is a local copy of the raw dataset retrieved from MongoDB.

Benefits include:

- Reproducibility
- Offline access
- Easier debugging
- Consistent training inputs

The Feature Store acts as the starting point for all subsequent processing stages.

---

# Data Flow

```text
MongoDB

↓

Pandas DataFrame

↓

Feature Store

↓

Train/Test Split

↓

Train.csv

Test.csv

↓

DataIngestionArtifact
```

---

# Produced Artifact

```text
DataIngestionArtifact

feature_store_path

train_file_path

test_file_path
```

This artifact provides all file locations required by Data Validation.

---

# Error Handling

Potential issues include:

- MongoDB connection failures
- Missing collections
- Empty datasets
- Invalid file paths
- Dataset write failures

The component catches these exceptions and wraps them using the project's custom exception framework.

---

# Design Decisions

Several software engineering decisions improve the robustness of the component.

### Dedicated Data Access Layer

Only Data Ingestion communicates with MongoDB.

Other components work exclusively with local files.

---

### Local Feature Store

Maintaining a local snapshot ensures reproducible experiments and simplifies debugging.

---

### Artifact-Based Communication

Instead of returning multiple variables, the component returns a structured artifact.

---

### Configuration-Driven Execution

Database names, collection names, paths, and split ratios are controlled through configuration objects rather than hardcoded values.

---

# Software Engineering Patterns

This component demonstrates several common design patterns.

| Pattern | Purpose |
|----------|---------|
| Repository-like Pattern | Encapsulates database access |
| Pipeline Pattern | First stage of sequential workflow |
| Dependency Injection | Receives configuration externally |
| Data Transfer Object (DTO) | Uses DataIngestionArtifact |
| Single Responsibility Principle | Handles only data ingestion |

---

## Implementation Notes

The current implementation includes several practical choices that are worth noting:

- MongoDB documents are converted directly into a Pandas DataFrame.
- The automatically generated `_id` column is removed before further processing.
- Placeholder values such as `"na"` are converted to `NaN`.
- The dataset is saved to a local Feature Store before splitting.
- Train and test datasets are written as CSV files and referenced through the `DataIngestionArtifact`.

# Current Limitations

The current implementation has several opportunities for improvement.

- Limited validation during data retrieval.
- Assumes the MongoDB collection exists.
- Fixed train/test split strategy.
- No retry mechanism for database connectivity.
- No support for incremental data ingestion.
- No data versioning in the Feature Store.

These limitations are acceptable for the current implementation but could be addressed in future iterations.

---

# Future Improvements

Possible enhancements include:

- Configurable random seed for reproducible splits.
- Incremental ingestion for large datasets.
- Data versioning.
- Automatic schema validation before ingestion.
- Support for multiple data sources (CSV, PostgreSQL, APIs, cloud storage).
- Data quality statistics before saving.
- Retry logic for transient database failures.
- Data lineage tracking.

---

# Summary

The Data Ingestion component is responsible for importing the dataset from MongoDB, preparing a local feature store, generating training and testing datasets, and producing the **DataIngestionArtifact** required by the next stage of the pipeline.

By isolating data access into a dedicated component, the project maintains a clean separation between data acquisition and machine learning logic, resulting in a more modular and maintainable architecture.

---

# Next Document

Continue with:

```text
06_Data_Validation.md
```

to understand how the ingested dataset is validated before preprocessing and model training.