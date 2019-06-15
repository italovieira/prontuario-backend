from flask_restful import Api

from .usuario import UsuarioApi, UsuarioListApi
from .paciente import PacienteApi, PacienteListApi


api = Api()
def configure_api(app):
    api.add_resource(UsuarioApi, '/usuarios/<cpf>')
    api.add_resource(UsuarioListApi, '/usuarios')

    api.add_resource(PacienteApi, '/pacientes/<cpf>')
    api.add_resource(PacienteListApi, '/pacientes')

    api.init_app(app)
