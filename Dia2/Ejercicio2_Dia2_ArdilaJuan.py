###################################
############## Dia 2 ##############
###################################

# Algoritmo para encontrar el mayor de 3 numeros

# Pedimos que ingrese tres numeros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

# Comparamos para encontrar el mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Mostramos numero mayor
print("El numero myor es: ", mayor)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297