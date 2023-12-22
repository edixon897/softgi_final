import sys
from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.proveedores import Dproveedores, Proveedores


@app.route('/proveedores')
def proveedores():
    if "nom_empleado" in session:
        sql = "SELECT * FROM proveedores WHERE estado_proveedor = 'ACTIVO'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return render_template('/proveedores/muestra_proveedores.html', resulta = resultado)
    else:
        flash('Por favor inicia sesion')
        return redirect(url_for('index'))


@app.route('/crearProveedores', methods=['POST'])
def crearProveedores():
    if "nom_empleado" in session:
        doc = session["nom_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE email_empleado='{doc}'"
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
        return redirect('/muestra_Proveedores')
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('home'))
    
    
#-----------------------------------------------------------mostrar proveedores---------------------------------------

@app.route('/muestra_Proveedores')
def muestra_Proveedores():
    if "nom_empleado" in session:
        sql = "SELECT * FROM `proveedores` WHERE estado_proveedor='ACTIVO'"           # consulta toda la info de proveedores.
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()   # no me toque el codigo niche pleace
        conn.commit()
        if (len(resultado) >= 1):
            return render_template("/provedor/muestra_proveedores.html", resul=resultado)   # si hay resultados se muestran.
        else:
            resultado2 = "No hay proveedores registrados"
            return render_template("/provedor/muestra_proveedores.html", resul2=resultado2)
    # sino se muestra el mensaje de resultado2.
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('home'))

@app.route('/buscarProvedores', methods=['POST', 'GET'])
def buscarProvedores():
    if request.method == 'POST':
        # Get the search term from the form
        buscar = request.form['buscarProvedor']

        # Query the database
        conn = mysql.connect()
        cursor = conn.cursor() 
        cursor.execute("SELECT * FROM proveedores WHERE estado_proveedor = %s AND nom_proveedor LIKE %s", ('ACTIVO', '%' + buscar + '%',))
        results = cursor.fetchall()
        cursor.close()

        return render_template('provedor/buscarProvedor.html', results=results)

    return render_template('provedor/buscarProvedor.html')