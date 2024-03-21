from pymongo import MongoClient
from bson import ObjectId
from flask import request
import requests

class UsersBll:
    def __init__(self):
        self.__uri='mongodb://shlomit5452:shk1234@ac-1nwpds7-shard-00-00.faecgrb.mongodb.net:27017,ac-1nwpds7-shard-00-01.faecgrb.mongodb.net:27017,ac-1nwpds7-shard-00-02.faecgrb.mongodb.net:27017/?ssl=true&replicaSet=atlas-axv6o2-shard-0&authSource=admin&retryWrites=true&w=majority'
        self.__client=MongoClient(self.__uri)
        self.__db=self.__client['usersProjects']
        self.__users_collection=self.__db['usersDB']

    def get_all_users(self):
        resp=requests.get('http://jsonplaceholder.typicode.com/users')
        if not resp.ok:
            return []
        else:
            users=resp.json()
            returned_users=list(
                map(
                   lambda user:{
                     "id":user["id"] , 
                     "name":user["name"],
                     "email":user['email'],
                     "city":user['address']['city']
                   },
                   users,
                )
            )
            self.__users_collection.insert_many(returned_users )
    
    def add_user(self,obj):
        self.__users_collection.insert_one(obj)
        return "Created"+ " "+ str(obj['id'])
    
    def update_user(self,obj,id):
        self.__users_collection.update_one({"id":ObjectId(id)},{'$set':obj})
        return "Updated"
    
    def delele_user(self, id):
        self.__users_collection.delete_one({'id':ObjectId(id)})
        return "Deleted"


        




