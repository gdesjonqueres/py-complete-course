def add_movie(movies, movie):
    movies.append(movie)

def find_movies(movies, parameter, value):
    # found = []
    p = parameter.lower()
    v = str(value).lower()
    return [movie for movie in movies if str(movie.get(p, '')).lower() == v]
