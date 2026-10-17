from pyspark.sql import SparkSession, DataFrame
from src.config import RAW_DATA_PATH, RAW_SCHEMA

def extract_raw_data(spark: SparkSession, file_path: str = RAW_DATA_PATH) -> DataFrame:
    """Reads CSV data applying strict typing and header validation."""
    print(f"[*] Extracting raw data from: {file_path}")
    df = spark.read \
        .option("header", "true") \
        .schema(RAW_SCHEMA) \
        .csv(file_path)
    
    print(f"[+] Successfully extracted {df.count()} records.")
    return df
