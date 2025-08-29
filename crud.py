# crud.py
from clases import Empleados, RolEmpleado, CargarGuardarTiposPagos, TipoDePago, CargarGuardarEmpleados,Categoria,Producto,CargarGuardarProductos

class MetodosCRUD:
    def agregar(self): pass
    def lista(self): pass
    def editar(self): pass
    def eliminar(self): pass


class CRUDMetodosPago(MetodosCRUD, CargarGuardarTiposPagos):
    def __init__(self, nombre):
        super().__init__()
        self.tipo_de_pago = self.cargar()

    def agregar(self, nombre):
        nuevo_pago = TipoDePago(nombre)
        self.tipo_de_pago[nuevo_pago.id_tipo_de_pago] = nuevo_pago
        print("Tipo de pago agregado exitosamente")
        self.guardar(self.tipo_de_pago)

    def lista(self):
        if not self.tipo_de_pago:
            print("No hay tipos de pago registrados.")
        else:
            print("---Lista de tipos de pago----")
            for tipo_pago in self.tipo_de_pago.values():
                print(f"{tipo_pago.id_tipo_de_pago}: {tipo_pago.nombre}")

    def editar(self, id_tipo_pago, nuevo_nombre):
        if id_tipo_pago in self.tipo_de_pago:
            self.tipo_de_pago[id_tipo_pago].nombre = nuevo_nombre
            print("Se guardaron los cambios exitosamente")
            self.guardar(self.tipo_de_pago)  # guardar cambios
        else:
            print("Tipo de pago no encontrado.")

    def eliminar(self, id_tipo_pago):
        if id_tipo_pago in self.tipo_de_pago:
            del self.tipo_de_pago[id_tipo_pago]
            print(f"Tipo de pago eliminado exitosamente")
            self.guardar(self.tipo_de_pago)  # guardar cambios
        else:
            print("Tipo de pago no encontrado.")

class CRUDRolesEmpleado(MetodosCRUD, RolEmpleado):
    def __init__(self):
        self.roles = {}
        self.cargar_rol()

    def cargar_rol(self):
        try:
            with open("roles.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_rol, nombre_rol = linea.split(":")
                        self.roles[id_rol] = RolEmpleado(nombre_rol)
            print("Roles importados exitosamente")
        except FileNotFoundError:
            print("No existe el archivo 'roles.txt'")

    def agregar(self):
        id_rol = input("Ingrese el ID del rol: ").upper()

        # Verificar si el ID ya existe
        if id_rol in self.roles:
            print("Error: Ya existe un rol con ese ID")
            return

        nombre_rol = input("Ingrese el nombre del rol: ")
        self.roles[id_rol] = RolEmpleado(id_rol, nombre_rol)
        print("Rol agregado correctamente.")

        # Guardar automáticamente después de agregar
        self.guardar_roles()

    def lista(self):
        print("--- Lista de Roles ---")
        if not self.roles:
            print("No hay roles registrados")
        else:
            for id_rol, rol in self.roles.items():
                print(f"{rol.id_rol} - {rol.nombre_rol}")

class CRUDCategoria(MetodosCRUD, Categoria):
    def __init__(self):
        self.categoria = {}
        self.cargar_categorias()

    def cargar_categorias(self):
        try:
            with open("categoria.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_categoria, nombre = linea.split(":")
                        self.categoria[id_categoria] = Categoria(nombre)
            print("Categorias importados exitosamente")
        except FileNotFoundError:
            print("No existe el archivo 'roles.txt'")

    def agregar(self):
        pass

    def lista(self):
        print("--- Lista de Roles ---")
        if not self.categoria:
            print("No hay roles registrados")
        else:
            for id_categoria, categoria in self.categoria.items():
                print(f"{categoria.id_categoria} - {categoria.nombre}")

class CRUDEmpleado(MetodosCRUD, CargarGuardarEmpleados):
    def __init__(self):
        super().__init__()
        self.cargar_empleados()

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
                        print("Error: Rol ingresado no existe! Intente de nuevo.")
                nuevo_empleado = Empleados(
                    id_rol_empleado,
                    nombre_empleado,
                    telefono_empleado,
                    direccion_empleado,
                    correo_empleado
                )
                self.empleados[nuevo_empleado.id_empleado] = nuevo_empleado
                print(f"Empleado agregado correctamente con ID: {nuevo_empleado.id_empleado}")
                self.guardar()
                break
            except ValueError:
                print("Error! Solo se permite ingreso numerico")

    def lista(self):
        print("--- Lista de Empleados ---")
        if not self.empleados:
            print("No hay empleados registrados")
        else:
            for empleado in self.empleados.values():
                print(f"{empleado.id_empleado} - {empleado.nombre} - {empleado.telefono} - {empleado.direccion} - {empleado.correo}")

    def editar(self):
        print("--- Editar Empleado ---")
        self.lista()
        id_empleado = input("Ingrese el ID del empleado a editar: ").upper()
        if id_empleado in self.empleados:
            empleado_editar = self.empleados[id_empleado]
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
            print("Empleado eliminado correctamente.")
        else:
            print("Error: ID no encontrado.")

class CRUDProducto(MetodosCRUD,CargarGuardarProductos):
    def __init__(self):
        super().__init__()
        self.cargar_productos()

    def agregar(self):
        categorias = CRUDCategoria()
        print("\n--- Crear Producto ---")
        nombre_producto = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))

        # seleccionar categoría válida
        while True:
            print("Seleccione la categoría")
            categorias.lista()
            id_categoria = input("Categoría: ").upper()
            if id_categoria in categorias.categoria:
                break
            else:
                print("Error: Categoría no existe, intente de nuevo.")

        nuevo_producto = Producto(
            nombre=nombre_producto,
            id_categoria=id_categoria,
            precio=precio,
            total_cantidad_compras=0,
            total_cantidad_ventas=0
        )
        self.productos[nuevo_producto.id_producto] = nuevo_producto
        print(f"Producto {nuevo_producto.nombre} agregado exitosamente")

        self.guardar()

    def lista(self):
        print("\n--- Lista de Productos ---")
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for producto in self.productos.values():
                print(
                    f"[{producto.id_producto}] {producto.nombre} | "
                    f"Categoría: {producto.id_categoria} | "
                    f"Precio: {producto.precio} | "
                    f"Compras: {producto.total_cantidad_compras} | "
                    f"Ventas: {producto.total_cantidad_ventas} | "
                    f"Stock: {producto.stock}"
                )

    def editar(self):
        self.lista()
        id_editar = input("\nIngrese el ID del producto a editar: ").upper()
        if id_editar in self.productos:
            producto = self.productos[id_editar]
            print(f"Editando producto {producto.nombre}")

            nuevo_nombre = input(f"Nuevo nombre ({producto.nombre}): ") or producto.nombre
            try:
                nuevo_precio = float(input(f"Nuevo precio ({producto.precio}): ")) or producto.precio
            except ValueError:
                print("Precio inválido, se mantiene el anterior")
                nuevo_precio = producto.precio


            producto.nombre = nuevo_nombre
            producto.precio = nuevo_precio

            print("Producto editado correctamente.")
            self.guardar()
        else:
            print("No existe un producto con ese ID")

    def eliminar(self):
        self.lista()
        id_eliminar = input("\nIngrese el ID del producto a eliminar: ").upper()
        if id_eliminar in self.productos:
            eliminado = self.productos.pop(id_eliminar)
            print(f"Producto '{eliminado.nombre}' eliminado correctamente.")
            self.guardar()
        else:
            print("No existe un producto con ese ID")