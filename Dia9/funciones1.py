

def mostrar_artista(artista):
    print(f"\nNombre: {artista['nombreArt']}")
    print(f"País: {artista['pais']} ({artista['pais ISO3']})")
    print(f"Años activo: {artista['Active years']}")
    print(f"Año primer disco: {artista['Release year of first charted record']}")
    print(f"Género: {artista['Genre']}")
    print("Unidades certificadas:")
    for pais, unidades in artista['Total certified units'].items():
        print(f"  {pais}: {unidades}")
    print(f"Ventas reclamadas: {artista['Claimed sales']}")
    print(f"Estado: {'Activo' if artista['Is Active'] else 'No activo'}")

def buscar_por_pais(artistas):
    pais = input("Ingrese el nombre del país: ")
    encontrados = [a for a in artistas if a["pais"].lower() == pais.lower()]
    if not encontrados:
        print(f"No se encontraron artistas para el país: {pais}")
    else:
        for artista in encontrados:
            mostrar_artista(artista)