# -*- coding: utf-8 -*- 
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
#Se ingresa la paguina por metodo get para extraer los datos
driver.get("https://www.leychile.cl/Navegar?idNorma=1106037&buscar=3731")
time.sleep(10)
#se buscan los datos de las siguientes etiquetas
b = driver.find_elements_by_class_name('norma')
#descripcion del proyecto 
print (b[0].text)

