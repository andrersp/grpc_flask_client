# -*- coding: utf-8 -*-

from google.protobuf.empty_pb2 import Empty

from grpc_client.ext.grpc_conn import client
from grpc_client.messages import movies_pb2 as pb2


class MovieClient(object):

    def get_movies(self):

        try:
            result = client.GetMovies(Empty())
        except Exception as e:
            print(e)
            return []
        else:
            return result
