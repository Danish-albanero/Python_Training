import requests
import os


ALBANERO_AUTH_SERVICE_URI = 'https://api.dev.albanero.io'

auth_api = f"{ALBANERO_AUTH_SERVICE_URI}/auth/api/token/validate"


def authenticate(token):
    auth_headers = {"Authorization": token}
    response = requests.get(auth_api, headers=auth_headers)

    if response.status_code == 200:
        return response.json()["payload"]
    elif response.status_code >= 400 and response.status_code < 500:
        return None
