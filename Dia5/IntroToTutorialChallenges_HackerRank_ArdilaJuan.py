###################################
############## Dia 5 ##############
###################################

# Intro to tutorial challenges

import math
import os
import random
import re
import sys

def introTutorial(V, arr):
    # busca el numero V en el arreglo arr
    for i in range(len(arr)):
        if arr[i] == V:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # busca el numero
    V = int(input().strip())
    
    # cantidad de elementos
    n = int(input().strip())
    
    # cconvierte numero enteros
    arr = list(map(int, input().rstrip().split()))
    
    # reesultado de buscar V
    result = introTutorial(V, arr)
    
    # resultado
    fptr.write(str(result) + '\n')

    fptr.close()

# Juan Esteban Ardila Serrano T.I. 1.097.496.297