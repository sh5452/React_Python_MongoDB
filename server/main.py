from flask import Flask, request, jsonify
from functools import wraps
from flask_cors import CORS
from bson import ObjectId
import json
from bll.movies_bll import MoviesBll
from bll.auth_bll import AuthBLL

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

app = Flask(__name__)
CORS(app)
SECRET_KEY = "iyXMaPrYGDcCcetxXcGyYPRVrT7Zwgip"
app.config['SECRET_KEY'] = SECRET_KEY
app.json_encoder = CustomJSONEncoder

auth_bll = AuthBLL()
movies_bll = MoviesBll()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401
        try:
            data = auth_bll.verify_token(token)
            if not data:
                return jsonify({'error': 'Invalid token!'}), 401
            current_user_id = data['userId']
        except Exception as e:
            return jsonify({'error': 'Invalid token!'}), 401
        return f(current_user_id, *args, **kwargs)
    return decorated

# Movies Routes
@app.route('/movies', methods=['GET'])
@token_required
def get_all_movies(current_user_id):
    movies = movies_bll.get_all_movies()
    return jsonify(movies), 200

@app.route('/movies/<movie_id>', methods=['GET'])
@token_required
def get_movie(current_user_id, movie_id):
    movie = movies_bll.get_movie_by_id(movie_id)
    if movie:
        return jsonify(movie), 200
    else:
        return jsonify({'error': 'Movie not found'}), 404

@app.route('/movies', methods=['POST'])
@token_required
def add_movie(current_user_id):
    return jsonify({'message': "This operation is not supported."}), 405

@app.route('/movies/<movie_id>', methods=['PUT'])
@token_required
def update_movie(current_user_id, movie_id):
    return jsonify({'message': "This operation is not supported."}), 405

@app.route('/movies/<movie_id>', methods=['DELETE'])
@token_required
def delete_movie(current_user_id, movie_id):
    return jsonify({'message': "This operation is not supported."}), 405

# Auth Routes
@app.route('/auth/login', methods=['POST'])
def login():
    auth_data = request.get_json()
    token = auth_bll.get_token(auth_data['UserName'], auth_data['Password'])
    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)