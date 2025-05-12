###################################
############## Dia 5 ##############
###################################

# Correctness and the loop invariant

# define funcion que toma una lista l como parametro
def insertion_sort(l):

    # recorre desde el segundo elemento hasta el final
    for i in range(1, len(l)):

        # valor que queremos insetar en la posicion correcta
        key = l[i]

        # se compara con el elemento anterior
        j = i - 1

        # mientras no haya llegado al inicio de lista, y el elemto a la izquierda sea mayor que key
        while j >= 0 and l[j] > key:
           
           #desplaza el elemento a la derecha
           l[j+ 1] = l[j]

           # compara hacia la izquierda
           j -= 1

           # inserta valor en la posicion correcta
        l[j + 1] = key

# lee el tamaño de la lista 
m = int(input().strip())

# lee los elemento de la lista separados por espacios, se convierte en enteros
ar = [int(i) for i in input().strip().split()]

# se llama la funcion, para ordenar lista
insertion_sort(ar)

# da la lista ordenada, con espacion y una sola linea
print(" ".join(map(str,ar)))

# Juan Esteban Ardila Serrano T.I. 1.097.496.297