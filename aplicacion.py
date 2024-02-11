from conexiondb import *
from routes.login import index, login
from routes.registro import registroUsario, confirmar_correo
from routes.recuperaContra import solicitarCambio_contraseña, recuperar_contraseña
from routes.clientes import clientes
from routes.productos import muestra_Productos
from routes.ventas import muestra_ventas
from routes.cotizaciones import Cotizacion
from routes.proveedores import proveedores
from routes.abonos import Dabonos
from routes.categoria import categorias
from routes.compra_proveedores import muestra_compra_proved
from routes.devoluciones import muestraDevoluciones
from routes.empleados import empleados
from models.lector_model import Lector
from models.vigilante_stock import Vigilante
 



if __name__ == '__main__':
    checker = Vigilante(mysql, app, socketio)
    socketio.start_background_task(target=checker.verificar_stock)
    socketio.run(app, host='0.0.0.0', debug=True, port="5080")
