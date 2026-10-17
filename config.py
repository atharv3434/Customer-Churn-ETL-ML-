import os
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, StringType, 
    IntegerType, DoubleType
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "customers.csv")
SILVER_DATA_PATH = os.path.join(BASE_DIR, "data", "silver", "customers_cleaned.parquet")
GOLD_DATA_PATH = os.path.join(BASE_DIR, "data", "gold", "customer_features.parquet")
MODEL_OUTPUT_PATH = os.path.join(BASE_DIR, "data", "gold", "churn_model")

# Explicit input schema definition
RAW_SCHEMA = StructType([
    StructField("customer_id", StringType(), False),
    StructField("gender", StringType(), True),
    StructField("senior_citizen", IntegerType(), True),
    StructField("tenure", IntegerType(), True),
    StructField("monthly_charges", DoubleType(), True),
    StructField("total_charges", DoubleType(), True),
    StructField("contract_type", StringType(), True),
    StructField("payment_method", StringType(), True),
    StructField("churn", StringType(), True)
])

def get_spark_session(app_name: str = "CustomerChurnETL") -> SparkSession:
    """Builds and returns a unified local Spark session."""
    return SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .config("spark.driver.memory", "2g") \
        .config("spark.sql.shuffle.partitions", "4") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .getOrCreate()
