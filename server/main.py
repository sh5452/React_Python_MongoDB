
from flask import Flask
from routers.movies_router import movies
from routers.users_router import users
from bson import ObjectId
import json
from flask_cors import CORS



class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if (isinstance(obj, ObjectId)):
            return str(obj)
        return json.JSONEncoder.default(self,obj)


app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False

app.json_encoder= CustomJSONEncoder

app.register_blueprint(movies, url_prefix='/movies')
app.register_blueprint(users, url_prefix='/users')

app.run()

