from conexiondb import conexion, mysql, app

class Productos:
    def __init__(self, DB, app):
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    
    def crearProductos(self, producto):
        
        # Validar que el precio de venta no sea inferior al precio de compra
        precio_compra = float(producto[8])
        precio_venta = float(producto[9])
        print(f"Precio de compra: {precio_compra}, Precio de venta: {precio_venta}")


        if precio_venta <= precio_compra:
            # Mostrar un mensaje de error o manejar la situación según tus necesidades
            print("Error: El precio de venta no puede ser igual o inferior al precio de compra.")
            return  

        sql = f"INSERT INTO `productos`(`ref_produ_1`, `ref_produ_2`, `ref_produ_3`, `categoria`, `nom_categoria`, `proveedor`, `nom_proveedor`, `nombre_producto`, `precio_compra`, `precio_venta`, `cantidad_producto`, `descripcion`, `stockminimo`, `ubicacion`, `estante`, `fechahora_registro`, `documento_operador`, `nombre_operador`, `apellido_operador`, `estado_producto`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (producto[0], producto[1], producto[2], producto[3], producto[4], producto[5], producto[6], producto[7], producto[8], producto[9], producto[10], producto[11], producto[12], producto[13], producto[14], producto[15], producto[16], producto[17], producto[18], 'ACTIVO')
        self.cursor.execute(sql, valores)
        self.conexion.commit()


    

    def producto_existe_en_db(self, ref_produ_1, ref_produ_2, ref_produ_3):
        condiciones = []

        if ref_produ_1 is not None:
            condiciones.append("ref_produ_1 = %s")
        if ref_produ_2 is not None:
            condiciones.append("ref_produ_2 = %s")
        if ref_produ_3 is not None:
            condiciones.append("ref_produ_3 = %s")

        condiciones_str = " AND ".join(condiciones)

        sql = f"SELECT COUNT(*) FROM productos WHERE {condiciones_str}"
        valores = [ref_produ_1, ref_produ_2, ref_produ_3]

        print("SQL:", sql)
        print("Valores:", valores)

        self.cursor.execute(sql, tuple(valores))
        resultado = self.cursor.fetchone()

        if resultado[0] > 0:
            return True  # El producto ya existe en la base de datos
        else:
            return False  # El producto no existe en la base de datos


        

    def buscar_productos(self, id_producto):
        sql = f"SELECT nombre_producto, ref_produ_1, ref_produ_2, ref_produ_3,  cantidad_producto,  descripcion, FROM productos WHERE ref_prod_1 = '{id_producto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        if(len(resultado)==0):
            return False
        else:
            return True

    
    def modificar(self, productos):
        sql = "UPDATE productos SET id_producto=%s, ref_produ_1=%s, ref_produ_2=%s, ref_produ_3=%s, nom_categoria=%s, nom_proveedor=%s, nombre_producto=%s, precio_compra=%s, precio_venta=%s, cantidad_producto=%s, descripcion=%s, stockminimo=%s, ubicacion=%s, estante=%s WHERE id_producto=%s"
        self.cursor.execute(sql, (
            productos[0], productos[1], productos[2], productos[3], productos[4],
            productos[5], productos[6], productos[7], productos[8], productos[9],
            productos[10], productos[11], productos[12], productos[13], productos[0]
        ))
        self.conexion.commit()

    
    def borrar_producto(self, id_producto):
        if not self.producto_existe_en_db(id_producto):
            print(f"Producto con id {id_producto} no encontrado.")
            return
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

        # Commit para aplicar los cambios
        self.conexion.commit()


        
Dproductos = Productos(mysql, app)