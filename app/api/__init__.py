from flask_restful import Api

from .usuario import UsuarioApi, UsuarioListApi
from .paciente import PacienteApi, PacienteListApi
from .medico import MedicoApi, MedicoListApi


api = Api()
def configure_api(app):
    api.add_resource(UsuarioApi, '/usuarios/<cpf>')
    api.add_resource(UsuarioListApi, '/usuarios')

    api.add_resource(PacienteApi, '/pacientes/<cpf>')
    api.add_resource(PacienteListApi, '/pacientes')

    api.add_resource(MedicoApi, '/medicos/<crm>')
    api.add_resource(MedicoListApi, '/medicos')

    api.init_app(app)
