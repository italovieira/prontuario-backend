from flask_restful import Resource, reqparse

from ..models.usuario import Usuario

from ..dao.usuario import UsuarioDAO


parser = reqparse.RequestParser()
parser.add_argument('cpf', required=True)
parser.add_argument('nome')
parser.add_argument('data_nasc')
parser.add_argument('telefone')
parser.add_argument('email')
parser.add_argument('senha')
parser.add_argument('sexo')
parser.add_argument('endereco')

_dao = UsuarioDAO()

class UsuarioApi(Resource):

    def get(self, cpf):
        usuario = _dao.get_usuario(cpf)
        return usuario.serialize()

    def put(self, cpf):
        args = parser.parse_args()
        usuario = Usuario(**args)
        _dao.update_usuario(cpf, usuario)
        return usuario.serialize(), 201

    def delete(self, cpf):
        _dao.delete_usuario(cpf)
        return '', 204


class UsuarioListApi(Resource):

    def get(self):
        usuarios = _dao.get_usuarios()
        return [usuario.serialize() for usuario in usuarios]

    def post(self):
        args = parser.parse_args()
        usuario = Usuario(**args)
        _dao.save_usuario(usuario)

        return usuario.cpf
