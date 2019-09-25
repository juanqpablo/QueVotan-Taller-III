#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')

class Words:
    @classmethod
    def levenshtein(self, seq1, seq2):
        size_x = len(seq1) + 1
        size_y = len(seq2) + 1
        matrix = np.zeros ((size_x, size_y))
        for x in xrange(size_x):
            matrix [x, 0] = x
        for y in xrange(size_y):
            matrix [0, y] = y

        for x in xrange(1, size_x):
            for y in xrange(1, size_y):
                if seq1[x-1] == seq2[y-1]:
                    matrix [x,y] = min(
                        matrix[x-1, y] + 1,
                        matrix[x-1, y-1],
                        matrix[x, y-1] + 1
                    )
                else:
                    matrix [x,y] = min(
                        matrix[x-1,y] + 1,
                        matrix[x-1,y-1] + 1,
                        matrix[x,y-1] + 1
                    )
        distance = matrix[size_x - 1, size_y - 1]
        return distance

    @classmethod
    def getDistance(self,tags,texto):
        distance = 0
        distances = []
        for tag in tags.split(" "):
            for _palabra in texto.split(" "):
                distance = self.levenshtein(tag,_palabra)
                dTuple = (_palabra,distance)
                distances.append(dTuple)
        return distances

    @classmethod
    def getFrequency(self,seq):
        freq = []
        aSeq = seq.split()
        for w in aSeq:
            freq.append((w,aSeq.count(w)))
        return freq



a = "monitoreo telemático".lower() # materia
b = 'cautelar especial favor víctimas violencia intrafamiliarfacultar tribunal calificados controlar cumplimiento monitoreo telemático'.lower()
palabras = Words()
distancia = palabras.getDistance(a,b)
#for i,k in distancia:
#    print i, k

#Frecuencias
#print palabras.getFrequency(b)
for i,k in palabras.getFrequency(b):
    print i, k
