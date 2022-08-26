import requests

class movie_repository:
    def __init__(self):
        self.__api_key = "75973ea0d608b5bfa409890e99bbb501"
        self.__url = "https://api.themoviedb.org/3/"
    
    def search_movie (self, query) :
        url = self.__url+"search/movie?"
        params = {"api_key": self.__api_key, "query":query}
        response = requests.get(url,params=params)
        return response




