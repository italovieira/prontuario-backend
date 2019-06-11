from flask_restful import Api

from .user import UserApi


api = Api()
def configure_api(app):
    api.add_resource(UserApi, '/user')

    api.init_app(app)
