from .usuario import Usuario


class Secretario(Usuario):
    def __init__(self, cpf, nome, data_nasc, telefone, email, senha, sexo, endereco, cnpj_hospital):
        super().__init__(cpf, nome, data_nasc, telefone, email, senha, sexo, endereco)
        self.cnpj_hospital = cnpj_hospital
