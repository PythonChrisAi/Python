#Primer ejercicio
numero1 = input('Escribe el primer numero: ')
numero2 = input('Escribe el segundo numero: ')
numero3 = input('Escribe el tercer numero: ')

for numero in numero1,numero2,numero3:
    print(numero, end = '-')

#Segundo ejercicio
numeros = (10, 20, 30, 40, 50)
print(len(numeros))
print(numeros[2])

#Tercer ejercicio
tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(len(tupla_anidada))
print(tupla_anidada[1][1])

#Cuarto ejercicio
pares = (2,4,6,8,10)
impares = (1,3,5,7,9)

for paresd in impares:
    print(impares+(pares))

#Quinto ejercicio
colores = ('rojo', 'azul', 'verde', 'rojo', 'amarillo', 'rojo')

cuantas = 0
for palabra in colores:
    if palabra == "rojo":
        cuantas += 1

print("El color 'rojo' aparece", cuantas, "veces.")

#Sexto ejercicio

nombres = ['Ana', 'Juan', 'Pedro', 'Luis']
tupla = ()
for nombre in nombres:
    tupla += (nombre,)
print(tupla)

#Septimo ejercicio

Larga = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(Larga[0:5])

#Octavo ejercicio
a = 5
b = 10

a, b = b, a

print("a =", a)
print("b =", b)

