from ..models.paciente import Paciente
from ..db import db
from .usuario import UsuarioDAO

_usuario_dao = UsuarioDAO()

class PacienteDAO:

    def get_paciente(self, cpf):
        usuario = _usuario_dao.get_usuario(cpf)

        cursor = db.connection.cursor()
        cursor.execute('SELECT tipo_sanguineo FROM paciente WHERE cpf_paciente = %s', (cpf,))
        result = cursor.fetchone()
        cursor.close()

        dados = usuario.serialize()
        dados['tipo_sanguineo'] = result[0]
        return Paciente(**dados)


    def get_pacientes(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_paciente, tipo_sanguineo FROM paciente')
        result = cursor.fetchall()
        cursor.close()

        pacientes = []
        for (cpf, tipo_sanguineo) in result:
            dados = _usuario_dao.get_usuario(cpf).serialize()
            dados['tipo_sanguineo'] = tipo_sanguineo
            pacientes.append(Paciente(**dados))
        return pacientes


    def save_paciente(self, paciente: Paciente):
        _usuario_dao.save_usuario(paciente)

        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO paciente (cpf_paciente, tipo_sanguineo) VALUES (%s ,%s)', (paciente.cpf, paciente.tipo_sanguineo))
        db.connection.commit()
        cursor.close()


    def update_paciente(self, cpf, paciente: Paciente):
        cursor = db.connection.cursor()
        cursor.execute('UPDATE paciente SET tipo_sanguineo = %s WHERE cpf_paciente = %s', (paciente.tipo_sanguineo, paciente.cpf))
        cursor.close()

        _usuario_dao.update_usuario(cpf, paciente)


    def delete_paciente(self, cpf):
        cursor = db.connection.cursor()
        cursor.execute('DELETE FROM paciente WHERE cpf_paciente = %s', (cpf,))
        cursor.close()

        _usuario_dao.delete_usuario(paciente)
