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
# - Articulos Determinados(ARTD)
# - Articulos Indeterminados(ARTI)
# - Conjunciones Coodinada(COC)
# - Conjunciones Subordinada(COS)
# - Adjetivos Numerales(ADNC)
# - Adjetivos Cardinales(ADNO)
# - Sustantivos (SUS)
# - Sustantivos de Espacio (SUSE)
# - Sustantivos Abstractos(SUSA)
# - verbos(VAUX)
# - verbos de Existencia(VEE)
# - verbos de Comunicación(VEC)
# - verbos de Actividades(VEA)
# - verbos Intransitivos(VEI)
# - verbos de Accion(VEA)
#----------------------------------------------------------------------------
#ARREGLO CON INFORMACIÖN
grammar= [("a","PRE"), ("ante","PRE"), ("bajo","PRE"), ("con","PRE"), ("de","PRE"),
       ("desde","PRE"), ("durante","PRE"),("en","PRE"), ("entre","PRE"), ("excepto","PRE"),
       ("hacia","PRE"), ("hasta","PRE"), ("mediante","PRE"),("para","PRE"),("por","PRE"),
       ("salvo","PRE"), ("según","PRE"), ("sin","PRE"), ("sobre","PRE"),("tras","PRE"),("yo","PP"),("tú","PP"),
       ("él","PP"),("me","PP"),("mí","PP"),("mí","PP"),("nos","PP"),
       ("nosotras","PP"),("nosotros","PP"),("conmigo","PP"),("te","PP"),("ti","PP"),("tú","PP"),
       ("os","PP"),("usted","PP"),("ustedes","PP"),("vosotras","PP"),("vosotros","PP"),("contigo","PP"),
       ("ella","PP"),("ellas","PP"),("ello","PP"),("ellos","PP"),("la","PP"),("las","PP"),("lo","PP"),
       ("los","PP"),("le","PP"),("les","PP"),("les","PP"),("se","PP"),("sí","PP"),("consigo","PP"),("aquéllas","PD"),
       ("aquélla","PD"),("aquéllos","PD"),("aquél","PD"),("aquellas","PD"),("aquella","PD"),
       ("aquellos","PD"),("aquel","PD"),("aquello","PD"),("ésas","PD"),("ésa","PD"),("esas","PD"),("esa","PD"),
       ("esos","PD"),("ese","PD"),("ésos","PD"),("ése","PD"),("eso","PD"),("esotra","PD"),("esotro","PD"),
       ("esta","PD"),("éstas","PD"),("ésta","PD"),("estas","PD"),("esta","PD"),("estos","PD"),("este","PD"),
       ("éstos","PD"),("éste","PD"),("esto","PD"),("estotra","PD"),("estotro","PD"),
       ("mía","PPO"),("mías","PPO"),("mío","PPO"),("míos","PPO"),("nuestra","PPO"),("nuestras","PPO"),("nuestro","PPO"),
       ("nuestros","PPO"),("suya","PPO"),("suyas","PPO"),("suyo","PPO"),("suyos","PPO"),("tuya","PPO"),("tuyas","PPO"),
       ("tuyo","PPO"),("tuyos","PPO"),("vuestra","PPO"),("vuestras","PPO"),("vuestro","PPO"),("vuestros","PPO"),
       ("algo","PPI"),("alguien","PPI"),("alguna","PPI"),("algunas","PPI"),("alguno","PPI"),("algunos","PPI"),("cualesquiera","PPI"),
       ("cualquiera","PPI"),("demás","PPI"),("misma","PPI"),("mismas","PPI"),("mismo","PPI"),("mismos","PPI"),("mucha","PPI"),
       ("muchas","PPI"),("mucho","PPI"),("muchos","PPI"),("nada","PPI"),("nadie","PPI"),("ninguna","PPI"),("ningunas","PPI"),
       ("ninguno","PPI"),("ningunos","PPI"),("otra","PPI"),("otras","PPI"),("otro","PPI"),("otros","PPI"),("poca","PPI"),("pocas","PPI"),
       ("poco","PPI"),("pocos","PPI"),("quienquiera","PPI"),("quienesquiera","PPI"),("quienquiera","PPI"),("tanta","PPI"),("tantas","PPI"),
       ("tanto","PPI"),("tantos","PPI"),("toda","PPI"),("todas","PPI"),("todo","PPI"),("todos","PPI"),("última","PPI"),("últimas","PPI"),
       ("último","PPI"),("últimos","PPI"),("una","PPI"),("unas","PPI"),("uno","PPI"),("unos","PPI"),("varias","PPI"),("varios","PPI"),
       ("adónde","PI"),("cómo","PI"),("cuál","PI"),("cuáles","PI"),("cuándo","PI"),("cuánta","PI"),("cuántas","PI"),("cuánto","PI"),
       ("cuántos","PI"),("dónde","PI"),("qué","PI"),("quién","PI"),("quiénes","PI"),
       ("como","PR"),("donde","PR"),("cuando","PR"),("cual","PR"),("cuales","PR"),("cuanta","PR"),("cuantas","PR"),("cuantos","PR"),
       ("cuya","PR"),("cuyas","PR"),("cuyo","PR"),("cuyos","PR"),("que","PR"),("quien","PR"),("quienes","PR"),
       ("ahora","ADT"), ("antes","ADT"),("después","ADT"),("tarde","ADT"),("luego","ADT"), ("ayer","ADT"),("temprano","ADT"),("ya","ADT"),
       ("todavía","ADT"),("anteayer","ADT"),("aún","ADT"),("pronto","ADT"),("hoy","ADT"),
       ("aquí","ADL"),("ahí","ADL"),("allí","ADL"),("cerca","ADL"),("lejos","ADL"),("fuera","ADL"),("dentro","ADL"),("alrededor","ADL"),
       ("aparte","ADL"),("encima","ADL"),("debajo","ADL"),("delante","ADL"),("detrás","ADL"),
       ("así","ADM"),("bien","ADM"),("mal","ADM"),("despacio","ADM"),("deprisa","ADM"),("como","ADM"),
       ("muchos","ADC"), ("poco","ADC") ,("muy","ADC") ,("casi","ADC"), ("todo","ADC"), ("nada","ADC"),("algo","ADC"),("medio","ADC"),
       ("demasiado","ADC"),("bastante","ADC"),("más","ADC"),("menos","ADC"),("además","ADC"),("incluso","ADC"),("también","ADC"),
       ("sí","ADA"),("también","ADA"),("asimismo","ADA"),
       ("no","ADN"),("tampoco","ADN"),("jamás","ADN"),("nunca","ADN"),("acaso","ADD"), ("quizás","ADD"),("quizásc","ADD"),("tal vez","ADD"),
       ("mejor","ADD"),("el","ARTD"),("la","ARTD"),("lo","ARTD"),("los","ARTD"),("las","ARTD"),("un","ARTI"),("unos","ARTI"),("una","ARTI"),("unas","ARTI"),
       ("e","COC"),("empero","COC"),("mas","COC"),
       ("ni","COC"),("o","COC"),("ora","COC"),("pero","COC"),("sino","COC"),("siquiera","COC"),("u","COC"),("y","COC"),("aunque","COS"),("como","COS"),
       ("conque","COS"),("cuando","COS"),("donde","COS"),("entonces","COS"),("ergo","COS"),("incluso","COS"),("luego","COS"),("mientras","COS"),
       ("porque","COS"),("pues","COS"),("que","COS"),("sea","COS"),("si","COS"),("ya","COS"),
       ("Uno","ADJN"),("Dos","ADJN"),("Tres","ADJN"),("Cuatro","ADJN"),("Cinco","ADJN"),("Seis","ADJN"),("siete","ADJN"),("Ocho","ADJN"),("Nueve","ADJN"),("Diez","ADJN"),
       ("Veinte","ADJN"),("Treinta","ADJN"),("Cuarenta","ADJN"),("Cincuenta","ADJN"),("Cien","ADJN"),("Doscientos","ADJN"),("Trescientos","ADJN"),("Cuatrocientos","ADJN"),
       ("Quinientos","ADJN"),("mil","ADJN"),("Diez","ADJN"),("millón","ADJN"),
       ("Primero","ADNO"),("Segundo","ADNO"),("Tercer","ADNO"),("Cuarto","ADNO"),("Quinto","ADNO"),("Sexto","ADNO"),("Séptimo","ADNO"),("Octavo","ADNO"),("Noveno","ADNO"),
       ("Décimo","ADNO"),("veinteavo","ADNO"),("Treintavo","ADNO"),("Cuarentavo","ADNO"),("Cincuentavo","ADNO"),("Último","ADNO"),
       ("humano","SUS"),("persona","SUS"),("gente","SUS"),("hombre","SUS"),("mujer","SUS"),("familia","SUS"),("amigo","SUS"),("conocido","SUS"),("colega","SUS"),("pareja","SUS"),("esposo","SUS"),("matrimonio","SUS"),("amor","SUS"),
       ("cuerpo","SUS"),("pie","SUS"),("pierna","SUS"),("talón","SUS"),("espinilla","SUS"),("rodilla","SUS"),("muslo","SUS"),("cabeza","SUS"),("cara","SUS"),("boca","SUS"),("labios","SUS"),("diente","SUS"),("nariz","SUS"),("bigote","SUS"),
       ("cabello","SUS"),("oreja","SUS"),("cerebro","SUS"),("estómago","SUS"),("brazo","SUS"),("codo","SUS"),("hombro","SUS"),("uña","SUS"),("mano","SUS"),("muñeca","SUS"),("palma","SUS"),("dedo","SUS"),("trasero","SUS"), ("culo","SUS"),
       ("cola","SUS"), ("glúteos","SUS"),("abdomen","SUS"),("hígado","SUS"),("músculo","SUS"),("cuello","SUS"),("corazón","SUS"),("mente","SUS"),("alma","SUS"),("cintura","SUS"),("cadera","SUS"),("corazón","SUS"),("espalda","SUS"),
       ("sangre","SUS"),("carne","SUS"),("piel","SUS"),("hueso","SUS"),("pecho","SUS"),("resfriado","SUS"),("diarrea","SUS"),("enfermedad","SUS"),("abuela","SUS"),("abuelo","SUS"),("esposa","SUS"),("esposo","SUS"),("hermana","SUS"),("hermano","SUS"),
       ("hija","SUS"),("hijas","SUS"),
       ("hijos","hijo"),("madre","SUS"),("madres","SUS"),("nieta","SUS"),("nieto","SUS"),("padre","SUS"),("padres","SUS"),("prima","SUS"),("primas","SUS"),("primos","SUS"),("primo","SUS"),("tía","SUS"),("tías","SUS"),("tío","SUS"),("tíos","SUS"),
       ("sobrino","SUS"),("sobrinos","SUS"),("sobrina","SUS"),("sobrinas","SUS"),("bisabuelo","SUS"),("bisabuela","SUS"),("criatura","SUS"),("especie","SUS"),("especies","SUS"),("ser","SUS"),("seres","SUS"),("vida","SUS"),
       ("vidas","SUS"),("naturaleza","SUS"),("campo","SUS"),("campos","SUS"),("bosque","SUS"),("bosques","SUS"),("selva","SUS"),("jungla","SUS"),("selvas","SUS"),("junglas","SUS"),("desierto","SUS"),("desiertos","SUS"),("costa","SUS"),("costas","SUS"),
       ("playa","playas"),("río","SUS"),("ríos","SUS"),("laguna","SUS"),("lago","SUS"),("lagunas","SUS"),("lagos","SUS"),("mar","SUS"),("océano","SUS"),("mares","SUS"),("océanos","SUS"),("cerro","SUS"),("cerros","SUS"),
       ("monte","SUS"),("montes","SUS"),("montaña","SUS"),("montañas","SUS"),("animal","SUS"),("animales","SUS"),("perro","SUS"),("perrito","SUS"),("perros","SUS"),("perritos","SUS"),("gato","SUS"),("gatos","SUS"),("gatitos","SUS"),("vaca","SUS"),
       ("vacas","SUS"),("cerdo","SUS"),("cerdos","SUS"),("caballo","SUS"),("yegua","SUS"),("caballos","SUS"),("yeguas","SUS"),("oveja","SUS"),("ovejas","SUS"),("mono","SUS"),("monos","SUS"),("monitos","SUS"),("ratón","SUS"),("rata","SUS"),
       ("ratas","SUS"),("ratónes","SUS"),("tigre","SUS"),("tigres","SUS"),("conejo","SUS"),("conejos","SUS"),("dragón","SUS"),("dragónes","SUS"),("ciervo","SUS"),("ciervos","SUS"),("rana","SUS"),("ranas","SUS"),("león","SUS"),("leones","SUS"),("jirafa","SUS"),("jirafas","SUS"),
       ("elefante","SUS"),("elefantes","SUS"),("pájaro","SUS"),("pájaros","SUS"),("gallina","SUS"),("gallinas","SUS"),("gorrión","SUS"),("gorriones","SUS"),("cuervo","SUS"),("cuervos","SUS"),("águila","SUS"),("águlas","SUS"),("halcón","SUS"),
       ("pez","SUS"),("camarón","SUS"),("langosta","SUS"),("sardina","SUS"),("atún","SUS"),("calamar","SUS"),("pulpo","SUS"),("insecto","SUS"),("bicho","SUS"),("mariposa","SUS"),("polilla","SUS"),("saltamontes","SUS"),("araña","SUS"),("mosca","SUS"),
       ("mosquito","SUS"),("cucaracha","SUS"),("caracol","SUS"),("babosa","SUS"),("lombriz","SUS"),("marisco","SUS"),("molusco","SUS"),("lagarto","SUS"),("serpiente","SUS"),("cocodrilo","SUS"),
       ("plantas","SUS"),("planta","SUS"),("pasto","SUS"),("pastizal","SUS"),("Pastizales","SUS"),("césped","SUS"),("flor","SUS"),("fruta","SUS"),("frutas","SUS"),("semilla","SUS"),("semillas","SUS"),("árbol","SUS"),("árboles","SUS"),("hoja","SUS"),("hojas","SUS"),("raíz","SUS"),
       ("raízes","SUS"),("tallo","SUS"),("hongo","SUS"),("ciruela","SUS"),("pino","SUS"),("bambú","SUS"),("nuez","SUS"),("almendra","SUS"),("castaña","SUS"),("arroz","SUS"),
       ("avena","SUS"),("cebada","SUS"),("trigo","SUS"),("vegetal","SUS"), ("verdura","SUS"),("patatas","SUS"), ("papas","SUS"),("judías","SUS"), ("guisantes","SUS"), ("porotos","SUS"),("rábano","SUS"),("zanahoria","SUS"),("manzana","SUS"),("naranja","SUS"),("plátano","SUS"),("pera","SUS"),("castaño","SUS"),("durazno","SUS"),("tomate","SUS"),("sandía","SUS"),
       ("alimento","SUS"),("comida","SUS"),("bebida","SUS"),("carne","SUS"),("gaseosa","SUS"),("tiempo","SUS"),("calendario","SUS"),("edad","SUS"),("época","SUS"),("era","SUS"),("fecha","SUS"),("segundo","SUS"),("minuto","SUS"),("hora","SUS"),("horas","SUS"),("día","SUS"),("días","SUS"),("semana","SUS"),("entre semana","SUS"),("semanas","SUS"),
       ("fin de semana","SUS"),("mes","SUS"),("año","SUS"),("ayer","SUS"),("hoy","SUS"),("mañana","SUS"),("amanecer","SUS"),("mediodía","SUS"),("tarde","SUS"),("anochecer","SUS"),("noche","SUS"),("lunes","SUS"),("martes","SUS"),("miércoles","SUS"),("jueves","SUS"),("viernes","SUS"),("sábado","SUS"),("domingo","SUS"),("ambiente","SUS"),("espacio","SUS"),
       ("entorno","SUS"),("sol","SUS"),("luna","SUS"),("estrella","SUS"),("clima","SUS"),("despejado","SUS"),("nublado","SUS"),("lluvia","SUS"),("nieve","SUS"),("viento","SUS"),("trueno","SUS"),("rayo","SUS"),("tifón","SUS"),("tormenta","SUS"),("cielo","SUS"),
       ("este","SUS"),("oeste","SUS"),("sur","SUS"),("norte","SUS"),("derecha","SUS"),("izquierda","SUS"),("arriba","SUS"), ("encima","SUS"),("abajo","SUS"),("debajo","SUS"),("adelante","SUS"), ("adelante","SUS"),("atrás","SUS"),("centro","SUS"), ("mediodía","SUS"),("encima","SUS"),("alrededor","SUS"),("diagonal","SUS"),("enfrente","SUS"),
       ("cerca","SUS"),("lejos","SUS"),("adentro","SUS"), ("dentro","SUS"),("afuera","SUS"),("fuera","SUS"),("aquí","SUS"),("acá","SUS"),("allá","SUS"),("exterior","SUS"),("interior","SUS"),
       ("agua","SUS"),("aguas","SUS"),("caliente","SUS"),("calor","SUS"),("frío","SUS"),("fresco","SUS"),("hielo","SUS"),("vapor","SUS"),("fuego","SUS"),("gas","SUS"),("aire","SUS"), ("atmósfera","SUS"),("tierra","SUS"), ("suelo","SUS"),("metal","SUS"), ("metálico","SUS"),("hierro","SUS"),("cobre","SUS"),("oro","SUS"),("plata","SUS"),("plomo","SUS"),("sal","SUS"),("barro","SUS"), ("lodo","SUS"),("arcilla","SUS"),("yeso","SUS"),
       ("peso","SUS"),("metro","SUS"),("metros","SUS"),("litro","SUS"),("litros","SUS"),("gramos","SUS"),("gramo","SUS"),("kilo","SUS"),("kilos","SUS"),("centímetro","SUS"),("mili","SUS"),
       ("sociedad","SUS"),("sociedades","SUS"),("comunidad","SUS"),("reuniones","SUS"),("reunión","SUS"),
       ("encuentro","SUS"),("calidad","SUS"),("estructura","SUS"),("estructuras","SUS"),("administración","SUS"),("administraciones","SUS"),("admnistradores","SUS"),("organización","SUS"),("organizaciones","SUS"),("asociación","SUS"),("asociaciones","SUS"),
       ("empresa","SUS"),("empresas","SUS"),("equipo","SUS"),("equipos","SUS"),("obligación","SUS"),("obligaciones","SUS"),("derecho","SUS"),("permiso","SUS"),("permisos","SUS"),("prohibición","SUS"),
       ("autoridad","SUS"),("autoridades","SUS"),("cargo","SUS"),("cargos","SUS"),("campaña","SUS"),("campañas","SUS"),("club","SUS"),("comisión","SUS"),("congreso","SUS"),("congresos","SUS"),("complexión","SUS"),
       ("constitución","SUS"),("contextura","SUS"),("temperamento","SUS"),("gobierno","SUS"),("gobiernos","SUS"),
       ("democracia","SUS"),("dictadura","SUS"),("dictaduras","SUS"),("presidente","SUS"),("presidenta","SUS"),("presidentes","SUS"),("ministerio","SUS"),
       ("ministro","SUS"),("ministros","SUS"),("director","SUS"),("directores","SUS"),("parlamentario","SUS"),("parlamentarios","SUS"), ("congresista","SUS"),("congresistas","SUS"), ("senador","SUS"),("senadores","SUS"), ("diputado","SUS"),("diputados","SUS"),
       ("representante","SUS"),("representantes","SUS"),("capital","SUS"),("capitales","SUS"),("ciudad","SUS"),("ciudades","SUS"),("pueblo","SUS"),("villa","SUS"),("villas","SUS"),
       ("estado","SUS"),("eatados","SUS"),("provincia","SUS"),("departamento","SUS"),("departamentos","SUS"),
       ("economía","SUS"),("consumo","SUS"),("demanda","SUS"),
       ("compañía","SUS"),("compañias","SUS"),("comercio","SUS"),("comercios","SUS"),("producto","SUS"),("productos","SUS"),("transacción","SUS"),("transacciones","SUS"),("almacén","SUS"),
       ("hotel","SUS"),("fábrica","SUS"),("fábricas","ASUS"),("cuenta","SUS"),("cuentas","SUS"),("dinero","SUS"),("vuelto","SUS"), ("cambio","SUS"),("máquina","SUS"),("expendedora","SUS"),
       ("boleto","SUS"),("boletos","SUS"), ("billete","SUS"),("billetes","SUS"),("precio","SUS"), ("tarifa","SUS"),("tarifas","SUS"),("captura","SUS"),("escritorio","SUS"),("silla","SUS"),("mesa","SUS"),("cama","SUS"),("puerta","SUS"),("dormitorio","SUS"),("habitación","SUS"),("cuarto","SUS"),("oficina","SUS"),("panel","SUS"),("puerta","SUS"),
       ("ventana","SUS"),("entrada","SUS"),("hogar","SUS"),("casa","SUS"),("apartamento","SUS"), ("departamento","SUS"),("edificio","SUS"),("construcción","SUS"),
       ("elevador","SUS"), ("ascensor","SUS"),("escalera","SUS"),("cámara","SUS"),
       ("aparato","SUS"),("aparatos","SUS"),("cámara","SUS"),("camaras","SUS"),("aguja","SUS"),("clavo","SUS"),("clavos","SUS"),("hilo","SUS"),("cuerda","SUS"),("cuerdas","SUS"), ("cordel","SUS"), ("cordón","SUS"),("bolsillo","SUS"),("bolso","SUS"),("bolsa","SUS"),("paraguas","SUS"),("parasol","SUS"),
       ("pomo","SUS"),("llave","SUS"),("trancar","SUS"),("arma","SUS"),("escultura","SUS"),("cuadro","SUS"),("grabado","SUS"),("energía","SUS"),("electricidad","SUS"),("corriente","SUS"),
       ("transporte","SUS"),("transportes","SUS"), ("público","SUS"),("públicos","SUS"),  ("privado","SUS"),("privados","SUS"),
       ("tránsito","SUS"), ("tráfico","SUS"),("vía","SUS"),("férrea","SUS"),("tren","SUS"), ("ferrocarril","SUS"),("subterráneo","SUS"), ("metropolitano","SUS"),("metropolitana","SUS"),("camino","SUS"),("caminos","SUS"),
       ("ruta","SUS"),("rutas","SUS"),("calle","SUS"),("calles","SUS"),("carretera","SUS"),("carreteras","SUS"),("autopista","SUS"),("autopistas","SUS"),("avenida","SUS"),("avenidas","SUS"),
       ("estación","SUS"), ("parada","SUS"),("paradas","SUS"),("avión","SUS"),("aviones","SUS"),("aeropuerto","SUS"),("aeropuertos","SUS"),("automóvil","SUS"),("automóviles","SUS"), ("coche","SUS"),("coches","SUS"), ("auto","SUS"),("autos","SUS"),
       ("bus","SUS"),("buses","SUS"), ("autobús","SUS"),("autobuses","SUS"), ("ómnibus","SUS"),("número","SUS"),("alfabeto","SUS"),("raíz","SUS"), ("origen","SUS"), ("fuente","SUS"),("papel","SUS"),
       ("carta","SUS"),("cartas","SUS"),("periódico","SUS"),("periódicos","SUS"), ("diario","SUS"),("diccionario","SUS"),("diccionarios","SUS"),("computadora","SUS"),("computadoras","SUS"), ("ordenador","SUS"),("idioma","SUS"),("extranjero","SUS"),("japonés","SUS"),("inglés","SUS"),("chino","SUS"),("alemán","SUS"),("español","SUS"),("francés","SUS"),
       ("color","SUS"),("colores","SUS"),("rojo","SUS"),("naranja","SUS"),("anaranjado","SUS"),("amarillo","SUS"),("verde","SUS"),("azul","SUS"),("violeta","SUS"),("blanco","SUS"),("negro","SUS"),("rosa","SUS"), ("rosado","SUS"),("marrón","SUS"), ("café","SUS"),("gris","SUS"),
       ("cultura","SUS"),("escultura","SUS"),("autor","SUS"), ("arte","SUS"),("cine","SUS"),("dibujo","SUS"),("pintura","SUS"),("música","SUS"),("religión","SUS"),("dios","SUS"),("artículo","SUS"),("educación","SUS"),("escuela","SUS"),("instituto","SUS"),("colegio","SUS"),("universidad","SUS"),("clase","SUS"),
       ("curso","SUS"),("estudio","SUS"),("estudios","SUS"),("formación","SUS"),("formaciones","SUS"),("análisis","SUS"),("sistemático","SUS"),("sistemática","SUS"),("sistematización","SUS"),("investigación","SUS"),("conocimiento","SUS"),
       ("idea","SUS"),("información","SUS"),("dato","SUS"),("datos","SUS"),("forma","SUS"),("estilo","SUS"),("figura","SUS"),("figuras","SUS"),
       ("elemento","SUS"),("elementos","SUS"),("comunicación","SUS"),("comunicaciones","SUS"),("expresión","SUS"),("periodismo","SUS"),("ciencia","SUS"),("científica","SUS"),("científico","SUS"),("aritmética","SUS"),
       ("historia","SUS"),("geografía","SUS"),("educación","SUS"),("física","SUS"),("deporte","SUS"),("deportes","SUS"),
       ("carrera","SUS"),("carreras","SUS"),("competición","SUS"), ("competencia","SUS"),("competencias","SUS"),("documento","SUS"),
       ("informe","SUS"),("información","SUS"),("noticia","SUS"),("necesidad","SUS"),("facultar","SUS"),("significado","SUS"),("cáracter","SUS"),("personalidad","SUS"),("pensamiento","SUS"),
       ("memoria","SUS"),("recuerdo","SUS"),("deseo","SUS"),("alegria","SUS"),("tristeza","SUS"),("enojo","SUS"),("placer","SUS"), ("éxtasis","SUS"),("empatía","SUS"),("interés","SUS"),
       ("aburrimiento","SUS"),("cansancio","SUS"),("sorpresa","SUS"),("susto","SUS"),("miedo","SUS"), ("temor","SUS"),("ejemplo","SUS"),("ayuda","SUS"),("favor","SUS"),("apoyo","SUS"),
       ("búsqueda","SUS"),("rápidamente","SUS"),("registro","SUS"),("registros","SUS"),("resultados","SUS"),("obtenidos","SUS"),("actividad","SUS"),("búsquedas","SUS"),
       ("duda","SUS"),("pregunta","SUS"),("respuesta","SUS"),("solicitudes","SUS"),("cuestión","SUS"),("solicitud","SUS"),("solicitudes","SUS"),("decisión","SUS"),("elección","SUS"),("consejo","SUS"),("sugerencia","SUS"),("sugerencias","SUS"),("orden","SUS"),("control","SUS"),("controlar","SUS"),("sistema","SUS"),("trabajo","SUS"),("empleo","SUS"),("profesión","SUS"),("esfuerzo","SUS"),("población","SUSE"),("poblar","SUSE"),("poblaciones","SUSE"),
       ("cosa","SUSE"),("lugar","SUSE"),("aspecto","SUSE"),("contenido","SUSE"),("cantidad","SUSE"),("área","SUSE"),("volumen","SUSE"),("ancho","SUSE"), ("anchura","SUSE"),("posición","SUSE"),("dirección","SUSE"),("tamaño","SUSE"),("largo","SUSE"), ("longitud","SUSE"),("alto","SUSE"), ("altura","SUSE"),("aumento","SUSE"),("reducciónote","SUSE"),("crecimiento","SUSE"),("fondo","SUSE"),("enfrente","SUSE"),
       ("eso","SUSA"),("aquello","SUSA"),("cual","SUSA"),("secreto","SUSA"),("automático","SUSA"),("formalidad","SUSA"),("presente","SUSA"),("pasado","SUSA"),("futuro","SUSA"),
       ("acción","SUSA"),("actividad","SUSA"),("acto","SUSA"),("acuerdo","SUSA"),("actitud","SUSA"),("capacidad","SUSA"),("concepto","SUSA"),("condición","SUSA"),("caso","SUSA"),("conjunto","SUSA"),("grupo","SUSA"),("creación","SUSA"),("destrucción","SUSA"),("origen","SUSA"),("destino","SUSA"),("objetivo","SUSA"), ("meta","SUSA"),("función","SUSA"),("intento","SUSA"), ("logro","SUSA"), ("efecto","SUSA"),("resultados","SUSA"),("éxito","SUSA"),("fracaso","SUSA"),
       ("causa","SUSA"),("consecuencia","SUSA"),("beneficio","SUSA"),("perjuicio","SUSA"),("ataque","SUSA"),("defensa","SUSA"),("conflicto","SUSA"),("guerra","SUSA"),("carácter","SUSA"),("característica","SUSA"),("crisis","SUSA"),("cambio","SUSA"),("desarrollo","SUSA"),("progreso","SUSA"),("avance","SUSA"),("avances","SUSA"),("retroceso","SUSA"),("mejora","SUSA"),("deterioro","SUSA"),("comienzo","SUSA"), ("inicio","SUSA"),("transcurso","SUSA"),
       ("fin","SUSA"), ("final","SUSA"), ("cabo","SUSA"),("etapa","SUSA"),("etapas","SUSA"),
       ("fase","SUSA"),("grado","SUSA"),("corte","SUSA"),("interrupción","SUSA"),("espera","SUSA"),("diferencia","SUSA"), ("similitud","SUSA"), ("sensación","SUSA"),("dolor","SUSA"),("sentido","SUSA"),("conciencia","SUSA"),
       ("percepción","SUSA"),("fuerza","SUSA"),("potencia","SUSA"),("existencia","SUSA"), ("experiencia","SUSA"),
       ("ser","AUX"),("estar","AUX"),("haber","AUX"),("aparecer","VEE"),("desaparecer","VEE"),("existir","VEE"),("cambiar","VEE"),("crecer","VEE"),("vivir","VEE"),("nacer","VEE"),("morir","VEE"),("romper","VEE"),
       ("comunicarse","VEC"),("afirmar","VEC"),("negar","VEC"),("decir","VEC"),("hablar","VEC"),("callar","VEC"),("escribir","VEC"),("leer","VEC"),
       ("analizar","VEA"),("pensar","VEA"),("dormir","VEA"),("cantar","VEA"),("morder","VEA"),("comer","VEA"),("beber","VEA"),("acordar","VEA"),("afectar","VEA"),("generar","VEA"),("añadir","VEA"), ("agregar","VEA"),("mejorar","VEA"),("empeorar","VEA"),("avanzar","VEA"),("retroceder","VEA"),("ayudar","VEA"),("complicar","VEA"),("reunirse","VEA"),("entrevistar","VEA"),("abrir","VEA"), ("desenvolver","VEA"),("jugar","VEA"),("recoger","VEA"),("levantar","VEA"),("tomar","VEA"),("vender","VEA"),("tener","VEA"),("faltar","VEA"),("dar","VEA"),("recibir","VEA"),("romper","VEA"),("doblar","VEA"),
       ("cortar","VEA"), ("comprar","VEA"), ("vender","VEA"),("llevar","VEA"),("puesto","VEA"),("cambiar","VEA"),("intercambiar","VEA"),("sustituir","VEA"), ("reemplazar","VEA"),("cerrar","VEA"),("buscar","VEA"),("encontrar","VEA"),("obtener","VEA"), ("conseguir","VEA"),("crear","VEA"),("creer","VEA"),("entrar","VEA"),("quedarse","VEA"),("salir","VEA"),("abandonar","VEA"),("dejar","VEA"),("comunicar","VEA"),("considerar","VEA"),("comparar","VEA"),("evaluar","VEA"),("decidir","VEA"),
       ("intentar","VEA"),("evitar","VEA"),("construir","VEA"),("destruir","VEA"),("deber","VEA"),("poder","VEA"),("conocer","VEA"),("entender","VEA"), ("comprender","VEA"),("atar","VEA"),("saber","VEA"),("cansarse","VEA"),("salir","VEA"),("trabajar","VEA"),("separar","VEA"), ("dividir","VEA"), ("partir","VEA"),("descansar","VEA"),("dormir","VEA"),("romper","VEA"),("aceptar","VEA"),("rechazar","VEA"),("descartar","VEA"),("acompañar","VEA"),("pedir","VEA"), ("solicitar","VEA"),("pretender","VEA"),("proponer","VEA"),
       ("sugerir","VEA"),("usar","VEA"),("hacer","VEA"),("fabricar","VEA"),("arreglar","VEA"), ("reparar","VEA"),("explicar","VEA"),("mostrar","VEA"),("comprobar","VEA"), ("intentar","VEA"),("comprobar","VEA"), ("verificar","VEA"),("variar","VEA"),("esperar","VEA"),("necesitar","VEA"), ("precisar","VEA"),("significar","VEA"),
       ("fue","VEI"),("dio","VEI"),("Cumple","VEI"),("cortar","VEI"),("tiene","VEI"),("decorando","VEI"),("pensaron","VEI"),("comimos","VEI"),("preparar","VEI"),("tomo","VEI"),("estudiando","VEI"),("escribir","VEI"),("pintar","VEI"),("viendo","VEI"),("Naturalizar","VEI"),("comprar","VEI"),("Prende","VEI"),("comenzó","VEI"),("contaré","VEI"),("escribiendo","VEI"),("Cumple","VEI"),("Encendí","VEI"),("Necesito","VEI"),("bailé","VEI"),("robaron","VEI"),("disfruté","VEI"),
       ("Manipular","VEI"),("Entrena","VEI"),("mirando","VEI"),("felicita","VEI"),("leía","VEI"),("Pidió","VEI"),("Escribiré","VEI"),("toca","VEI"),("dictará","VEI"),("Tengo","VEI"),("tiene","VEI"),("siembra","VEI"),("Adorna","VEI"),("rompieron","VEI"),("tuvieron","VEI"),("propusieron","VEI"),("revoquen","VEI"),("entrenando","VEI"),("Escucha","VEI"),("preparé","VEI"),("Paga","VEI"),("tendrá","VEI"),("cuidó","VEI"),("sopló","VEI"),("Busca","VEI"),("sacará","VEI"),
       ("agroalimentación","VEA"),("agroalimentario","VEA"),("agrodesia","VEA"),("agroforestal","VEA"),("agroforestería","VEA"),("agroindustria","VEA"),("agrología","VEA"),("agropecuario","VEA"),("agroquímica","VEA"),("agroquímico","VEA"),("agrosilvicultura","VEA"),("agroturismo","VEA"),("agrómena","VEA"),
       ("cultivar","VEA"),("plantar","VEA"),
       ("agricultura","VEA"),("apicultura","VEA"),("arboricultura","VEA"),("Avicultura","VEA"),("Caficultura","VEA"),("Cunicultura","VEA"),("Floricultura","VEA"),("Horticultura","VEA"),("Oleicultura","VEA"),("Olivicultura","VEA"),("Puericultura","VEA"),("Piscicultura","VEA"),("Sericicultura","VEA"),("Sericultura","VEA"),("Silvicultura","VEA"),("Vinicultura","VEA"),("Viticultura","VEA"),("Vitivinicultura","VEA"),

       ]


with open("../Data/grammar-CL.bin","wb") as file:
    c = 0
    for _palabra,_key in grammar:
        #if type(_tuple)!=tuple:

        #rint type(_tuple)
        file.write(str(_palabra)+" "+str(_key)+"\n")
print "Listo"
file.close()
