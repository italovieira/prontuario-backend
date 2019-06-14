from flask_restful import Resource, reqparse

from ..models.user import User

from ..dao.user import UserDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf', required=True)
parser.add_argument('nome')
parser.add_argument('data_nasc')
parser.add_argument('telefone')
parser.add_argument('email')
parser.add_argument('senha')
parser.add_argument('sexo')
parser.add_argument('endereco')

_dao = UserDAO()

class UserApi(Resource):

    def get(self, cpf):
        user = _dao.get_user(cpf)
        return user.serialize()

    def put(self, cpf):
        args = parser.parse_args()
        user = User(**args)
        _dao.update_user(cpf, user)
        return user.serialize(), 201

    def delete(self, cpf):
        delete_user(cpf)
        return '', 204


class UserListApi(Resource):

    def get(self):
        users = _dao.get_users()
        return [user.serialize() for user in users]

    def post(self):
        args = parser.parse_args()
        user = User(**args)
        _dao.save_user(user)

        return user.cpf
