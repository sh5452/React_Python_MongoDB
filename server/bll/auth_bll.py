import jwt


class AuthBLL:
    def __init__(self):
        self.__key = "iyXMaPrYGDcCcetxXcGyYPRVrT7Zwgip"
        self.__algorithm = "HS256"

    def get_token(self, username, password):
        user_id = self.__check_user(username, password)
        token = None
        if user_id is not None:
            token = jwt.encode({"userId": user_id}, self.__key, self.__algorithm)
        return token

    def verify_token(self, token):
        data = jwt.decode(token, self.__key ,self.__algorithm)
                          
        user_id = data["userId"]
        # check if the user exists...

        return True

    def __check_user(self, username, password):
        # check if user exits in users db
        return "user_id"
    
