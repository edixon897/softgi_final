from conexiondb import conexion, mysql, app
class manejoUsuarios():
    def __init__(self, DB, app):  # Recibe mysql y app como parámetros
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()  # Usa el método connect() para crear la conexión
        self.cursor = self.conexion.cursor()
        
    def registrar(self, registro):
        bsq = f"INSERT INTO `empleados`( `nom_empleado`, `ape_empleado`, `doc_empleado`,`fecha_nacimiento_empleado`, `contacto_empleado`, `email_empleado`,  `ciudad_empleado`, `direccion_empleado`, `contrasena`, `rol`, `fechahora_registroempleado`, `estado`) VALUES ('{registro[0]}','{registro[1]}','{registro[2]}','{registro[3]}','{registro[4]}','{registro[5]}','{registro[6]}','{registro[7]}','{registro[8]}','{registro[9]}','{registro[10]}', 'ACTIVO')"
        self.cursor.execute(bsq)
        self.conexion.commit()

RegistroDeUsario = manejoUsuarios(mysql, app)