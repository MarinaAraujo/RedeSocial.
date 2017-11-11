#from App import *
import sqlite3

class Mensagem ():
    def __init__(self, id, idRemetente, coments):
        self.id = id
        self.idRemetente = idRemetente
        self.coments = coments


    def inserir():
        conn = sqlite3.connect("novacon.db")
        cursor= conn.cursor()
        cursor.execute("""
            INSERT INTO tb.mensagem (idRemetente, coments)
            VALUES (self.idRemetente, self.coments)
            """)

    def listar():
        mensagens = []
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM tb.mensagem """, (tb.mensagem))

        for linha in cursor.fetchall:
            idRemetente = linha[1]
            coments = linha[2]
            Mensagem = Mensagem(idRemetente, coments)
            mensagens.append(Mensagem)
        conn.close()
        return mensagens

    def deletar(self, id):
        novo_id = 3
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""
                DELETE FROM tb.mensagem
                WHERE id=?""", (novo_id,))
        conn.commit()
        conn.close()

    def atualizar(self, idRemetente, coments):
        conn = sqlite3.connect("novacon.db")
        cursor = conn.cursor()
        cursor.execute("""UPDATE tb.mensagem
            SET * VALUES(?,?,?,?,?,?,?)
            WHERE id = ?""", ())
        conn.commit()
        conn.close()
