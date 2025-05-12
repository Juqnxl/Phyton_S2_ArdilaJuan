###################################
############## Dia 5 ##############
###################################

# Couting sort 1

import math
import os
import random
import re
import sys

def countingSort(arr):

    # crea una lista con 100 ceros, cada posicion refleja una posicion de 0-99
    frecuencia = [0] * 100
    for numero in arr: # recorre cada numero en la lista
        frecuencia[numero] += 1 # suma 1 en la posicion que refleja cada numero
    return frecuencia

if __name__ == '__main__':

    # abre un archivo donde se guarda la salida
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip()) # lee numeros enteros que indican cuantos elementos estan en la lista
    arr = list(map(int, input().rstrip().split())) # lee la lista separada por espacio, y lo transforma en enteros
    result = countingSort(arr)
    
    # transforma los resultado a texto y los escribe separados por espacios
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close() # cierra el archivo de salida

# Juan Esteban Ardila Serrano T.I. 1.097.496.297