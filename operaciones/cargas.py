#Opcion 1
def cargar_herramientas(inventario):
    while True:
        try:
            try:
                cantidad_herramientas = int(
                    input("\n¿Cuántas herramientas quiere cargar? ")
                )
            except ValueError:
                raise ValueError(
                    "La cantidad de herramientas debe ser un número entero."
                )

            if cantidad_herramientas <= 0:
                raise ValueError("La cantidad debe ser mayor que cero.")

            break

        except ValueError as error:
            print("Error:", error)

    for numero in range(cantidad_herramientas):
        print(f"\nHerramienta {numero + 1} de {cantidad_herramientas}")

        while True:
            try:
                nombre = input("Nombre de la herramienta: ").strip()

                if nombre == "":
                    raise ValueError("El nombre no puede estar vacío.")

                for producto in inventario:
                    if producto["herramienta"].lower() == nombre.lower():
                        raise ValueError("\nLa herramienta ya está registrada.")

                break

            except ValueError as error:
                print("Error:", error)

        while True:
            try:
                try:
                    cantidad = int(input("Stock inicial: "))
                except ValueError:
                    raise ValueError("El stock inicial debe ser un número entero.")

                if cantidad < 0:
                    raise ValueError("\nEl stock no puede ser negativo.") 
                
                break

            except ValueError as error:
                print("Error", error)


        inventario.append({"herramienta": nombre, "cantidad": cantidad})
        print("\nHerramienta agregada correctamente.")

    print("Carga completa.")

#Opción 5
def agregar_producto(inventario):
    nombre = input("Nombre de la herramienta: ").strip()

    if nombre == "":
        raise ValueError("El nombre no puede estar vacío.")

    for producto in inventario:
        if producto["herramienta"].lower() == nombre.lower():
            raise ValueError("La herramienta ya está registrada.")

    try:
        cantidad = int(input("Stock inicial: "))
    except ValueError:
        raise ValueError("El stock inicial debe ser un número entero.")

    if cantidad < 0:
        raise ValueError("El stock no puede ser negativo.")

    inventario.append({"herramienta": nombre, "cantidad": cantidad})

    print("Herramienta agregada correctamente.")
