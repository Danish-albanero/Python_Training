from kafka import KafkaProducer
import json
import os
from utils import datetime_encoder, helpers

# ALBANERO_KAFKA_BROKERS = 'kafka-1:9092'
ALBANERO_KAFKA_BROKERS = 'localhost:9092'
ALBANERO_KAFKA_STATUS_TOPIC = 'data-profile-status'


class KafkaConnector:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v, cls=datetime_encoder.DateTimeEncoder).encode("utf-8")
        )

    def send_message(self, topic, message):
        self.producer.send(topic, value=message).get(timeout=60)
        

    def update_analyzer_status(
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
            "userId": "1231231231321231",
            # "databaseName": source_details["databaseName"],
            "databaseName": "public",
            # "tableName": source_details["tableName"],
            "tableName": "PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb",
            "status": status,
            "message": message,
            "updatedAt": helpers.current_time_ms(),
        }
        print(status_dict)

        self.send_message(ALBANERO_KAFKA_STATUS_TOPIC, status_dict)

    def update_analyzer_status_multiple(
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
            "description":  "analyzer_params",
            # "userId": user_details["userId"],
            "userId": "1231231231321231",
            "databaseName": "joined",
            "tableName": "joined",
            "status": status,
            "message": message,
            "updatedAt": helpers.current_time_ms(),
        }

        self.send_message(ALBANERO_KAFKA_STATUS_TOPIC, status_dict)
