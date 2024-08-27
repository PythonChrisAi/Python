#Primer ejercicio
sexo = input("Introduce tu sexo (Hombre/Mujer): ")

peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)

if sexo == "hombre":
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 24.9:
        categoria = "Normal"
    elif imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
elif sexo == "mujer":
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 24.9:
        categoria = "Normal"
    elif imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
else:
    categoria = "Sexo no aceptado"

if categoria != "Sexo no aceptado":
    print(f"Tu IMC es {imc:.2f}. Categoría: {categoria}")
else:
    print("Por favor, introduce un sexo válido (Hombre o Mujer).")

print(f"Tu IMC es {imc:.2f}, lo que indica {categoria}.")

# Ejercicio 2
calificacion1 = float(input("Ingresa la primera calificación: "))
calificacion2 = float(input("Ingresa la segunda calificación: "))
calificacion3 = float(input("Ingresa la tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

if promedio >= 70:
    resultado = "Aprobado"
elif promedio >= 50:
    resultado = "Recuperación"
else:
    resultado = "Reprobado"

print(f"Tu promedio es {promedio:.2f}. Resultado: {resultado}.")

# Ejercicio 3
numero = input("Ingresa un número de 5 dígitos: ")

if numero == numero[::-1]:
    print(f"El número {numero} es capicúa.")
else:
    print(f"El número {numero} no es capicúa.")

# Ejercicio 4
lado1 = int(input("Ingresa el primer lado del triángulo: "))
lado2 = int(input("Ingresa el segundo lado del triángulo: "))
lado3 = int(input("Ingresa el tercer lado del triángulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print(f"El triángulo es {tipo}.")
else:
    print("Los lados no forman un triángulo válido.")

# Ejercicio 5
numero = int(input("Ingresa un número entero positivo: "))

if numero <= 1:
    es_primo = False
elif numero == 2 or numero == 3:
    es_primo = True
elif numero % 2 == 0 or numero % 3 == 0:
    es_primo = False
elif numero % 5 == 0 or numero % 7 == 0:
    es_primo = numero == 5 or numero == 7
else:
    es_primo = True

if es_primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

# Ejercicio 6
año = int(input("Ingresa un año: "))
bisiesto = False
siglo_xxi = False

if año % 4 == 0:
    if año % 100 != 0 or año % 400 == 0:
        bisiesto = True

if 2001 <= año <= 2100:
    siglo_xxi = True

if bisiesto:
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")

if siglo_xxi:
    print(f"El año {año} es del siglo XXI.")
else:
    print(f"El año {año} no es del siglo XXI.")

# Ejercicio 7
pin_correcto = "1234"
saldo = 1000

# Primer intento
pin = input("Ingresa tu PIN: ")
if pin == pin_correcto:
    print("PIN correcto.")
    opcion = input("1. Ver saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir\nElige una opción: ")
    if opcion == "1":
        print(f"Tu saldo es: ${saldo}")
    elif opcion == "2":
        retiro = float(input("¿Cuánto deseas retirar? "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Has retirado ${retiro}. Tu nuevo saldo es ${saldo}.")
        else:
            print("Fondos insuficientes.")
    elif opcion == "3":
        deposito = float(input("¿Cuánto deseas depositar? "))
        saldo += deposito
        print(f"Has depositado ${deposito}. Tu nuevo saldo es ${saldo}.")
    elif opcion == "4":
        print("Saliendo...")
    else:
        print("Opción no válida.")
else:
    print("PIN incorrecto. Intentos restantes: 2")
    pin = input("Ingresa tu PIN: ")
    if pin == pin_correcto:
        print("PIN correcto.")
        opcion = input("1. Ver saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir\nElige una opción: ")
        if opcion == "1":
            print(f"Tu saldo es: ${saldo}")
        elif opcion == "2":
            retiro = float(input("¿Cuánto deseas retirar? "))
            if retiro <= saldo:
                saldo -= retiro
                print(f"Has retirado ${retiro}. Tu nuevo saldo es ${saldo}.")
            else:
                print("Fondos insuficientes.")
        elif opcion == "3":
            deposito = float(input("¿Cuánto deseas depositar? "))
            saldo += deposito
            print(f"Has depositado ${deposito}. Tu nuevo saldo es ${saldo}.")
        elif opcion == "4":
            print("Saliendo...")
        else:
            print("Opción no válida.")
    else:
        print("PIN incorrecto. Intentos restantes: 1")
        pin = input("Ingresa tu PIN: ")
        if pin == pin_correcto:
            print("PIN correcto.")
            opcion = input("1. Ver saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir\nElige una opción: ")
            if opcion == "1":
                print(f"Tu saldo es: ${saldo}")
            elif opcion == "2":
                retiro = float(input("¿Cuánto deseas retirar? "))
                if retiro <= saldo:
                    saldo -= retiro
                    print(f"Has retirado ${retiro}. Tu nuevo saldo es ${saldo}.")
                else:
                    print("Fondos insuficientes.")
            elif opcion == "3":
                deposito = float(input("¿Cuánto deseas depositar? "))
                saldo += deposito
                print(f"Has depositado ${deposito}. Tu nuevo saldo es ${saldo}.")
            elif opcion == "4":
                print("Saliendo...")
            else:
                print("Opción no válida.")
        else:
            print("Fallaste los tres intentos. Acceso bloqueado.")
            
# Ejercicio 8
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

if (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes in [4, 5]):
    estacion = "Primavera"
elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 22) or (mes in [7, 8]):
    estacion = "Verano"
elif (mes == 9 and dia >= 23) or (mes == 12 and dia <= 20) or (mes in [10, 11]):
    estacion = "Otoño"
else:
    estacion = "Invierno"

print(f"La fecha {dia}/{mes} es: {estacion}.")

# Ejercicio 9
numero_dia = int(input("Ingresa un número del 1 al 7: "))

if numero_dia == 1:
    dia = "Lunes"
elif numero_dia == 2:
    dia = "Martes"
elif numero_dia == 3:
    dia = "Miércoles"
elif numero_dia == 4:
    dia = "Jueves"
elif numero_dia == 5:
    dia = "Viernes"
elif numero_dia == 6:
    dia = "Sábado"
elif numero_dia == 7:
    dia = "Domingo"
else:
    dia = "Número inválido"

if dia in ["Sábado", "Domingo"]:
    print(f"{dia} te toca descansito.")
else:
    print(f"{dia} te toca chambear.")

# Ejercicio 10
calificacion = int(input("Ingresa una calificación de 1 a 5 estrellas: "))
reseña = input("Por favor da una breve reseña: ")

if calificacion == 4 or calificacion == 5:
    print("Gracias por tu reseña positiva.")
elif calificacion == 3:
    print("Gracias por tu reseña, mejoraremos.")
elif calificacion == 1 or calificacion == 2:
    detalles = input("Por favor, da más detalles sobre tu experiencia negativa: ")
    print("Gracias por tu feedback. Trabajaremos para mejorar nuestro servicio.")
else:
    print("Calificación inválida.")