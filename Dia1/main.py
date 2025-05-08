######################
##### Clase Dia 1#####
######################

#Imprimir en Piton

print("Hola Mundo!")

#Creacion de variables
#1. Dato tipo string

nombre = "Juan"
print(type(nombre))

#2. Dato tipo numero entrero

numeroEntero=5
print(numeroEntero)
print(type(numeroEntero))

#3. Dato tipo numero real

numeroReal = 5.3
print(type(numeroReal))

#4. Dato tipo double
numeroPi=3.1416

print(numeroPi)

#5. Dato tipo booleano

booleanito = True
print(booleanito)

#6. (SOLO PHYTON) Numero complejo

numeroComplejo = complex("+1.23")
print(type(numeroComplejo))
print(type(numeroEntero))

#Convertir numero int a float

nuemroNuevo = float(numeroEntero)
print(type(nuemroNuevo))
print(" ")

#Cliclo for (Desde)

for i in range(5):
    print(i)
print(" ")

#Ciclo for (Desde-Hasta)

for i in range(0,5):
    print(i)
    print("")
for i in range(1,5):
    print(i)
    print("")

#Ciclo for ( Desde-Hasta-Paso)

for i in range(1,5,1):
    print(i)

# ###########################
#Ciclo white

booleanitoNuevo = True
while(booleanitoNuevo==True):
    print("Sigo siendo verdadero!!!!")
    booleanitoNuevo=False

booleanitoNuevo = True
while(booleanitoNuevo):
    print("Sigo siendo verdadero!!!!!")
    booleanitoNuevo = False

    # ########################
    # Condicionales if-else

    texto = "Juan"
    if(texto=="Juan"):
        print("Sos juan :yay:")
    else:
        if(texto=="Ardila"):
            print("Sos Ardila :yay:")
        else:
            print("No sos ninguno :sadfeis:")

Condicionales elif
if(texto=="Juan"):
    print("Sos juan :yay")
elif(texto=="Ardila"):
    print("Sos ardila :yay:")
else:
    print("No sos ninguno :sadfeis:")

# ###################

Anidar condicionales
booleanitoJuan1 = True
booleanitoJuan2 = True
if(booleanitoJuan1==True and booleanitoJuan2==True):
    print("Todos somos verdades :)")
else:
    print("No somos iguales :()")

# ###################

Anidar condicionales
booleanitoJuan1 = True
booleanitoJuan2 = True
if(booleanitoJuan1==True and booleanitoJuan2==True):
    print("Todos somos verdades :)")
else:
    print("No somos iguales :()")

# ############################

Entradas de usuario
nombreusuario= input("Cual es tu nombre?: ") ## Todos los inputs son string
print("Tu nombre es: " +nombreusuario)#Cpmcatemacopm

# Casteo de string a numero

edadUsuario=int(input("Cual es tu edad?: "))
edadUsuario = edadUsuario + 5
print("La edad de "+nombreusuario+" es de:"+str(edadUsuario))

# #####################################

Funciones

#1. Funcion con retorno y con parametros

def areaCirculo(radio):
    valorPi=3.1416
    resultadoFinal = valorPi + (radio*+2)
    return resultadoFinal
radioUsuario= float(input("Cual es el radio de su circulo: ?"))
print("El area del circulo es de: "+str(areaCirculo(radioUsuario)))

# 2. Funcion con retorno y sin parámetros

def valorDolar():
    return 4299
valorFinalDolar=valorDolar()
print("El valor del dólar es:"+str(valorFinalDolar))

# 3. Función sin retorno y con parámetros

def concatenarNombres(nombre,apellido):
    print("Su nombre completo es:"+nombre+" "+apellido)
concatenarNombres("Sharick","Ibañez")

# 4. Función sin retorno y sin parámetros

def funcionX():
    print("Soy una función que solo vive y existe")
funcionX()

# Desarrollado por : Juan Esteban Ardila Serrano - T.I. : 1.097.496.297#