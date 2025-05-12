###################################
############## Dia 5 ##############
###################################

# Big sorting

import math
import os
import random
import re
import sys


def bigSorting(unsorted):
    # se ordena por longitud y luego alfabeticamente
    return sorted(unsorted, key = lambda x: (len(x), x))
    
if __name__ == '__main__':
    # se abre el archivo de salidad 
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # lee el numero de elementos
    n = int(input().strip())

    unsorted = []
    
    # lee los numeros como string
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
        
        # da la lista ordenada
    result = bigSorting(unsorted)
    
    # da el resultado al archivo de salida
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

# Juan Esteban Ardila Serrano T.I. 1.097.496.297