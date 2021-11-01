from flask.wrappers import Response
import requests
import os
from flask import make_response

from requests import status_codes

ALBANERO_CONNECTOR_SERVICE_URI = 'https://api.dev.albanero.io/streaming'

DATABASES = {"postgresql", "oracle"}
DATASTORES = {"s3"}


def get_datastore(connector_id, user_details):
    data_store_api = (
        f"{ALBANERO_CONNECTOR_SERVICE_URI}/connector/data-store/{connector_id}"
    )
    auth_headers = {"Authorization": user_details["token"]}
    response = requests.get(data_store_api, headers=auth_headers)

    if response.status_code == 200:
        return response.json()["payload"]
    elif response.status_code >= 400:
        raise Exception(response.content)


def get_database(connector_id, user_details):
    data_store_api = (
        f"{ALBANERO_CONNECTOR_SERVICE_URI}/connector/database/{connector_id}"
    )
    #auth_headers = {"Authorization": user_details["token"]}
    #response = requests.get(data_store_api, headers=auth_headers)
    dictionary = {"connectorId":"2df64ba4-fb49-46c8-a9d3-774a202debaf","title":"test","dataStoreType":"S3","dbType":"SQL","userId":"PRODUCTS_07d544e2_20d4_4c77_adfb_7b2782b619fb","databaseName":"public"}

    response = make_response(dictionary,200)
    print(response.status_code)
    
    

    if response.status_code == 200:
        #return response.json()["payload"]
        return dictionary

        
    elif response.status_code >= 400:
        raise Exception(response.content)


def get_connection_config(source_type, connector_id, user_details):
    connector = None

    if source_type in DATABASES:
        connector = get_database(connector_id, user_details)
    elif source_type in DATASTORES:
        connector = get_datastore(connector_id, user_details)
    else:
        raise Exception(f"Unsupported data source {source_type}")
    print(connector,"hi")

    connector.pop("connectorId", None)
    connector.pop("title", None)
    connector.pop("dataStoreType", None)
    connector.pop("dbType", None)
    connector.pop("userId", None)
    print(connector)

    return connector
