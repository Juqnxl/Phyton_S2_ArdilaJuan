total = 0 

# Personaliza tu hamburguesa c:
while True:
    print("======== Personaliza tu hamburguesa c: =======")

    print("Que pan deseas agregar?")
    print("1. Pan centeno $1000   2. Pan avena $1500")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        total += 1000
        print("Escogiste pan centeno")
    elif opcion == "2":
        total += 1500
        print("Escogiste pan avena")

    print("Cuanta carne deseas agregarle?")
    print("1. Carne 250g $5000   2. Carne 300g $7000")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        total += 5000
        print("Escogiste carne de 250g")
    elif opcion == "2":
        total += 7000
        print("Escogiste carne de 300g")

    print("Cuanto pollo deseas agregarle?")
    print("1. Pollo 250g $4500   2. Pollo 350g $5500")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        total += 4500
        print("Escogiste pollo de 250g")
    elif opcion == "2":
        total += 5500
        print("Escogiste pollo de 350g")

    print("Cuanto pollo desmechado deseas agregarle?")
    print("1. 250g $6500   2. 350g $7500")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        total += 6500
        print("Escogiste pollo desmechado de 250g")
    elif opcion == "2":
        total += 7500
        print("Escogiste pollo desmechado de 350g")

    print("Cuanta tocineta deseas agregarle?")
    print("1. Lonja $1500   2. Lonjas $2500")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        total += 1500
        print("Escogiste una lonja de tocineta")
    elif opcion == "2":
        total += 2500
        print("Escogiste dos lonjas de tocineta")

    seguir = input("Deseas agregar otra hamburguesa? (S/N): ")
    if seguir.lower() == "n":
        break

# Papas
print("Que papas deseas agregarle?")
print("1. Papas a la Francesa $5000  2. Papas en cascos $6000")
opcion = input("Elige una opcion: ")
if opcion == "1":
    total += 5000
    print("Escogiste papas a la francesa")
elif opcion == "2":
    total += 6000
    print("Escogiste papas en cascos")

# Bebida
print("Que bebida deseas?")
print("1. Gaseosa $5000   2. Cerveza $8000   3. Naranjada $9000")
opcion = input("Elige una opcion: ")
if opcion == "1":
    total += 5000
    print("Escogiste gaseosa")
elif opcion == "2":
    total += 8000
    print("Escogiste cerveza")
elif opcion == "3":
    total += 9000
    print("Escogiste naranjada")

# Servicio total
servicio = total * 0.10
print("El 10% de servicio: $", servicio)
total += servicio
print("Total a pagar: $", total)
