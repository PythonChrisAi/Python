def tablapitagorica():
    return [[(i + 1) * (j + 1) for j in range(10)] for i in range(10)]

def tabla(tabla):
    for fila in tabla:
        print(" ".join(f"{num:2d}" for num in fila))

def producto(tabla, x, y):
    return tabla[x - 1][y - 1]

def main():
    tablapitagoras = tablapitagorica()
    tabla(tablapitagoras)

    x = int(input("Ingrese el primer factor (entre 1 y 10): "))
    y = int(input("Ingrese el segundo factor (entre 1 y 10): "))

    resultado = producto(tablapitagoras, x, y)
    print(f"El producto de {x} y {y} es: {resultado}")

if __name__ == "__main__":
    main()