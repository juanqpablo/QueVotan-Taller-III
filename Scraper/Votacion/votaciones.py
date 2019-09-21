# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.realpath('../'))

#from pathlib import Path
from bs4 import BeautifulSoup as BS
import requests
#from listado import Listado



class Votacion(object):
    def __init__(self, Id, Id_Diputado, voto):
        self.Id = Id
        self.Id_Diputado = Id_Diputado
        self.voto = voto



class Listado(object):
    @classmethod
    def getVotaciones(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, Id, Id_Diputado, voto):
        v = Votacion(Id, Id_Diputado, voto)
        return v



class Votaciones(Listado):
    @classmethod
    def getVotaciones(cls, _id):
        aId_Diputados = []
        aVotos = []
        idVotos = []
        vot = []

        Url_VotaDetalle = "http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionDetalle?prmVotacionId=" + str(_id)
        r = requests.get(Url_VotaDetalle)
        data = r.text
        soup = BS(data, 'xml')
        voto = soup.find_all("Voto")
        for i in voto:
            aId_Diputados.append(i.Id.text)
            if i.OpcionVoto["Valor"] == "0":
                aVotos.append("4")
            if i.OpcionVoto["Valor"] == "1":
                aVotos.append("1")
            if i.OpcionVoto["Valor"] == "2":
                aVotos.append("7")
            idVotos.append(i.Id)

        for i in range(0, len(aVotos)):
            Id = str(idVotos[i])
            Id_Diputado = str(aId_Diputados[i])
            voto = str(aVotos[i])
            vot.append(cls.toObject(Id, Id_Diputado, voto))
        return vot
