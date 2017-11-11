from mensagem import *
import sqlite3

class Mensagem ():
    def __init__(self, id, idUsuario, idRemetente):
        self.id = id
        self.idUsuario = idUsuario
        self.idRemetente = idRemetente

    def inserir():
        conn = sqlite3.connect("novacon.db")
        cursor= conn.cursor()
        cursor.execute("""
            INSERT INTO tb.chat (idUsuario, idRemetente)
            VALUES (self.idUsuario,self.idRemetente)
            """)

    def listar(Mensagem):
        return Mensagem

    def deletar(self, id):
        novo_id = 8
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""
                DELETE FROM tb.chat
                WHERE id=?""", (novo_id,))
        conn.commit()
        conn.close()

    def atualizar(self, idUsuario, idRemetente):
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""UPDATE tb.chat
            SET * VALUES(?,?,?,?,?,?,?)
            WHERE id = ?""", ())
        conn.commit()
        conn.close()
