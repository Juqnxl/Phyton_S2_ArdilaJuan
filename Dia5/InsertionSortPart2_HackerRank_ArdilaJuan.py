###################################
############## Dia 5 ##############
###################################

# Insertion sort part 2

import math
import os
import random
import re
import sys

# ordena la lista usando insertion sort
def insertionSort2(n, arr):

    # empiesza desde el segundo elemento
    for i in range(1, n):
        key = arr[i]

        # valor que vamos a insertar
        j = i - 1

        # movera elementos mas grande que key, una posicion a la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insertara el valor en el lugar correcto
        arr[j + 1] = key

        # muestra ek arreglo despues de una insercion
        print(' '.join(map(str, arr)))

if __name__ == '__main__':

    # cantidad de numeros
    n = int(input().strip())
    
    # lista de numeros
    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297