from pyspark.sql import SparkSession


def get_spark_session():
    """
    Returns the Spark session.

    :return: SparkSession object.
    """
    spark = (
        SparkSession.builder.appName("airline-data-system")
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("INFO")
    return spark
