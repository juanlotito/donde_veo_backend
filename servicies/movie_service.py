from repository import movie_repository
from entities import Movie_Entity

class movie_service:
    def __init__(self):
        self.movie_repository = movie_repository()
        

    def from_entity (self, entity):
        print(entity)
        entity = Movie_Entity(entity["id"], entity["adult"], entity["backdrop_path"], entity["genre_ids"], entity["original_language"], entity["original_title"], entity["overview"], entity["popularity"],
        entity["poster_path"], entity["release_date"], entity["title"], entity["video"], entity["vote_average"], entity["vote_count"])

        return entity

    def get_movie_by_popularity(self, dic):       
        movies = dic["results"]
        final_movie = ""
        popularity = 0
        

        for index in range(len(movies)):
            if(movies[index]["popularity"] > popularity):
                popularity = movies[index]["popularity"]
                final_movie = movies[index]
      
        return final_movie


    def search_movie(self, query):
        response = self.movie_repository.search_movie(query)
        
        raw_movie = self.get_movie_by_popularity(response.json())

        entity = self.from_entity(raw_movie)

        return entity
        




