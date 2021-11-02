from flask_restful import Resource
from flask import request
import time

from grpc_client.services.movies import MovieClient
from grpc_client.utils.http_responses import success, error

from grpc_client.ext.grpc_conn import client
from grpc_client.utils import serializers


# Fix: Usar Exception do projeto
from marshmallow.exceptions import ValidationError


class Movies(Resource):
    def get(self):
        start = time.time()

        service = MovieClient()
        result = service.get_movies()
        end = time.time()
        response_time = '{:.2f}'.format(end - start)

        movies = serializers.serialize_all_movies(result.movies)

        return success({"reponse_time": response_time, "data": movies})
        return success(status_code=201)
