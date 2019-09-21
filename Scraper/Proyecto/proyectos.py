# -*- coding: utf-8 -*-
#import os
#import sys
#sys.path.insert(0, os.path.realpath('../'))
from bs4 import BeautifulSoup as BS
import requests
#from listado import Listado

import spacy
import nltk
from nltk import SnowballStemmer


nlp = spacy.load('es')
#spanishstemmer = SnowballStemmer('spanish')

class Analisis():
    #nlp = spacy.load('es')
    #spanishstemmer = SnowballStemmer('spanish')
    
    def normalize(text):
        doc = nlp(text)
        words = [t.orth_ for t in doc if not (t.is_punct | t.is_stop)]
        lexical_tokens = [t.lower() for t in words if len(t) > 3 and t.isalpha()]
        return lexical_tokens
    # return words



class Proyecto(object):
    def __init__(self, _id, nombre, id_votacion, materia, tags):
        self._id = _id
        self.nombre = nombre
        self.id_votacion = id_votacion
        self.materia = materia
        self.tags = tags


class Listado(object):
    @classmethod
    def getProyectos(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, _id, nombre, id_votacion, materia, tags):
        pro = Proyecto(_id, nombre, id_votacion, materia, tags)
        return pro


class Proyectos(Listado):
    votaciones = {}

    @classmethod
    def getProyectos(cls, _id):
        proyectos = []
        Url_Proyecto = "http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarProyectoLey?prmNumeroBoletin=" + str(_id)
        r = requests.get(Url_Proyecto)
        data = r.text
        soup = BS(data, 'xml')
        proyecto = soup.find("ProyectoLey")
        votacion = soup.find_all("VotacionProyectoLey")
        materia = soup.find("Materia")
        if (soup.find("VotacionProyectoLey")):
            _id = proyecto.Id.text.encode("utf-8")
            _id = _id.decode()
            nombre = proyecto.Nombre.text.encode("utf-8")    
            nombre = nombre.decode()
            
            tags = Analisis.normalize(nombre) #limpio y tokenizo
            #print (str(tags) + '\n')
            
            
            for j in votacion:
                id_votacion = j.Id.text.encode("utf-8")
                id_votacion = id_votacion.decode()
            try:
                materia = materia.Nombre.text.encode("utf-8")
                materia = materia.decode()
            except AttributeError:
                materia = None

            proyectos.append(cls.toObject(_id, nombre, id_votacion, materia, tags))
        return proyectos
