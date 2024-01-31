from conexiondb import conexion, mysql, app

class Empleados:
    def __init__(self, DB, app):  
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()  
        self.cursor = self.conexion.cursor()

    def modificar(self,empleados):
        sql = f"UPDATE empleados SET doc_empleado='{empleados[0]}', nom_empleado='{empleados[1]}', ape_empleado='{empleados[2]}', fecha_nacimiento_empleado='{empleados[3]}',`contacto_empleado`='{empleados[4]}',`email_empleado`='{empleados[5]}', direccion_empleado='{empleados[6]}',`ciudad_empleado`='{empleados[7]}', rol='{empleados[8]}' WHERE doc_empleado='{empleados[0]}' "
        self.cursor.execute(sql)
        self.conexion.commit()

    def emp_existe_en_db(self, empleado):
            sql = f"SELECT COUNT(*) FROM empleados WHERE doc_cliente = '{empleado}'"

            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()

            if resultado[0] > 0:
                return True
            else:
                return False
        
    def eliminar(self,doc_empleado):
        
        sql = f"UPDATE empleados SET estado = 'INACTIVO' WHERE doc_empleado ='{doc_empleado}'"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            return True
        except Exception as e:
             print(f"Error al borrar empelado: {str(e)}")
             self.conexion.rollback()
             return False

Dempleados = Empleados(mysql, app)