import json

from homework_20.movie import Movie

if __name__ == '__main__':
    movies = Movie.from_xml("market.xml")

    for movie in movies:
        print(json.dumps(movie.__dict__, sort_keys=True, indent=4))
