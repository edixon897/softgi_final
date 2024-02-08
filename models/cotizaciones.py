from conexiondb import conexion, mysql, app

class Cotizaciones:
    def __init__(self, DB, app): 
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()  
        self.cursor = self.conexion.cursor()
        
        
    def crearCotizaciones(self, registro):           
        sql = f"INSERT INTO `cotizaciones`(`num_cotizacion`, `cliente_cotizacion`, `documento_operador`, `nombre_operador`, `apellido_operador`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_cliente_cotizacion`, `estado`) VALUES ('{registro[0]}','{registro[1]}','{registro[2]}','{registro[3]}','{registro[4]}','{registro[5]}','{registro[6]}', '{registro[7]}', 'ACTIVO')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
        
        
    def editarCotizacion(self,editar):
        bsql = f"UPDATE `cotizaciones` SET num_cotizacion='{editar[0]}', documento_operador='{editar[1]}', documento_operador='{editar[2]}', nombre_operador='{editar[3]}', apellido_operador='{editar[4]}', fecha_inicio_cotizacion='{editar[5]}', fecha_fin_cotizacion='{editar[6]}', nombre_cliente_cotizacion='{editar[7]}' WHERE num_cotizacion='{editar[0]}'"
        self.cursor.execute(bsql)
        self.conexion.commit()
        

    def eliminarCotizacion(self,id_cotizaciones):
        try:
            sql = F"UPDATE cotizaciones  SET cotizaciones.estado = 'INACTIVO'  WHERE cotizaciones.num_cotizacion='{id_cotizaciones}'"
            self.cursor.execute(sql)
            self.conexion.commit()
            
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            self.conexion.rollback()
        
        

    def crearDetalleCotizacion(self, registrar):
        bsql = f"INSERT INTO `detallecotizaciones`(`num_cotizacion`, `producto_cotizacion`, `nombre_producto`, `cantidad_productos_cotizacion`, `valorunidad_prodcotizacion`, `valortotal_cantidaproductos_cotizacion`, `detalle_estado`) VALUES ('{registrar[0]}','{registrar[1]}','{registrar[2]}','{registrar[3]}','{registrar[4]}','{registrar[5]}', 'ACTIVO')"
        self.cursor.execute(bsql)
        self.conexion.commit()
    
    def editarDetalleCotizaciones(self, editar):
        bsql =f"UPDATE `detallecotizaciones` SET `id_detalle_cotizacion`='{editar[0]}',`num_cotizacion`='{editar[1]}',`producto_cotizacion`='{editar[2]}',`cantidad_productos_cotizacion`='{editar[3]}',`valorunidad_prodcotizacion`='{editar[4]}',`valortotal_cantidaproductos_cotizacion`='{editar[5]}' WHERE `id_detalle_cotizacion`='{editar[0]}'"
        self.cursor.execute(bsql)
        self.conexion.commit()
        
    def eliminarDetalleCotizacion(self,id_cotizaciones):
        try:
            sql = "UPDATE `detalledevoluciones` SET `estado` = 'INACTIVO' WHERE `num_cotizacion` = %s"
            self.cursor.execute(sql, (id_cotizaciones,))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            self.conexion.rollback()


cotizaciones = Cotizaciones(mysql, app)