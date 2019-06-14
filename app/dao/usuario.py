from ..models.usuario import Usuario
from ..db import db


class UsuarioDAO:

    def get_usuario(self, cpf):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM usuario WHERE cpf = %s', (cpf,))
        result = cursor.fetchone()
        cursor.close()

        return Usuario(*result)


    def get_usuarios(self):
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM usuario')
        result = cursor.fetchall()
        cursor.close()

        return [Usuario(*u) for u in result]


    def save_usuario(self, usuario: Usuario):
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO usuario (cpf, nome, data_nasc, telefone, email, senha, sexo, endereco) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)', (usuario.cpf, usuario.nome, usuario.data_nasc, usuario.telefone, usuario.email, usuario.senha, usuario.sexo, usuario.endereco))
        db.connection.commit()
        cursor.close()


    def update_usuario(self, cpf, usuario: Usuario):
        cursor = db.connection.cursor()
        cursor.execute('UPDATE usuario SET nome = %s, data_nasc = %s, telefone = %s, email = %s, senha = %s, sexo = %s, endereco = %s WHERE cpf = %s', (usuario.nome, usuario.data_nasc, usuario.telefone, usuario.email, usuario.senha, usuario.sexo, usuario.endereco, cpf))
        db.connection.commit()
        cursor.close()


    def delete_usuario(self, cpf):
        cursor = db.connection.cursor()
        cursor.execute('DELETE FROM usuario WHERE cpf = %s', (cpf,))
        db.connection.commit()
        cursor.close()
