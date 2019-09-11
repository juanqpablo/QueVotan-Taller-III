# by Tata
# -*- coding: utf-8 -*-
import spacy
import nltk
from nltk import SnowballStemmer


nlp = spacy.load('es')
spanishstemmer = SnowballStemmer('spanish')


text3 = "TRATADO INTEGRAL Y PROGRESISTA DE ASOCIACION TRANSPACIFICO ENTRE AUSTRALIA, BRUNEI"


def normalize(text):
    doc = nlp(text)
    words = [t.orth_ for t in doc if not (t.is_punct | t.is_stop)]
    lexical_tokens = [t.lower() for t in words if len(t) > 3 and t.isalpha()]
    return lexical_tokens
    # return words


f = open("materias.txt", "r")
for linea in f:
    print (linea)
    word_list = normalize(linea)
    print (str(word_list) + '\n')
    tokens = normalize(linea)
    stems = [spanishstemmer.stem(token) for token in tokens]
    print (str(stems) + '\n')

f.close()


#text6 = "Modifica la ley N°20.551, que regula el cierre de las faenas e instalaciones mineras."
#text5 = "Modifica la ley N°18.892, General de Pesca y Acuicultura, en materia de prohibición de captura de especies salmonídeas provenientes de cultivos de acuicultura"
#print (text6)
# tokens = normalize(text6) # crear una lista de tokens
#print (tokens)
#stems = [spanishstemmer.stem(token) for token in tokens]
#print (stems)
