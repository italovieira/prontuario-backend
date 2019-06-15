from flask import jsonify
from flask_restful import Resource, reqparse

from ..models.internacao import Internacao

from ..dao.internacao import InternacaoDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf_paciente', required=True)
parser.add_argument('crm_medico', required=True)
parser.add_argument('cnpj_hospital', required=True)
parser.add_argument('descricao')
parser.add_argument('data_in')
parser.add_argument('data_out')

_dao = InternacaoDAO()

class InternacaoApi(Resource):

    def get(self, cpf):
        internacao = _dao.get_internacao(cpf)
        return internacao.serialize()

    def put(self, cpf):
        args = parser.parse_args()
        internacao = Internacao(**args)
        _dao.update_internacao(cpf, internacao)
        return internacao.serialize(), 201

    def delete(self, cpf):
        _dao.delete_internacao(cpf)
        return '', 204


class InternacaoListApi(Resource):

    def get(self):
        internacoes = _dao.get_internacoes()
        return [internacao.serialize() for internacao in internacaoes]

    def post(self):
        args = parser.parse_args()
        internacao = Internacao(**args)
        _dao.save_internacao(internacao)

        return internacao


class PacienteInternacaoListApi(Resource):

    def get(self, cpf):
        internacoes = _dao.get_internacoes_from_paciente(cpf)
        return [internacao.serialize() for internacao in internacoes]


class IniciarInternacaoApi(Resource):

    def post(self, crm):
        args = parser.parse_args()
        args['crm_medico'] = crm
        internacao = Internacao(**args)
        _dao.save_internacao(internacao)

        return internacao
