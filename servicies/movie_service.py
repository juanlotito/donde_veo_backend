from repository import movie_repository
from entities import Movie_Entity, Watch_Provider_Entity

class movie_service:
    def __init__(self):
        self.movie_repository = movie_repository()
        

    def from_entity_movie (self, entity):
        entity = Movie_Entity(entity["id"], entity["adult"], entity["backdrop_path"], entity["genre_ids"], entity["original_language"], entity["original_title"], entity["overview"], entity["popularity"],
        entity["poster_path"], entity["release_date"], entity["title"], entity["video"], entity["vote_average"], entity["vote_count"])

        return entity
    
    def from_entity_watch_providers (self, entity):
        watch_providers = Watch_Provider_Entity(None, None, None, None)
        
        if entity == None:
            return None
        try:
            if entity["buy"] is not None:
                watch_providers.buy_provider = entity["buy"]
        except: 
            pass
        try:
            if entity["rent"] is not None:
                watch_providers.rent_provider = entity["rent"]
        except:
            pass

        try:
            if entity["flatrate"] is not None:
                watch_providers.flatrate_provider = entity["flatrate"]
        except:
            pass
        
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

    def get_watch_providers_by_country(self, country, watch_providers):
        raw_watch_providers = watch_providers["results"]
        
        try:
            entity = self.from_entity_watch_providers(raw_watch_providers[country])
            return entity

        except KeyError:
            return None


    def search_movie(self, query):
        response = self.movie_repository.search_movie(query)
        
        raw_movie = self.get_movie_by_popularity(response.json())

        entity = self.from_entity_movie(raw_movie)

        return entity


    def get_watch_providers(self, id, country):
        response = self.movie_repository.get_watch_providers(id)

        watch_providers = self.get_watch_providers_by_country(country, response.json())

        return watch_providers


        
        




