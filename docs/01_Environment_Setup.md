# Environment Setup

This document describes how to set up the complete development environment required to run the Network Security ML Pipeline.

---

# Prerequisites

Before setting up the project, ensure the following software is installed.

| Software | Purpose |
|----------|---------|
| Python 3.11+ | Programming Language |
| Git | Version Control |
| uv | Python package and environment manager |
| MongoDB | Dataset storage |
| Docker (Optional) | Containerization |
| DagsHub Account | Remote MLflow Tracking |
| MLflow | Experiment Tracking |

---

# Clone the Repository

```bash
git clone <repository-url>
cd Network-Security-Log-Triage-Agent
```

---

# Python Version

The project uses Python **3.11**.

The Python version is specified in

```text
.python-version
```

Verify your installation:

```bash
python --version
```

---

# Environment Management using uv

This project uses **uv** instead of Conda for dependency management.

Install uv.

### Windows

```powershell
pip install uv
```

### Linux / macOS

```bash
pip install uv
```

Verify installation:

```bash
uv --version
```

---

# Create Virtual Environment

Create a new virtual environment.

```bash
uv venv
```

This creates

```text
.venv/
```

Activate the environment.

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

# Install Dependencies

Install all project dependencies.

```bash
uv pip install -r requirements.txt
```

Alternatively, if using editable installation:

```bash
uv pip install -e .
```

---

# Project Dependencies

The primary dependencies include:

- pandas
- numpy
- scikit-learn
- pymongo
- mlflow
- fastapi
- uvicorn
- python-dotenv
- certifi

Additional dependencies are automatically installed through:

```text
requirements.txt
```

---

# pyproject.toml

The project includes a modern Python package configuration file.

The file defines:

- Project metadata
- Python version
- Build configuration
- Package information

Although `setup.py` is currently retained for compatibility, future dependency management will primarily use `pyproject.toml`.

---

# Environment Variables

Create a file named

```text
.env
```

inside the project root.

Example:

```text
MONGODB_URL_KEY=<your_mongodb_connection_string>

MLFLOW_TRACKING_URI=<your_mlflow_tracking_uri>

MLFLOW_TRACKING_USERNAME=<your_mlflow_username>

MLFLOW_TRACKING_PASSWORD=<your_mlflow_password>
```

Never commit the `.env` file to Git.

---

# MongoDB Setup

The training pipeline retrieves the dataset from MongoDB.

Steps:

1. Install MongoDB locally or use MongoDB Atlas.
2. Create a database.
3. Create the required collection.
4. Import the dataset.
5. Copy the MongoDB connection string.
6. Store the connection string inside `.env`.

The Data Ingestion component automatically reads data from MongoDB during training.

---

# MLflow Setup

The project uses MLflow for experiment tracking.

MLflow records:

- Model parameters
- Evaluation metrics
- Artifacts
- Trained models

Set the following environment variables:

```text
MLFLOW_TRACKING_URI
MLFLOW_TRACKING_USERNAME
MLFLOW_TRACKING_PASSWORD
```

These values are loaded automatically from `.env`.

---

# DagsHub Setup

This project uses DagsHub as the remote MLflow tracking server.

Steps:

1. Create a DagsHub account.
2. Create a repository.
3. Enable MLflow tracking.
4. Generate an access token.
5. Configure the following environment variables:

```text
MLFLOW_TRACKING_URI
MLFLOW_TRACKING_USERNAME
MLFLOW_TRACKING_PASSWORD
```

Once configured, every training run is automatically logged to DagsHub through MLflow.

---

# Docker

The repository includes a Dockerfile for containerized deployment.

To build the Docker image:

```bash
docker build -t network-security-ml .
```

To run the container:

```bash
docker run -p 8000:8000 network-security-ml
```

Docker provides a consistent runtime environment independent of the host operating system.

---

# Running the Training Pipeline

Start model training through the FastAPI endpoint:

```text
GET /train
```

or execute the training pipeline directly from Python.

The training workflow performs:

```text
Data Ingestion
        ↓
Data Validation
        ↓
Data Transformation
        ↓
Model Training
        ↓
MLflow Tracking
        ↓
Model Saving
```

---

# Running the FastAPI Application

Start the application:

```bash
python app.py
```

or

```bash
uvicorn app:app --reload
```

The application will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

# Project Directory After Setup

A successful setup should produce a structure similar to:

```text
Network-Security-Log-Triage-Agent/

│
├── .venv/
├── .env
├── pyproject.toml
├── requirements.txt
├── app.py
├── Dockerfile
├── networksecurity/
├── data/
├── artifacts/
├── models/
└── templates/
```

---

# Verify Installation

The environment is correctly configured if:

- Virtual environment activates successfully.
- All dependencies install without errors.
- MongoDB connection succeeds.
- FastAPI starts successfully.
- Swagger UI is accessible.
- The training pipeline executes successfully.
- MLflow logs experiments.
- Predictions can be generated through the `/predict` endpoint.

---

# Troubleshooting

### MongoDB Connection Error

- Verify the connection string.
- Check database permissions.
- Confirm the MongoDB service is running.

---

### Missing Environment Variables

Ensure `.env` exists and contains all required variables.

---

### Package Installation Issues

Upgrade pip before installing packages:

```bash
python -m pip install --upgrade pip
```

Reinstall dependencies:

```bash
uv pip install -r requirements.txt
```

---

# Next Document

Continue with:

```text
02_Project_Structure.md
```

to understand the organization of the repository before exploring individual components.