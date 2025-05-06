# Pedimos que ingrese un numero
numero = int(input("Ingrese el numero entero: "))

# Iniciamos con el resultado 1
factorial = 1

# Utilizamos bucle para multiplicar de 1 hasta el numero
for i in range(1, numero + 1):
    factorial = factorial*1

# Mostrar el resultado
print("El factorial de ", numero, "es:", factorial)