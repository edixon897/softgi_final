from conexiondb import conexion, mysql, app
import keyboard
import time

class Lector:
    def __init__(self, DB, app):
        self.mysql = DB
        self.app = app
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()


    # Agrega una función que obtenga el código de barras leído
    def read_barcode(self):
        barcode_data = ""               # Almacena temporalmente el código de barras leído
        last_key_time = time.time()     # Tiempo de la última tecla presionada

        while True:
            # Verifica si la tecla "ENTER" está presionada
            if keyboard.is_pressed("ENTER"):
                # Comprueba si hay datos en el código de barras antes de procesar
                if barcode_data:
                    return barcode_data  # Devuelve el código de barras
            else:
                # Lee el evento del teclado para detectar si se presiona una tecla
                event = keyboard.read_event(suppress=True)
                if event.event_type == keyboard.KEY_DOWN:
                    key = event.name
                    # Verifica si la tecla es alfanumérica o la tecla "BACKSPACE"
                    if key.isalnum() or key == "BACKSPACE":
                        # Maneja la tecla "BACKSPACE" o agrega la tecla al código de barras
                        if key == "BACKSPACE":
                            barcode_data = barcode_data[:-1]  # Elimina el último carácter
                        else:
                            barcode_data += key  # Agrega la tecla al código de barras
                            last_key_time = time.time()  # Actualiza el tiempo de la última tecla

            # Verifica si ha pasado un tiempo desde la última tecla para considerar la entrada completa
            if time.time() - last_key_time > 0.1 and barcode_data:
                return barcode_data  # Devuelve el código de barras

            # Introduce una pequeña pausa para evitar el bloqueo del bucle
            time.sleep(0.01)


Dlector = Lector(mysql, app)

