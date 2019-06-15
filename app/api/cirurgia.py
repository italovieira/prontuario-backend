from flask_restful import Resource, reqparse

from ..models.cirurgia import Cirurgia

from ..dao.cirurgia import CirurgiaDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf_paciente')
parser.add_argument('data')
parser.add_argument('descricao')

_dao = CirurgiaDAO()

class CirurgiaApi(Resource):

    def get(self, cpf):
        cirurgia = _dao.get_cirurgia(cpf)
        return cirurgia.serialize()

    def put(self, cpf):
        args = parser.parse_args()
        cirurgia = Cirurgia(**args)
        _dao.update_cirurgia(cpf, cirurgia)
        return cirurgia.serialize(), 201

    def delete(self, cpf):
        _dao.delete_cirurgia(cpf)
        return '', 204


class CirurgiaListApi(Resource):

    def get(self):
        cirurgias = _dao.get_cirurgias()
        return [cirurgia.serialize() for cirurgia in cirurgiaes]

    def post(self):
        args = parser.parse_args()
        cirurgia = Cirurgia(**args)
        _dao.save_cirurgia(cirurgia)

        return cirurgia.cpf


class PacienteCirurgiaListApi(Resource):

    def get(self, cpf):
        cirurgias = _dao.get_cirurgias_from_paciente(cpf)
        return [cirurgia.serialize() for cirurgia in cirurgias]
