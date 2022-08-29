import requests
from decouple import config

class movie_repository:
    def __init__(self):
        self.__api_key = config('API_KEY')
        self.__url = config('API_URL_BASE')
    
    def search_movie (self, query) :
        url = self.__url+"search/movie"
        params = {"api_key": self.__api_key, "query":query}
        response = requests.get(url,params=params)
        return response

    def get_watch_providers (self, id) : 
        url = self.__url+'movie/'+id+'/watch/providers?'
        params = {"api_key": self.__api_key}
        response = requests.get(url, params=params)
        return response




