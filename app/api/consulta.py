from flask import jsonify
from flask_restful import Resource, reqparse

from ..models.consulta import Consulta

from ..dao.consulta import ConsultaDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf_paciente')
parser.add_argument('crm_medico')
parser.add_argument('data')

_dao = ConsultaDAO()

class ConsultaApi(Resource):

    def get(self, cpf):
        consulta = _dao.get_consulta(cpf)
        return consulta.serialize()

    def put(self, cpf):
        args = parser.parse_args()
        consulta = Consulta(**args)
        _dao.update_consulta(cpf, consulta)
        return consulta.serialize(), 201

    def delete(self, cpf):
        _dao.delete_consulta(cpf)
        return '', 204


class ConsultaListApi(Resource):

    def get(self):
        consultas = _dao.get_consultas()
        return [consulta.serialize() for consulta in consultas]

    def post(self):
        args = parser.parse_args()
        consulta = Consulta(**args)
        _dao.save_consulta(consulta)

        return consulta.cpf


class PacienteConsultaListApi(Resource):

    def get(self, cpf):
        consultas = _dao.get_consultas_from_paciente(cpf)
        return [consulta.serialize() for consulta in consultas]
