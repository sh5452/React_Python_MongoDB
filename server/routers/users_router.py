from flask import Blueprint, jsonify, request, Response
from bll.users_bll import UsersBll

users=Blueprint('users', __name__)
users_bll=UsersBll()

@users.route('/',methods=['GET'] )
def get_all_users():
    users=users_bll.get_all_users()
    return  jsonify(users)

@users.route('/', methods=['POST'])
def add_user():
    user=request.json
    status=users_bll.add_user(user)
    return jsonify(status)

@users.route('/<id>/', methods=['PUT'])
def update_user(id):
    obj=request.json
    print(obj)
    print(id)
    result=users_bll.update_user(id, obj)
    return jsonify(result)

users.route('/<id>/', methods=['DELETE'])
def delete_user(id):
    result=users_bll.delele_user(id)
    return jsonify(result)




