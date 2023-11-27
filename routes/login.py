import hashlib
from flask import Flask, request, render_template, session, flash, redirect, url_for
from conexiondb import conexion, mysql, app

@app.route('/') 
def index(): 
    return render_template('login/index.html') 

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        documento = request.form['cedula'] 
        password = request.form['contrasena']
        connt = mysql.connect()
        cursor = connt.cursor()
        cifrado = hashlib.sha512(password.encode('utf-8')).hexdigest()
        bsql_emp = f"SELECT * FROM empleados WHERE doc_empleado='{documento}' AND contrasena='{cifrado}' AND estado='activo'"
        cursor.execute(bsql_emp) 
        resultado = cursor.fetchone()
        if resultado is not None:
            session["doc_empleado"] = resultado[0]
            return render_template('inicio/home.html')
        else:
            flash('Algo está mal en tus credenciales o tu correo no ha sido confirmado.', 'success')
            return redirect(url_for('index'))
    return  redirect(url_for('index'))



