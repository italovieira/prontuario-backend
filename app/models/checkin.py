from .model import Model

from ..util import format_date


class Checkin(Model):

    def __init__(self, cpf_paciente, cpf_secretario, data):
        self.cpf_paciente = cpf_paciente
        self.cpf_secretario = cpf_secretario
        self.data = format_date(data)
