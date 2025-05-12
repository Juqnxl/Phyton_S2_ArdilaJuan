###################################
############## Dia 5 ##############
###################################

# Insertion sort part 1

import math
import os
import random
import re
import sys

# funcion que simula insertar el ultimo numero de la lista casi ordenada
def insertionSort1(n, arr):
    # toma el ultimo numero que se va a insertar
    value = arr[-1]
    # empieza a comparar desde el penultimo elemento
    i = n - 2
    
    # mientras no encontremos un numero menor y no salgamos del arreglo
    while i >= 0 and arr[i] > value:
        # desplaza el numero a la derecha
        arr[i + 1] = arr[i]
        # muestra el arreglo actual
        print(' '.join(map(str, arr)))
        # sigue comparando hacia la izquierda
        i -= 1
    
    # cuando se encuentra la posicion correcta inserta el valor
    arr[i + 1] = value
    # muestra el arreglo final con el valor insertado
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    # numero de elemtos
    n = int(input().strip())
    
    # lista de enteros
    arr = list(map(int, input().rstrip().split()))
    
    # se llama a la funcion con los datos
    insertionSort1(n, arr)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297