from ..models.checkin import Checkin
from ..db import db


class CheckinDAO():

    def get_checkin(self, id_checkin):
        pass


    def get_checkins(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_paciente, cpf_secretario, data FROM check_in')
        result = cursor.fetchall()
        cursor.close()

        return [Checkin(*d) for d in result]


    def save_checkin(self, checkin: Checkin):
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO check_in (cpf_paciente, cpf_secretario, data) VALUES (%s ,%s ,%s)', (checkin.cpf_paciente, checkin.cpf_secretario, checkin.data))
        db.connection.commit()
        cursor.close()


    def get_checkins_from_hospital(self, cnpj_hospital):
        cursor = db.connection.cursor()
        cursor.execute('SELECT c.cpf_paciente, c.cpf_secretario, data FROM check_in AS c, secretario AS s WHERE c.cpf_secretario = s.cpf_secretario AND s.cnpj_hospital = %s', (cnpj_hospital,))
        result = cursor.fetchall()
        cursor.close()

        return [Checkin(*d) for d in result]
