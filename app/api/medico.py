from flask import jsonify
from flask_restful import Resource, reqparse

from ..models.medico import Medico

from ..dao.medico import MedicoDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf')
parser.add_argument('nome')
parser.add_argument('data_nasc')
parser.add_argument('telefone')
parser.add_argument('email')
parser.add_argument('senha')
parser.add_argument('sexo')
parser.add_argument('endereco')
parser.add_argument('crm', required=True)
parser.add_argument('hospitais', default=[])

_dao = MedicoDAO()

class MedicoApi(Resource):

    def get(self, crm):
        medico = _dao.get_medico(crm)
        if medico:
            return medico.serialize()

    def put(self, crm):
        args = parser.parse_args()
        medico = Medico(**args)
        _dao.update_medico(crm, medico)
        return medico.serialize(), 201

    def delete(self, crm):
        delete_medico(crm)
        return '', 204


class MedicoListApi(Resource):

    def get(self):
        medicos = _dao.get_medicos()
        return [medico.serialize() for medico in medicos]

    def post(self):
        args = parser.parse_args()
        medico = Medico(**args)
        _dao.save_medico(medico)

        return medico.crm
