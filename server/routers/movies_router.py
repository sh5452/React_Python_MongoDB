from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import jwt

movies = Blueprint('movies', __name__)

# ההתחברות למסד הנתונים
client = MongoClient('localhost', 27017)
db = client.movie_database
movies_collection = db.movies
SECRET_KEY = "iyXMaPrYGDcCcetxXcGyYPRVrT7Zwgip"

@movies.route('/', methods=['GET'])
def get_all_movies():
    token = request.headers.get('x-access-token')
    if not token:
        return jsonify({"error": "No token provided"}), 401

    try:
        print(f"Received token: {token}")
        print(f"Using secret key: {SECRET_KEY}")
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(f"Decoded token data: {data}")
        user_id = data['userId']

        # שליפת הסרטים מתוך מסד הנתונים
        movies = movies_collection.find({"userId": user_id})
        
        # המרת ObjectId למחרוזת
        movie_list = []
        for movie in movies:
            movie['_id'] = str(movie['_id'])
            movie_list.append(movie)

        return jsonify({"movies": movie_list}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500