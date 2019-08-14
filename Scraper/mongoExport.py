# -*- coding: utf-8 -*-
# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
import json
from pymongo import MongoClient
from Votacion.votaciones import Votaciones
from Proyecto.proyectos import Proyectos
from Boletin.boletines import Boletines
from sesiones.sesiones import Sesiones
from legislatura.legislaturas import Legislaturas


client = MongoClient('localhost', 27017)
db = client.feature


for l in Legislaturas.getLegislaturas():
  #db.legislaturas.insert(s.__dict__) #se descomenta para agregar todas las legislaturas ...
  #...ademas para eso se debe descomentar la linea la linea 13 de legislaturas.py
  for s in Sesiones.getSesiones(l._id):
    db.sesiones.insert(s.__dict__)
    for b in Boletines.getBoletines(s._id):
      try:
        db.boletines.insert(b.__dict__)
      except pymongo.errors.DuplicateKeyError:
        continue  # quita el error de id boletines que se repiten y da error en mongo por duplicidad
      for p in Proyectos.getProyectos(b._id):
        db.proyectos.insert(p.__dict__)
        for v in Votaciones.getVotaciones(p.id_votacion):
          db.votaciones.insert(v.__dict__)

client.close()
print "guardado"



