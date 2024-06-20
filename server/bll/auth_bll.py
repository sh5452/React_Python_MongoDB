import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId

SECRET_KEY = 'iyXMaPrYGDcCcetxXcGyYPRVrT7Zwgip'

class AuthBLL:
    def __init__(self):
        self.__key = SECRET_KEY
        self.__algorithm = "HS256"
        self.__client = MongoClient('mongodb://localhost:27017/')
        self.__db = self.__client['UserDB']  # שנה לשם ה-Database שלך
        self.__users_collection = self.__db['user']  # שם ה-Collection של המשתמשים

    def get_token(self, username, password):
        user_id = self.__check_user(username, password)
        token = None
        if user_id is not None:
            token = jwt.encode({"userId": user_id, "exp": datetime.utcnow() + timedelta(hours=1)}, self.__key, self.__algorithm)
        print(f"Generated token: {token}")  # Log the generated token
        return token

    def verify_token(self, token):
        try:
            data = jwt.decode(token, self.__key, algorithms=[self.__algorithm])
            user_id = data["userId"]
            print(f"Decoded token data: {data}")  # Log the decoded data
            return data
        except ExpiredSignatureError:
            print("Token has expired")
            return False
        except InvalidTokenError:
            print("Invalid token")
            return False

    def __check_user(self, username, password):
        user = self.__users_collection.find_one({"UserName": username, "Password": password})
        if user:
            return str(user["_id"])
        return None