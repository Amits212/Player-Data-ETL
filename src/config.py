import os

AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

SPARK_APP_NAME = os.getenv("SPARK_APP_NAME", "PlayerDataETL")
SPARK_MASTER = os.getenv("SPARK_MASTER", "local[*]")
