from flask_restful import Resource, reqparse

from ..models.checkin import Checkin

from ..dao.checkin import CheckinDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf_paciente', required=True)
parser.add_argument('cpf_secretario')
parser.add_argument('data')

_dao = CheckinDAO()

class CheckinApi(Resource):

    def get(self, cnpj):
        checkin = _dao.get_checkin(cnpj)
        return checkin.serialize()

    def put(self, cnpj):
        args = parser.parse_args()
        checkin = Checkin(**args)
        _dao.update_checkin(cnpj, checkin)
        return checkin.serialize(), 201

    def delete(self, cnpj):
        _dao.delete_checkin(cnpj)
        return '', 204


class CheckinListApi(Resource):

    def get(self):
        checkins = _dao.get_checkins()
        return [checkin.serialize() for checkin in checkins]

    def post(self):
        args = parser.parse_args()
        checkin = Checkin(**args)
        _dao.save_checkin(checkin)

        return checkin.cnpj


class HospitalCheckinListApi(Resource):

    def get(self, cnpj):
        checkins = _dao.get_checkins_from_hospital(cnpj)
        return [checkin.serialize() for checkin in checkins]


class NovoCheckinApi(Resource):

    def post(self, cpf):
        args = parser.parse_args()
        args['cpf_secretario'] = cpf
        checkin = Checkin(**args)
        _dao.save_checkin(checkin)

        return checkin.serialize()
