

def write_data(df, output_path: str):
    df.write.partitionBy("Continent").mode("overwrite").parquet(output_path)
