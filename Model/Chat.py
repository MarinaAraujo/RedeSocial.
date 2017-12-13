from Model.Mensagem import Mensagem
import sqlite3

class Chat ():
    def __init__(self, id, idUsuario, idRemetente):
        self.id = id
        self.idUsuario = idUsuario
        self.idRemetente = idRemetente

  
