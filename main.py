#CLASES PRINCIPALES
class Producto:
    def __init__(self, id_producto,nombre, id_categoria, precio, total_compras, total_ventas):
        self.id_producto = id_producto
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.precio = precio
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = CalcularStock.calcular(total_compras, total_ventas)

class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Clientes:
    def __init__(self, id_cliente, nombre, telefono, direccion, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Empleados:
    def __init__(self, id_empleado, id_tipo_empleado,nombre, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.id_tipo_empleado = id_tipo_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class TipoEmpleados:
    def __init__(self, id_tipo_empleado, nombre):
        self.id_tipo_empleado = id_tipo_empleado
        self.nombre = nombre

class TipoDePago:
    def __init__(self, id_tipo_de_pago, nombre):
        self.id_tipo_de_pago = id_tipo_de_pago
        self.nombre = nombre
#Clase para calcular Stock del Producto
class CalcularStock:
    def calcular(self, total_compras, total_ventas):
        return total_compras-total_ventas

#Clase para generar ID
class GeneradorId:
    def generar_id(self, id):
        return id
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
