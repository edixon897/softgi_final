from conexiondb import conexion, mysql, app

class Cotizaciones:
    def __init__(self, DB, app): 
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()  
        self.cursor = self.conexion.cursor()
        
        
    def crearCotizaciones(self, registro):           
        sql = f"INSERT INTO `cotizaciones`(`num_cotizacion`, `cliente_cotizacion`, `documento_operador`, `nombre_operador`, `apellido_operador`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_cliente_cotizacion`, `direcion_cliente`, `correo_cliente`, `cuidad_cliente`, `contacto_cliente`, `estado`) VALUES ('{registro[0]}','{registro[1]}','{registro[2]}','{registro[3]}','{registro[4]}','{registro[5]}','{registro[6]}', '{registro[7]}', '{registro[8]}', '{registro[9]}', '{registro[10]}', '{registro[11]}', 'ACTIVO')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
        
        
    """ def editarCotizacion(self,editar):
        bsql = f"UPDATE `cotizaciones` SET `num_cotizacion`='{editar[0]}', `cliente_cotizacion`='{editar[1]}', `documento_operador`='{editar[2]}', `nombre_operador`='{editar[3]}', `apellido_operador`='{editar[4]}', `fecha_inicio_cotizacion`='{editar[5]}', `fecha_fin_cotizacion`='{editar[6]}', `nombre_cliente_cotizacion`='{editar[7]}', `direcion_cliente`='{editar[8]}', `correo_cliente`='{editar[9]}', `cuidad_cliente`='{editar[10]}', `contacto_cliente`='{editar[11]}' WHERE num_cotizacion='{editar[0]}'"
        self.cursor.execute(bsql)
        self.conexion.commit() """
    
    def editarCotizacion(self, editar):
        """ id_cotizacion, clienteCotizacion, documento_registro, nombre_operador, apellido_operador, fecha_inicio_cotizacion= editar, fecha_fin_cotizacion= editar, cliente_seleccionado, direcion_cliente, correo_cliente, cuidad_cliente, contacto_cliente = editar

        # Verificar valores y asignar valor predeterminado si es necesario
        fecha_inicio_cotizacion = fecha_inicio_cotizacion if fecha_inicio_cotizacion is not None else ''
        fecha_fin_cotizacion = fecha_fin_cotizacion if fecha_fin_cotizacion is not None else '' 
        clienteCotizacion = clienteCotizacion if clienteCotizacion is not None else ''
        direcion_cliente = direcion_cliente if direcion_cliente is not None else ''
        correo_cliente = correo_cliente if correo_cliente is not None else ''
        cuidad_cliente = cuidad_cliente if cuidad_cliente is not None else ''
        contacto_cliente = contacto_cliente if contacto_cliente is not None else '' """

        bsql = f"UPDATE `cotizaciones` SET `num_cotizacion`='{editar[0]}', `cliente_cotizacion`='{editar[1]}', `documento_operador`='{editar[2]}', `nombre_operador`='{editar[3]}', `apellido_operador`='{editar[4]}', `fecha_inicio_cotizacion`='{editar[5]}', `fecha_fin_cotizacion`='{editar[6]}', `nombre_cliente_cotizacion`='{editar[7]}', `direcion_cliente`='{editar[8]}', `correo_cliente`='{editar[9]}', `cuidad_cliente`='{editar[10]}', `contacto_cliente`='{editar[11]}' WHERE num_cotizacion='{editar[0]}'"
        print('datos ')
        
        try:
            self.cursor.execute(bsql)
            self.conexion.commit()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
        

    def eliminarCotizacion(self,id_cotizaciones):
        try:
            sql = F"UPDATE cotizaciones  SET estado = 'INACTIVO'  WHERE num_cotizacion='{id_cotizaciones}'"
            self.cursor.execute(sql)
            self.conexion.commit()
            
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            self.conexion.rollback()
        
        
    def crearDetalleCotizacion(self, registrar):
        try:
            bsql = "INSERT INTO `detallecotizaciones`(`num_cotizacion`, `producto_cotizacion`, `nombre_producto`, `cantidad_productos_cotizacion`, `valorunidad_prodcotizacion`, `valortotal_cantidaproductos_cotizacion`, `totalpagar_cotizacion`, `detalle_estado`) VALUES (%s, %s, %s, %s, %s, %s, %s, 'ACTIVO')"
            self.cursor.execute(bsql, tuple(registrar))
            self.conexion.commit()
            print("Datos insertados exitosamente.")
        except Exception as e:
            print(f"Error al insertar datos: {e}")

    def editarDetalleCotizaciones(self, editar):
        bsql = f"UPDATE `detallecotizaciones` SET `id_detalle_cotizacion`='{editar[0]}',  `producto_cotizacion`='{editar[1]}', `nombre_producto`='{editar[2]}', `cantidad_productos_cotizacion`='{editar[3]}', `valorunidad_prodcotizacion`='{editar[4]}', `valortotal_cantidaproductos_cotizacion`='{editar[5]}', `totalpagar_cotizacion`='{editar[6]}'  WHERE `id_detalle_cotizacion`='{editar[0]}'"
        print("Valores antes de la actualización en detallecotizaciones:", bsql)
        self.cursor.execute(bsql)
        self.conexion.commit()
        
        print("Valores antes de la actualización en cotizaciones:", editar[7], editar[8])
        # Actualizar los campos en la tabla cotizaciones
        sql2 = f"UPDATE `cotizaciones` SET `fecha_inicio_cotizacion`='{editar[7]}', `fecha_fin_cotizacion`='{editar[8]}' WHERE `num_cotizacion`='{editar[0]}'"
        self.cursor.execute(sql2)
        
        # Confirmar los cambios en la base de datos
        self.conexion.commit()

        
    def eliminarDetalleCotizacion(self,id_cotizaciones):
        try:
            sql = "UPDATE `detallecotizaciones` SET `detalle_estado` = 'INACTIVO' WHERE `id_detalle_cotizacion` = %s"
            self.cursor.execute(sql, (id_cotizaciones,))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            self.conexion.rollback()


cotizaciones = Cotizaciones(mysql, app)