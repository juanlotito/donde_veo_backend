class Movie_Entity:
  def __init__(self, id, adult, backdrop_path, genre_ids, original_language, original_title, overview, popularity, poster_path, release_date,
               title, video, vote_average, vote_count):
    self.id = id
    self.adult = adult
    self.backdrop_path = backdrop_path
    self.genre_ids = genre_ids
    self.original_language = original_language
    self.original_title = original_title
    self.overview = overview
    self.popularity = popularity
    self.poster_path = poster_path
    self.release_date = release_date
    self.title = title
    self.video = video
    self.vote_average = vote_average
    self.vote_count = vote_count