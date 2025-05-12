###################################
############## Dia 5 ##############
###################################

# Running time of algorithms

import math
import os
import random
import re
import sys

# cuenta cuantos shifts se hacen al ordenar el arreglo con insertion sort
def runningTime(arr):

    # cuenta los desplazamientos
    shifts = 0

    # empieza desde el segundo elemento
    for i in range(1, len(arr)):

        # elemento que queremos insertar
        key = arr[i]
        j = i - 1

        # compara elementos anteriores y los mueve sin son mayor que el key
        while j >= 0 and arr[j] > key:

            # mover el numero a la derecha
            arr[j + 1] = arr[j]

            # cuenta este movimiento
            shifts += 1
            j -= 1

            # inserta key en su lugar correcto
            arr[j + 1] = key
    return shifts
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # lee cantidad de numeros
    n = int(input().strip())

    # lee la lista de numeros
    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')
    fptr.close()

# Juan Esteban Ardila Serrano T.I. 1.097.496.297