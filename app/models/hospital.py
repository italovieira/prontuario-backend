from .model import Model


class Hospital(Model):

    def __init__(self, cnpj, nome, endereco, gerente_secretario_cpf):
        self.cnpj = cnpj
        self.nome = nome
        self.endereco = endereco
        self.gerente_secretario_cpf = gerente_secretario_cpf
