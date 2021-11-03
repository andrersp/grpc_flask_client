# -*- coding: utf-8 -*-

import csv
from ast import literal_eval


HEADER = ['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id', 'imdb_id', 'original_language', 'original_title', 'overview', 'popularity', 'poster_path',
          'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count']
MAP = {
    "adult": 'adult',
    "language": "original_language",
    "title": "title",
    "genres": "genres"
}

LITERAL = ['adult']

LIST_TYPE = ['genres']


def read_file(file_path, header):
    csvfile = open(file_path, "r", encoding='latin1')
    data_reader = csv.DictReader((line.replace('\0', '')
                                  for line in csvfile), fieldnames=header, delimiter=',')
    next(data_reader)
    return data_reader


def get_values():
    output_data = []
    for raw in read_file('/app/movies_metadata.csv', HEADER):
        to_insert = {}
        for movie_field in MAP:

            if movie_field in LITERAL:
                try:
                    value = literal_eval(raw[MAP[movie_field]])
                except:
                    value = False
                to_insert[movie_field] = value
            elif movie_field in LIST_TYPE:
                lst = []

                try:
                    value = literal_eval(raw[MAP[movie_field]])
                except:
                    value = []

                to_insert[movie_field] = value

            else:
                to_insert[movie_field] = raw[MAP[movie_field]]
        output_data.append(to_insert)

    return output_data
