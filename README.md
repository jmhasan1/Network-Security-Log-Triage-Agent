# 🛡️ Network Security Log Triage Agent

> **An evolving AI-powered security operations assistant for detecting, investigating, and triaging network security events.**

The project is being developed incrementally from a modular Machine Learning pipeline into a **production-oriented Network Security Log Triage Agent** combining ML detection, Retrieval-Augmented Generation (RAG), LangGraph-based investigation workflows, and MCP-powered security tools.

---

## 🚧 Project Status

**Current release:** `v0.1.x` — ML Pipeline Foundation
**Next milestone:** `v0.2.0` — Reproducible & Hardened ML Foundation

The existing system provides the ML foundation required for the future triage agent.

### ✅ Implemented

* Modular ML training pipeline
* MongoDB data ingestion
* Schema and dataset validation
* KS-test based drift detection
* Data transformation and preprocessing
* Multi-model training and hyperparameter tuning
* MLflow experiment tracking
* FastAPI inference API
* Docker support
* Artifact-based pipeline architecture
* Project documentation

### 🔧 Current Development — `v0.2.x`

* Improve data ingestion and validation
* Strengthen preprocessing
* Improve model training and evaluation
* Establish reproducible ML experiments
* Improve MLflow tracking
* Add comprehensive model benchmarking
* Add tests and pipeline hardening
* Establish the Version 1 ML benchmark

### 🔭 Planned

* Security log processing
* Historical incident retrieval
* RAG knowledge base
* LangGraph investigation agent
* MCP security tools
* Multi-step investigation loop
* Agent evaluation and monitoring

---

# 🎯 Project Objective

Traditional security classification answers:

```text
Is this event malicious?
```

The goal of this project is to evolve that into:

```text
What happened?
        ↓
How serious is it?
        ↓
What evidence supports the decision?
        ↓
Have we seen something similar before?
        ↓
Do we need more information?
        ↓
Should we escalate, auto-close, or investigate further?
```

The final system is intended to **assist SOC analysts with evidence-based security triage**, rather than simply produce a binary prediction.

📖 [Read the Project Overview](docs/00_Project_Overview.md)

---

# 🏗️ Architecture Evolution

### Current — ML Foundation

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
FastAPI Inference
```

📖 [Architecture Overview](docs/03_Architecture_Overview.md)

### Target — Log Triage Agent

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
Historical / Knowledge Retrieval
      │
      ▼
LangGraph Investigation Agent
      │
      ├──────────────► RAG
      │
      ├──────────────► MCP Security Tools
      │
      └──────────────► Related Logs / Incidents
      │
      ▼
Evidence-Based Decision
      │
      ├──► Escalate
      ├──► Auto-Close
      └──► Request More Data
```

The existing ML pipeline is therefore not being discarded. It becomes one of the quantitative components used by the future investigation system.

---

# 🗺️ Development Roadmap

The project follows incremental `v0.x` releases before reaching `v1.0.0`.

```text
v0.x — Development & Evolution
│
├── v0.1.x
│     Existing ML pipeline foundation
│
├── v0.2.x
│     Reproducible + hardened ML foundation
│
├── v0.3.x
│     Security log processing
│
├── v0.4.x
│     RAG + historical incident retrieval
│
├── v0.5.x
│     LangGraph investigation agent
│
├── v0.6.x
│     MCP security tools
│
├── v0.7.x
│     Evaluation + monitoring
│
├── v0.8.x
│     Integrated security triage system
│
└── v0.9.x
      Release candidate + hardening

v1.0.0
│
└── Production-oriented
    Network Security Log Triage Agent
```

📖 [Detailed Future Roadmap](docs/12_Future_Roadmap.md)

---

# 📚 Documentation

The repository documentation explains the current ML system in detail so that the README can remain concise.

| Topic                                                               | Description                                   |
| ------------------------------------------------------------------- | --------------------------------------------- |
| [Project Overview](docs/00_Project_Overview.md)                     | Project goal, problem, workflow and vision    |
| [Environment Setup](docs/01_Environment_Setup.md)                   | uv, Python, MongoDB, MLflow, Docker and setup |
| [Project Structure](docs/02_Project_Structure.md)                   | Repository organization and responsibilities  |
| [Architecture](docs/03_Architecture_Overview.md)                    | Current and evolving architecture             |
| [Configuration & Artifacts](docs/04_Configuration_and_Artifacts.md) | Configuration and artifact design             |
| [Data Ingestion](docs/05_Data_Ingestion.md)                         | Dataset acquisition and ingestion             |
| [Data Validation](docs/06_Data_Validation.md)                       | Schema validation and drift detection         |
| [Data Transformation](docs/07_Data_Transformation.md)               | Preprocessing and feature preparation         |
| [Model Training](docs/08_Model_Training.md)                         | Model selection, tuning and MLflow            |
| [Training Pipeline](docs/09_Training_Pipeline.md)                   | End-to-end ML orchestration                   |
| [Inference API](docs/10_Inference_API.md)                           | FastAPI model serving                         |
| [Utilities](docs/11_Utilities.md)                                   | Shared infrastructure                         |
| [Future Roadmap](docs/12_Future_Roadmap.md)                         | Evolution toward the triage agent             |

---

# 📊 Evaluation

Model and system evaluation is maintained separately from architectural documentation.

```text
evaluation/
│
├── baseline_candidate.md
├── experiments.md
├── v1_benchmark.md
├── figures/
├── ml/
├── rag/
└── agent/
```

The current model serves as a **baseline candidate**, not the final Version 1 benchmark.

The `v0.2.x` milestone will establish a stronger and reproducible ML benchmark before the project moves into security-log and agentic development.

---

# 🛠️ Technology Stack

### Current

* Python 3.11
* uv
* Pandas
* NumPy
* Scikit-learn
* MongoDB
* MLflow
* FastAPI
* Uvicorn
* Docker

### Planned

* LangChain
* LangGraph
* Vector database
* Embedding models
* Hybrid retrieval
* Reranking
* LLMs
* MCP

Technologies are introduced when they solve a specific architectural requirement rather than simply expanding the technology stack.

---

# 📂 Repository Structure

```text
network-security-log-triage-agent/
│
├── .github/
├── .vscode/
├── src/
│   └── network_security/
├── data/
├── models/
├── artifacts/
├── configs/
├── docs/
├── evaluation/
├── tests/
├── notebooks/
├── scripts/
├── docker/
│
├── pyproject.toml
├── uv.lock
├── CHANGELOG.md
├── README.md
└── .env.example
```

📖 [Project Structure Guide](docs/02_Project_Structure.md)

---

# 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/jmhasan1/Network-Security-Log-Triage-Agent.git
cd Network-Security-Log-Triage-Agent
```

Create the environment:

```bash
uv venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
uv sync
```

Configure environment variables using `.env`.

Then run the application:

```bash
uv run uvicorn app:app --reload
```

📖 [Environment Setup Guide](docs/01_Environment_Setup.md)

---

# 🔬 Development Philosophy

The project follows an incremental engineering approach:

```text
Build
  ↓
Measure
  ↓
Evaluate
  ↓
Improve
  ↓
Version
  ↓
Freeze
  ↓
Extend
```

Each major capability is introduced only after the previous layer is sufficiently stable.

This prevents the future RAG and agentic layers from hiding weaknesses in the underlying ML system.

---

# 🌐 Long-Term Vision

The final system should be capable of taking a security alert and performing a genuine investigation:

```text
Security Alert
      │
      ▼
Understand Event
      │
      ▼
ML Risk Assessment
      │
      ▼
Retrieve Related Incidents
      │
      ▼
Retrieve Security Knowledge
      │
      ▼
Determine Missing Evidence
      │
      ▼
Call Security Tools
      │
      ▼
Re-evaluate
      │
      ▼
Investigation Decision
      │
 ┌────┼─────────────┐
 ▼    ▼             ▼
Escalate  Auto-Close  Request Data
```

The long-term objective is **not simply another RAG chatbot**.

It is an **evidence-driven security triage system with a genuine investigation loop**, where the agent can decide when additional context or quantitative analysis is necessary.

---

# 👨‍💻 Author

**Jahid Hasan**

AI / ML Engineer

[GitHub](https://github.com/jmhasan1)
