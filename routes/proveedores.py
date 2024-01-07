import sys
from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.proveedores import Dproveedores, Proveedores


@app.route('/proveedores')
def proveedores():
    if "nom_empleado" in session:
        sql = "SELECT `doc_proveedor`, `nom_proveedor`, `contacto_proveedor`, `email_proveedor`, `direccion_proveedor` FROM `proveedores` WHERE estado_proveedor = 'ACTIVO'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return render_template('/proveedores/muestra_Proveedores.html', resul = resultado)
    else:
        flash('Por favor inicia sesion')
        return redirect(url_for('index'))


@app.route('/crearProveedores', methods=['POST', 'GET'])
def crear_Proveedores():
    if "nom_empleado" in session:
        if request.method == 'POST':
            doc = session["nom_empleado"]
            bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
            print(bsq)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq)
            resultado = cursor.fetchone()
            print(resultado)
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]
            documento = request.form['documentoProveedor']
            nombre = request.form['nombreProveedor']
            numero = request.form['numeroProveedores']
            correo = request.form['correoProveedores']
            direcion = request.form['direccionProveedores']
            ciudad = request.form['ciudadProveedor']
            tiempo = datetime.datetime.now()

            Dproveedores.crear([documento,nombre,numero,correo,direcion,ciudad, tiempo, documento_registro, nombre_operador, apellido_operador])
            return redirect('/proveedores')
        else:
            return render_template('proveedores/crear_proveedores.html')
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('home'))
    
    
@app.route('/actializarProveedor/<proveedor>', methods=['POST', 'GET'])
def actializar_Proveedor(proveedor):
    if "nom_empleado" in session:
        sql= f"SELECT `doc_proveedor`, `nom_proveedor`, `contacto_proveedor`, `email_proveedor`, `direccion_proveedor`, `ciudad_proveedor` FROM `proveedores` WHERE doc_proveedor = '{proveedor}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchone()
        return render_template('proveedores/actualizar_proveedores.html', resul = resultado)

@app.route('/actializarProveed', methods=['POST', 'GET'])
def actializar_Proveed():
    if "nom_empleado" in session:
        doc = session["nom_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsq)
        resultado = cursor.fetchone()
        print(resultado)
        documento_registro = resultado[0]
        nombre_operador = resultado[1]
        apellido_operador = resultado[2]
        documento = request.form['documentoProveedor']
        nombre = request.form['nombreProveedor']
        numero = request.form['numeroProveedores']
        correo = request.form['correoProveedores']
        direcion = request.form['direccionProveedores']
        ciudad = request.form['ciudadProveedor']
        Dproveedores.modificar([documento,nombre,numero,correo,direcion,ciudad, documento_registro, nombre_operador, apellido_operador])
        return redirect('/proveedores')




@app.route('/borraProveedor/<documento>')
def borrarProveedor(documento):
    if "nom_empleado" in session:
        Dproveedores.borrar(documento)                 
        return redirect("/proveedores")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
