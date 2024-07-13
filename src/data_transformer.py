from pyspark.sql.functions import udf, col, lit
from pyspark.sql.types import DecimalType, StringType
from src.config import AWS_S3_BUCKET


def convert_currency(value):
    if value:
        value = value.replace('€', '').replace('M', 'e6').replace('K', 'e3')
        return float(eval(value))
    return None


def transform_data(df):
    convert_currency_udf = udf(convert_currency, DecimalType(10, 2))

    df = df.withColumn("Value", convert_currency_udf(col("Value")))
    df = df.withColumn("Salary", convert_currency_udf(col("Salary")))

    continent_mapping = {
        'Argentina': 'South America',
        'Brazil': 'South America',
        'Germany': 'Europe',
        'Spain': 'Europe',
        'Portugal': 'Europe',
        'Uruguay': 'South America',
        'Poland': 'Europe',
        'Belgium': 'Europe',
        'Chile': 'South America',
        'Croatia': 'Europe',
        'Wales': 'Europe',
        'Italy': 'Europe',
        'Slovenia': 'Europe',
        'France': 'Europe',
        'Gabon': 'Africa',
    }

    def get_continent(nationality):
        return continent_mapping.get(nationality, 'Unknown')

    get_continent_udf = udf(get_continent, StringType())
    df = df.withColumn("Continent", get_continent_udf(col("Nationality")))

    return df
