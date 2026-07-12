# ☁️ Week 4 - Azure Cloud Fundamentals and Data Pipeline Implementation using Azure Data Factory (ADF)

## 📌 Overview

This project is part of my **Celebal Technologies Internship 2026**. The objective of this assignment is to understand the core concepts of Microsoft Azure Cloud and build an end-to-end data pipeline using **Azure Storage Account** and **Azure Data Factory (ADF)**.

The pipeline reads a CSV file from Azure Blob Storage, validates metadata, copies the data to a destination container, and monitors successful execution.

---

## 🎯 Objective

- Understand Azure Cloud Fundamentals.
- Create and manage Azure Resources.
- Build an end-to-end ETL pipeline using Azure Data Factory.
- Learn Linked Services, Datasets, Pipelines, Activities, and IAM Roles.
- Validate file metadata and execute the pipeline successfully.

---

## ☁️ Azure Services Used

- Microsoft Azure Portal
- Azure Resource Group
- Azure Storage Account
- Azure Blob Storage
- Azure Data Factory (ADF)
- Azure IAM (Identity and Access Management)

---

## 🛠️ Technologies Used

- Microsoft Azure
- Azure Data Factory
- Azure Blob Storage
- Azure Portal
- CSV Dataset
- VS Code
- Jupyter Notebook

---

## 📂 Project Structure

```text
Week_4/
│
├── data/
│   └── Sample - Superstore.csv
│
├── screenshots/
│
├── week4_azure_adf_pipeline.ipynb
│
├── README.md
│
└── summary.md
```

---

## 📊 Dataset

**Dataset:** Sample Superstore Dataset

The dataset contains sales transaction information including:

- Customer Details
- Orders
- Products
- Sales
- Quantity
- Discount
- Profit
- Region
- Category

---

# 🚀 Assignment Tasks

## ✅ Task 1 – Azure Portal

- Explored Azure Portal
- Created Resource Group

### Deliverable

- Resource Group Screenshot

---

## ✅ Task 2 – Azure Storage

- Created Storage Account
- Created Blob Container
- Uploaded CSV Dataset

### Deliverables

- Storage Account Screenshot
- Blob Container Screenshot
- Uploaded CSV Screenshot

---

## ✅ Task 3 – Azure Data Factory

- Created Azure Data Factory
- Explored ADF Studio
- Created Linked Service
- Created Source Dataset
- Created Destination Dataset
- Used Get Metadata Activity

### Deliverables

- Linked Service Screenshot
- Dataset Screenshot
- Get Metadata Screenshot

---

## ✅ Task 4 – Pipeline Development

Built an Azure Data Factory pipeline using:

- Copy Data Activity
- Source Configuration
- Destination Configuration
- Metadata Validation

### Deliverable

Pipeline Design Screenshot

---

## ✅ Task 5 – Pipeline Execution

Executed the pipeline using:

- Debug
- Trigger

Verified successful execution through Monitor.

### Deliverable

Pipeline Success Screenshot

---

## ✅ Task 6 – IAM Roles

Configured Azure permissions by assigning:

- Reader Role
- Contributor Role

Ensured Azure Data Factory had access to Storage Account.

### Deliverable

IAM Role Assignment Screenshot

---

# 🏗️ Mini Project

## Problem Statement

Build a complete Azure Data Factory pipeline that reads a CSV file from Azure Blob Storage and copies it to a destination while validating metadata.

---

## Pipeline Flow

```text
CSV Dataset
      │
      ▼
Azure Blob Storage
      │
      ▼
Linked Service
      │
      ▼
Source Dataset
      │
      ▼
Get Metadata Activity
      │
      ▼
Copy Data Activity
      │
      ▼
Destination Dataset
      │
      ▼
Azure Blob Storage (Destination)
```

---

## 📈 Expected Output

- Resource Group Created
- Storage Account Created
- Blob Container Created
- Dataset Uploaded
- Linked Service Configured
- Source Dataset Created
- Destination Dataset Created
- Metadata Retrieved
- Pipeline Executed Successfully
- Data Copied Successfully
- IAM Roles Assigned

---

## 📁 Deliverables

| File | Description |
|------|-------------|
| `week4_azure_adf_pipeline.ipynb` | Azure implementation documentation with screenshots |
| `README.md` | Project documentation |
| `summary.md` | Assignment summary |
| `data/Sample - Superstore.csv` | Source dataset |
| `screenshots/` | Azure Portal screenshots |

---

## ▶️ Steps to Reproduce

1. Sign in to Azure Portal.
2. Create a Resource Group.
3. Create a Storage Account.
4. Create a Blob Container.
5. Upload the CSV dataset.
6. Create Azure Data Factory.
7. Configure Linked Services.
8. Create Source and Destination Datasets.
9. Build the pipeline.
10. Execute using Debug/Trigger.
11. Monitor execution.
12. Verify copied data.

---

## 📚 Learning Outcomes

Through this assignment I learned:

- Azure Cloud Fundamentals
- Azure Resource Management
- Azure Storage Services
- Azure Blob Storage
- Azure Data Factory Basics
- Linked Services
- Datasets
- Get Metadata Activity
- Copy Data Activity
- Pipeline Monitoring
- Azure IAM Roles
- End-to-End Cloud Data Pipeline Development

---

## 👨‍💻 Author

**Gaurav Gaikwad**

B.Tech – Information Technology

Sanjivani College of Engineering

Celebal Technologies Internship 2026

---

⭐ This project demonstrates the implementation of an end-to-end cloud data pipeline using Microsoft Azure Storage Account and Azure Data Factory (ADF), showcasing practical knowledge of Azure cloud services, data integration, and pipeline orchestration.