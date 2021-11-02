from flask import Blueprint
from flask_restful import Api
from grpc_client.blueprints.rest_v1.movies import Movies

bp = Blueprint("rest_v1", __name__, url_prefix="/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(Movies, "/movies")
    app.register_blueprint(bp)
