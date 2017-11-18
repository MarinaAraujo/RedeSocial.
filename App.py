import sqlite3
from Model.Usuario import Usuario
from Model.Chat import Chat
from Model.Comenttario import Comentario
from Model.Mensagem import Mensagem
from Model.Publicacao import Publicacao

conn = sqlite3.connect("novacon.db")

cursor= conn.cursor()

cursor.execute(""" CREATE TABLE tb.usuario(
    codigo INTEGER PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(40) NOT NULL UNIQUE,
    senha INTEGER NOT NULL,
    idade INTEGER,
    telefone INTEGER,
    profissao VARCHAR(70)
);""")

cursor.execute("""CREATE TABLE tb.publicacao(
    idRemetente INTEGER NOT NULL,
    idPublicacao INTEGER NOT NULL,
    horario INTEGER NOT NULL,
    texto TEXT,
    publico VARCHAR(15),
    nToploose INTEGER NOT NULL,
    nXonei  INTEGER NOT NULL,
    nHu3 INTEGER NOT NULL,
    nExasperado INTEGER NOT NULL
    nSad INTEGER NOT NULL
);""")

cursor.execute("""CREATE TABLE tb.comentario(
    codigo INTEGER,
    idRemetente INTEGER NOT NULL,
    idPublicacao INTEGER NOT NULL,
    horario INTEGER NOT NULL,
    texto TEXT,
    nToploose INTEGER NOT NULL,
    nXonei  INTEGER NOT NULL,
    nHu3 INTEGER NOT NULL,
    nExasperado INTEGER NOT NULL
    nSad INTEGER NOT NULL
); """)

cursor.execute(""" CREATE TABLE tb.menssagem(
    id INTEGER,
    idRemetente INTEGER,
    coments TEXT
);""")

cursor.execute(""" CREATE TABLE tb.chat(
    idUsuario INTEGER,
    idRemetente INTEGER,
    id INTEGER,
);""")
conn.close()

def logIn():
   pass

def verifExist(nick):
    pass

def validarEmail(email):
    if ((email.find('@')>0) and(len(email)>9)):
        return(1)
    else:
        return(0)

def signIn():
    NovoUsuario = Usuario
    NovoUsuario.nome = input('Digite o nome de usuário')
    if verifExist(NovoUsuario.nome) == 0:
        NovoUsuario.nome = input('Nome de usuário já utilizado, tente outro')
    NovoUsuario.email = input('Digie seu E-mail')
    if validarEmail(NovoUsuario.email) == 0:
        NovoUsuario.email = input('Email inválido, digite novamente')
    senha1 = input('Qual será sua senha? Remonmendamos uma senha com mais de 8 dígitos mesclando letras e numeros ')
    senha2 = input('Por favor confirme sua senha')
    if senha1 == senha2:
        NovoUsuario.senha = senha1
        senha2 = 0
        senha1 = 0
    else:
        senha1 = input(
            'Senha inválida, Ddigite novamente, Remonmendamos uma senha com mais de 8 dígitos mesclando letras e numeros ')
        senha2 = input('Por favor confirme sua senha')
    NovoUsuario.idade = input('Digite sua idade')
    NovoUsuario.telefone = input('Digite seu Telefone')
    NovoUsuario.profissao = input('Digite sua profissão')
    Usuario.inserir()

def menuzinho():
    print('========================================================================================================================')
    print('bem vindo')
    menu1=input('o que gostaria de fazer agora? \n 1-Realizar LogIn \n 2-Cadastrar um novo usuário')
    if (menu1 ==1):
        logIn()
    elif (menu1== 2):
        signIn()
 else:
        x=1

def Main():
    menuzinho()

if __name__ == "__main__":
    app.run()
