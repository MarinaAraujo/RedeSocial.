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

    
