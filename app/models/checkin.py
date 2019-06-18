from .model import Model

from ..util import format_date


class Checkin(Model):

    def __init__(self, cpf_paciente, cpf_secretario, data):
        self.cpf_paciente = cpf_paciente
        self.cpf_secretario = cpf_secretario
        self.data = format_date(data)

    def serialize(self):
        from ..dao.usuario import UsuarioDAO
        get_nome = UsuarioDAO().get_nome_usuario_from_cpf

        data = super().serialize()
        data['nome_paciente'] = get_nome(data['cpf_paciente'])
        data['nome_secretario'] = get_nome(data['cpf_secretario'])

        return data
