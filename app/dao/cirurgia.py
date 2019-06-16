from ..models.cirurgia import Cirurgia
from ..db import db


class CirurgiaDAO:

    def get_cirurgia(self, id_cirurgia):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_paciente, data, descricao FROM cirurgia WHERE id_cirurgia = %s', (id_cirurgia,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return Cirurgia(*result)


    def get_cirurgias(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_paciente, data, descricao FROM cirurgia')
        result = cursor.fetchall()
        cursor.close()

        return [Cirurgia(*d) for d in result]


    def save_cirurgia(self, cirurgia: Cirurgia):
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO cirurgia (cpf_paciente, data, descricao) VALUES (%s, %s, %s)', (cirurgia.cpf_paciente, cirurgia.data, cirurgia.descricao))
        db.connection.commit()
        cursor.close()


    def get_cirurgias_from_paciente(self, cpf_paciente):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_paciente, data, descricao FROM cirurgia WHERE cpf_paciente = %s', (cpf_paciente,))
        result = cursor.fetchall()
        cursor.close()

        return [Cirurgia(*d) for d in result]
