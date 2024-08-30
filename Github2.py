# Ejercicio 1

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = []
for i in range(len(matriz1)):
    fila = []
    for j in range(len(matriz1[0])):
        suma = matriz1[i][j] + matriz2[i][j]
        fila.append(suma)
    resultado.append(fila)

print("La sumita de las matrices es:")
for fila in resultado:
    print(fila)

#Ejercicio 2

matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

resultado = []
for i in range(len(matriz1)):
    fila = []
    for j in range(len(matriz2[0])):
        producto = 0
        for k in range(len(matriz1[0])):
            producto += matriz1[i][k] * matriz2[k][j]
        fila.append(producto)
    resultado.append(fila)

print("La multiplicación de las matrices es:")
for fila in resultado:
    print(fila)


#Ejercicio 3

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta = []
for i in range(len(matriz[0])):
    fila = []
    for j in range(len(matriz)):
        fila.append(matriz[j][i])
    transpuesta.append(fila)

print("la matriz transpuesta es:")
for fila in transpuesta:
    print(fila)

#Ejercicio 4

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

print("La matriz es:")
for fila in matriz:
    print(fila)
    
n = len(matriz)
suma = sum(matriz[0])

hobbit= True

for fila in matriz:
    if sum(fila) != suma:
        hobbit = False

for j in range(n):
    columna = sum(matriz[i][j] for i in range(n))
    if columna != suma:
        hobbit = False

diagonal1 = sum(matriz[i][i] for i in range(n))
diagonal2 = sum(matriz[i][n-i-1] for i in range(n))

if diagonal1 != suma or diagonal2 != suma:
    hobbit = False

if hobbit:
    print("La matriz es un cuadrado mágico.")
else:
    print("La matriz no es un cuadrado mágico.")
