###################################
############## Dia 3 ##############
###################################

# Find The Runner-Up Score

# entrada principal del programa
if __name__ == '__main__':

    # lee numeros enteros
    n = int(input())

    # lee linia de entrada, las divide en partes separadas por espacion, la guarda en la lista
    Tabla = list(map(int, input().split()))
    
    # enecuentra valor dentro de la lista
    MaxTabla = max(Tabla)
    # crea lista que contenga todo lo de la tabla, excepto lo mismo que el valor maximo
    FiltradoTabla = [x for x in Tabla if x != MaxTabla]
    
    # da los resultados
    print(max(FiltradoTabla))

# Juan Esteban Ardila Serrano T.I. 1.097.496.297