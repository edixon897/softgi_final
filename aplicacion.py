from conexiondb import *
from routes.login import index, login
from routes.registro import registroUsario, confirmar_correo
from routes.recuperaContra import solicitarCambio_contraseña, recuperar_contraseña
from routes.clientes import clientes
from routes.productos import productos
from routes.ventas import Dventas
from routes.cotizaciones import cotizaciones
from routes.proveedores import Dproveedores
from routes.abonos import Dabonos


    



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5080")