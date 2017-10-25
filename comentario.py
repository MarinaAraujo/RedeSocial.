from App import *
import sqlite3


conn = sqlite3.connect("novacon.db")

cursor= conn.cursor()

cursor.execute("""
INSERT INTO tb.comentario (codigo, idRemetente,idPublicacao, horario, texto, nToploose,nXonei,nHu3,nExasperado, nSad)
VALUES ("54657", "56465", "00:00", "ggbfbfyssghthdf", "somente eu", "80", "4", "35", "55", "7")
""")

cursor.execute("""SELECT * FROM tb.comentario """, (tb.comentario))

cursor.execute("""
UPDATE tb.comentario
SET texto=?
WHERE id=?
""", (novoTexto, idcodigo))

cursor.execute("""
DELETE FROM tb.comentario
WHERE texto=?""", (texto))

conn.commit()
conn.close()
