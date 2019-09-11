# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Categorización de Palabras
#
# - Preposiciones(PREP)
# - Pronombres Personales(PP)
# - Pronombres Demostrativos(PD)
# - Pronombres Posesivos (PPO)
# - Pronombres Indefinidos(PI)
# - Pronombres Interrogativos(PIN)
# - Pronombres Relativos(PR)
# - Adverbios de TIEMPO(ADT)
# - Adverbios de Lugar(ADL)
# - Adverbios de Modo (ADM)
# - Adverbios de Cantidad(ADC)
# - Adverbios de Afirmación(ADA)
# - Advervios de Negación(ADN)
# - Advervios de Duda(ADD)
# - Articulos(ART)
# - Conjunciones Coodinada(COC)
# - Conjunciones Subordinada(COS)
#----------------------------------------------------------------------------
#Preposiciones(PREP)
PRE = [("a","PRE"), ("ante","PRE"), ("bajo","PRE"), ("con","PRE"), ("de","PRE"),
        ("desde","PRE"), ("durante","PRE"),("en","PRE"), ("entre","PRE"), ("excepto","PRE"),
        ("hacia","PRE"), ("hasta","PRE"), ("mediante","PRE"),("para","PRE"),("por","PRE"),
        ("salvo","PRE"), ("según","PRE"), ("sin","PRE"), ("sobre","PRE"),("tras","PRE")]

#Pronombres Personales
PP = [("yo","PP"),("tú","PP"),("él","PP"),("me","PP"),("mí","PP"),("mí","PP"),("nos","PP"),
      ("nosotras","PP"),("nosotros","PP"),("conmigo","PP"),("te","PP"),("ti","PP"),("tú","PP"),
      ("os","PP"),("usted","PP"),("ustedes","PP"),("vosotras","PP"),("vosotros","PP"),("contigo","PP"),
      ("ella","PP"),("ellas","PP"),("ello","PP"),("ellos","PP"),("la","PP"),("las","PP"),("lo","PP"),
      ("los","PP"),("le","PP"),("les","PP"),("les","PP"),("se","PP"),("sí","PP"),("consigo","PP")]
#Pronombres Demostrativos(PD)
PD = [("aquéllas","PD"),("aquélla","PD"),("aquéllos","PD"),("aquél","PD"),("aquellas","PD"),("aquella","PD"),
      ("aquellos","PD"),("aquel","PD"),("aquello","PD"),("ésas","PD"),("ésa","PD"),("esas","PD"),("esa","PD"),
      ("esos","PD"),("ese","PD"),("ésos","PD"),("ése","PD"),("eso","PD"),("esotra","PD"),("esotro","PD"),
      ("esta","PD"),("éstas","PD"),("ésta","PD"),("estas","PD"),("esta","PD"),("estos","PD"),("este","PD"),
      ("éstos","PD"),("éste","PD"),("esto","PD"),("estotra","PD"),("estotro")]
#Pronombres Posesivos (PPO)
PPO = [("mía","PPO"),("mías","PPO"),("mío","PPO"),("míos","PPO"),("nuestra","PPO"),("nuestras","PPO"),("nuestro","PPO"),
       ("nuestros","PPO"),("suya","PPO"),("suyas","PPO"),("suyo","PPO"),("suyos","PPO"),("tuya","PPO"),("tuyas","PPO"),
       ("tuyo","PPO"),("tuyos","PPO"),("vuestra","PPO"),("vuestras","PPO"),("vuestro","PPO"),("vuestros","PPO")]
#Pronombres Indefinidos(PI)
PI = [("algo","PPI"),("alguien","PPI"),("alguna","PPI"),("algunas","PPI"),("alguno","PPI"),("algunos","PPI"),("cualesquiera","PPI"),
        ("cualquiera","PPI"),("demás","PPI"),("misma","PPI"),("mismas","PPI"),("mismo","PPI"),("mismos","PPI"),("mucha","PPI"),
        ("muchas","PPI"),("mucho","PPI"),("muchos","PPI"),("nada","PPI"),("nadie","PPI"),("ninguna","PPI"),("ningunas","PPI"),
        ("ninguno","PPI"),("ningunos","PPI"),("otra","PPI"),("otras","PPI"),("otro","PPI"),("otros","PPI"),("poca","PPI"),("pocas","PPI"),
        ("poco","PPI"),("pocos","PPI"),("quienquiera","PPI"),("quienesquiera","PPI"),("quienquiera","PPI"),("tanta","PPI"),("tantas","PPI"),
        ("tanto","PPI"),("tantos","PPI"),("toda","PPI"),("todas","PPI"),("todo","PPI"),("todos","PPI"),("última","PPI"),("últimas","PPI"),
        ("último","PPI"),("últimos","PPI"),("una","PPI"),("unas","PPI"),("uno","PPI"),("unos","PPI"),("varias","PPI"),("varios","PPI")]
#Pronombres Interrogativos
PIN = [("adónde","PI"),("cómo","PI"),("cuál","PI"),("cuáles","PI"),("cuándo","PI"),("cuánta","PI"),("cuántas","PI"),("cuánto","PI"),
      ("cuántos","PI"),("dónde","PI"),("qué","PI"),("quién","PI"),("quiénes","PI")]

#Pronombres Relativos
PR = [("como","PR"),("donde","PR"),("cuando","PR"),("cual","PR"),("cuales","PR"),("cuanta","PR"),("cuantas","PR"),("cuantos","PR"),
      ("cuya","PR"),("cuyas","PR"),("cuyo","PR"),("cuyos","PR"),("que","PR"),("quien","PR"),("quienes","PR")]

#Adverbios de TIEMPO(ADT)
ADT = [("ahora","ADT"), ("antes","ADT"),("después","ADT"),("tarde","ADT"),("luego","ADT"), ("ayer","ADT"),("temprano","ADT"),("ya","ADT"),
       ("todavía","ADT"),("anteayer","ADT"),("aún","ADT"),("pronto","ADT"),("hoy","ADT")]

#Adverbios de Lugar(ADL)
ADL = [("aquí","ADL"),("ahí","ADL"),("allí","ADL"),("cerca","ADL"),("lejos","ADL"),("fuera","ADL"),("dentro","ADL"),("alrededor","ADL"),
       ("aparte","ADL"),("encima","ADL"),("debajo","ADL"),("delante","ADL"),("detrás","ADL")]
#Adverbios de Modo (ADM)
ADM = [("así","ADM"),("bien","ADM"),("mal","ADM"),("despacio","ADM"),("deprisa","ADM"),("como","ADM")]

#Adverbios de Cantidad(ADC)
ADC = [("muchos","ADC"), ("poco","ADC") ,("muy","ADC") ,("casi","ADC"), ("todo","ADC"), ("nada","ADC"),("algo","ADC"),("medio","ADC"),
       ("demasiado","ADC"),("bastante","ADC"),("más","ADC"),("menos","ADC"),("además","ADC"),("incluso","ADC"),("también","ADC")]
#Adverbios de Afirmación(ADA)
ADA = [("sí","ADA"),("también","ADA"),("asimismo","ADA")]
#Advervios de Negación(ADN)
ADN = [("no","ADN"),("tampoco","ADN"),("jamás","ADN"),("nunca","ADN")]
#Advervios de Duda(ADD)
ADD = [("acaso","ADD"), ("quizás","ADD"),("quizásc","ADD"),("tal vez","ADD") ,("a lo mejor","ADD")]

#Articulos (ART)
ART = [("el","ART"),("la","ART"),("lo","ART"),("los","ART"),("las","ART")]

#COnjunciones Coodinada(COC)
COC = [("e","COC"),("empero","COC"),("mas","COC"),("ni","COC"),("o","COC"),("ora","COC"),("pero","COC"),("sino","COC"),("siquiera","COC"),
       ("u","COC"),("y","COC")]
#Conjunciones Subordinada (COS)
COS = [("aunque","COS"),("como","COS"),("conque","COS"),("cuando","COS"),("donde","COS"),("entonces","COS"),("ergo","COS"),("incluso","COS"),
       ("luego","COS"),("mientras","COS"),("porque","COS"),("pues","COS"),("que","COS"),("sea","COS"),("si","COS"),("ya","COS")]

ADNO=("Primero"),("Segundo"),("Tercer"),("Cuarto"),("Quinto"),("Sexto"),("Séptimo"),("Octavo"),("Noveno"),("Décimo"),("veinteavo"),("Treintavo"),("Cuarentavo"),("Cincuentavo"),("Último")
with open("grammar-CL.bin","wb") as file:

    file.write()
