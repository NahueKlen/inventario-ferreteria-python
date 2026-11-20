#Opción 2
def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    print("\nInventario actual: ")

    for producto in inventario:
        print(
            f"Herramientas: {producto['herramienta']}"
            f" - Stock: {producto['cantidad']}"
        )

#Opción 3
def consultar_stock(inventario):
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    nombre = input("Nombre de la herramienta a consultar: ").strip()

    if nombre == "":
        raise ValueError("El nombre no puede estar vacío")

    for producto in inventario:
        if producto["herramienta"].lower() == nombre.lower():
            print(
                f"Herramienta: {producto['herramienta']} "
                f" - Stock: {producto['cantidad']}"
            )
            return

    print("La herramienta no se encuentra en el catálogo.")

#Opción 4
def reportar_agotados(inventario):
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    hay_agotados = False

    for producto in inventario:
        if producto["cantidad"] == 0:
            print("Herramienta agotada: ", producto["herramienta"])
            hay_agotados = True

    if hay_agotados == False:
        print("Ninguna herramienta tiene stock cero.")