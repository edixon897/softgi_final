from conexiondb import conexion, mysql, app

class Abonos:
    def __init__(self, DB, app):
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def abono_completo(self, contador):
                sql = f"UPDATE `ventas_credito` SET `credito_restante`='{0}', `estado`='PAGADO' WHERE contador = '{contador}'"
                self.cursor.execute(sql)
                self.conexion.commit()

    # actualiza credito restante
    def actualiza_credito_rest(self, info):
            sql = f"UPDATE `ventas_credito` SET `credito_restante`='{info[0]}' WHERE contador = '{info[1]}'"
            self.cursor.execute(sql)
            self.conexion.commit()

    # incerta el abono en el historial 
    def insert_historial_abn(self, info):
            sql = f"INSERT INTO `historial_credito`(`contador_ventacredito`, `abono`, `operador`, `fecha_abono`) VALUES ('{info[0]}','{info[1]}','{info[2]}','{info[3]}')"
            self.cursor.execute(sql)
            self.conexion.commit()

Dabonos = Abonos(mysql, app)