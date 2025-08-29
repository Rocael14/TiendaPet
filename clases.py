# clases.py

class Producto:
    def __init__(self, nombre, id_categoria, precio, total_cantidad_compras, total_cantidad_ventas):
        self.id_producto = GeneradorIdProducto.generar_id()
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.precio = precio
        self.total_cantidad_compras = total_cantidad_compras
        self.total_cantidad_ventas = total_cantidad_ventas
        self.stock = CalcularStock.calcular(total_cantidad_compras, total_cantidad_ventas)

class Categoria:
    def __init__(self, nombre):
        self.id_categoria = GeneradorIdCategoria.generar_id()
        self.nombre = nombre

class Clientes:
    def __init__(self, id_cliente, nombre, telefono, direccion, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Empleados:
    def __init__(self, id_rol_empleado, nombre, telefono, direccion, correo):
        self.id_empleado = GeneradorIdEmpleado.generar_id()
        self.id_tipo_empleado = id_rol_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Proveedor:
    def __init__(self, id_proveedor, nombre, id_empresa, telefono, direccion, correo):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.id_empresa = id_empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Empresas:
    def __init__(self, id_empresa, nombre, id_categoria):
        self.id_empresa = id_empresa
        self.nombre = nombre
        self.id_categoria = id_categoria

class Ventas:
    def __init__(self, id_venta, fecha, nit, id_empleado, total):
        self.id_venta = id_venta
        self.fecha = fecha
        self.nit = nit
        self.id_empleado = id_empleado
        self.total = total

class DetalleVentas:
    def __init__(self, id_detalle_venta,id_venta, id_producto, cantidad, precio, subtotal):
        self.id_detalle_venta = id_detalle_venta
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = subtotal

class Compras:
    def __init__(self, id_compras, fecha, id_proovedor, id_empleado, total):
        self.id_compras = id_compras
        self.fecha = fecha
        self.id_proovedor = id_proovedor
        self.id_empleado = id_empleado
        self.total = total

class DetalleCompras:
    def __init__(self, id_detalle_compras,id_compras, id_producto, cantidad, precio_compra, subtotal, fecha_caducidad):
        self.id_detalle_compras = id_detalle_compras
        self.id_compras = id_compras
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.subtotal = subtotal
        self.fecha_caducidad = fecha_caducidad

class RolEmpleado:
    def __init__(self, nombre_rol):
        self.id_rol = GeneradorIdRolEmpleado.generar_id()
        self.nombre_rol = nombre_rol

class TipoDePago:
    def __init__(self, nombre):
        self.id_tipo_de_pago = GeneradorIdTipoPago.generar_id()
        self.nombre = nombre

# Clase para calcular Stock del Producto
class CalcularStock:
    @staticmethod
    def calcular(total_compras, total_ventas):
        return total_compras - total_ventas

# Clase para generar ID
class GeneradorId:
    contador = 0
    @classmethod
    def generar_id(cls):
        pass

class GeneradorIdProducto(GeneradorId):
    contador = 0
    @classmethod
    def generar_id(cls):
        cls.contador += 1
        return f"P{cls.contador}"

class GeneradorIdEmpleado(GeneradorId):
    contador = 0
    @classmethod
    def generar_id(cls):
        cls.contador += 1
        return f"E{cls.contador}"

class GeneradorIdCategoria(GeneradorId):
    contador = 0
    @classmethod
    def generar_id(cls):
        cls.contador += 1
        return f"C{cls.contador}"

class GeneradorIdRolEmpleado(GeneradorId):
    contador = 0
    @classmethod
    def generar_id(cls):
        cls.contador += 1
        return f"R{cls.contador}"

class GeneradorIdTipoPago(GeneradorId):
    contador = 0
    @classmethod
    def generar_id(cls):
        cls.contador += 1
        return f"TP{cls.contador}"


class CargarGuardar:
    def cargar(self):
        try:
            with open("nombre.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        pass
            print("Informacion cargada")
        except FileNotFoundError:
            print("No existe el archivo ")

    def guardar(self):
        with open("nombre.txt", "w", encoding="utf-8") as archivo:
            pass


class CargarGuardarTiposPagos(CargarGuardar):
    def __init__(self):
        self.tipo_de_pago = {}
    def cargar_tipo_pago(self):
        try:
            with open("tipos_pagos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea :
                       id_tipo_pago, nombre = linea.split(":")
                       self.tipo_de_pago[id_tipo_pago] = {"Nombre": nombre}
            print("Tipos de pago importados desde tipos_pagos.txt")
        except FileNotFoundError:
            print("No existe el archivo tipos_pagos.txt, se creará uno nuevo al guardar.")

    def guardar(self):
        with open("tipos_pagos.txt", "w", encoding="utf-8") as archivo:
            for tipo_pago in self.tipo_de_pago.values():
                archivo.write(
                    f"{tipo_pago.id_tipo_pago}:{tipo_pago.nombre}\n"
                )
        print("Datos guardados correctamente.")


class CargarGuardarEmpleados(CargarGuardar):
    def __init__(self):
        self.empleados = {}

    def cargar_empleados(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split(":")
                        if len(datos) == 6:
                            id_empleado, id_rol_empleado, nombre_empleado, telefono_empleado, direccion_empleado, correo_empleado = datos

                            # Crear instancia de Empleados
                            nuevo_empleado = Empleados(
                                id_rol_empleado,
                                nombre_empleado,
                                int(telefono_empleado),
                                direccion_empleado,
                                correo_empleado
                            )
                            # Mantener el ID del archivo
                            nuevo_empleado.id_empleado = id_empleado

                            # Actualizar contador para no repetir IDs
                            if id_empleado.startswith('E'):
                                try:
                                    num = int(id_empleado[1:])
                                    if num >= GeneradorIdEmpleado.contador:
                                        GeneradorIdEmpleado.contador = num
                                except ValueError:
                                    pass

                            # Guardar en el diccionario
                            self.empleados[id_empleado] = nuevo_empleado

            print("Empleados cargados desde empleados.txt")
        except FileNotFoundError:
            print("No existe el archivo empleados.txt, se creará cuando registre datos.")

    def guardar(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for empleado in self.empleados.values():
                archivo.write(
                    f"{empleado.id_empleado}:{empleado.id_tipo_empleado}:{empleado.nombre}:{empleado.telefono}:{empleado.direccion}:{empleado.correo}\n"
                )
        print("Datos guardados correctamente.")


class CargarGuardarProductos(CargarGuardar):
    def __init__(self):
        self.productos = {}

    def cargar_productos(self):
        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split(":")
                        if len(datos) == 6:
                            id_producto, nombre, id_categoria, precio, compras, ventas = datos

                            # Crear instancia de Producto
                            nuevo_producto = Producto(
                                nombre=nombre,
                                id_categoria=id_categoria,
                                precio=float(precio),
                                total_cantidad_compras=int(compras),
                                total_cantidad_ventas=int(ventas)
                            )
                            # Mantener ID del archivo
                            nuevo_producto.id_producto = id_producto

                            # Actualizar contador del generador
                            if id_producto.startswith('P'):
                                try:
                                    num = int(id_producto[1:])
                                    if num >= GeneradorIdProducto.contador:
                                        GeneradorIdProducto.contador = num
                                except ValueError:
                                    pass

                            # Guardar en el diccionario
                            self.productos[id_producto] = nuevo_producto

            print("Productos cargados desde productos.txt")
        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará cuando registre datos.")

    def guardar(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for producto in self.productos.values():
                archivo.write(
                    f"{producto.id_producto}:"
                    f"{producto.nombre}:"
                    f"{producto.id_categoria}:"
                    f"{producto.precio}:"
                    f"{producto.total_cantidad_compras}:"
                    f"{producto.total_cantidad_ventas}\n"
                )
        print("Productos guardados en productos.txt")