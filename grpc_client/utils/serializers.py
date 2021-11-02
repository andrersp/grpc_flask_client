# -*- coding: utf-8 -*-

def serialize_all_movies(movies):

    return list(map(lambda x: {
        "title": x.title,
        "language": x.language,
        "adult": x.adult
    }, movies))
