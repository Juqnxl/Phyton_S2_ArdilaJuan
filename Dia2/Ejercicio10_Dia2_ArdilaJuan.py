###################################
############## Dia 2 ##############
###################################

# Algoritmo para calcular el promedio de una lista de numeros

# Ingresamos numeros separados por comas
entrada = input("Ingrese una lista de numeros, separados por comas: ")

# Convertimos la lista(cadena) a numeros
numeros = [float(num) for num in entrada.split(",")]

# Calcula los numeros y promedio
suma = sum(numeros)
promedio = suma / len(numeros)

# Mostramos resultado
print("El promedio es: ", promedio)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297