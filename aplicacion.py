from conexiondb import *
from routes.login import index, login
from routes.registro import registroUsario, confirmar_correo
from routes.recuperaContra import solicitarCambio_contraseña, recuperar_contraseña
from routes.clientes import clientes
from routes.productos import Dproductos
from routes.ventas import Dventas
from routes.cotizaciones import cotizaciones

    



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5080")