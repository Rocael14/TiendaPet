# main.py
from menus import MenuInventario, MenuVentas, MenuUsuario, MenuReportes
from crud import CRUDEmpleado
def main():
    while True:
        print("--- MENU PRINCIPAL ---")
        print("1. Inventario")
        print("2. Ventas")
        print("3. Usuarios")
        print("4. Reportes")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            MenuInventario().menu_inventario()
        elif opcion == 2:
            MenuVentas().menu_ventas()
        elif opcion == 3:
            while True:
                MenuUsuario().menu_usuario()
                opcion_usuario = int(input("Seleccione una opcion: "))
                if opcion_usuario == 1:
                    CRUDEmpleado().agregar()
                    opcion = 3
                elif opcion_usuario == 2:
                    CRUDEmpleado().editar()
                elif opcion_usuario == 3:
                    CRUDEmpleado().eliminar()
                elif opcion_usuario == 4:
                    CRUDEmpleado().lista()
                elif opcion_usuario == 5:
                    break
        elif opcion == 4:
            MenuReportes().menu_reportes()
        elif opcion == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()

