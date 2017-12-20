import mysql.connect
from Model.Usuario import Usuario
from Model.Chat import Chat
from Model.Comentario import Comentario
from Model.Mensagem import Mensagem
from Model.Publicacao import Publicacao
from Model.RedeSocial import RedeSocial
from UsuarioDAO import UsuarioDAO
from ChatDAO import ChatDAO
from ComentarioDAO import ComentarioDAO
from MensagemDAO import MensagemDAO
from PublicacaoDAO import PublicacaoDAO

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

userfeed = Usuario()

#função para criar a rede social
def criarRedeSocial():
    nome = str(input("Digite um nome da Rede Social: "))
    redeSocial = RedeSocial(nome)
    idRedeSocial = redeSocial.inserirRedeSocial(redeSocial)
    
        cursor= conn.cursor()
        
        #criando tabelas do banco de dados
    cursor.execute(""" CREATE TABLE tb_usuario(
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        email VARCHAR(40) NOT NULL UNIQUE,
        senha INTEGER NOT NULL,
        idade INTEGER,
        telefone INTEGER,
        profissao VARCHAR(70)
    );""")

    cursor.execute("""CREATE TABLE tb_publicacao(
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

    cursor.execute("""CREATE TABLE tb_comentario(
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
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

    cursor.execute(""" CREATE TABLE tb_chat(
        idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
        idRemetente INTEGER,
        id INTEGER,
    );""")
    
    cursor.execute(""" CREATE TABLE tb_contato(
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        emailuser1 VARCHAR(40) NOT NULL UNIQUE,
        emailuser2 VARCHAR(40) NOT NULL UNIQUE,
        nomeuser2 varchar (50)
        dataAmizade DATE
    );""")
    conn.close()

    cursor.execute("""CREATE TABLE tb_mensagem(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email-remetente VARCHAR (50) not NULL),
    email-destinatario VARCHAR (50) NOT NULL,
    texto VARCHAR (256)""")

    # adicionando contatos
def addcontato():
    pesq=input('digite o nome do amigo que procura')
    print(cursor = conn.cursor("""
    select nome, email from tb_Usuario WHERE nome like %?%""")pesq)
    conn.close()
    auxemail=input('digite o email do amigo a ser adicionado')
    cursor=conn.cursor("""
    insert into tb_amizade values (userfeed.email, auxemail,"today")
    """)
    conn.close()

    #listando contatos
def listarcontatos():
    cursor=conn.cursor()
    for i in cursor.fetchall:
        print(cursor.execute(""" select nomeuser2 from tb_contato where codigo = ?""")i)
    conn.close

#executando login do usuario
def logIn():
    print('========================================================================================================================')
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
        userfeed=usuario
        return (True, usuario)
    
# checando se o email realmente é valido
def validarEmail(email):
    if ((email.find('@')>0) and(len(email)>9)):
        return(1)
    else:
        return(0)
#fução para cadastar um novo usuario
def signUp():
    print('========================================================================================================================')
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
    UsuarioDAO.inserir()

def LerMensagens():
    cursor=conn.cursor()
    cursor.execute("""select email_remetende,texto from tb_mensagem where email_destinatario = ?
    """,(userfeed.email))
    print(cursor)
    conn.close

def enviarMensagem()
    m=Mensagem()
    m.email=input("digite o email do destinatário da mensagem")
    m.texto=input("digite a mensagem a ser enviada")
    MensagemDAO.inserir(m)
    
def ExcluirContato(): 
    delEmail=input("Digite o email do usuário a ser deletado")
    cursor=conn.cursor()
    cursor.execute(""" DELETE FROM tb_Contatos
    WHERE email=?
    """,(delEmail))

def menu2 ():
     continuar = True

    while continuar:
 
        try:
            menuzinho2=input('o que desseja fazer agora?')
            print('0-sair\n1-ver amigos\n 2-adicionar amigos\n3-ler as mensagens recebidas\n 4-enviar mensagem\n5-excluir contato')
            if menuzinho2 ==1:
                listarcontatos()
            elif menuzinho2==2:
                addcontato()
            elif menuzinho2 ==3:
                LerMensagens()
            elif menuzinho2 == 4:
                enviarMensagem()
            elif menuzinho2 ==5:
                ExcluirContato()
            elif menuzinho2 == 0 :
                break
        except ValueError:
            print("Digite um valor válido")

#criando o menu
def menuzinho():
     print('====================================================(   NOVACON   )==========================================================')
    print('bem vindo!')
    menu1=input('o que gostaria de fazer agora? \n 1-criar rede social\n 2-Realizar LogIn \n 3-Cadastrar um novo usuário\n 0-Sair' )
    
         continuar = True

    while continuar:
 
        try:
          
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                criarRedeSocial()

            elif (opcao == 2):
                logIn()
                menu2()
                
            elif (opcao == 3):
                signUp()

            elif (opcao == 0):
                continuar = False
            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite um valor válido")

def Main():
    criarRedeSocial()
    menuzinho()

if __name__ == "__main__":
    app.run()
