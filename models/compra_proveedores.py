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
        num_compra = datos_compra[0]
        detalles_productos = datos_compra[1]

        for i in range(len(detalles_productos['producto_compra[]'])):
            producto_nombre = detalles_productos['producto_compra'][i]
            cantidad = detalles_productos['cantidad_compra'][i]
            valor_unidad = detalles_productos['valor_unidad'][i]
            total = int(cantidad) * int(valor_unidad)

            sql = "INSERT INTO detallecomprasproveedores (detallenum_compra, producto_compra, cantidad_producto_compra, valorunidad_prodcompra, valortotal_cantidadcomp) VALUES (%s, %s, %s, %s, %s)"
            valores_producto = (num_compra, producto_nombre, cantidad, valor_unidad, total)

            self.cursor.execute(sql, valores_producto)
            print("Datos a detallecomprasproveedores:", valores_producto)

        self.conexion.commit()
        return True


    def cacela_compra(self,num_compra):
        sql = f"UPDATE comprasproveedores SET estado = 'CANCELADO' WHERE num_compra = '{num_compra}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def edita_detalles_compra(self,datos_compra):
        sql = f"UPDATE detallecomprasproveedores SET num_compra='{datos_compra[0]}' ,producto_compra='{datos_compra[1]}', cantidad_producto_compra='{datos_compra[2]}', valorunidad_prodcompra='{datos_compra[3]}',valortotal_cantidadcomp='{datos_compra[4]}'"
        self.cursor.execute(sql)
        self.conexion.commit()

Dcompra_proveedores = Compras_proved(mysql, app)