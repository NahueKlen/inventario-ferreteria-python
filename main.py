from interfaz.menu import mostrar_menu

from operaciones.consultas import (
    mostrar_inventario,
    consultar_stock,
    reportar_agotados,
)

from operaciones.cargas import cargar_herramientas, agregar_producto

from operaciones.movimientos import actualizar_stock

from persistencia import guardar_inventario, cargar_inventario


def main():
    try:
        inventario = cargar_inventario()
    except ValueError as error:
        print("Error:", error)
        return

    while True:
        mostrar_menu()
        
        try:
            try:
                opcion = int(input("\nSeleccioná una opción: "))
            except ValueError:
                raise ValueError("La opción debe ser un número entero.")

            if opcion < 1 or opcion > 7:
                raise ValueError("Las opciones deben estar entre 1 y 7.")

            if opcion == 1:
                cargar_herramientas(inventario)
                guardar_inventario(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reportar_agotados(inventario)
            elif opcion == 5:
                agregar_producto(inventario)
                guardar_inventario(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
                guardar_inventario(inventario)
            elif opcion == 7:
                print("Programa finalizado.")
                break

        except ValueError as error:
            print("Error: ", error)

if __name__ == "__main__":
    main()