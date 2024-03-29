import time
from conexiondb import conexion, mysql, app
from flask import flash, jsonify, redirect, url_for

class Productos:
    def __init__(self, DB, app):
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    
    def crearProductos(self, producto):

        try:
            precio_compra = float(producto[6])
            precio_venta = float(producto[7])
        except ValueError:
            print("Error: El precio de compra o el precio de venta no son valores numéricos válidos.")
            return

        print(f"Precio de compra: {precio_compra}, Precio de venta: {precio_venta}")

        # Validar que el precio de venta no sea inferior al precio de compra
        if precio_venta <= precio_compra:
            error_mensaje = "Error: El precio de venta no puede ser igual o inferior al precio de compra."
            return jsonify({'error': error_mensaje})

        sql = f"INSERT INTO `productos`(`ref_produ_1`, `categoria`, `nom_categoria`, `proveedor`, `nom_proveedor`, `nombre_producto`, `precio_compra`, `precio_venta`, `cantidad_producto`, `descripcion`, `stockminimo`, `ubicacion`, `estante`, `fechahora_registro`, `documento_operador`, `nombre_operador`, `apellido_operador`, `estado_producto`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (producto[0], producto[1], producto[2], producto[3], producto[4], producto[5], producto[6], producto[7], producto[8], producto[9], producto[10], producto[11], producto[12], producto[13], producto[14], producto[15], producto[16],  'ACTIVO')
        self.cursor.execute(sql, valores)
        self.conexion.commit()


    

    def producto_existe_en_db(self, ref_produ_1, nombre_producto):
        condiciones = []

        if ref_produ_1 is not None:
            condiciones.append("ref_produ_1 = %s")
        if nombre_producto is not None:
            condiciones.append("nombre_producto = %s")

        condiciones_str = " AND ".join(condiciones)

        sql = f"SELECT COUNT(*) FROM productos WHERE {condiciones_str}"
        valores = []
        if ref_produ_1 is not None:
            valores.append(ref_produ_1)
        if nombre_producto is not None:
            valores.append(nombre_producto)

        print("SQL:", sql)
        print("Valores:", valores)

        self.cursor.execute(sql, tuple(valores))
        resultado = self.cursor.fetchone()

        if resultado[0] > 0:
            return True  # El producto ya existe en la base de datos
        else:
            return False  # El producto no existe en la base de datos



        

    def buscar_productos(self, id_producto):
        sql = f"SELECT nombre_producto, ref_produ_1,  cantidad_producto,  descripcion, FROM productos WHERE ref_prod_1 = '{id_producto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        if(len(resultado)==0):
            return False
        else:
            return True

    
    def modificar(self, productos):
        sql = "UPDATE productos SET id_producto=%s, ref_produ_1=%s, nom_categoria=%s, nom_proveedor=%s, nombre_producto=%s, precio_compra=%s, precio_venta=%s, cantidad_producto=%s, descripcion=%s, stockminimo=%s, ubicacion=%s, estante=%s WHERE id_producto=%s"
        self.cursor.execute(sql, (
            productos[0], productos[1], productos[2], productos[3], productos[4],
            productos[5], productos[6], productos[7], productos[8], productos[9],
            productos[10], productos[11], productos[0]
        ))
        self.conexion.commit()

    
    def borrar_producto(self, id_producto):
        """ if not self.producto_existe_en_db(id_producto):
            print(f"Producto con id {id_producto} no encontrado.")
            return """
        sql = f"UPDATE productos SET estado_producto='INACTIVO' WHERE id_producto=%s"
        self.cursor.execute(sql, (id_producto,))
        self.conexion.commit()
        print(self.cursor.rowcount, "registros afectado/s")

    def modificar_cantidad(self, producto):
        # Obtener la cantidad actual del producto
        sql = "SELECT cantidad_producto FROM productos WHERE id_producto = %s"
        self.cursor.execute(sql, (producto[0],))
        cantidad_actual = self.cursor.fetchone()[0]

        # Sumar la cantidad actual con la nueva cantidad
        nueva_cantidad = cantidad_actual + int(producto[3])

        # Actualizar la base de datos con la nueva cantidad
        sql_update = "UPDATE productos SET cantidad_producto = %s WHERE id_producto = %s"
        self.cursor.execute(sql_update, (nueva_cantidad, producto[0]))
        self.conexion.commit()  # Commit para aplicar los cambios

        
Dproductos = Productos(mysql, app)