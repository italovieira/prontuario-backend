from .model import Model


class Checkin(Model):

    def __init__(self, cpf_paciente, cpf_secretario, data):
        self.cpf_paciente = cpf_paciente
        self.cpf_secretario = cpf_secretario
        self.data = data
