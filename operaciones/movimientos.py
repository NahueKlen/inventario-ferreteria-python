#Opción 6
def actualizar_stock(inventario):
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    nombre = input("Nombre de la herramienta a actualizar:  ").strip()

    if nombre == "":
        raise ValueError("El nombre no puede estar vacío.")

    for producto in inventario:
        if producto["herramienta"].lower() == nombre.lower():
            print(
                f"Herramienta encontrada: {producto['herramienta']}"
                f" - Stock actual: {producto['cantidad']}"
            )

            movimiento = input("Tipo de movimiento (venta/ingreso): ").strip().lower()

            if movimiento != "venta" and movimiento != "ingreso":
                print("El tipo de movimiento debe ser venta o ingreso.")
                return

            try:
                unidades = int(input("Cantidad de unidades: "))
            except ValueError:
                raise ValueError("La cantidad de unidades debe ser un número entero.")
            
            if unidades <= 0:
                raise ValueError("Las unidades deben ser mayores a cero.")

            if movimiento == "venta":
                if unidades > producto["cantidad"]:
                    raise ValueError("No hay stock suficiente para esta venta.")

                producto["cantidad"] = producto["cantidad"] - unidades

            else:
                producto["cantidad"] = producto["cantidad"] + unidades

            print("Movimiento registrado. Stock actual:", producto["cantidad"])
            return
        
    print("La herramienta no se encuentra en el catálogo.")
