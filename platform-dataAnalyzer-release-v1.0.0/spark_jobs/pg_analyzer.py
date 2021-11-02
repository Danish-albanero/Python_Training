from pyspark.sql import SparkSession
from datetime import datetime, timezone
from spark_jobs.analyzers import run_analyzer
from kafka_connector import connector
from db.profile_db import DataAnalyzerDB
from pyspark.conf import SparkConf
from pyspark.context import SparkContext


def analyze_data(source_details, user_details):
    kafka = None
    
    db = DataAnalyzerDB()

    db.insert_profiling_status(
        source_details,
        user_details,
        "In Progress",
        "Started analyzing data",
    )

    kafka = connector.KafkaConnector()
    print(kafka)

    spark = SparkSession.builder.config(
        "spark.jars", "deequ-1.0.3.jar,postgresql-42.2.14.jar"
    ).getOrCreate()
    print(spark)

    spark.sparkContext.addPyFile(r"C:\Users\Dell\Desktop\albanero\platform-dataAnalyzer-release-v1.0.0\deequ-1.0.3.jar")

    # conf = SparkConf().set("spark.jars", "deequ-1.0.3.jar,postgresql-42.2.14.jar")
    # print(conf)
    # spark = SparkContext(conf=conf)
    # print(spark)

    # spark = SparkSession.builder.config('spark.driver.extraClassPath', 'deequ-1.0.3.jar').getOrCreate()
    # print(spark)
    # spark.sparkContext._jsc.addJar(r'C:\Users\Dell\Desktop\albanero\platform-dataAnalyzer-release-v1.0.0\deequ-1.0.3.jar')


    # spark.sparkContext.addPyFile(r"C:\Users\Dell\Desktop\albanero\platform-dataAnalyzer-release-v1.0.0\deequ-1.0.3.jar")

    
    
    
    print(f"[{datetime.now(timezone.utc)}] started profiling")

    spark.conf.set("spark.sql.debug.maxToStringFields", 1000)

    print(f"[{datetime.now(timezone.utc)}] started profiling")

    # url = f"jdbc:postgresql://{source_details['connection_config']['host']}:{source_details['connection_config']['port']}/{source_details['connection_config']['authDb']}"
    url = "jdbc:postgresql://localhost:5432/"

    df = (
        spark.read.format("jdbc")
        .options(
            url=url,
            # dbtable=f'"{source_details["databaseName"]}"."{source_details["tableName"]}"',
            dbtable='sparkDB.SparkTable',
            # user=source_details["connection_config"]["username"],
            user='postgres',
            # password=source_details["connection_config"]["password"],
            password='1333545',
            driver="org.postgresql.Driver",
        )
        .load()
    )

    analysisResult_json = run_analyzer(
        spark, df, source_details["analyzer_params"]
    )

    

    db.save_column_Analysis(
        source_details, user_details, analysisResult_json
    )

    print(f"[{datetime.now(timezone.utc)}] Done profiling")

    kafka.update_analyzer_status(
        source_details,
        user_details,
        "Done",
        "Completed profiling  the data",
    )

 