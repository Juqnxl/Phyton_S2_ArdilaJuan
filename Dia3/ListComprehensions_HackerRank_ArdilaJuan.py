###################################
############## Dia 3 ##############
###################################

# List Comprehensions

# ubicaciones
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# dar todas las combinacion posibles
resul = [[i, j, k] for i in range(x+1) 
                        for j in range(y+1) 
                        for k in range(z+1) 
                        if i + j + k != n]

# da el resultado
print(resul)

# Juan Esteban Ardila Serrano T.I. 1.097.496.297