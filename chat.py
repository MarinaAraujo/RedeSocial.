from App import *
import sqlite3


conn = sqlite3.connect("novacon.db")

cursor= conn.cursor()

cursor.execute("""
INSERT INTO tb.chat (idUsuario, idRemetente, id)
VALUES ("455423", "45725", "65675")
""")

cursor.execute("""SELECT * FROM tb.chat """, (tb.chat))

cursor.execute("""
UPDATE tb.chat
SET id=?
WHERE id=?
""", ())

cursor.execute("""
DELETE FROM tb.chat
WHERE id=?""", ())

conn.commit()
conn.close()
