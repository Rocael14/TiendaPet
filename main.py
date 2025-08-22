class Producto:
    def __init__(self, id_producto,nombre, id_categoria, precio, total_compras, total_ventas):
        self.id_producto = id_producto
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.precio = precio
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = CalcularStock.calcular(total_compras, total_ventas)

class CalcularStock:
    def calcular(self, total_compras, total_ventas):
        return total_compras-total_ventas
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

