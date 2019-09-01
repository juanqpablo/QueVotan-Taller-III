from collections import Counter
import spacy
#numero de veces que se repite cada palabra
text = "voy a dormir, estoy escribiendo algo, el diputado le pasa la palabra al diputado"
print Counter(text.split(" "))
nlp = spacy.load("es_core_news_sm")
doc = nlp(text.decode('utf8'))
print "frases:",[chunk.text for  chunk  in doc.noun_chunks]
print "verbos:", [token.lemma_ for token in doc if token.pos_ == "VERB" ]
for token in doc:
    print token.pos_,token.text,token.lemma_
print [token.text for token in doc if token.pos_ != "AUX" and token.pos_ != "ADP" and token.pos_ != "PUNCT" and token.pos_ != "DET" and token.pos_ != "PRON" ]
