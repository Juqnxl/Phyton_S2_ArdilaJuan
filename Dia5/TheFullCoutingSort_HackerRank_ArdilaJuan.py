###################################
############## Dia 5 ##############
###################################

# The full counting sort

import math
import os
import random
import re
import sys

def countSort(arr):
    n = len(arr) # se obtiene la cantidad total de elementos
    resultado = [[] for _ in range(100)] # crea una lista con 100, lista vacia 0-99
    for i in range(n): # recorre cada elemento de arr

        # convierte el primer  elemento a entero
        numero = int(arr[i][0])
        texto = "-" if i < n // 2 else arr[i][1]
        resultado[numero].append(texto)
    for grupo in resultado: # da todas las palabras en orden y con espacios
        for palabra in grupo:
            print(palabra, end=' ')

if __name__ == '__main__':
    n = int(input().strip()) # numeros de elementos
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297