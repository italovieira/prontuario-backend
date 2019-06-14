from flask_restful import Api

from .usuario import UsuarioApi, UsuarioListApi


api = Api()
def configure_api(app):
    api.add_resource(UsuarioApi, '/usuarios/<cpf>')
    api.add_resource(UsuarioListApi, '/usuarios')

    api.init_app(app)
