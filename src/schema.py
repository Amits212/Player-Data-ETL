from pyspark.sql.types import StructType, StructField, StringType, IntegerType

def get_player_schema():
    return StructType([
        StructField("Name", StringType(), True),
        StructField("Age", IntegerType(), True),
        StructField("Nationality", StringType(), True),
        StructField("Fifa Score", IntegerType(), True),
        StructField("Club", StringType(), True),
        StructField("Value", StringType(), True),
        StructField("Salary", StringType(), True),
        StructField("UpdatedAt", StringType(), True)
    ])
