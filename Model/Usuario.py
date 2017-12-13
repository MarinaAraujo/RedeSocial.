#from App import *
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

    
