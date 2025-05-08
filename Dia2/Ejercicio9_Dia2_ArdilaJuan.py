###################################
############## Dia 2 ##############
###################################

# Algoritmo para hacer una tabla de multiplicar

# Ingrese un numero
numero = int(input("Ingrese un numero para generar una tabla de multiplicar: "))

# Imprime la tabla
print (f"Tabla de multiplicar del {numero}:")

for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Juan Esteban Ardila Serrano T.I. 1.097.496.297