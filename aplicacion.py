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


    



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5080")