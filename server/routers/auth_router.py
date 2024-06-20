from flask import Blueprint, request, jsonify
from bll.auth_bll import AuthBLL

auth_route = Blueprint('auth', __name__)
auth_bll = AuthBLL()

@auth_route.route('/login', methods=['POST'])
def login():
    auth_data = request.get_json()
    token = auth_bll.get_token(auth_data['username'], auth_data['password'])
    if token:
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401