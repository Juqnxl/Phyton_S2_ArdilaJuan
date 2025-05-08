###################################
############## Dia 3 ##############
###################################

# Find a string

# cuenta cuantas veces aapara subString
def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)

    # recoremos la cadena desde el inicio hasta el punto donde aun cabe la subcadena
    for i in range(len(string) - sub_len + 1):

        # comparamos parte de la cadena del mismo tamaño de la subcadena
        if string[i:i+sub_len] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    # lee la candena principal e subcadena, eliminando espacio al princio o al final
    string = input().strip()
    sub_string = input().strip()
    
    # se le llama a la funcion, y da el resultado
    count = count_substring(string, sub_string)
    print(count)

    # Juan Esteban Ardila Serrano T.I. 1.097.496.297