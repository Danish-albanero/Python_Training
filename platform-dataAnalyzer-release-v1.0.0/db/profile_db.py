import os
from pymongo import MongoClient
from utils import helpers

# ALBANERO_DB_URI = 'mongodb://localhost:27017,localhost:27018/?replicaSet=rs0'
ALBANERO_DB_URI = 'mongodb://localhost:27017'

ALBANERO_DB_DATA_PROFILE = 'dataProfileDB'
ALBANERO_COL_COLUMN_ANALYSIS = 'columnAnalysis'
ALBANERO_COL_PROFILE_STATUS = 'profileStatus'

ALBANERO_COL_COLUMN_ANALYSIS_JOINED = 'columnAnalysisMultiple'
ALBANERO_COL_PROFILE_STATUS_JOINED = 'profileStatusMultiple'


class DataAnalyzerDB:
    def __init__(self):
        self.mongo_client = MongoClient(ALBANERO_DB_URI)

    def save_column_Analysis(
        self, source_details, user_details, analysisResult
    ):
        columnAnalysis = {
            # "analysisId": source_details["id"],
            "analysisId": "12334234",
            # "connectorId": source_details["connectorId"],
            "connectorId": "2df64ba4-fb49-46c8-a9d3-774a202debaf",
            # "sourceType": source_details["sourceType"],
            "sourceType": "postgresql",
            # "userId": user_details["userId"],
            "userId": "PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
            # "databaseName": source_details["databaseName"],
            "databaseName": "public",
            # "tableName": source_details["tableName"],
            "tableName":"accounts" ,
            "timestamp": helpers.current_time_ms(),
            "analysisResult": analysisResult,
        }

        db = self.mongo_client[ALBANERO_DB_DATA_PROFILE]
        collection = db[ALBANERO_COL_COLUMN_ANALYSIS]
        collection.insert_one(columnAnalysis)

    def save_column_Analysis_multiple(
        self, source_details, user_details, analysisResult
    ):
        columnAnalysis = {
            # "analysisId": source_details["id"],
            "analysisId": "12334234",
            # "connectorId": source_details["connectorId"],
            "connectorId": "2df64ba4-fb49-46c8-a9d3-774a202debaf",
            # "sourceType": source_details["sourceType"],
             "sourceType": "postgresql",
            # "userId": user_details["userId"],
             "userId": "PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
            # "databaseName": source_details["databaseName"],
            # "tableName": source_details["tableName"],
            "timestamp": helpers.current_time_ms(),
            "analysisResult": analysisResult,
        }

        db = self.mongo_client[ALBANERO_DB_DATA_PROFILE]
        collection = db[ALBANERO_COL_COLUMN_ANALYSIS_JOINED]
        collection.insert_one(columnAnalysis)

    def insert_profiling_status(
        self, source_details, user_details, status, message
    ):
        status_dict = {
            # "id": source_details["id"],
            "id": "123243443",
            # "connectorId": source_details["connectorId"],
            "connectorId": "2df64ba4-fb49-46c8-a9d3-774a202debaf",
            # "sourceType": source_details["sourceType"],
            "sourceType": "postgresql",
            "type": "analysis",
            # "name": source_details["name"],
            "name": "test",
            # "description": source_details["description"],
            "description": "analyzer_params",
            # "userId": user_details["userId"],
            "userId": "PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
            # "databaseName": source_details["databaseName"],
            "databaseName": "public",
            # "tableName": source_details["tableName"],
            "tableName":"PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
            "startedAt": helpers.current_time_ms(),
            "status": status,
            "message": message,
        }

        db = self.mongo_client[ALBANERO_DB_DATA_PROFILE]
        collection = db[ALBANERO_COL_PROFILE_STATUS]

        collection.insert_one(status_dict)

    def insert_profiling_status(
        self, source_details, user_details, status, message
    ):
        status_dict = {
            # "id": source_details["id"],
            "id": "123243443",
            # "connectorId": source_details["connectorId"],
            "connectorId": "2df64ba4-fb49-46c8-a9d3-774a202debaf",
            # "sourceType": source_details["sourceType"],
            "sourceType": "postgresql",
            "type": "analysis",
            # "name": source_details["name"],
            "name": "test",
            # "description": source_details["description"],
             "description": "analyzer_params",
            # "userId": user_details["userId"],
            "userId": "PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
            # "databaseName": source_details["databaseName"],
            "databaseName": "public",
            # "tableName": source_details["tableName"],
            "tableName": "PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
            "startedAt": helpers.current_time_ms(),
            "status": status,
            "message": message,
        }

        db = self.mongo_client[ALBANERO_DB_DATA_PROFILE]
        collection = db[ALBANERO_COL_PROFILE_STATUS]

        collection.insert_one(status_dict)

    def insert_profiling_status_multiple(
        self, source_details, user_details, status, message
    ):
        status_dict = {
            # "id": source_details["id"],
            "id": "123243443",
            # "connectorId": source_details["connectorId"],
            "connectorId": "2df64ba4-fb49-46c8-a9d3-774a202debaf",
            # "sourceType": source_details["sourceType"],
            "sourceType": "postgresql",
            "type": "analysis",
            # "name": source_details["name"],
            "name": "test",
            # "description": source_details["description"],
            "description": "analyzer_params",
            # "userId": user_details["userId"],
            "userId": "PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
            # "databaseName": source_details["databaseName"],
            # "tableName": source_details["tableName"],
            "startedAt": helpers.current_time_ms(),
            "status": status,
            "message": message,
            # "operation": source_details["join"],
            "operation": "wqeqe",
        }

        db = self.mongo_client[ALBANERO_DB_DATA_PROFILE]
        collection = db[ALBANERO_COL_PROFILE_STATUS_JOINED]

        collection.insert_one(status_dict)
