
from bs4 import BeautifulSoup as BS
import requests
#from listado import Listado


class Legislatura(object):
    def __init__(self, _id, numero, fecha_inicio, fecha_termino):
        self._id = _id
        self.numero = numero
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino


class Listado(object):
    @classmethod
    def getLegislaturas(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, _id, numero, fecha_inicio, fecha_termino):
        l = Legislatura(_id, numero, fecha_inicio, fecha_termino)
        return l


class Legislaturas(Listado):
    sesiones = {}

    @classmethod
    def getLegislaturas(cls):
        legislaturas = []
        # Url_legislaturas = "http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturas" # para todas la legis
        Url_legislaturas = "http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual"  # ultima legis
        r = requests.get(Url_legislaturas)
        data = r.text
        soup = BS(data, 'xml')
        legis = soup.find_all("Legislatura")
        for i in legis:
            _id = i.ID.text.encode('utf-8')
            _id = _id.decode()
            numero = i.Numero.text.encode('utf-8')
            numero = numero.decode()
            FechaInicio = i.FechaInicio.text.encode('utf-8')
            FechaInicio = FechaInicio.decode().split("T")[0]
            FechaTermino = i.FechaTermino.text.encode('utf-8')
            FechaTermino = FechaTermino.decode().split("T")[0]
            legislaturas.append(cls.toObject(_id, numero, FechaInicio, FechaTermino))
        return legislaturas
