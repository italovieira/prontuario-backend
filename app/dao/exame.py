from ..models.exame import Exame
from ..db import db


class ExameDAO:

    def get_exame(self, id_exame):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM exame WHERE id_exame = %s', (id_exame,))
        result = cursor.fetchone()
        cursor.close()

        return Exame(*result)


    def get_exames(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM exame')
        result = cursor.fetchall()
        cursor.close()

        return [Exame(*d) for d in result]


    def save_exame(self, exame: Exame):
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO exame (cpf_paciente, resultado, tipo, data, nome_local) VALUES (%s ,%s ,%s ,%s, %s)', (exame.cpf_paciente, exame.resultado, exame.tipo, exame.data, exame.nome_local))
        db.connection.commit()
        cursor.close()


    def get_exames_from_paciente(self, cpf_paciente):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM exame WHERE cpf_paciente = %s', (cpf_paciente,))
        result = cursor.fetchall()
        cursor.close()

        return [Exame(*d) for d in result]
