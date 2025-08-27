#CLASES PRINCIPALES
class Producto:
    def __init__(self, nombre, id_categoria, precio, total_compras, total_ventas):
        self.id_producto = GeneradorIdProducto.generar_id()
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.precio = precio
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = CalcularStock.calcular(total_compras, total_ventas)

class Categoria:
    def __init__(self, id_categoria,nombre):
        self.id_categoria =id_categoria
        self.nombre = nombre

class Clientes:
    def __init__(self, id_cliente,nombre, telefono, direccion, correo):
        self.id_cliente =id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Empleados:
    def __init__(self, id_rol_empleado,nombre, telefono, direccion, correo):
        self.id_empleado = GeneradorIdEmpleado.generar_id()
        self.id_tipo_empleado = id_rol_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class RolEmpleado:
    def __init__(self, id_rol, nombre):
        self.id_rol = id_rol
        self.nombre = nombre

class TipoDePago:
    TIPOS = {
        "TP1": "Efectivo",
        "TP2": "Tarjeta",
        "TP3": "Transferencia"
    }

    def __init__(self, id_tipo_de_pago):
        if id_tipo_de_pago not in self.TIPOS:
            raise ValueError("Tipo de pago no válido")
        self.id_tipo_de_pago = id_tipo_de_pago
        self.nombre = self.TIPOS[id_tipo_de_pago]

#Clase para calcular Stock del Producto
class CalcularStock:
    def calcular(self, total_compras, total_ventas):
        return total_compras-total_ventas

#Clase para generar ID
class GeneradorId:
    contador = 0
    def generar_id(self):
        pass
class GeneradorIdProducto(GeneradorId):
    contador = 0
    def generar_id(self):
        self.contador += 1
        return f"P{self.contador}"
class GeneradorIdEmpleado(GeneradorId):
    contador = 0
    def generar_id(self):
        self.contador += 1
        return f"E{self.contador}"
#CRUD
class MetodosCRUD:
    def agregar(self): pass
    def lista(self): pass
    def editar(self): pass
    def eliminar(self): pass

class CRUDRolesEmpleado(MetodosCRUD):
    def __init__(self):
        self.roles = {}
    def agregar(self):
        pass
    def lista(self):
        for rol in self.roles.values():
            print(rol.id_rol, rol.nombre)


class CRUDEmpleado(MetodosCRUD):
    def __init__(self):
        self.empleados = {}
    def agregar(self):
        roles = CRUDRolesEmpleado()
        print("--- Crear Empleado ----")
        while True:
            try:
                nombre_empleado = input("Ingresa el nombre completo del empleado: ")
                telefono_empleado = int(input("Ingresa el telefono del empleado: "))
                direccion_empleado = input("Ingresa el direccion del empleado: ")
                correo_empleado = input("Ingresa el correo del empleado: ")
                while True:
                    print("Seleccione el rol del empleado")
                    roles.lista()
                    id_rol_empleado = input("").upper()
                    if id_rol_empleado in roles.roles:
                        break
                    else:
                        print("Error: Rol ingresado no existe!")
                        print("Porfavor Ingrese un rol valido")
                nuevo_empleado = Empleados(
                    id_rol_empleado,
                    nombre_empleado,
                    telefono_empleado,
                    direccion_empleado,
                    correo_empleado
                )
                self.empleados[nuevo_empleado.id_empleado] = nuevo_empleado
                print(f"Empleado agregado correctamente el ID es:{nuevo_empleado.id_empleado}")
                while True:
                    continuar_agregando_empleado=int(input("¿Desea seguir agregando empleados? 1.Si o 2.No"))
                    if continuar_agregando_empleado == 1:
                        print("Enter para continuar")
                        input()
                        break
                    elif continuar_agregando_empleado == 2:
                        print("Vuelve al menu de Usuarios")
                        break
                    else:
                        print("Error: Ingrese una opcion valida, vuelva a intentarlo")
                if continuar_agregando_empleado == 2:
                    break
            except ValueError:
                print("Error! Solo se permite ingreso numerico")

    def lista(self):
        print("--- Lista de Empleados ---")
        if not self.empleados:
            print("No hay empleados registrados")
        else:
            pass

    def editar(self):
        print("--- Editar Empleado ---")
        self.lista()
        id_empleado = input("Ingrese el ID del empleado a editar: ").upper()

        if id_empleado in self.empleados:
            empleado_editar = self.empleados[id_empleado]
            print(f"Editando {empleado_editar.nombre}...")
            print("Si no deseas cambiar el dato del empleado solo presiona enter")
            input()
            nuevo_nombre = input(f"Nuevo nombre ({empleado_editar.nombre}): ") or empleado_editar.nombre
            try:
                nuevo_telefono = int(input(f"Nuevo telefono ({empleado_editar.telefono}): "))
            except ValueError:
                print("AVISO: Queda el mismo numero de telefono")
                nuevo_telefono = empleado_editar.telefono

            nueva_direccion = input(f"Nueva dirección ({empleado_editar.direccion}): ") or empleado_editar.direccion
            nuevo_correo = input(f"Nuevo correo ({empleado_editar.correo}): ") or empleado_editar.correo

            empleado_editar.nombre = nuevo_nombre
            empleado_editar.telefono = nuevo_telefono
            empleado_editar.direccion = nueva_direccion
            empleado_editar.correo = nuevo_correo

            print("Empleado actualizado correctamente.")
        else:
            print("Error: ID no encontrado.")

    def eliminar(self):
        print("--- Eliminar Empleado ---")
        self.lista()
        id_empleado = input("Ingrese el ID del empleado a eliminar: ").upper()

        if id_empleado in self.empleados:
            self.empleados.pop(id_empleado)
            print(f"Empleado eliminado correctamente.")
        else:
            print("Error: ID no encontrado.")

##############################################
class MenuInventario:
    def menu_inventario(self):
        print("Menu Inventario")
        print("1. Agregar Producto")
        print("2. Comprar Producto")
        print("3. Lista Productos")
        print("4. Editar Producto")
        print("5. Eliminar Producto")
        print("6. Volver al menu principal")
class MenuVentas:
    def menu_ventas(self):
        print("Menu Ventas")
        print("1. Venta de Producto")
        print("2. Reimpresion Factura")
        print("3. Volver al menu principal")
class MenuUsuario:
    def menu_usuario(self):
        print("Menu Usuario")
        print("1. Agregar Usuario")
        print("2. Editar Usuario")
        print("3. Eliminar Usuario")
        print("4. Lista de Usuarios")
        print("5. Volver al menu principal")
class MenuReportes:
    def menu_reportes(self):
        print("Menu Reportes")
        print("1. Reporte de Compras")
        print("2. Reporte de Ventas")
        print("3. Reporte de Productos")
        print("4. Reporte de Empleados")
        print("5. Reporte de Clientes")
        print("6. Volver al menu principal")

while True:
    print("--- MENU ---")
    print("1. Inventario")
    print("2. Ventas")
    print("3. Usuarios")
    print("4. Reporte")
    print("5. Salir")
