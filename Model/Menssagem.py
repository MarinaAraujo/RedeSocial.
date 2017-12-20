#from App import *
import sqlite3

class Mensagem ():
    def __init__(self, id, idRemetente, texto,status):
        self.id = id
        self.idRemetente = idRemetente
        self.texto = texto
        self.status=status

    
