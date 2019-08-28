import requests
import xmltodict
import json
from pymongo import MongoClient

# retorna los datos en formato json


def obtener():
    datos = requests.get(url)
    if len(datos.text) > 50:
        jsonDatos = json.dumps(xmltodict.parse(datos.text))
        jsonDatos = json.loads(jsonDatos)
    return jsonDatos


def guardar(document, collectionNombre):
    collection = db[collectionNombre]
    collection.insert_one(document)
    return


# connecion mongo
c = MongoClient('localhost', 27017)
db = c.DatosSenado

# legislatura
url = "http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual"
jsonDatos = obtener()
# sesiones
url = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=" + \
    jsonDatos['Legislatura']['ID']
jsonDatos = obtener()

for sesion in jsonDatos['Sesiones']['Sesion']:
    document = {'id_sesion': sesion['ID'], 'fecha': sesion['Fecha'],
                'tipo': sesion['Tipo']['#text'], 'estado': sesion['Estado']['#text']}
    guardar(document, 'Sesion')
    
    # boletines
    url = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=" + \
        sesion['ID']
    jsonDatos = obtener()
    datos = requests.get(url)
    if len(datos.text) > 50:
        if jsonDatos.has("ORDEN_DIA"):
            for proyecto_ley in jsonDatos['BOLETINXML']['SESION']['ORDEN_DIA']['PROYECTO_LEY']:
                print proyecto_ley["@BOLETIN"]
            # proyecto
            url = "https://www.senado.cl/wspublico/tramitacion.php?boletin=" + sesion['ID']
            jsonDatos = obtener()
