""" import sys
from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.productos import Dproductos


@app.route()
def mostrar_modal_en_frontend(self, mensaje):
        # Envía la información al frontend (por ejemplo, usando sockets, API REST, etc.)
        # Aquí, puedes implementar la lógica para enviar la información al frontend.
        # Puedes usar algún mecanismo como WebSockets o Ajax.

        # Ejemplo usando Flask-SocketIO (debes instalarlo con pip install flask-socketio)
        from flask_socketio import SocketIO

        socketio = SocketIO(self.app)
        socketio.emit('mostrar_modal', {'mensaje': mensaje}, namespace='/test') """