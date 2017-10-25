from App import *
import sqlite3


conn = sqlite3.connect("novacon.db")

cursor= conn.cursor()

cursor.execute("""
INSERT INTO tb.publicacao (idRemetente,idPublicacao, horario, texto,publico, nToploose,nXonei,nHu3,nExasperado, nSad)
VALUES ("54654", "5645", "20:00", "ggbfbfhssghthdf", "somente eu", "90", "5", "65", "35", "3")
""")

cursor.execute("""SELECT * FROM tb.publicacao """, (tb.publicacao))

cursor.execute("""
UPDATE tb.publicacao
SET horario=?
WHERE h=?
""", ())

cursor.execute("""
DELETE FROM tb.publicacao
WHERE publico=?""", ())

conn.commit()
conn.close()
