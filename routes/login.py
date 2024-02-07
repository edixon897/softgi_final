""" import hashlib
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
        bsql_emp = f"SELECT nom_empleado FROM empleados WHERE doc_empleado='{documento}' AND contrasena='{cifrado}' AND estado='ACTIVO'"
        cursor.execute(bsql_emp) 
        resultado = cursor.fetchone()
        if resultado is not None:
            session["nom_empleado"] = resultado[0]
            print(session)
            return redirect(url_for('inicio'))
        else:
            flash('Algo está mal en tus credenciales o tu correo no ha sido confirmado.', 'success')
            return redirect(url_for('index'))
    return  redirect(url_for('index'))


@app.route("/inicio")
def inicio():
    if "nom_empleado" in session:                                
        return render_template('inicio/home.html')    
    else:
        flash('Algo esta mal en sus datos digitados')
        return redirect(url_for('index')) """


import hashlib
from flask import Flask, request, render_template, session, flash, redirect, url_for
from conexiondb import conexion, mysql, app

# Definir roles permitidos
ROLES_PERMITIDOS = ['administrador', 'vendedor', 'almacenista']

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
        bsql_emp = f"SELECT nom_empleado, rol FROM empleados WHERE doc_empleado='{documento}' AND contrasena='{cifrado}' AND estado='ACTIVO'"
        cursor.execute(bsql_emp) 
        resultado = cursor.fetchone()
        if resultado is not None:
            # Verificar que el rol del usuario esté permitido
            rol = resultado[1]
            if rol in ROLES_PERMITIDOS:
                session["nom_empleado"] = resultado[0]
                session["rol"] = rol  # Asignar el rol a la sesión
                session["documento_operador"] = documento
                print("aca va la sesion",session)
                return redirect(url_for('inicio'))
            else:
                flash('No tienes permisos suficientes para acceder.', 'error')
        else:
            flash('Algo está mal en tus credenciales o tu correo no ha sido confirmado.', 'error')
    return  redirect(url_for('index'))

@app.route("/inicio")
def inicio():
    if "nom_empleado" in session:
        # Acceder al rol desde la sesión
        rol = session.get("rol", None)
        if rol == 'administrador':
            # Lógica para el administrador
            return render_template('inicio/home.html')
        elif rol == 'vendedor':
            # Lógica para el vendedor
            return render_template('inicio/home.html')
        elif rol == 'almacenista':
            # Lógica para el almacenista
            return render_template('inicio/home.html')
        else:
            flash('No tienes permisos suficientes para acceder.', 'error')
            return redirect(url_for('index'))
    else:
        flash('Algo está mal en tus credenciales o tu correo no ha sido confirmado.', 'error')
        return redirect(url_for('index'))
