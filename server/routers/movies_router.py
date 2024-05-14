from flask import Blueprint, jsonify,request, Response, make_response
from bll.movies_bll import MoviesBll
import json
from bson import ObjectId
import logging
from bll.auth_bll import AuthBLL

movies=Blueprint('movies',__name__)

movies_bll=MoviesBll()
auth_bll=AuthBLL()

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

@movies.route('/',methods=['GET'])
def get_all_movies():
    if request.headers and request.headers.get("x-access-token"):
        token=request.headers.get("x-access-token")
        exist=auth_bll.verify_token(token)
        if exist==True:
            movies=movies_bll.get_all_movies()
            return make_response({"movies":movies},200)
        else:
            return make_response({"error":"not Authorized"},401)
    else:
        return make_response({"error":"not Authorized"},401)
    

@movies.route('/<id>/', methods=['GET'])
def get_movie_by_id(id):
    movie = movies_bll.get_movie_by_id(id)
    if 'error' in movie:
        return jsonify(movie), 404
    else:
        return jsonify(movie), 200
    

@movies.route('/',methods=['POST'])
def add_movie():
    movieDetails=request.json
    requestStatus=movies_bll.add_movie(movieDetails)
    return Response(json.dumps(requestStatus)) 

@movies.route('/<id>/', methods=['PUT'])
def update_movie(id):
    movie_data = request.json
    logging.debug(f'Updating user {id} with data: {movie_data}')
    result, status = movies_bll.update_movie(id, movie_data)
    return jsonify(result), status


@movies.route('/<id>/', methods=['DELETE'])
def delete_movie(id):
    result=movies_bll.delete_movie(id)
    return jsonify(result)