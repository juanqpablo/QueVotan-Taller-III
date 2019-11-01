from pymongo import MongoClient
from pprint import pprint

class Buscador:
    @classmethod
    def clean(cls, frase):
        msg = (frase[1:(len(frase) - 2)])
        msg = msg.split(",")
        arr = []
        for info in msg:
            temp = ""
            for letra in info:
                if letra != " " and letra != "'":
                    temp = temp + letra
            arr.append(temp)
        return arr

    @classmethod
    def getProyects(cls, option, valor):
        client = MongoClient("localhost", 27017)
        db = client.virtual
        cursor = db.LegislaturaActual.find()
        proyectos = {}
        cont=0
        for data in cursor:
            for sesion in data["51"]["sesiones"]:
                if option == "sesion":
                    print(sesion)    # Mostrar todas las sesiones
                for boletines in sesion["boletines"]:
                    if option == "boletin":
                        print(boletines)
                    # if boletines["_id"] == "10268-12":
                    #     return boletines
                    for proyecto in boletines["proyectos"]:
                        if option == "proyecto":
                            print(proyecto)
                #         # proyectos[proyecto["_id"]] = proyecto
                #         # proyectos[proyecto["_id"]].append(proyecto["nombre"])
                        datos=dict(id=proyecto["id_votacion"], nombre=proyecto["nombre"], materia=proyecto["materia"],
                                   tags=proyecto["tags"])
                        # proyectos[proyecto["id_votacion"]] = datos
                        # proyectos[proyecto["_id"]] = datos
                        if option == "detalle":
                            pprint(datos)
                        # pprint(datos["tags"])
                        # print(type((cls.clean(datos["tags"]))))
                        for item in cls.clean(datos["tags"]):
                            if item == valor:
                                print(datos)

        # return proyectos


s = Buscador()

#
# a=input("Ingrese palabra clave de busqueda: ")
# print(s.getProyects("cuerpos",a))
