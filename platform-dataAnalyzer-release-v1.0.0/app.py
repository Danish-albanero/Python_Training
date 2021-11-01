from dotenv import load_dotenv

load_dotenv()

import os
from flask import Flask, request, jsonify
from auth.middleware import authenticate
from connector.connector_service import get_connection_config
from spark_jobs.handler import analyzers
from spark_jobs.join.handler import join_analyzers
from multiprocessing import Process
from uuid import uuid4

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add(
        "Access-Control-Allow-Headers", "authorization,content-type"
    )
    response.headers.add(
        "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
    )
    response.headers.add("Access-Control-Allow-Credentials", "true")
    if request.method == "OPTIONS":
        response.status = 200

    return response


app.before_request(authenticate)


@app.post("/data-analyzer/start")
def start_analyzing():
    source_details = request.json
    source_type = source_details["sourceType"]

    if source_type not in analyzers:
        return (
            jsonify(
                {
                    "message": f"Unsupported source {source_type}.",
                    "success": False,
                }
            ),
            400,
        )

    connection_config = get_connection_config(
        source_type, source_details["connectorId"], request.user_details
    )
    source_details["connection_config"] = connection_config
    source_details["id"] = str(uuid4())

    process = Process(
        target=analyzers[source_type].analyze_data,
        args=(source_details, request.user_details),
    )

    process.start()

    return (
        jsonify(
            {
                "message": "Data analyzer has been initiated.",
                "success": True,
            }
        ),
        202,
    )


@app.post("/data-analyzer/join/start")
def start_analyzing_data():
    source_details = request.json
    source_type = source_details["sourceType"]

    if source_type not in join_analyzers:
        return (
            jsonify(
                {
                    "message": f"Unsupported source {source_type}.",
                    "success": False,
                }
            ),
            400,
        )

    connection_config = get_connection_config(
        source_type, source_details["connectorId"], request.user_details
    )
    source_details["connection_config"] = connection_config
    source_details["id"] = str(uuid4())

    process = Process(
        target=join_analyzers[source_type].analyze_join_data,
        args=(source_details, request.user_details),
    )

    process.start()

    return (
        jsonify(
            {
                "message": "Data analyzer has been initiated.",
                "success": True,
            }
        ),
        202,
    )


if __name__ == "__main__":
    PORT = 3082
    app.run(host="0.0.0.0", port=PORT)
