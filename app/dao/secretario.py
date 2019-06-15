from ..models.secretario import Secretario
from ..db import db
from .usuario import UsuarioDAO

_usuario_dao = UsuarioDAO()

class SecretarioDAO:

    def get_secretario(self, cpf):
        usuario = _usuario_dao.get_usuario(cpf)

        cursor = db.connection.cursor()
        cursor.execute('SELECT cnpj_hospital FROM secretario WHERE cpf_secretario = %s', (cpf,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            dados = usuario.serialize()
            dados['cnpj_hospital'] = result[0]
            return Secretario(**dados)


    def get_secretarios(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_secretario, cnpj_hospital FROM secretario')
        result = cursor.fetchall()
        cursor.close()

        secretarios = []
        for (cpf, cnpj) in result:
            dados = _usuario_dao.get_usuario(cpf).serialize()
            dados['cnpj_hospital'] = cnpj
            secretarios.append(Secretario(**dados))
        return secretarios


    def save_secretario(self, secretario: Secretario):
        _usuario_dao.save_usuario(secretario)

        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO secretario (cpf_secretario, cnpj_hospital) VALUES (%s ,%s)', (secretario.cpf, secretario.cnpj_hospital))
        db.connection.commit()
        cursor.close()


    def update_secretario(self, cpf, secretario: Secretario):
        cursor = db.connection.cursor()
        cursor.execute('UPDATE secretario SET cnpj_hospital = %s WHERE cpf_secretario = %s', (secretario.cnpj_hospital, secretario.cpf))
        cursor.close()

        _usuario_dao.update_usuario(cpf, secretario)


    def delete_secretario(self, cpf):
        cursor = db.connection.cursor()
        cursor.execute('DELETE FROM secretario WHERE cpf_secretario = %s', (cpf,))
        cursor.close()

        _usuario_dao.delete_usuario(secretario)
