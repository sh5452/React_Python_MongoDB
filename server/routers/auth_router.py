from flask import Blueprint, request, jsonify
import jwt
import datetime

auth_route = Blueprint('auth_route', __name__)

SECRET_KEY = 'YOUR_SECRET_KEY'

@auth_route.route('/login', methods=['POST'])
def login():
    # כאן אמור להיות קוד לבדיקת פרטי המשתמש וליצירת הטוקן
    
    # הנחה שאנחנו יוצרים טוקן עבור משתמש עם user_id
    user_id = 'user_id'
    
    token = jwt.encode({'userId': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY, algorithm='HS256')
    
    print(f"Generated token: {token}")
    
    return jsonify({'token': token}), 200