from flask_restful import Resource
from flask import request
import time


from grpc_client.services.movies import MovieClient
from grpc_client.utils.http_responses import success, error

from grpc_client.ext.grpc_conn import client
from grpc_client.utils import serializers
from grpc_client.utils import insert_movies


# Fix: Usar Exception do projeto
from marshmallow.exceptions import ValidationError


class Movies(Resource):
    def get(self):

        args = request.args
        page = args.get("page") or 1
        limit = args.get("limit") or 20

        start = time.time()
        service = MovieClient()
        result = service.get_movies(page=page, limit=limit)
        end = time.time()
        response_time = '{:.2f}'.format(end - start)

        movies = serializers.serialize_all_movies(result)

        return success({"reponse_time": response_time, "data": movies})

    def post(self):

        movies = insert_movies.get_values()

        service = MovieClient()

        result = service.send_movies(movies)
        if result.success:
            return success()
        return error()


class Movie(Resource):
    def get(self, movie_id):

        if not movie_id:
            return error({"msg": "invalid Movie id"})

        service = MovieClient()

        result = service.get_movie(movie_id)

        if not result.success:
            return error({"msg": "Movie not found"}, status_code=404)

        return success(serializers.serialize_movie(result))
