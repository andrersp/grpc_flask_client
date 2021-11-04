# -*- coding: utf-8 -*-

import grpc
from google.protobuf.empty_pb2 import Empty
from grpc_client.ext.grpc_conn import client
from grpc_client.messages import movies_pb2 as pb2


class MovieClient(object):

    def get_movies(self, page: int = 0, limit: int = 20):

        page = int(page)
        limit = int(limit)

        try:

            message = pb2.GetMoviesParam(page=page, limit=limit)
            result = client.GetMovies(message)
        except grpc.RpcError as e:
            print(e)
            return []
        else:
            return result

    def send_movies(self, movies):

        message = pb2.Data(movies=movies)

        return client.UpdateMovies(message)

    def get_movie(self, movie_id):

        message = pb2.MovieId(movie_id=movie_id)
        return client.GetMovie(message)
