# -*- coding: utf-8 -*-
__author__      = "Juan Pablo Quezada"

class Grammar:
    """
        - grammar-CL.bin: Archivo binario quee contiene todas las palabras categorizadas
        - Tokens: Metodo que tokeniza las palabras, y retorna un arreglo de tuplas.
        - Post_tags: Metodo que retorna un arreglo de tuplas con cada palabra categorizada del texto entregado.
    """
    @classmethod
    def Tokens(self):
        palabras = []
        with open("./Data/grammar-CL.bin","rb") as file:
            data = file.readlines()
            for i in data:
                palabra = i[:-1].split(" ")
                palabras.append((palabra[0],palabra[1]))
        return palabras

    @classmethod
    def Post_tags(self,text):
        text_filter = []
        for p in text.split():
            for i,k in self.Tokens():
                if p==i:
                    text_filter .append((i,k))
                if p!=i:
                    text_filter.append((p,"DES"))
                else:
                    continue
        return set(text_filter)


def main():

    grammar = Grammar()
    #arr = grammar.Tokens()
    msg = "Modifica la ley N°18.892, General de Pesca y Acuicultura, en materia de prohibición de captura de especies salmonídeas provenientes de cultivos de acuicultura"

    text_tags = grammar.Post_tags(msg)
    text_filtered = [t for t in text_tags if t[1]!= "DES" and t[1]!="PP" and t[1]!="COC" and t[1]!="ARTD" and t[1]!="PRE"]
    print text_filtered

if __name__ == '__main__':
    main()
