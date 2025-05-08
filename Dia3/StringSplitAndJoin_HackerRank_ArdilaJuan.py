###################################
############## Dia 3 ##############
###################################

# String split and join

def split_and_join(line):
    
    # se divide la cadena utilizando un espacio como delimitador
    listaPalabras = line.split(" ")
    
    # se une la lista de palabras con un guion
    resultado = "-".join(listaPalabras)
    
    # se devuelve la cadena
    return resultado

if __name__ == '__main__':
    
    # se captura la entrada
    line = input()

    # llamamos la funcion
    result = split_and_join(line)

    # da el resultado
    print(result)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297