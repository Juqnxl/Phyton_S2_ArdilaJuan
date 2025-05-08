###################################
############## Dia 3 ##############
###################################

# Mutations

# se define la funcion de la cadena
def mutate_string(string, position, character):

    # remplaza caracteres en la pucision, para antes, nuevo caracter y parte despues
    return string[:position] + character + string[position + 1:]


# se usa cuando se ejecuta directamente
if __name__ == '__main__':
    # lee la cadena original des la entrada estandar
    s = input()
    
    # lee indices y el nuevo caracter, separandolos con un espacio
    i, c = input().split()

    # se convierte i en entero, y devuelve la cadena
    s_new = mutate_string(s, int(i), c)

    # da resultado
    print(s_new)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297