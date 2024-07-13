from pyspark.sql import SparkSession
from src.schema import get_player_schema

def load_data(spark: SparkSession, file_path: str):
    return spark.read.csv(file_path, header=True, schema=get_player_schema())
