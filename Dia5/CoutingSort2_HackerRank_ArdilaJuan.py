###################################
############## Dia 5 ##############
###################################

# Couting sort 2

import math
import os
import random
import re
import sys

def countingSort(arr):
    conteo = [0] * 100 # cuenta cuantas veces aparace cada numero, 0-99
    for numero in arr: # recorre todos los numeros 
        conteo[numero] += 1 # por cada numero aumenta 1 de valor en su posicion

    resultado = [] # crea la lista ordenada
    for i in range(len(conteo)): # recorre de 0-99 en la lista
        for _ in range(conteo[i]): # agrega tantas veces el resultado, dependiendo de cuantas veces aparecio
            resultado.append(i)

    return resultado # lo da ordenado 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip()) # lee cuantos numeros tiene la lista
    arr = list(map(int, input().rstrip().split())) # convierte los numeros en enteros y los lee
    result = countingSort(arr) 
    
    # da el resultado en una linea de numeros separados por espacios
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Juan Esteban Ardila Serrano T.I. 1.097.496.297