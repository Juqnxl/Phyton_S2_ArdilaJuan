from funciones1 import abrirJSON, buscar_por_pais



def menu():
    artistas = abrirJSON()
    booleanito = True
    while booleanito:
        print("\n========= Menu =========")
        print("1. Buscar artistas por pais")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            buscar_por_pais(artistas)
        elif opcion == "2":
            print("Saliendo...")
            booleanito = False
        else:
            print("Opcion no valida, intente de nuevo.")

if __name__ == "__main__":
    menu()