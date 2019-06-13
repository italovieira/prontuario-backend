from flask_restful import Api

from .user import UserApi, UserListApi


api = Api()
def configure_api(app):
    api.add_resource(UserApi, '/users/<cpf>')
    api.add_resource(UserListApi, '/users')

    api.init_app(app)
