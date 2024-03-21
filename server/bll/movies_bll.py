from pymongo import MongoClient
from bson import ObjectId
from flask import request
import requests

class MoviesBll:
    def __init__(self):
        self.__uri="mongodb://shlomit5452:shk1234@ac-1nwpds7-shard-00-00.faecgrb.mongodb.net:27017,ac-1nwpds7-shard-00-01.faecgrb.mongodb.net:27017,ac-1nwpds7-shard-00-02.faecgrb.mongodb.net:27017/?ssl=true&replicaSet=atlas-axv6o2-shard-0&authSource=admin&retryWrites=true&w=majority"
        self.__client = MongoClient(self.__uri)
        self.__db=self.__client['moviesProject']
        self.__movies_collection=self.__db["movie"]
        
        
       
    def get_all_movies(self):
        
        # resp = requests.get("https://api.tvmaze.com/shows")
        # if not resp.ok:
        #   return []
        # else:
        #     movies =resp.json()
        #     returned_movies =list(
        #         map(
        #             lambda movie: {
        #                 "name": movie["name"],
        #                 "genres": movie["genres"],
        #                 "premiered":movie["premiered"],
        #                 "image":movie["image"]["medium"]
        #             },
        #             movies, 
                   
        #         )
        #     )
        #     self.__movies_collection.insert_many(returned_movies)
        #     return returned_movies
        movies_cursor = self.__movies_collection.find({}, { 'name': 1, 'genres': 1, 'premiered': 1, "image":1})
        movies_list = list(movies_cursor)
        return movies_list
            

    def get_movie_by_id(self, movieId):
        movie = self.__movies_collection.find_one({'_id': ObjectId(movieId)})
        if movie:
            return movie
        else:
            return {'error': 'Movie not found'}, 404
    
    def add_movie(self,obj):
        self.__movies_collection.insert_one(obj)
        return "Created" + "  " + str(obj["_id"])
    
    def update_movie(self, id, movie):
        result = self.__movies_collection.update_one({'_id': ObjectId(id)}, {'$set': movie})
        if result.matched_count == 0:
            return {'error': 'User not found'}, 404
        else:
            return {'status': 'Updated', 'id': id}, 200
    
    def delete_movie(self,id):
        self.__movies_collection.delete_one({'_id':ObjectId(id)})
        return "Deleted"