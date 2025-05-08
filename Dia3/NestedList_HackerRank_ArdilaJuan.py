###################################
############## Dia 3 ##############
###################################

# Nested Lists

# Almacenar informacion de estudiantes
estudiantes = []

# lee numero de estudiantes
n = int(input())

# lee su nombre y su calificacion
for _ in range(n):
    nombre = input()
    nota = float(input())
    estudiantes.append([nombre, nota])
    
# obtiene todas las calificaciones en orden
notasUnicas = sorted(set(nota for nombre, nota in estudiantes))
    
# hace el segundo grado mas bajo
segundaMenor = notasUnicas[1]
    
# segundo grado mas bajo se agrega a la lista de notas
nombresConSegundaMenor = [nombre for nombre, nota in estudiantes if nota == segundaMenor]

# ordena los nombres en abecedario
nombresConSegundaMenor.sort()

# da el resultado
for nombre in nombresConSegundaMenor:
    print(nombre)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297