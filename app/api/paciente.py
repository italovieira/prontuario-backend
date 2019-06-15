from flask import jsonify
from flask_restful import Resource, reqparse

from ..models.paciente import Paciente

from ..dao.paciente import PacienteDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf', required=True)
parser.add_argument('nome')
parser.add_argument('data_nasc')
parser.add_argument('telefone')
parser.add_argument('email')
parser.add_argument('senha')
parser.add_argument('sexo')
parser.add_argument('endereco')
parser.add_argument('tipo_sanguineo')

_dao = PacienteDAO()

class PacienteApi(Resource):

    def get(self, cpf):
        paciente = _dao.get_paciente(cpf)
        return paciente.serialize()

    def put(self, cpf):
        args = parser.parse_args()
        paciente = Paciente(**args)
        _dao.update_paciente(cpf, paciente)
        return paciente.serialize(), 201

    def delete(self, cpf):
        delete_paciente(cpf)
        return '', 204


class PacienteListApi(Resource):

    def get(self):
        pacientes = _dao.get_pacientes()
        return [paciente.serialize() for paciente in pacientes]

    def post(self):
        args = parser.parse_args()
        paciente = Paciente(**args)
        _dao.save_paciente(paciente)

        return paciente.cpf
