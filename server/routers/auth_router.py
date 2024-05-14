from bll.auth_bll import AuthBLL
from flask import Blueprint, jsonify, request, make_response

auth_bll = AuthBLL()

auth_route = Blueprint("auth", __name__)


@auth_route.route("/login", methods=["POST"])
def login():
    username = request.json['username']
    password = request.json["password"]
    token = auth_bll.get_token(username, password)

    if token is not None:
        return make_response({"token": token}, 200)
    else:
        return make_response({"error": "Not Authorized"}, 401)
