from .model import Model

from ..util import format_date


class Cirurgia(Model):

    def __init__(self, cpf_paciente, data, descricao):
        self.cpf_paciente = cpf_paciente
        self.data = format_date(data)
        self.descricao = descricao
