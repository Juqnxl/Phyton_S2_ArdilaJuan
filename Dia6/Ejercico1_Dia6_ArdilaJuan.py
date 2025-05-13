'''
Juanes c:
{
    "nombre":"Juan",
    "apellido":"Ardila"
}
'''
miPrimerDiccionario={
    "nombre":"Juan",
    "apellido":"Ardila",
    "edad":18
}
print(miPrimerDiccionario)
print(type(miPrimerDiccionario))

# para recorrer un DICcionario debes llamar a la llave
print(miPrimerDiccionario["nombre"])
print(type(miPrimerDiccionario["nombre"]))
# Se puede recorrer con puntos en algunos casos
'''
print(miPrimerDiccionario.nombre)
'''
# para reemplazar un valor del diccionario
miPrimerDiccionario["nombre"]="Juan"
nombre = miPrimerDiccionario["nombre"]
apellido= miPrimerDiccionario["apellido"]
print(miPrimerDiccionario["nombre"]+" "+miPrimerDiccionario["apellido"])

miPrimerDiccionario["ciudadNacimiento"]="Zapatoca"

print(miPrimerDiccionario)
miPrimerDiccionario["ciudadNacimiento"]="Bucaramanga"

print(miPrimerDiccionario)

listaPersonas=[]
listaPersonas.append(miPrimerDiccionario)
print("")
print("")
print(listaPersonas)
listaPersonas.append({
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27
})
print("")
print("")
print(listaPersonas)
print("")
print("")
print(listaPersonas[1])
print(type(listaPersonas[1]))
print(listaPersonas[0]["edad"])

# recorrer listas con diccionarios
for i in range(len(listaPersonas)):
    print("#################")
    print("####Persona #",i+1," ####")
    print("#################")
    print("Nombre:",listaPersonas[i]["nombre"])
    print("Apllido:",listaPersonas[i]["apellido"])
    print("Edad:",listaPersonas[i]["edad"])

# diccionario con listas
diccionarioRobusto={
    "id":1,
    "nombre":"Juan",
    "apellido":"Ardila",
    "edad":18,
    "telefonos":[{"codigo":57,"numero":3108698155,"tipo":"trabajo"},
                 {"codigo":57,"numero":3108698155,"tipo":"personal"}]
}
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"},
                 {"codigo":22,"numero":6857493658,"tipo":"personal"}]
}
listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)
print("")
print("")
print(listaRobusta)
print("")
print("")

for i in range(len(listaRobusta[0]["telefonos"])):
    if(listaRobusta[0]["telefonos"][i]['tipo']=="trabajo"):
        print(listaRobusta[0]["telefonos"][i]['numero'])
print("")
print("")
numeroPrimeraPersona=listaRobusta[0]["telefonos"][1]['numero']
tipoNumeroPP=listaRobusta[0]["telefonos"][1]['tipo']
print(str(numeroPrimeraPersona)+ tipoNumeroPP)

booleanito = True
while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    # crud (create,read,update y delete)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))

    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        diccionarioVacio = {}
        diccionarioVacio["id"] = int(input("ID de la persona: "))
        diccionarioVacio["nombre"] = input("Nombre: ")
        diccionarioVacio["apellido"] = input("Apellido: ")
        diccionarioVacio["edad"] = int(input("Edad: "))
        diccionarioVacio["telefonos"] = []
        cantidadTelefonos = int(input("¿Cuántos teléfonos desea agregar?: "))
        for i in range(cantidadTelefonos):
            telefono = {}
            telefono["codigo"] = int(input("Código del teléfono: "))
            telefono["numero"] = int(input("Número del teléfono: "))
            telefono["tipo"] = input("Tipo de teléfono (personal/trabajo): ")
            diccionarioVacio["telefonos"].append(telefono)
        listaRobusta.append(diccionarioVacio)
        print("Persona creada exitosamente.")

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                print("---------------------------")

    elif(opcionUsuario==3):
        print("#################")
        print("#### Mostrar Persona Individual ####")
        print("#################")
        idBuscado = int(input("Ingrese el ID de la persona: "))
        personaEncontrada = None
        for persona in listaRobusta:
            if persona["id"] == idBuscado:
                personaEncontrada = persona
                break
        if personaEncontrada:
            print("Nombre:", personaEncontrada["nombre"])
            print("Apellido:", personaEncontrada["apellido"])
            print("Edad:", personaEncontrada["edad"])
            for tel in personaEncontrada["telefonos"]:
                print("Código:", tel["codigo"])
                print("Número:", tel["numero"])
                print("Tipo:", tel["tipo"])
        else:
            print("No se encontró una persona con ese ID.")

    elif(opcionUsuario==4):
        print("#################")
        print("#### Actualizar Persona ####")
        print("#################")
        idActualizar = int(input("Ingrese el ID de la persona a actualizar: "))
        for persona in listaRobusta:
            if persona["id"] == idActualizar:
                persona["nombre"] = input("Nuevo nombre: ")
                persona["apellido"] = input("Nuevo apellido: ")
                persona["edad"] = int(input("Nueva edad: "))
                for i, tel in enumerate(persona["telefonos"]):
                    print(f"Teléfono #{i+1}")
                    tel["codigo"] = int(input("Nuevo código: "))
                    tel["numero"] = int(input("Nuevo número: "))
                    tel["tipo"] = input("Nuevo tipo (personal/trabajo): ")
                print("Persona actualizada correctamente")
                break
        else:
            print("No se encontro una persona con ese ID")

    elif(opcionUsuario==5):
        print("#################")
        print("#### Eliminar Persona ####")
        print("#################")
        idEliminar = int(input("Ingrese el ID de la persona a eliminar: "))
        for i in range(len(listaRobusta)):
            if listaRobusta[i]["id"] == idEliminar:
                del listaRobusta[i]
                print("Persona eliminada correctamente")
                break
        else:
            print("No se encontro una persona con ese ID")

    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")

# Juan Esteban Ardila Serrano T.I. 1.097.496.297