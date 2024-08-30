#Ejercicio 1

palabras = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]

cuantas = 0
for palabra in palabras:
    if palabra == "Python":
        cuantas += 1

print("La palabra 'Python' aparece", cuantas, "veces.")

#Ejercicio 2

frases = ["hola", "mundo", "python", "es", "genial"]

mayusculas = []
for frase in frases:
    nueva = ""
    for caracter in frase:
        if 'a' <= caracter <= 'z':  
            nueva += chr(ord(caracter) - 32) 
        else:
            nueva += caracter
    mayusculas.append(nueva)

print("Frases en mayúsculas:", mayusculas)

#Ejercicio 3

palabras = ["sol", "luna", "cielo", "mar", "estrella", "pez"]

nuevas = []
for palabra in palabras:
    if len(palabra) >= 4:
        nuevas.append(palabra)

print("Palabras con 4 o más letras:", nuevas)

#Ejercicio 4

numeros = [15, 22, 8, 34, 9, 6, 17]

maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero

print("El número máximo es:", maximo)

#Ejercicio 5

numeros = [-3, 5, -7, 2, -8, 10, -4, 6]

positivos = 0
for numero in numeros:
    if numero > 0:
        positivos += 1

print("Hay" ,positivos, "números positivos")

#Ejercicio 6 

numeros = [1, 2, 3, 4, 5]

invertidos = []
for i in range(len(numeros) - 1, -1, -1):
    invertidos.append(numeros[i])

print("Lista invertida:", invertidos)

#Ejercicio 7

numeros = [4, 7, 2, 9, 3, 8, 5]

suma = 0
for numero in numeros:
    suma += numero

media = suma / len(numeros)
print("La media de los numeros es:", media)

