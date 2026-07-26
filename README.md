# 🛡️ Network Security ML Pipeline  
> End-to-End Production-Ready Machine Learning System for Network Intrusion Detection  

---

## 📌 Project Overview

This project implements a **modular, production-grade Machine Learning pipeline** for Network Security / Intrusion Detection.

It follows a real-world industry architecture:

ETL → Data Ingestion → Data Validation → Data Transformation → Model Training → Evaluation → Deployment

The project is designed with:

- ✅ Clean modular architecture
- ✅ Custom logging & exception handling
- ✅ Schema validation
- ✅ Data drift detection
- ✅ Feature store concept
- ✅ Artifact-driven pipeline
- ✅ CI/CD ready structure
- 🚧 Model training & deployment (in progress)

---

## 🏗️ Architecture Overview

### 1️⃣ ETL Pipeline (Extract → Transform → Load)

- Extract data from local CSV
- Convert into JSON records
- Push into MongoDB Atlas
- Uses:
  - `pymongo`
  - `certifi`
  - `.env` for secure Mongo URI
  - Custom exception handling

MongoDB is used as the centralized data source for training.

---

### 2️⃣ Data Ingestion Component

Reads data from MongoDB and:

- Exports collection as DataFrame
- Creates **Feature Store**
- Splits data into:
  - `train.csv`
  - `test.csv`
- Saves artifacts with timestamped directory

Artifacts:

```
artifacts/
   └── <timestamp>/
         └── data_ingestion/
               ├── feature_store/
               └── ingested/
```

---

### 3️⃣ Data Validation Component

Ensures production-grade data consistency:

✔ Schema validation (based on `schema.yaml`)  
✔ Column count validation  
✔ Numerical column validation  
✔ Data drift detection using **KS Test (scipy.stats.ks_2samp)**  

Generates:
- Drift report (YAML)
- Validation artifacts

If validation fails → pipeline stops.

---

### 4️⃣ Data Transformation Component

Performs preprocessing:

- KNN Imputation for missing values
- Train/Test separation
- Target column split
- Preprocessing pipeline creation
- Saves:
  - `preprocessing.pkl`
  - `train.npy`
  - `test.npy`

Artifacts:

```
data_transformation/
    ├── preprocessing.pkl
    ├── train.npy
    └── test.npy
```

---

### 5️⃣ Model Trainer Component (🚧 In Progress)

Planned architecture:

- Load transformed numpy arrays
- Model Factory:
  - Train multiple models
  - Select best model
- Accuracy threshold comparison
- Save:
  - `model.pkl`
  - Metrics artifact
- Combine with preprocessing object

---

### 6️⃣ Model Evaluation (🚧 Planned)

- Compare new model vs previous production model
- Accept only if performance improves

---

### 7️⃣ Model Pusher (🚧 Planned)

- Push model to:
  - AWS S3 / EC2
  - Docker container
  - Production inference system

---

### 8️⃣ Deployment Architecture (CI/CD Ready)

Deployment plan:

Local Code → Docker Image → AWS ECR → AWS EC2  
                                ↑  
                     GitHub Actions CI/CD  

- GitHub Actions workflow included
- Dockerfile included
- Environment variable support via `.env`

---

## 📂 Project Structure

```
NetworkSecurity/
│
├── .github/workflows/
│      └── main.yml
│
├── networksecurity/
│      ├── components/
│      ├── constant/
│      ├── entity/
│      ├── exception/
│      ├── logging/
│      ├── pipeline/
│      ├── utils/
│      └── cloud/
│
├── data_schema/
│      └── schema.yaml
│
├── notebooks/
├── network_data/
├── setup.py
├── requirements.txt
├── Dockerfile
└── main.py
```

---

## ⚙️ Key Engineering Highlights

### 🔹 Custom Logging System
- Timestamped log files
- Auto log directory creation
- Centralized logging configuration

### 🔹 Custom Exception Class
Captures:
- File name
- Line number
- Error message
- Full traceback

### 🔹 Configuration-Driven Design
All paths and parameters controlled via:

```
constant/training_pipeline/
```

No hardcoded paths inside components.

### 🔹 Artifact-Based Pipeline
Each stage produces structured artifacts:
- Clean separation of concerns
- Easier debugging
- Reproducibility
- Production scalability

### 🔹 MongoDB Integration
- Secure Atlas connection
- Environment variable usage
- JSON-based data loading

---

## 🧠 Machine Learning Design Philosophy

- Separation of configuration & execution
- Pipeline modularization
- Schema enforcement before training
- Drift detection before transformation
- Model selection using factory pattern
- Threshold-based model acceptance

This follows enterprise ML standards.

---

## 🚀 How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/jmhasan1/NetworkSecurity.git
cd NetworkSecurity
```

### 2️⃣ Create Environment

```bash
conda create -n network python=3.10 -y
conda activate network
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create `.env`:

```
MONGO_DB_URL=your_mongodb_connection_string
```

### 5️⃣ Run ETL

```bash
python push_data.py
```

### 6️⃣ Run Training Pipeline

```bash
python main.py
```

---

## 📊 Current Status

| Component | Status |
|-----------|--------|
| ETL | ✅ Completed |
| Data Ingestion | ✅ Completed |
| Data Validation | ✅ Completed |
| Data Transformation | ✅ Completed |
| Model Trainer | ✅ Completed |
| Model Evaluation | ✅ Completed |
| MLFlow Tracking | ✅ Completed |
| Docker Deployment | 🚧 Planned |
| AWS Deployment | 🚧 Planned |

---

## 🔮 Upcoming Enhancements

- Advanced model selection (XGBoost, LightGBM, Random Forest)
- MLFlow experiment tracking
- Model versioning
- REST API (FastAPI)
- Real-time inference endpoint
- AWS ECR + EC2 auto deployment
- Monitoring & alerting
- Batch prediction pipeline


## 👤 Author

**Jahid Hasan**  
AI / ML Engineer  
GitHub: https://github.com/jmhasan1/NetworkSecurity

---
