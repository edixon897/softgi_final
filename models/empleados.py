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

    def eliminar(self,doc_empleado):
        sql = f"DELETE FROM `empleados` WHERE doc_empleado='{doc_empleado}'"
        self.cursor.execute(sql)
        self.conexion.commit()

Dempleados = Empleados(mysql, app)