from flask import request, jsonify
from auth.auth_service import authenticate as auth


def authenticate():
    token = request.headers.get("Authorization")

    if token is None:
        return jsonify({"message": "Authentication token is missing.", "success": False}), 401

    result = auth(token)

    # if result is None:
    #     return jsonify({"message": "Could not authenticate the token.", "success": False}), 401

    # request.user_details = {"userId": result["userId"], "token": token}
    request.user_details = {"userId": 'danish', "token": token}
