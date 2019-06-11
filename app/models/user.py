class User:
    def __init__(self, cpf, name):
        self.cpf = cpf
        self.name = name

    def serialize(self):
        return {
                'cpf': self.cpf,
                'name': self.name
        }
