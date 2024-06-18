
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

class AuthBLL:
    def __init__(self):
        self.__key = "iyXMaPrYGDcCcetxXcGyYPRVrT7Zwgip"
        self.__algorithm = "HS256"

    def get_token(self, username, password):
        user_id = self.__check_user(username, password)
        token = None
        if user_id is not None:
            token = jwt.encode({"userId": user_id}, self.__key, self.__algorithm)
        print(f"Generated token: {token}")  # Log the generated token
        return token

    def verify_token(self, token):
        try:
            data = jwt.decode(token, self.__key, algorithms=[self.__algorithm])
            user_id = data["userId"]
            print(f"Decoded token data: {data}")  # Log the decoded data
            # בדוק אם המשתמש קיים...
            return True
        except ExpiredSignatureError:
            print("Token has expired")
            return False
        except InvalidTokenError:
            print("Invalid token")
            return False

    def __check_user(self, username, password):
        # בדוק אם המשתמש קיים בבסיס הנתונים
        return "user_id" if username == "test" and password == "test" else None