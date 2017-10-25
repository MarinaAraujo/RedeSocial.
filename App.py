import sqlite3

conn = sqlite3.connect("novacon.db")

cursor= conn.cursor()

cursor.execute(""" CREATE TABLE tb.usuario(
    codigo INTEGER NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(40) NOT NULL,
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



