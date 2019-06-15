from .model import Model


class Cirurgia(Model):

    def __init__(self, cpf_paciente, data, descricao):
        self.cpf_paciente = cpf_paciente
        self.data = data
        self.descricao = descricao
