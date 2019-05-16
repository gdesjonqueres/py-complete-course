from unittest import TestCase, main
from movie_collection import add_movie, find_movies


class MovieCollectionTestCase(TestCase):
    def setUp(self) -> None:
        self.movies = [
            {
                'name': 'Toto',
                'director': 'Titi',
                'year': 1995
            },
            {
                'name': 'Tutu',
                'director': 'Tata',
                'year': 1995
            },
            {
                'name': 'Tyty',
                'director': 'Ytyt',
                'year': 1980
            }
        ]

    def test_add_movie(self):
        new_movie = {
            'name': 'Prout',
            'director': 'Jean-Luc',
            'year': 2005
        }
        add_movie(self.movies, new_movie)
        self.assertEqual(4, len(self.movies))
        self.assertEqual(new_movie, self.movies[-1])

    def test_find_movies_by_name(self):
        expected = [{
            'name': 'Tutu',
            'director': 'Tata',
            'year': 1995
        }]
        self.assertEqual(expected, find_movies(self.movies, 'name', 'Tutu'))

    def test_find_movies_by_director(self):
        expected = [{
            'name': 'Tutu',
            'director': 'Tata',
            'year': 1995
        }]
        self.assertEqual(expected, find_movies(self.movies, 'director', 'Tata'))

    def test_find_movies_by_year(self):
        expected = [{
            'name': 'Tyty',
            'director': 'Ytyt',
            'year': 1980
        }]
        self.assertEqual(expected, find_movies(self.movies, 'year', 1980))

    def test_find_movies_multiple_results(self):
        expected = [
            {
                'name': 'Toto',
                'director': 'Titi',
                'year': 1995
            },
            {
                'name': 'Tutu',
                'director': 'Tata',
                'year': 1995
            }
        ]
        self.assertEqual(expected, find_movies(self.movies, 'year', 1995))

    def test_find_movies_no_results(self):
        self.assertEqual([], find_movies(self.movies, 'year', 1990))

    def test_find_movies_non_exist_parameter(self):
        self.assertEqual([], find_movies(self.movies, 'parameter-not-exist', 'dummy'))


if __name__ == '__main__':
    main()
