from flask import jsonify
from flask_restful import Resource, reqparse

from ..models.secretario import Secretario

from ..dao.secretario import SecretarioDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf', required=True)
parser.add_argument('nome')
parser.add_argument('data_nasc')
parser.add_argument('telefone')
parser.add_argument('email')
parser.add_argument('senha')
parser.add_argument('sexo')
parser.add_argument('endereco')
parser.add_argument('cnpj_hospital')

_dao = SecretarioDAO()

class SecretarioApi(Resource):

    def get(self, cpf):
        secretario = _dao.get_secretario(cpf)
        return secretario.serialize()

    def put(self, cpf):
        args = parser.parse_args()
        secretario = Secretario(**args)
        _dao.update_secretario(cpf, secretario)
        return secretario.serialize(), 201

    def delete(self, cpf):
        _dao.delete_secretario(cpf)
        return '', 204


class SecretarioListApi(Resource):

    def get(self):
        secretarios = _dao.get_secretarios()
        return [secretario.serialize() for secretario in secretarios]

    def post(self):
        args = parser.parse_args()
        secretario = Secretario(**args)
        _dao.save_secretario(secretario)

        return secretario.cpf
