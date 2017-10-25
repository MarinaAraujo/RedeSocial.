from App import *
import sqlite3


conn = sqlite3.connect("novacon.db")

cursor= conn.cursor()

cursor.execute("""
INSERT INTO tb.menssagem (id, idRemetente, coments)
VALUES ("45423", "45425", "aaaaaaaaaaaaaaaa")
""")

cursor.execute("""SELECT * FROM tb.menssagem """, (tb.menssagem))

cursor.execute("""
UPDATE tb.menssagem
SET coments=?
WHERE id=?
""", ())

cursor.execute("""
DELETE FROM tb.menssagem
WHERE coments=?""", ())

conn.commit()
conn.close()
