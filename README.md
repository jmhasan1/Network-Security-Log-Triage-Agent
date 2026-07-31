![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-green)

# 🛡️ Network Security Log Triage Agent

> **Building an AI-powered Security Operations (SOC) assistant using Machine Learning, Retrieval-Augmented Generation (RAG), Agentic AI, and MCP.**

---

## 🚧 Current Status

This repository is currently **Version 1** of the project.

The existing implementation is a production-oriented **Machine Learning pipeline** that serves as the foundation for a future AI-powered Security Log Triage Agent.

### ✅ Implemented

- Modular ML Pipeline
- MongoDB Data Ingestion
- Data Validation
- Dataset Drift Detection (KS Test)
- Data Transformation
- Multi-model Training
- MLflow Experiment Tracking
- FastAPI Inference API
- Docker Support
- Modular Architecture

### 🚧 Currently Building

- Production model improvements
- Better evaluation framework
- Documentation
- Repository refactoring

### 🎯 Planned

- Security Log Ingestion
- Retrieval-Augmented Generation (RAG)
- LangGraph Agent
- MCP Tool Integration
- Investigation Workflow
- SOC Dashboard

---

# 🎯 Project Goal

The long-term objective is to build an **AI-powered Network Security Log Triage Agent** capable of:

- Understanding security alerts
- Retrieving historical incidents
- Using organizational documentation
- Performing multi-step investigations
- Calling specialized security tools
- Assisting SOC analysts with evidence-based decisions

Instead of simply predicting **"Attack"** or **"Normal"**, the system will answer:

> **What happened? Why did it happen? How confident are we? What should the analyst do next?**

---

# 🏗️ Architecture

Current architecture:

```text
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
FastAPI
```

Target architecture:

```text
Security Logs
      │
      ▼
Log Processing
      │
      ▼
ML Detection
      │
      ▼
RAG Retrieval
      │
      ▼
LangGraph Agent
      │
      ▼
MCP Tools
      │
      ▼
Investigation Report
```

---

# 📚 Documentation

Comprehensive documentation is available in the **docs/** directory.

| Topic | Description |
|--------|-------------|
| 📖 [Project Overview](docs/00_Project_Overview.md) | Goals, workflow, and project vision |
| ⚙️ [Environment Setup](docs/01_Environment_Setup.md) | Installation and development environment |
| 🗂️ [Project Structure](docs/02_Project_Structure.md) | Repository organization |
| 🏛️ [Architecture Overview](docs/03_Architecture_Overview.md) | High-level system design |
| ⚙️ [Configuration & Artifacts](docs/04_Configuration_and_Artifacts.md) | Core architectural concepts |
| 📥 [Data Ingestion](docs/05_Data_Ingestion.md) | MongoDB → Feature Store |
| ✅ [Data Validation](docs/06_Data_Validation.md) | Schema validation & KS-test drift detection |
| 🔄 [Data Transformation](docs/07_Data_Transformation.md) | Preprocessing pipeline |
| 🤖 [Model Training](docs/08_Model_Training.md) | Training, evaluation & MLflow |
| 🚀 [Training Pipeline](docs/09_Training_Pipeline.md) | End-to-end orchestration |
| 🌐 [Inference API](docs/10_Inference_API.md) | FastAPI deployment |
| 🧰 [Utilities](docs/11_Utilities.md) | Shared infrastructure |
| 🛣️ [Future Roadmap](docs/12_Future_Roadmap.md) | Evolution toward Agentic AI |

---

# 🛠️ Technology Stack

### Machine Learning

- Scikit-learn
- NumPy
- Pandas
- MLflow

### Backend

- FastAPI
- Uvicorn

### Database

- MongoDB

### Development

- Python 3.11
- uv
- Docker

### Future Stack

- LangGraph
- LangChain
- MCP
- Vector Database
- Rerankers
- LLMs
- Hybrid Retrieval

---

# 🗺️ Roadmap

## Version 1 (Current)

✅ Production Machine Learning Pipeline

---

## Version 2

- Better feature engineering
- Improved evaluation
- Model monitoring
- Better deployment

---

## Version 3

- Security Log Processing
- RAG
- Vector Database
- Historical Incident Retrieval

---

## Version 4

- LangGraph Agent
- MCP Integration
- Multi-step Investigation
- Security Reasoning

---

## Version 5

AI-powered Security Investigation Platform

---

# 📂 Repository

```text
docs/
networksecurity/
data/
models/
evaluation/
tests/
app.py
main.py
```

See **Project Structure** for a complete explanation.

➡️ docs/02_Project_Structure.md

---

# 🚀 Quick Start

```bash
git clone https://github.com/jmhasan1/Network-Security-Log-Triage-Agent.git

cd Network-Security-Log-Triage-Agent

uv venv

.venv\Scripts\activate

uv pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app:app --reload
```

---

# 🌟 End Goal

This repository is **not intended to remain a classical ML project**.

The goal is to build an intelligent Security Operations assistant capable of:

- Understanding alerts
- Retrieving organizational knowledge
- Investigating incidents
- Calling external security tools through MCP
- Producing structured investigation reports
- Assisting security analysts rather than replacing them

The current Machine Learning pipeline is the foundation upon which these capabilities will be built.

---

## 👨‍💻 Author

**Jahid Hasan**

AI / ML Engineer

GitHub: https://github.com/jmhasan1