from App import *
import sqlite3

class Usuario():
    def __init__(self,codigo, nome, email, senha, idade, telefone, profissao):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade
        self.telefone = telefone
        self.profissao = profissao

    def inserir(self):
            conn = sqlite3.connect("novacon.db")
            cursor= conn.cursor()
            cursor.execute("""
            INSERT INTO tb.usuario (nome, email, senha, idade, telefone, profissao)
            VALUES (self.nome,self.email,self.senha,self.idade,self.telefone,self.profissao)
            """)
            conn.commit()
            conn.close()


    def listar(self):
        usuarios = []
            conn = sqlite3.connect("novacon.db")
            cursor= conn.cursor()
            cursor.execute("""SELECT * FROM tb.usuario """, (tb.usuario))

            for linha in cursor.fetchall:
                nome = linha[1]
                email=linha[2]
                senha=linha[3]
                idade=linha[4]
                telefone=linha[5]
                profissao=linha[6]
                usuario = Usuario(nome, email, senha, profissao, sexo, data_nasc)
                usuarios.append(usuario)
        conn.close()
        return usuarios

    def deletar(self, id):
        pass

    def atualizar(self, nome, email, senha, profissao, sexo, data_nasc):
        pass



cursor.execute("""
''' UPDATE tb.usuario
SET codigo=?
WHERE id=?
""", ())

cursor.execute("""
DELETE FROM tb.usuario
WHERE id=?""", ()) '''
