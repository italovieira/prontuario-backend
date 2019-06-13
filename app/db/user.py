from ..models.user import User
from ..db import db

def get_user(cpf):
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM usuario WHERE cpf = %s', (cpf,))
    result = cursor.fetchone()
    cursor.close()

    return User(*result)


def get_users():
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM usuario')
    result = cursor.fetchall()
    cursor.close()

    return [User(*u) for u in result]


def save_user(user: User):
    cursor = db.connection.cursor()
    cursor.execute('INSERT INTO usuario (cpf, nome, data_nasc, telefone, email, senha, sexo, endereco) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)', (user.cpf, user.nome, user.data_nasc, user.telefone, user.email, user.senha, user.sexo, user.endereco))
    db.connection.commit()
    cursor.close()


def update_user(cpf, user: User):
    cursor = db.connection.cursor()
    cursor.execute('UPDATE usuario SET nome = %s, data_nasc = %s, telefone = %s, email = %s, senha = %s, sexo = %s, endereco = %s WHERE cpf = %s', (user.nome, user.data_nasc, user.telefone, user.email, user.senha, user.sexo, user.endereco, cpf))
    db.connection.commit()
    cursor.close()


def delete_user(cpf):
    cursor = db.connection.cursor()
    cursor.execute('DELETE FROM usuario WHERE cpf = %s', (cpf,))
    db.connection.commit()
    cursor.close()
