import requests
from pymongo import MongoClient

class MoviesBll:
    def __init__(self):
        self.api_url = "https://api.tvmaze.com/shows"
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['movies_db']
        self.collection = self.db['movies']

    def fetch_and_store_movies(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            movies = response.json()
            returned_movies = []
            for movie in movies:
                if not self.collection.find_one({"id": movie['id']}):
                    movie_data = {
                        "id": movie['id'],
                        "name": movie['name'],
                        "premiered": movie.get('premiered'),
                        "genres": movie.get('genres'),
                        "image": movie.get('image', {}).get('medium')
                    }
                    self.collection.insert_one(movie_data)
                    returned_movies.append(movie_data)
            return returned_movies
        return []

    def get_all_movies(self):
        movies = list(self.collection.find({}, {"_id": 1, "name": 1, "premiered": 1, "genres": 1, "image": 1}))
        for movie in movies:
            movie["_id"] = str(movie["_id"])
        if not movies:
            movies = self.fetch_and_store_movies()
        return movies

    def get_movie_by_id(self, movie_id):
        movie = self.collection.find_one({"id": int(movie_id)}, {"_id": 1, "name": 1, "premiered": 1, "genres": 1, "image": 1})
        if movie:
            movie["_id"] = str(movie["_id"])
        return movie

    def add_movie(self, movie_data):
        # לא ניתן להוסיף סרטים ל-API של TVMaze
        return "This operation is not supported."

    def update_movie(self, movie_id, movie_data):
        # לא ניתן לעדכן סרטים ב-API של TVMaze
        return "This operation is not supported."

    def delete_movie(self, movie_id):
        # לא ניתן למחוק סרטים מה-API של TVMaze
        return "This operation is not supported."