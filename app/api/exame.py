from flask import jsonify
from flask_restful import Resource, reqparse

from ..models.exame import Exame

from ..dao.exame import ExameDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf_paciente')
parser.add_argument('resultado')
parser.add_argument('tipo')
parser.add_argument('data')
parser.add_argument('nome_local')

_dao = ExameDAO()

class ExameApi(Resource):

    def get(self, cpf):
        exame = _dao.get_exame(cpf)
        return exame.serialize()

    def put(self, cpf):
        args = parser.parse_args()
        exame = Exame(**args)
        _dao.update_exame(cpf, exame)
        return exame.serialize(), 201

    def delete(self, cpf):
        _dao.delete_exame(cpf)
        return '', 204


class ExameListApi(Resource):

    def get(self):
        exames = _dao.get_exames()
        return [exame.serialize() for exame in exames]

    def post(self):
        args = parser.parse_args()
        exame = Exame(**args)
        _dao.save_exame(exame)

        return exame.cpf


class PacienteExameListApi(Resource):

    def get(self, cpf):
        exames = _dao.get_exames_from_paciente(cpf)
        return [exame.serialize() for exame in exames]
