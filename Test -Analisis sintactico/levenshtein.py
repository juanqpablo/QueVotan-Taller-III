#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
a = "Modifica las leyes Nos. 19.968 y 20.066 para incorporar una medida cautelar especial en favor de las víctimas de violencia intrafamiliar y facultar al tribunal, en casos calificados, a controlar su cumplimiento por medio del monitoreo telemático."
b = 'monitoreo telemático' #tag 1
c = 'MONITOREO TELEMÁTICO' #tag 2
d = "pensión universal solidaria para las personas en situación de discapacidad y mecanismos unificados de evaluación."

def levenshtein(seq1, seq2):
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
    print (matrix)
    return (matrix[size_x - 1, size_y - 1])

print(levenshtein(a,c))
