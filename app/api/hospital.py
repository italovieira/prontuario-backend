from flask_restful import Resource, reqparse

from ..models.hospital import Hospital

from ..dao.hospital import HospitalDAO


parser = reqparse.RequestParser()
parser.add_argument('cnpj', required=True)
parser.add_argument('nome')
parser.add_argument('endereco')
parser.add_argument('gerente_secretario_cpf')

_dao = HospitalDAO()

class HospitalApi(Resource):

    def get(self, cnpj):
        hospital = _dao.get_hospital(cnpj)
        return hospital.serialize()

    def put(self, cnpj):
        args = parser.parse_args()
        hospital = Hospital(**args)
        _dao.update_hospital(cnpj, hospital)
        return hospital.serialize(), 201

    def delete(self, cnpj):
        _dao.delete_hospital(cnpj)
        return '', 204


class HospitalListApi(Resource):

    def get(self):
        hospitals = _dao.get_hospitals()
        return [hospital.serialize() for hospital in hospitals]

    def post(self):
        args = parser.parse_args()
        hospital = Hospital(**args)
        _dao.save_hospital(hospital)

        return hospital.cnpj
