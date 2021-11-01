from pyspark.sql import SparkSession
from datetime import datetime, timezone
from spark_jobs.analyzers import run_analyzer
from kafka_connector import connector
from db.profile_db import DataAnalyzerDB


def analyze_join_data(source_details, user_details):
    kafka = None
    try:
        db = DataAnalyzerDB()

        db.insert_profiling_status_multiple(
            source_details,
            user_details,
            "In Progress",
            "Started analyzing data",
        )

        kafka = connector.KafkaConnector()

        spark = SparkSession.builder.config(
            "spark.jars", "deequ-1.0.3.jar,ojdbc6.jar"
        ).getOrCreate()

        spark.conf.set("spark.sql.debug.maxToStringFields", 1000)

        url = (
            f"jdbc:oracle:thin:{source_details['connection_config']['username']}/{source_details['connection_config']['password']}"
            + f"@//{source_details['connection_config']['host']}:{source_details['connection_config']['port']}"
            + f"/{source_details['connection_config']['authDb']}"
        )
        # url = (
        #     f"jdbc:oracle:thin:{'abcdef'}/{'123456789'}"
        #     + f"@//{'http://192.168.1.211'}:{'3082'}"
        #     + f"/{'qwerttyyuu'}"
        # )

        print(f"[{datetime.now(timezone.utc)}] started profiling")

        df1 = df2 = None

        df1 = (
            spark.read.format("jdbc")
            .options(
                url=url,
                dbtable='"{0}"."{1}"'.format(
                    source_details["join"][0]["databaseName"],
                    source_details["join"][0]["tableName"],
                ),
                # dbtable='"{0}"."{1}"'.format(
                #     "public",
                #     "accounts",
                # ),
                # user=source_details["connection_config"]["username"],
                user='abcdef',
                # password=source_details["connection_config"]["password"],
                password='123456789',
                driver="oracle.jdbc.driver.OracleDriver",
            )
            .load()
        )

        df2 = (
            spark.read.format("jdbc")
            .options(
                url=url,
                dbtable='"{0}"."{1}"'.format(
                    source_details["join"][1]["databaseName"],
                    source_details["join"][1]["tableName"],
                ),
                # dbtable='"{0}"."{1}"'.format(
                #     "public",
                #     "PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
                # ),
                user='abcdef',
                password='123456789',
                driver="oracle.jdbc.driver.OracleDriver",
            )
            .load()
        )

        df = df1.join(
            df2,
            df2[source_details["join"][1]["mappingColumn"]]
            == df1[source_details["join"][0]["mappingColumn"]],
        )
        # df = df1.join(
        #     df2,
        #     df2["product_id"]
        #     == df1["username"],
        # )

        analysisResult_json = run_analyzer(
            spark, df, source_details["analyzer_params"]
        )

        # fake = {
        #     "operation": "histogram",
        #     "column": [
        #         "username"
        #     ],
        #     "maxBins": 4,
        #     "filters": {
        #         "conditions": [
        #             {
        #                 "column": "user_id",
        #                 "operation": "lt",
        #                 "value": "500"
        #             }
        #         ],
        #         "relationships": ["and"]
        #     }
        # }


        # analysisResult_json = run_analyzer(
        #     spark, df, fake
        # )

        db.save_column_Analysis_multiple(
            source_details, user_details, analysisResult_json
        )

        print(f"[{datetime.now(timezone.utc)}] Done profiling")

        kafka.update_analyzer_status_multiple(
            source_details,
            user_details,
            "Done",
            "Completed profiling  the data",
        )

    except Exception as err:
        if kafka is not None:
            kafka.update_analyzer_status_multiple(
                source_details,
                user_details,
                "Failed",
                "Error occurred while profiling the data",
            )

        print(err)
