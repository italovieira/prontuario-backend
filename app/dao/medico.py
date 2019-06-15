from ..models.medico import Medico
from ..db import db
from .usuario import UsuarioDAO

_usuario_dao = UsuarioDAO()

class MedicoDAO:

    def get_medico(self, crm):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cpf_medico FROM medico WHERE crm_medico = %s', (crm,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            cpf = result[0]
        else:
            return None

        usuario = _usuario_dao.get_usuario(cpf)
        if usuario:
            dados = usuario.serialize()
            dados['crm'] = crm
            dados['hospitais'] = self.get_hospitais_by_medico(crm)
            return Medico(**dados)
        return None


    def get_medico_from_cpf(self, cpf):
        cursor = db.connection.cursor()
        cursor.execute('SELECT crm_medico FROM medico WHERE cpf_medico = %s', (cpf,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            crm = result[0]
            return self.get_medico(crm)

        return None


    def get_medicos(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT crm_medico, cpf_medico FROM medico')
        result = cursor.fetchall()
        cursor.close()

        medicos = []
        for (crm, cpf) in result:
            dados = _usuario_dao.get_usuario(cpf).serialize()
            dados['crm'] = crm
            medicos.append(Medico(**dados))
        return medicos


    def save_medico(self, medico: Medico):
        _usuario_dao.save_usuario(medico)

        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO medico (crm_medico, cpf_medico) VALUES (%s ,%s)', (medico.crm, medico.cpf))

        for cnpj in medico.hospitais:
            self.save_medico_trabalha_em(medico.crm, cnpj)

        db.connection.commit()
        cursor.close()


    def update_medico(self, crm, medico: Medico):
        cpf = self.get_medico(crm).cpf
        _usuario_dao.update_usuario(cpf, medico)


    def delete_medico(self, crm):
        cursor = db.connection.cursor()
        cursor.execute('DELETE FROM medico WHERE crm_medico = %s', (crm,))
        cursor.close()

        _usuario_dao.delete_usuario(medico)


    def get_hospitais_by_medico(self, crm):
        cursor = db.connection.cursor()
        cursor.execute('SELECT cnpj_hospital FROM trabalha_em WHERE crm_medico = %s', (crm,))
        result = cursor.fetchall()
        cursor.close()

        return [cnpj for (cnpj,) in result]


    def save_medico_trabalha_em(self, crm, cnpj):
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO trabalha_em (cnpj_hospital, crm_medico) VALUES (%s ,%s)', (cnpj, crm))
        cursor.close()
