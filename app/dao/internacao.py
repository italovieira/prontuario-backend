from ..models.internacao import Internacao
from ..db import db


class InternacaoDAO:

    def get_internacao(self, id_internacao):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM internacao WHERE id_internacao = %s', (id_internacao,))
        result = cursor.fetchone()
        cursor.close()

        return Internacao(*result)


    def get_internacoes(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM internacao')
        result = cursor.fetchall()
        cursor.close()

        return [Internacao(*d) for d in result]


    def save_internacao(self, internacao: Internacao):
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO internacao (cpf_paciente, crm_medico, cnpj_hospital, descricao, data_in, data_out) VALUES (%s ,%s ,%s ,%s, %s, %s)', (internacao.cpf_paciente, internacao.crm_medico, internacao.cnpj_hospital, internacao.descricao, internacao.data_in, internaca.data_out))
        db.connection.commit()
        cursor.close()


    def get_internacoes_from_paciente(self, cpf_paciente):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM internacao WHERE cpf_paciente = %s', (cpf_paciente,))
        result = cursor.fetchall()
        cursor.close()

        return [Internacao(*d) for d in result]
