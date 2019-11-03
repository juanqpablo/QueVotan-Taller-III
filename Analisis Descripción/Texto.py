import spacy
from collections import Counter
from pymongo import MongoClient
f = open("dley.txt")
datos = f.read().decode('utf8')
datos = datos.replace(".","")
print datos
datos_frecuencia = Counter(datos.split())
npl = spacy.load("es_core_news_sm")
datos = npl(datos)
datos_limpios = []

for token in datos:
    if token.pos_ == "VERB":
        datos_limpios.append({str(token) : datos_frecuencia.get(token.text)})

for dato in datos_limpios:
    if dato.values()== [None]:
        dato.update({dato.items()[0][0]:1})

conn = MongoClient()
db = conn.DatosSenado
collections = db.Palabras
print datos_limpios
collections.insert_many(datos_limpios)
