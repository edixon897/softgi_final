from conexiondb import conexion, mysql, app

class Productos:
    def __init__(self, DB, app):
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    
    def crearProductos(self, producto):
        sql = f"INSERT INTO `productos`(`ref_produ_1`, `ref_produ_2`, `ref_produ_3`, `categoria`, `nom_categoria`, `proveedor`, `nom_proveedor`, `nombre_producto`, `precio_compra`, `precio_venta`, `cantidad_producto`, `descripcion`, `stockminimo`, `ubicacion`, `estante`, `fechahora_registro`, `documento_operador`, `nombre_operador`, `apellido_operador`, `estado_producto`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (producto[0], producto[1], producto[2], producto[3], producto[4], producto[5], producto[6], producto[7], producto[8], producto[9], producto[10], producto[11], producto[12], producto[13], producto[14], producto[15], producto[16], producto[17], producto[18], 'ACTIVO')
        self.cursor.execute(sql, valores)
        self.conexion.commit()


    

    def producto_existe_en_db(self, producto):
        sql = f"SELECT COUNT(*) FROM productos WHERE id_producto = '{producto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()

        if resultado[0] > 0:
            return True
        else:
            return False
        

    def buscar_productos(self, id_producto):
        sql = f"SELECT nombre_producto, ref_produ_1, ref_produ_2, ref_produ_3,  cantidad_producto,  descripcion, FROM productos WHERE ref_prod_1 = '{id_producto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        if(len(resultado)==0):
            return False
        else:
            return True


    def modificar(self,productos):
        sql=f"UPDATE productos SET id_producto='{productos[0]}', ref_produ_1='{productos[1]}', ref_produ_2='{productos[2]}', ref_produ_3='{productos[3]}', nom_categoria='{productos[4]}', nom_proveedor='{productos[5]}', nombre_producto='{productos[6]}', precio_compra='{productos[7]}', precio_venta='{productos[8]}', cantidad_producto='{productos[9]}', descripcion='{productos[10]}', stockminimo='{productos[11]}', ubicacion='{productos[12]}', estante='{productos[13]}',documento_operador='{productos[14]}', nombre_operador='{productos[15]}', apellido_operador='{productos[16]}' WHERE id_producto='{productos[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
    

    
    def borrar_producto(self, id_producto):
        
        sql = f"UPDATE productos SET estado_producto='INACTIVO' WHERE id_producto = '{id_producto}'"
        print("aca voy",sql)

        try:
            self.cursor.execute(sql)
            print("aca voy",sql)
            self.conexion.commit()
            return True  # Borrado exitoso
        except Exception as e:
            print(f"Error al borrar el producto: {str(e)}")
            self.conexion.rollback()
            return False
        
Dproductos = Productos(mysql, app)