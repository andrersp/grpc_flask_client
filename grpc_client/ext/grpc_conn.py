# -*- coding: utf-8

from os import environ as env
import grpc
from grpc_client.messages.movies_pb2_grpc import MoviesServiceStub

channel = grpc.insecure_channel(
    f'{env.get("GRPC_HOST")}:{env.get("GRP_PORT")}')

client = MoviesServiceStub(channel)
# from app.
