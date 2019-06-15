from .model import Model

from ..util import format_date

class Exame(Model):

    def __init__(self, cpf_paciente, resultado, tipo, data, nome_local):
        self.cpf_paciente = cpf_paciente
        self.resultado = resultado
        self.tipo = tipo
        self.data = format_date(data)
        self.nome_local = nome_local
