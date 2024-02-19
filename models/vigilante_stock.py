
from flask_socketio import SocketIO
from conexiondb import conexion, mysql, app
import time

class Vigilante:
    def __init__(self, DB, app, socketio):
        self.mysq = DB
        self.app = app
        self.socketio = socketio
        self.conexion = self.mysq.connect()
        self.cursor = self.conexion.cursor()

    def verificar_stock(self):
        while True:
            try:
                # Consulta para obtener productos con bajo stock
                sql = "SELECT id_producto, ref_produ_1, cantidad_producto, stockminimo FROM productos WHERE cantidad_producto <= stockminimo"
                self.cursor.execute(sql)
                productos_bajo_stock = self.cursor.fetchall()

                # Verificar y enviar alertas
                for producto in productos_bajo_stock:
                    mensaje = f"¡Alerta! El producto '{producto[1]}' está cerca del stock mínimo."
                    self.mostrar_modal_en_frontend(mensaje)
                    print("Mensaje de alerta mostrado:", mensaje)

                # Esperar un intervalo de tiempo antes de volver a verificar
                time.sleep(60)  # Verificar cada minuto (60 segundos)

            except mysql.connector.Error as e:
                print(f"Error en la consulta SQL: {e}")

            except mysql.connector.DatabaseError as e:
                print(f"Error de base de datos: {e}")

            except Exception as e:
                print(f"Excepción en la función verificar_stock: {e}")
                print(f"Excepción no manejada: {e}")

    def mostrar_modal_en_frontend(self, mensaje):
        # Envía la información al frontend utilizando la instancia de SocketIO
        self.socketio.emit('mostrar_modal', {'mensaje': mensaje}, namespace='/test')


