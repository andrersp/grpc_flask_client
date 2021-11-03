# -*- coding: utf-8 -*-

def serialize_all_movies(result):

    return {
        "data": list(map(lambda x: {
            "id": x.id,
            "title": x.title,
            "language": x.language,
            "adult": x.adult
        }, result.movies)),
        "actual_page": result.actual_page,
        "total_page": result.total_pages,
        "itens": f'{result.itens} of {result.total_itens}'
    }


def serialize_movie(movie):
    return {
        "id": movie.id,
        "title": movie.title,
        "language": movie.language,
        "adult": movie.adult,
        "genres": list(map(lambda x: {
            "id": x.id,
            "name": x.name
        }, movie.genres))
    }
