from movie_collection import add_movie, find_movies
from my_movies import movies

# movie = {
#     'name': 'Rambo',
#     'director': 'Stalone',
#     'year': 1981
# }
# add_movie(movies, movie)
#
# movie = {
#     'name': 'Rambo II',
#     'director': 'Stalone',
#     'year': 1983
# }
# add_movie(movies, movie)
#
# movie = {
#     'name': 'Rambo III',
#     'director': 'Stalone',
#     'year': 1986
# }
# add_movie(movies, movie)
#
# movie = {
#     'name': 'Mon Oncle',
#     'director': 'Jacques Tatie',
#     'year': 1968
# }
# add_movie(movies, movie)
#
# movie = {
#     'name': 'Les Enfants du Paradis',
#     'director': 'Je sais plus',
#     'year': 1945
# }
# add_movie(movies, movie)
#
# print('Showing all my movies...')
# show_all_movies(movies)
#
# print('Finding... Mon Oncle')
# print(find_movies(movies, 'name', 'mon oncle'))
#
# print('Finding... Movies from 1945')
# print(find_movies(movies, 'year', 1945))
#
# print('Finding... Movies from 1968')
# print(find_movies(movies, 'year', 1968))
#
# print('Finding... Movies from 1969')
# print(find_movies(movies, 'year', 1969))
#
# print('Finding... Movies from director Stalone')
# print(find_movies(movies, 'director', 'Stalone'))

def input_movie():
    new_movie = {}
    new_movie['name'] = input('Name: ')
    new_movie['director'] = input('Director: ')
    new_movie['year'] = input('Year: ')
    return new_movie


def input_search_parameter():
    choice = 0
    while choice not in [1, 2, 3, 4]:
        menu = """
            Search by:
                - 1 - Name
                - 2 - Director
                - 3 - Year
                - 4 - Back to main menu
            """
        print(menu)
        choice = int(input('Your choice: '))

    if choice == 4:
        return

    value = input('Value: ')

    if choice == 1:
        return ('name', value)
    elif choice == 2:
        return ('director', value)
    elif choice == 3:
        return ('year', int(value))
    else:
        return


def print_movies(movies):
    for movie in movies:
        print(f'Name: {movie["name"]}')
        print(f'Director: {movie["director"]}')
        print(f'Year: {movie["year"]}\n')


# Main loop
while True:
    choice = ''
    while choice not in ['a', 'l', 's', 'q']:
        menu = """
            Menu:
            a: Add a movie
            l: List all movies
            s: Search
            q: Quit
        """
        print(menu)
        choice = input('Your choice: ')

    if choice == 'a':
        new_movie = input_movie()
        add_movie(movies, new_movie)
    elif choice == 'l':
        print_movies(movies)
    elif choice == 's':
        ret = input_search_parameter()
        if (ret):
            parameter, value = ret
            search_results = find_movies(movies, parameter, value)
            print_movies(search_results)
    elif choice == 'l':
        print_movies(movies)
    elif choice == 'q':
        break