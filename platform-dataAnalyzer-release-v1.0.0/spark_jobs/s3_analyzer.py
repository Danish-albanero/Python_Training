from pyspark.sql import SparkSession
from datetime import datetime, timezone
from spark_jobs.analyzers import run_analyzer
from kafka_connector import connector
from db.profile_db import DataAnalyzerDB


def analyze_data(source_details, user_details):
    kafka = None
    try:
        db = DataAnalyzerDB()

        db.insert_profiling_status(
            source_details,
            user_details,
            "In Progress",
            "Started analyzing data",
        )

        kafka = connector.KafkaConnector()

        spark = (
            SparkSession.builder.config(
                "spark.jars",
                "aws-java-sdk-1.7.4.2.jar,hadoop-aws-2.7.4.jar,deequ-1.0.3.jar",
            )
            .config(
                "spark.executor.extraJavaOptions",
                "-Dcom.amazonaws.services.s3.enableV4=true",
            )
            .config(
                "spark.driver.extraJavaOptions",
                "-Dcom.amazonaws.services.s3.enableV4=true",
            )
            .getOrCreate()
        )

        spark.conf.set("spark.sql.debug.maxToStringFields", 1000)
        hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()
        hadoop_conf.set(
            "fs.s3a.aws.credentials.provider",
            "org.apache.hadoop.fs.s3a.BasicAWSCredentialsProvider",
        )
        hadoop_conf.set(
            "fs.s3a.access.key",
            source_details["connection_config"]["accessKeyId"],
        )
        hadoop_conf.set(
            "fs.s3a.secret.key",
            source_details["connection_config"]["secretAccessKey"],
        )
        hadoop_conf.set(
            "fs.s3a.endpoint", f"s3.{source_details['region']}.amazonaws.com"
        )

        print(f"[{datetime.now(timezone.utc)}] started profiling")

        df = None
        if source_details["tableName"].endswith(".csv"):
            df = spark.read.csv(
                f"s3a://{source_details['databaseName']}/{source_details['tableName']}/",
                inferSchema=True,
                header=True,
            )
        elif source_details["tableName"].endswith(".parquet"):
            df = spark.read.parquet(
                f"s3a://{source_details['databaseName']}/{source_details['tableName']}/",
            )
        else:
            raise Exception(
                f"Unsupported format for the file {source_details['tableName']}"
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

    except Exception as err:
        if kafka is not None:
            kafka.update_analyzer_status(
                source_details,
                user_details,
                "Failed",
                "Error occurred while profiling the data",
            )

        print(err)
