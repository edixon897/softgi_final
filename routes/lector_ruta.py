from flask import Flask, request, render_template, flash, redirect, url_for, session, jsonify
from conexiondb import conexion, mysql, app
from models.lector_model import Lector, read_barcode

# Define una variable global para almacenar el código de barras
codigo_barras_global = None

# Define una ruta para la página principal que renderiza el formulario HTML
@app.route('/')
def formulario():
    return render_template('formulario.html', codigo_barras=codigo_barras_global)

# Define una ruta para la acción de guardar código, se activa al enviar el formulario
@app.route('/guardar_codigo', methods=['POST'])
def guardar_codigo():
    global codigo_barras_global
    if request.method == 'POST':
        # Obtén los valores de los campos del formulario
        ref_produ_1 = request.form.get('ref_produ_1')
        # Aquí, puedes agregar lógica para obtener otros campos del formulario

        # Verifica si el campo ref_produ_1 ya está lleno y no hay código de barras global
        if ref_produ_1 and not codigo_barras_global:
            # Llama a la función para leer el código de barras
            codigo_barras_global = read_barcode()

        return render_template('formulario.html', codigo_barras=codigo_barras_global)
