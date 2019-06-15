from flask_restful import Resource, reqparse

from ..login import login


parser = reqparse.RequestParser()
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True)

class LoginApi(Resource):

    def post(self):

        args = parser.parse_args()
        return login(**args)
