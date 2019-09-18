import os
import sys
sys.path.insert(0, os.path.realpath('../'))
from bs4 import BeautifulSoup as BS
import requests
#from listado import Listado



class Sesion(object):
    def __init__(self, _id, fecha, tipo, estado):
        self._id = _id
        self.fecha = fecha
        self.tipo = tipo
        self.estado = estado



class Listado(object):
    @classmethod
    def getSesiones(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')
    @classmethod
    def toObject(cls, _id, fecha, tipo, estado):
        s = Sesion(_id, fecha, tipo, estado)
        return s


class Sesiones(Listado):
    @classmethod
    def getSesiones(cls, _id):
        sesiones = []
        Url_Sesion = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=" + str(_id)
        r = requests.get(Url_Sesion)
        data = r.text
        soup = BS(data, 'xml')
        sesi = soup.find_all("Sesion")
        for i in sesi:
            _id = i.ID.text.encode('utf-8')
            _id = _id.decode()
            Fecha = i.Fecha.text.encode('utf-8')
            Fecha = Fecha.decode().split("T")[0]
            tipo = i.Tipo.text.encode('utf-8')
            tipo = tipo.decode()
            estado = i.Estado.text.encode('utf-8')
            estado = estado.decode()
            sesiones.append(cls.toObject(_id, Fecha, tipo, estado))
        return sesiones
