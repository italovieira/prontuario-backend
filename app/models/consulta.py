from .model import Model

from ..util import format_date


class Consulta(Model):

    def __init__(self, cpf_paciente, crm_medico, data):
        self.cpf_paciente = cpf_paciente
        self.resultado = resultado
        self.tipo = tipo
        self.data = format_date(data)
        self.nome_local = nome_local
