import json
from conexiondb import conexion, mysql, app

class Compras_proved:
    def __init__(self, DB, app):  
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()  
        self.cursor = self.conexion.cursor()

    def registrar_compra(self,datos_compra):
        sql = f"INSERT INTO `comprasproveedores`( `proveedor_compra`, `fecha_compra`, `documento_operador`, `nombre_operador`, `apellido_operador`, `tiempo_registro`, `num_factura_proveedor`,`codigo_tabla`,  `estado`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (datos_compra[0], datos_compra[1], datos_compra[2], datos_compra[3], datos_compra[4], datos_compra[5], datos_compra[6], datos_compra[7], 'ACTIVO')
        self.cursor.execute(sql, valores)
        print("los datos a comprasproveedores", valores)
        self.conexion.commit()
    
    def registrar_detalles_compra(self, datos_compra):
        sql = "INSERT INTO detallecomprasproveedores (detallenum_compra, producto_compra, cantidad_producto_compra, valorunidad_prodcompra, valortotal_cantidadcomp) VALUES (%s, %s, %s, %s, %s)"
        valores_producto = (datos_compra[0], datos_compra[1], datos_compra[2], datos_compra[3], datos_compra[4])
        self.cursor.execute(sql, valores_producto)
        print("Datos a detallecomprasproveedores:", valores_producto)
        self.conexion.commit()


    def cacela_compra(self,num_compra):
        sql = f"UPDATE comprasproveedores SET estado = 'CANCELADO' WHERE num_compra = '{num_compra}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def edita_detalles_compra(self, datos_compra):
        num_compra, detallenum_compra, producto_compra, cantidad_compra, valorunidad_prodcompra, valor_total_unidad, fecha_compra, num_factura_proveedor = datos_compra
        sql = (
            f"UPDATE detallecomprasproveedores "
            f"SET producto_compra='{producto_compra}', "
            f"cantidad_producto_compra='{cantidad_compra}', "
            f"valorunidad_prodcompra='{valorunidad_prodcompra}', "
            f"valortotal_cantidadcomp='{valor_total_unidad}' "
            f"WHERE detallenum_compra='{detallenum_compra}'"
        )
        self.cursor.execute(sql)
        self.conexion.commit()

        sql_compra = (
            "UPDATE comprasproveedores "
            "SET fecha_compra = %s, "
            "num_factura_proveedor = %s "
            "WHERE num_compra = %s"
        )
        valores_compra = (fecha_compra, num_factura_proveedor, num_compra)
        self.cursor.execute(sql_compra, valores_compra)
        self.conexion.commit()



Dcompra_proveedores = Compras_proved(mysql, app)