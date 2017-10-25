from App import *
import sqlite3


conn = sqlite3.connect("novacon.db")

cursor= conn.cursor()

cursor.execute("""
INSERT INTO tb.usuario ( codigo, nome, email, senha, idade, telefone, profissao)
VALUES ("3333", "kleber", "fjdhnd@gmail.com", "12345", "18", "55544432", "professor")
""")

cursor.execute("""SELECT * FROM tb.usuario """, (tb.usuario))

cursor.execute("""
UPDATE tb.usuario
SET codigo=?
WHERE id=?
""", ())

cursor.execute("""
DELETE FROM tb.usuario
WHERE id=?""", ())


conn.commit()
conn.close()
