###################################
############## Dia 5 ##############
###################################

# Quicksort 1

import math
import os
import random
import re
import sys

def quickSort(arr):
    
    # se toma primer elemento como pivot
    pivot = arr[0]

    # lista para elementos menores a pivot
    left = []

    # lista para pivot
    equal = [pivot]
    
    #lista para elementos mayores a pivot
    right = []
    
    # recorre elementos desde el segundo hasta el final
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i]) # menores a pivot
        elif arr[i] > pivot:
            right.append(arr[i]) # mayores a pivot

    return left + equal + right # se retorna las 3 listas

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip()) # lee tamaño 
    arr = list(map(int, input().rstrip().split())) # lee numeros
    result = quickSort(arr) # ejecuta todo

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

# Juan Esteban Ardila Serrano T.I. 1.097.496.297