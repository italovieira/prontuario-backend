from .usuario import Usuario


class Medico(Usuario):
    def __init__(self, cpf, nome, data_nasc, telefone, email, senha, sexo, endereco, crm, hospitais=[]):
        super().__init__(cpf, nome, data_nasc, telefone, email, senha, sexo, endereco)
        self.crm = crm
        self.hospitais = hospitais

    def serialize(self):
        data = super().serialize()
        data['crm'] = self.crm
        data['hospitais'] = self.hospitais
        return data
