from flask import jsonify
from flask_restful import Resource

from ..models.user import User


class UserApi(Resource):
    def get(self):
        user = User('14248998424', 'Fulano')
        return jsonify(user.serialize())
