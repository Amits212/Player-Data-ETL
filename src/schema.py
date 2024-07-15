from pyspark.sql.types import StructType, StructField, StringType, IntegerType

def get_player_schema():
    return StructType([
        StructField("Name", StringType()),
        StructField("Age", IntegerType()),
        StructField("Nationality", StringType()),
        StructField("Fifa Score", IntegerType()),
        StructField("Club", StringType()),
        StructField("Value", StringType()),
        StructField("Salary", StringType()),
        StructField("UpdatedAt", StringType())
    ])
