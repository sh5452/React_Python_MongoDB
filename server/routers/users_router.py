from flask import Blueprint, jsonify, request, Response, make_response
from bll.users_bll import UsersBll
from bll.auth_bll import AuthBLL
import logging
import json
from bson import ObjectId

users=Blueprint('users', __name__)
users_bll=UsersBll()
auth_bll=AuthBLL()

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

@users.route('/',methods=['GET'] )
def get_all_users():
    if request.headers and request.headers.get("x-access-token"):
        token = request.headers.get("x-access-token")
        exist = auth_bll.verify_token(token)

        if exist == True:
            prods = users_bll.get_all_users()
            return make_response({"products": prods}, 200)
        else:
            return make_response({"error": "Not authorized"}, 401)
    else:
        return make_response({"error": "Not authorized"}, 401)







# @users.route('/',methods=['GET'] )
# def get_all_users():
#     user_list = users_bll.get_all_users()
#     logging.debug(f'Request data:\n {user_list} \n') 
#     return Response(json.dumps(user_list, cls=CustomJSONEncoder), mimetype='application/json')


@users.route('/', methods=['POST'])
def add_user():
    user = request.json
    result = users_bll.add_user(user)
    logging.debug(f'Request data:\n USER : {user} \n\n USERs_LIST : {result}\n\n')  
    return Response(json.dumps(result, cls=CustomJSONEncoder), mimetype='application/json', status=201)


@users.route('/<id>/', methods=['PUT'])
def update_user(id):
    user_data = request.json
    logging.debug(f'Updating user {id} with data: {user_data}')
    result, status = users_bll.update_user(id, user_data)
    return jsonify(result), status

@users.route('/<id>/', methods=['DELETE'])
def delete_user(id):
    logging.debug(f'Deleting user {id}')    
    result, status = users_bll.delele_user(id)
    return jsonify(result), status