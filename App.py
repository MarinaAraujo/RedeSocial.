import mysql.connect
from Model.Usuario import Usuario
from Model.Chat import Chat
from Model.Comentario import Comentario
from Model.Mensagem import Mensagem
from Model.Publicacao import Publicacao
from model.RedeSocial import RedeSocial

try:
    # conectando ao banco :3
    conn = mysql.connector.connect(user='root',
                              password='ifpbinfo',
                              host='127.0.0.1',
                              database='Novacondb')

except mysql.connector.Error as err:
    print("erro na base de dados")
else:
    # encerrando conexão por precaução
    conn.close()



def criarRedeSocial():
    nome = str(input("Digite um nome da Rede Social: "))
    redeSocial = RedeSocial(nome)
    idRedeSocial = redeSocial.inserirRedeSocial(redeSocial)
    
        cursor= conn.cursor()

    cursor.execute(""" CREATE TABLE tb.usuario(
        codigo INTEGER PRIMARY KEY AUTOCOMPLETE,
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
   def logar(conn):
    cursor = conn.cursor()

    email = input("Digite seu email:\n ")
    senha = input("Digite sua senha:\n ")

    cursor.execute("""
        Select * From tb_Usuario where email = ? and senha = ?;
    """, (email, senha))
    usuario = cursor.fetchone()
    print(usuario)

    if (usuario == None):
        return (False, "NADA")
    else:
        return (True, usuario)

def validarEmail(email):
    if ((email.find('@')>0) and(len(email)>9)):
        return(1)
    else:
        return(0)

def signIn():
    NovoUsuario = Usuario('','',0,0,0,'')
    NovoUsuario.nome = input('Digite o nome de usuário')
    NovoUsuario.email = input('Digie seu E-mail')
    if validarEmail(NovoUsuario.email) == 0:
        NovoUsuario.email = input('Email inválido, digite novamente')
    senha1 = input('Qual será sua senha? Remonmendamos uma senha com mais de 8 dígitos numeros ')
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
    menu1=input('o que gostaria de fazer agora? \n 1-criar rede social\n 2-Realizar LogIn \n 3-Cadastrar um novo usuário\n 0-Sair' )
    
         continuar = True

    while continuar:
 
        try:
          
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                criarRedeSocial()

            elif (opcao == 2):
                logIn()
                
            elif (opcao == 3):
                signIn()   

            elif (opcao == 0):
                continuar = False
            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite um valor válido")

def Main():
    menuzinho()

if __name__ == "__main__":
    app.run()
