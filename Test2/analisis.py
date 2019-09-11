# -*- coding: utf-8 -*-
from collections import Counter
import spacy
import sys
#numero de veces que se repite cada palabra
text = "voy a dormir, estoy escribiendo algo, el diputado le pasa la palabra al diputado, habla Roberto"
msg = "Modifica la ley N°18.892, General de Pesca y Acuicultura, en materia de prohibición de captura de especies salmonídeas provenientes de cultivos de acuicultura"
print msg
print Counter(text.split(" "))
nlp = spacy.load("es_core_news_sm")
doc = nlp(msg.decode('utf8'))
print "frases:",[chunk.text for  chunk  in doc.noun_chunks]
print "verbos:", [token.lemma_ for token in doc if token.pos_ == "VERB" ]
for token in doc:
    print token.pos_,token.text,token.lemma_
print [token.text for token in doc if token.pos_ == "NOUN" ]
print "Nombres:"
for ent in doc.ents:
    print ent.text