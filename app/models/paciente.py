from .usuario import Usuario


class Paciente(Usuario):
    def __init__(self, cpf, nome, data_nasc, telefone, email, senha, sexo, endereco, tipo_sanguineo):
        super().__init__(cpf, nome, data_nasc, telefone, email, senha, sexo, endereco)
        self.tipo_sanguineo = tipo_sanguineo

    def serialize(self):
        data = super().serialize()
        data['tipo_sanguineo'] = self.tipo_sanguineo
        return data
