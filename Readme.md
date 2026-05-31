## Network Security Project for phising data
<div align="center">

# 🛡️ Network Security — Phishing Detection MLOps System

### An End-to-End Production-Grade Machine Learning Pipeline for Cybersecurity

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![AWS](https://img.shields.io/badge/AWS-Deployment_Ready-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com)
[![DagsHub](https://img.shields.io/badge/DagsHub-Experiment_Tracking-FC4F4F?style=for-the-badge&logo=dagshub&logoColor=white)](https://dagshub.com)

<br/>

> 🎓 **Capstone MLOps Project** — Demonstrates real-world production ML engineering practices including automated pipelines, experiment tracking, containerization, and REST API deployment.

<br/>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

</div>

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [System Architecture](#-system-architecture)
- [ML Pipeline Stages](#-ml-pipeline-stages)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Model Performance](#-model-performance)
- [Running Locally](#-running-locally)
- [CI/CD & Deployment](#-cicd--deployment)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🔍 Overview

**Network Security** is a fully automated, production-oriented MLOps system that classifies websites as **legitimate or phishing** based on security-related features. It covers the complete ML lifecycle — from raw data in MongoDB through model training, experiment tracking, and serving predictions via a REST API.

This project was built as a **capstone MLOps project** to demonstrate the engineering practices required to take a machine learning model from experiment to production.

**Key Highlights:**
- 🔁 Fully automated training pipeline (no manual steps)
- 📊 Experiment tracking with MLflow + DagsHub
- 🐳 Dockerized for consistent, reproducible environments
- 🚀 FastAPI prediction service with CSV upload support
- ⚙️ CI/CD via GitHub Actions for automated testing and deployment
- ☁️ AWS deployment-ready architecture

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🎯 Problem Statement

Phishing attacks are among the most widespread cybersecurity threats, tricking users into revealing sensitive data such as passwords, banking credentials, and personal information.

This project builds a **machine learning classifier** that automatically identifies phishing websites by analyzing engineered security features — enabling real-time threat detection without human intervention.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                               │
│   Raw CSV Data  ──►  push_data.py  ──►  MongoDB Atlas          │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                     TRAINING PIPELINE                           │
│                                                                 │
│  📥 Data Ingestion  ──►  ✅ Data Validation                     │
│         │                      │                               │
│         ▼                      ▼                               │
│  🔄 Data Transformation  ──►  🤖 Model Training                 │
│         │                      │                               │
│         └──────────────────────▼                               │
│                        📈 MLflow Tracking                       │
│                               │                                │
│                               ▼                                │
│                    💾 Model Serialization                       │
│                  (Final_models/model.pkl)                       │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                     SERVING LAYER                               │
│                                                                 │
│         FastAPI Application  ──►  /predict  endpoint           │
│                                       │                        │
│                              CSV Upload & Inference            │
│                              HTML Result Visualization         │
└─────────────────────────────────────────────────────────────────┘
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🔬 ML Pipeline Stages

### 1. 📥 Data Ingestion
- Pulls phishing dataset records from **MongoDB Atlas**
- Converts collections into **pandas DataFrames**
- Stores processed features in a **feature store**
- Automatically performs **train/test split**

### 2. ✅ Data Validation
- Validates incoming data against a defined **schema**
- Checks for missing or unexpected columns
- Runs **Kolmogorov-Smirnov statistical tests** for data drift detection
- Generates drift reports to flag distribution shifts

### 3. 🔄 Data Transformation
- Handles missing values using **KNN Imputer**
- Builds and persists a **scikit-learn preprocessing pipeline**
- Outputs NumPy arrays ready for model training

### 4. 🤖 Model Training & Selection

Six algorithms are evaluated and the best is selected automatically via **GridSearchCV**:

| Model | Type |
|---|---|
| Logistic Regression | Linear |
| K-Nearest Neighbors | Instance-based |
| Decision Tree | Tree-based |
| Random Forest | Ensemble |
| AdaBoost | Boosting |
| Gradient Boosting | Boosting |

Metrics tracked: **F1 Score**, **Precision**, **Recall**

### 5. 📊 Experiment Tracking
- All runs logged to **MLflow** (local `mlflow.db`)
- Remote tracking synced to **DagsHub**
- Metrics, parameters, and model artifacts versioned per experiment

### 6. 🚀 Prediction Service
- Final model and preprocessor serialized to `Final_models/`
- Served via **FastAPI** REST endpoints
- Accepts CSV uploads, returns predictions as a rendered HTML table

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🧰 Tech Stack

<table>
  <tr>
    <td align="center" width="140"><img src="https://skillicons.dev/icons?i=python" width="48"/><br/><b>Python</b></td>
    <td align="center" width="140"><img src="https://skillicons.dev/icons?i=fastapi" width="48"/><br/><b>FastAPI</b></td>
    <td align="center" width="140"><img src="https://skillicons.dev/icons?i=mongodb" width="48"/><br/><b>MongoDB</b></td>
    <td align="center" width="140"><img src="https://skillicons.dev/icons?i=docker" width="48"/><br/><b>Docker</b></td>
    <td align="center" width="140"><img src="https://skillicons.dev/icons?i=github" width="48"/><br/><b>GitHub Actions</b></td>
    <td align="center" width="140"><img src="https://skillicons.dev/icons?i=aws" width="48"/><br/><b>AWS</b></td>
  </tr>
  <tr>
    <td align="center"><img src="https://skillicons.dev/icons?i=sklearn" width="48"/><br/><b>Scikit-Learn</b></td>
    <td align="center"><img src="https://img.shields.io/badge/-MLflow-0194E2?style=flat&logo=mlflow&logoColor=white" height="48" style="padding:10px"/><br/><b>MLflow</b></td>
    <td align="center"><img src="https://img.shields.io/badge/-DagsHub-FC4F4F?style=flat&logo=dagshub&logoColor=white" height="48" style="padding:10px"/><br/><b>DagsHub</b></td>
    <td align="center"><img src="https://skillicons.dev/icons?i=numpy" width="48"/><br/><b>NumPy</b></td>
    <td align="center"><img src="https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white" height="48" style="padding:10px"/><br/><b>Pandas</b></td>
    <td align="center"><img src="https://skillicons.dev/icons?i=git" width="48"/><br/><b>Git</b></td>
  </tr>
</table>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 📁 Project Structure

```
Network_security/
│
├── 📂 Networksecurity/                  # Core Python package
│   ├── 📂 components/                   # Pipeline stage implementations
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── Model_Trainer.py
│   │
│   ├── 📂 entity/                       # Config & artifact data classes
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   │
│   ├── 📂 Pipeline/                     # Orchestration layer
│   │   └── Training_pipeline.py
│   │
│   ├── 📂 utils/                        # Shared utilities
│   │   ├── main_utils/
│   │   └── ml_utils/
│   │
│   ├── 📂 Logging/                      # Custom logging
│   ├── 📂 Exception/                    # Custom exceptions
│   └── 📂 Constants/                    # Config constants
│
├── 📂 .github/workflows/                # CI/CD pipeline definitions
├── 📂 Final_models/                     # Serialized model & preprocessor
├── 📂 Network_Data/                     # Raw phishing dataset
├── 📂 data_schema/                      # Schema validation files
├── 📂 prediction_output/                # Prediction result CSVs
├── 📂 templates/                        # Jinja2 HTML templates
├── 📂 valid_data/                       # Validation split
│
├── 🐳 Dockerfile                        # Container definition
├── ⚙️  app.py                           # FastAPI application entry point
├── 🚀 main.py                           # Training pipeline runner
├── 📤 push_data.py                      # MongoDB data loader
├── 📋 requirements.txt                  # Python dependencies
├── 🔧 setup.py                          # Package setup
└── 🗄️  mlflow.db                        # Local MLflow tracking database
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Redirects to interactive Swagger docs |
| `GET` | `/train` | Triggers the full training pipeline |
| `POST` | `/predict` | Upload a CSV file to receive phishing predictions |

### Prediction Flow

```
Client ──► POST /predict (CSV file)
               │
               ▼
        Load preprocessor.pkl
               │
               ▼
          Load model.pkl
               │
               ▼
        Run inference on features
               │
               ▼
  Return HTML table with predicted_column
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 📈 Model Performance

The pipeline evaluates all candidate models and automatically selects the best performer after hyperparameter tuning. Tracked metrics per experiment:

| Metric | Description |
|--------|-------------|
| **F1 Score** | Harmonic mean of Precision and Recall |
| **Precision** | Proportion of true phishing predictions that were correct |
| **Recall** | Proportion of actual phishing sites correctly identified |

All experiments and metric histories are available in the MLflow / DagsHub dashboard.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🚀 Running Locally

### Prerequisites

- Python 3.10+
- Docker (for MongoDB)
- MongoDB URI (local or Atlas)

---

### 1. Clone the Repository

```bash
git clone https://github.com/Chinmaypalshetkar74/Network_security.git
cd Network_security
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv netvenv

# Windows
netvenv\Scripts\activate

# macOS / Linux
source netvenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_DB_KEY=your_mongodb_connection_string
```

### 5. Start MongoDB (Docker)

```bash
docker start mongodb
```

### 6. Push Data to MongoDB

```bash
python push_data.py
```

### 7. Run the Training Pipeline

```bash
python main.py
```

### 8. Start the FastAPI Server

```bash
python app.py
```

Open **[http://localhost:8000/docs](http://localhost:8000/docs)** to access the interactive Swagger UI.

---

### 🐳 Run with Docker

```bash
docker build -t network-security .
docker run -p 8000:8000 --env-file .env network-security
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## ⚙️ CI/CD & Deployment

The project includes a **GitHub Actions** workflow (`.github/workflows/`) that automates:

- ✅ Code linting and testing
- 🐳 Docker image build
- ☁️ Push to container registry
- 🚀 Deploy to AWS (ECR + EC2 / ECS)

> **Note:** AWS deployment steps (requiring `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and related secrets) are intentionally excluded from this public repository for security reasons. The CI/CD pipeline is fully functional once credentials are configured in GitHub Secrets. All local development, training pipeline, and API functionality remain fully operational.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🔮 Future Enhancements

- [ ] 🔁 Automated model retraining scheduler
- [ ] 📡 Real-time model monitoring & alerting
- [ ] 🗄️ Data versioning with DVC
- [ ] 🏪 Feature store integration
- [ ] ☸️ Kubernetes (K8s) deployment
- [ ] 🌐 Full AWS production deployment (ECR + ECS/EC2)
- [ ] 🔍 Advanced model explainability (SHAP / LIME)
- [ ] 📊 Live dashboard for prediction analytics

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🎓 Learning Outcomes

This project demonstrates hands-on expertise in:

| Domain | Skills |
|--------|--------|
| **MLOps** | End-to-end pipeline automation, model lifecycle management |
| **Backend** | FastAPI REST API design, async endpoints |
| **Data Engineering** | MongoDB integration, data validation, drift detection |
| **ML Engineering** | Multi-model evaluation, hyperparameter tuning, serialization |
| **DevOps** | Docker containerization, GitHub Actions CI/CD |
| **Experiment Tracking** | MLflow runs, metric logging, DagsHub remote tracking |
| **Software Engineering** | Modular architecture, custom exceptions, structured logging |

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 👨‍💻 Author

<div align="center">

### **Chinmay Palshetkar**

*Passionate about Data , Artificial Intelligence, Machine Learning, Data Science, MLOps ,Generative AI , AI Agents , AIOps,*
*and building production-ready AI and Analytical systems.*

[![GitHub](https://img.shields.io/badge/GitHub-Chinmaypalshetkar74-181717?style=for-the-badge&logo=github)](https://github.com/Chinmaypalshetkar74)

<br/>

## Guide resources -KrishAI Technologies - udemy Krish naik Complete Mlops Bootcamp course

<img width="1026" height="670" alt="image" src="https://github.com/user-attachments/assets/0ff58927-fd88-4aa9-ac71-34f96364acfd" />

<img width="1012" height="601" alt="image" src="https://github.com/user-attachments/assets/b20d8989-1254-4195-b127-f92dad0e6b7c" />

<img width="1020" height="630" alt="image" src="https://github.com/user-attachments/assets/3a5523f2-a9fb-4e11-9265-9df477049b47" />

<img width="1913" height="1026" alt="image" src="https://github.com/user-attachments/assets/3b402311-1d61-45ea-adc8-dfb9c2302eed" />

<img width="1919" height="1020" alt="Screenshot 2026-05-31 115551" src="https://github.com/user-attachments/assets/449aa660-f0ae-460e-989f-f1282bd3b473" />

<img width="1919" height="1020" alt="Screenshot 2026-05-31 115551" src="https://github.com/user-attachments/assets/5ad70582-7bae-4ce2-af24-22827e3167b9" />

<img width="1906" height="1024" alt="Screenshot 2026-05-31 122917" src="https://github.com/user-attachments/assets/b91bfd8b-a43e-4c60-a4a3-6a63d499b78c" /> 

<img width="865" height="1021" alt="Screenshot 2026-05-31 195916" src="https://github.com/user-attachments/assets/6d483715-4150-4dee-87b4-474c1b26f3ed" />

⭐ **If you found this project helpful, please give it a star!** ⭐

</div>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<div align="center">

*Built with ❤️ as an MLOps Capstone Project*

</div>
