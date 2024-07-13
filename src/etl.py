import boto3
import os
import pandas as pd
from pyspark.sql import SparkSession
import logging
from config import AWS_S3_BUCKET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, SPARK_APP_NAME, SPARK_MASTER

spark = SparkSession.builder \
    .appName(SPARK_APP_NAME) \
    .master(SPARK_MASTER) \
    .getOrCreate()


s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def upload_to_s3(file_path, bucket_name, object_name):
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        logging.log(f"File {file_path} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        logging.log(f"Error uploading file: {e}")


def process_and_upload_data(input_file, output_path):
    df = pd.read_csv(input_file)

    spark_df = spark.createDataFrame(df)

    parquet_path = f"{output_path}/players.parquet"
    spark_df.write.mode("overwrite").parquet(parquet_path)

    s3_key = "players_data/players.parquet"
    upload_to_s3(parquet_path, AWS_S3_BUCKET, s3_key)


if __name__ == "__main__":
    input_file = "data/FIFA-18-Video-Game-Player-Stats.csv"
    output_path = "data/parquet"

    process_and_upload_data(input_file, output_path)
