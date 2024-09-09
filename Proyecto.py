inventario = []

def agregar(nombre, cantidad, precio):
    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            return
    inventario.append([nombre, cantidad, precio])

def actualizar(nombre, cantidad):
    for producto in inventario:
        if producto[0] == nombre:
            producto[1] = cantidad  
            if producto[1] == 0:
                eliminar(nombre)  
            return
    print(f"Producto {nombre} no encontrado.")

def mostrar():
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\nInventario:")
    for producto in inventario:
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Precio: ${producto[2]:.2f}")
    print(f"Valor total del inventario: ${valor():.2f}\n")

def valor():
    total = 0
    for producto in inventario:
        total += producto[1] * producto[2] 
    return total

def eliminar(nombre):
    for producto in inventario:
        if producto[0] == nombre:
            inventario.remove(producto)
            print(f"Producto {nombre} eliminado del inventario.")
            return
    
def gestion():
    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar cantidad de un producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            actualizar(nombre, cantidad)
        elif opcion == "3":
            mostrar()
        elif opcion == "4":
            print("Ba bay")
            break
        else:
            print("Opción no válida.")
gestion()
