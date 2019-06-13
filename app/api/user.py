from flask import jsonify
from flask_restful import Resource, reqparse

from ..models.user import User
from ..db.user import get_user, get_users, save_user, update_user, delete_user


parser = reqparse.RequestParser()
parser.add_argument('cpf', required=True)
parser.add_argument('nome')
parser.add_argument('data_nasc')
parser.add_argument('telefone')
parser.add_argument('email')
parser.add_argument('senha')
parser.add_argument('sexo')
parser.add_argument('endereco')

class UserApi(Resource):

    def get(self, cpf):
        user = get_user(cpf)
        return jsonify(vars(user))

    def put(self, cpf):
        args = parser.parse_args()
        user = User(**args)
        update_user(cpf, user)
        return vars(user), 201

    def delete(self, cpf):
        delete_user(cpf)
        return '', 204


class UserListApi(Resource):

    def get(self):
        users = get_users()
        return jsonify([vars(user) for user in users])

    def post(self):
        args = parser.parse_args()
        user = User(**args)
        save_user(user)

        return user.cpf
