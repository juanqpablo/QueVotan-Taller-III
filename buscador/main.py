from search import Buscador

a = Buscador()
print("Escribe salir para SALIR")
print("Ingresa 1 para obtener datos de SESIONES")
print("Ingresa 2 para obtener datos de BOLETINES")
print("Ingresa 3 para obtener datos de PROYECTOS")
print("Ingresa 4 para obtener datos de DETALLES DE PROYECTO")
print("Ingresa palabra clave de proyecto")

flag=True
while flag:
    option = input("Ingresa palabra clave para buscar: ")
    if option == "salir" or option == "SALIR":
        flag = False
    if option == "1":
        print(a.getProyects("sesion", option))
    if option == "2":
        print(a.getProyects("boletin", option))
    if option == "3":
        print(a.getProyects("proyecto", option))
    if option == "4":
        print(a.getProyects("detalle", option))
    else:
        print(a.getProyects("boletisssssn", option))
