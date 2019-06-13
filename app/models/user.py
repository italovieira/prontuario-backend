from .model import Model

from ..db import db


class User:

    def __init__(self, cpf, nome, data_nasc, telefone, email, senha, sexo, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.sexo = sexo
        self.endereco = endereco
