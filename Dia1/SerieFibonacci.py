# Ingrese cuantos terminos desea ver
n = int(input("Cuantos terminos quiere tener en la serie fibonacci?: "))

# Los primeros dos digitos de la serie
a = 0
b = 1

# Contador de serie
Contador = 0

# Se muestra serie
print("Serie fibonacci: ")

while Contador < n:
    print(a)
    siguiente = a + b
    a = b
    b = siguiente
    Contador += 1