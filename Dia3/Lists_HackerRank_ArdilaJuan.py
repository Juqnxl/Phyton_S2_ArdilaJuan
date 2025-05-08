###################################
############## Dia 3 ##############
###################################

# Lists

# lista basia
lista = []

# lee cantidad de comandos que se ejecutara
n = int(input())

#ejecuta cada comando
for _ in range(n):
    # lee el comando y lo divide por partes
    entrada = input().split()
    comando = entrada[0]
    argumentos = entrada[1:]

    # Evalua el comando
    if comando == "insert":
        lista.insert(int(argumentos[0]), int(argumentos[1]))
    elif comando == "print":
        print(lista)
    elif comando == "remove":
        lista.remove(int(argumentos[0]))
    elif comando == "append":
        lista.append(int(argumentos[0]))
    elif comando == "sort":
        lista.sort()
    elif comando == "pop":
        lista.pop()
    elif comando == "reverse":
        lista.reverse()

# Juan Esteban Ardila Serrano T.I. 1.097.496.297