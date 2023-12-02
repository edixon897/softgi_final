from conexiondb import *
from routes.login import index, login
from routes.registro import registroUsario, confirmar_correo
from routes.recuperaContra import solicitarCambio_contraseña, recuperar_contraseña
from routes.clientes import clientes
from routes.ventas import muestra_ventas
from routes.productos import muestra_Productos

    



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5080")