###################################
############## Dia 2 ##############
###################################

# Algoritmo para verificar si un numero es primo

# Ingresa un numero
numero = int(input("Ingrese un numero: "))

# Verificar si es menor o igual a 1
if numero <= 1:
    print("No es un numero primo")
else:
    # Si es primo
    Es_primo = True

    # Verificar su tiene un divisor distion a 1 o si mismo
    for i in range(2, numero):
        if numero % i == 0:
            Es_primo = False
            break

# Mostramos resultado
if Es_primo:
    print("Es un numero primo")
else:
    print("No es un numero primo")

# Juan Esteban Ardila Serrano T.I. 1.097.496.297