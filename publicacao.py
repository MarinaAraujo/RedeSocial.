#from App import *
import sqlite3


class Publicacao:
    def __init__(self,idPublicacao,idRemetente,horario,texto,nToploose,nXonei,nHu3,nExasperado,nSad):
        self.idPublicacao = idPublicacao
        self.idRemetente = idRemetente
        self.horario = horario
        self.texto = texto
        self.nToploose = nToploose
        self.nXonei = nXonei
        self.nHu3 = nHu3
        self.nExasperado = nExasperado
        self.nSad = nSad

    def inserir ():
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb.publicacao (idRemetente, horario, texto, nToploose,nXonei,nHu3,nExasperado, nSad)
            VALUES (self.idRemetente,self.horario,self.texto,self.nToploose,self.nXonei,self.nHu3,self.nExasperado,self.nSad)
            """)
        conn.commit()
        conn.close()

    def listar():
        publicacoes=[]
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM tb.publicacao """, (tb.publicacao))

        for linha in cursor.fetchall:
            idRemetente = linha[1]
            horario = linha[2]
            texto = linha[3]
            nToploose = linha[4]
            nXonei = linha[5]
            nHu3 = linha[6]
            nExasperado = linha[7]
            nSad = linha[8]
            Publicacao = Publicacao(idRemetente, horario, texto, nToploose,nXonei,nHu3,nExasperado, nSad)
            publicacoes.append(Publicacao)
        conn.close()
        return publicacoes

    def deletar (self, codigo):
        novo_id = 4
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM tb.publicacao
            WHERE idPublicacao=?""", (novo_id,))
        conn.commit()
        conn.close()

    def atualizar (self,idRemetente, horario, texto, nToploose,nXonei,nHu3,nExasperado, nSad):
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""UPDATE tb.publicacao
        SET * VALUES(?,?,?,?,?,?,?)
        WHERE idPublicacao = ?""",())

        conn.commit()
        conn.close()
