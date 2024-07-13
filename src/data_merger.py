from pyspark.sql import DataFrame

def merge_data(existing_df: DataFrame, new_df: DataFrame) -> DataFrame:
    merged_df = existing_df.alias("existing").join(
        new_df.alias("new"),
        on="Name",
        how="outer"
    ).select(
        col("new.Name").alias("Name"),
        col("new.Age").alias("Age"),
        col("new.Nationality").alias("Nationality"),
        col("new.Fifa Score").alias("Fifa Score"),
        col("new.Club").alias("Club"),
        col("new.Value").alias("Value"),
        col("new.Salary").alias("Salary"),
        col("new.Continent").alias("Continent"),
        col("new.UpdatedAt").alias("UpdatedAt")
    ).withColumn(
        "last_updated",
        lit(datetime.now())
    )
    return merged_df
