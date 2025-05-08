###################################
############## Dia 3 ##############
###################################

# Finding the percentage

if __name__ == '__main__':

# lee numero de estudiantes
n = int(input())

# crea un diccionario para almacenar los datos
registroEstudiantes = {}

# lee datos de cada estudiantes
for _ in range(n):
    entrada = input().split()
    nombre = entrada[0]
    calificaciones = list(map(float, entrada[1:]))
    registroEstudiantes[nombre] = calificaciones
    
# lee el nmombre del estudiante a consultar
consultaNombre = input()

# calcula el promedio de calificaciones del estudiante
promedio = sum(registroEstudiantes[consultaNombre]) / len(registroEstudiantes[consultaNombre])

# da el resultado
print("{:.2f}".format(promedio))

# Juan Esteban Ardila Serrano T.I. 1.097.496.297
