from ..models.hospital import Hospital
from ..db import db


class HospitalDAO:

    def get_hospital(self, cnpj):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM hospital WHERE cnpj = %s', (cnpj,))
        result = cursor.fetchone()
        cursor.close()

        return Hospital(*result)


    def get_hospitals(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM hospital')
        result = cursor.fetchall()
        cursor.close()

        return [Hospital(*d) for d in result]


    def save_hospital(self, hospital: Hospital):
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO hospital (cnpj, nome, endereco, gerente_secretario_cpf) VALUES (%s ,%s ,%s ,%s)', (hospital.cnpj, hospital.nome, hospital.endereco, hospital.gerente_secretario_cpf))
        db.connection.commit()
        cursor.close()


    def update_hospital(self, cnpj, hospital: Hospital):
        cursor = db.connection.cursor()
        cursor.execute('UPDATE hospital SET nome = %s, endereco = %s, gerente_secretario_cpf', (hospital.cnpj, hospital.nome, hospital.endereco, hospital.gerente_secretario_cpf))
        db.connection.commit()
        cursor.close()


    def delete_hospital(self, cnpj):
        cursor = db.connection.cursor()
        cursor.execute('DELETE FROM hospital WHERE cnpj = %s', (cnpj,))
        db.connection.commit()
        cursor.close()
