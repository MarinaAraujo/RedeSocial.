#from App import *
import sqlite3


class Comentario:
    def __init__(self,codigo,idRemetente,idPublicacao,horario,texto,nToploose,nXonei,nHu3,nExasperado,nSad):
        self.codigo = codigo
        self.idRemetente = idRemetente
        self.idPublicacao = idPublicacao
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
            INSERT INTO tb.comentario (idRemetente,idPublicacao, horario, texto, nToploose,nXonei,nHu3,nExasperado, nSad)
            VALUES (self.codigo,self.idRemetente,self.idPublicacao,self.horario,self.texto,self.nToploose,self.nXonei,self.nHu3,self.nExasperado,self.nSad)
            """)
        conn.commit()
        conn.close()

    def listar():
        comentarios=[]
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM tb.comentario """, (tb.comentario))

        for linha in cursor.fetchall:
            idRemetente = linha[1]
            idPublicacao = linha[2]
            horario = linha[3]
            texto = linha[4]
            nToploose = linha[5]
            nXonei = linha[6]
            nHu3 = linha[7]
            nExasperado = linha[8]
            nSad = linha[9]
            Comentario = Comentario(idRemetente,idPublicacao, horario, texto, nToploose,nXonei,nHu3,nExasperado, nSad)
            comentarios.append(Comentario)
        conn.close()
        return comentarios

    def deletar (self, codigo):
        novo_codigo = 2
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM tb.comentario
            WHERE codigo=?""", (novo_codigo,))
        conn.commit()
        conn.close()

    def atualizar (self,idRemetente,idPublicacao, horario, texto, nToploose,nXonei,nHu3,nExasperado, nSad):
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""UPDATE tb.comentario
        SET * VALUES(?,?,?,?,?,?,?)
        WHERE codigo = ?""",())

        conn.commit()
        conn.close()




