from ..models.consulta import Consulta
from ..db import db


class ConsultaDAO():

    def get_consulta(self, id_consulta):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_paciente, crm_medico, data FROM consulta WHERE id_consulta = %s', (id_consulta,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return Consulta(*result)


    def get_consultas(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM consulta')
        result = cursor.fetchall()
        cursor.close()

        return [Consulta(*d) for d in result]


    def save_consulta(self, consulta: Consulta):
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO consulta (cpf_paciente, crm_medico, data) VALUES (%s ,%s ,%s)', (consulta.cpf_paciente, consulta.crm_medico, consulta.data))
        db.connection.commit()
        cursor.close()


    def get_consultas_from_paciente(self, cpf_paciente):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_paciente, crm_medico, data FROM consulta WHERE cpf_paciente = %s', (cpf_paciente,))
        result = cursor.fetchall()
        cursor.close()

        return [Consulta(*d) for d in result]
