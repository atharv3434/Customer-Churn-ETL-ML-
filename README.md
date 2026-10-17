# PySpark End-to-End Customer Churn ETL & ML Pipeline

A scalable batch-processing pipeline built on Apache Spark using the **Medallion Architecture**.

## Architecture Overview
1. **Raw Tier**: Ingestion of raw business logs into Spark DataFrame with schema enforcement.
2. **Silver Tier**: Deduplication, data validation, and automated imputation of missing revenue columns.
3. **Gold Tier**: Feature engineering (aggregates, tenure cohorts, high-value spenders) partitioned by `contract_type`.
4. **Machine Learning**: An end-to-end Spark MLlib Pipeline using Vector Assemblers and a Random Forest Classifier to score customer churn probability.

## Setup & Execution

### 1. Prerequisites
- Python 3.9+
- Java 8 or Java 11 (required for PySpark execution)

### 2. Installation
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
