from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from flask import request
class UsersBll:
    def __init__(self):
        self.__uri='mongodb://shlomit5452:shk1234@ac-1nwpds7-shard-00-00.faecgrb.mongodb.net:27017,ac-1nwpds7-shard-00-01.faecgrb.mongodb.net:27017,ac-1nwpds7-shard-00-02.faecgrb.mongodb.net:27017/?ssl=true&replicaSet=atlas-axv6o2-shard-0&authSource=admin&retryWrites=true&w=majority'
        self.__client=MongoClient(self.__uri)
        self.__db=self.__client['usersProjects']
        self.__users_collection=self.__db['usersDB']

    def get_all_users(self):
        # resp=requests.get('http://jsonplaceholder.typicode.com/users')
        # if not resp.ok:
        #     return []           
        # else:
        #     users=resp.json()
            
        #
        #     returned_users=list(
        #         map(
        #            lambda user:{
        #              "id":user["id"] , 
        #              "name":user["name"],
        #              "email":user['email'],
        #              "city":user['address']['city']
        #            },
        #            users,
        #         )
        #     )
        #     self.__users_collection.insert_many(returned_users )
        #     return returned_users         
        users_cursor = self.__users_collection.find({}, {'id': 1, 'name': 1, 'email': 1, 'city': 1})
        users_list = list(users_cursor)
        return users_list
    def add_user(self,user):
        result = self.__users_collection.insert_one(user)
        
        return {'status': 'Created', 'id': str(result.inserted_id)}
    
    def update_user(self, id, user):
        result = self.__users_collection.update_one({'_id': ObjectId(id)}, {'$set': user})
        if result.matched_count == 0:
            return {'error': 'User not found'}, 404
        else:
            return {'status': 'Updated', 'id': id}, 200
        
    def delele_user(self, id):
        result = self.__users_collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count > 0:
            return {'status': 'Deleted', 'id': id}, 200
        else:
            return {'error': 'Failed to delete user'}, 404


