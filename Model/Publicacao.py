#from App import *
import sqlite3


class Publicacao:
    def __init__(self,idPublicacao,idRemetente,horario,texto,nToploose,nXonei,nHu3,nExasperado,nSad):
        self.idPublicacao = idPublicacao
        self.idRemetente = idRemetente
        self.horario = horario
        self.texto = texto
        self.nToploose = nToploose
        self.nXonei = nXonei
        self.nHu3 = nHu3
        self.nExasperado = nExasperado
        self.nSad = nSad

    
