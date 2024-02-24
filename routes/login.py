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
        bsql_emp = f"SELECT nom_empleado FROM empleados WHERE doc_empleado='{documento}' AND contrasena='{cifrado}' AND estado='ACTIVO'"
        cursor.execute(bsql_emp) 
        resultado = cursor.fetchone()
        if resultado is not None:
            session["nom_empleado"] = resultado[0]
            session["documento_operador"] = documento

            sql = f"SELECT `rol` FROM `empleados` WHERE doc_empleado = '{documento}'"
            conn = mysql.connect()                    
            cursor = conn.cursor()
            cursor.execute(sql)                                          
            rol_usuario = cursor.fetchall()
            conn.commit()
            session["rol"] = rol_usuario[0][0]
            print(rol_usuario[0][0])
            print(session)
            
            return redirect(url_for('inicio'))
        else:
            flash('Algo está mal en tus credenciales o tu correo no ha sido confirmado.', 'success')
            return redirect(url_for('index'))
    return  redirect(url_for('index'))


@app.route("/inicio")
def inicio():
    if "nom_empleado" in session:    
        rol_usuario = session["rol"]                            
        return render_template('inicio/home.html', rol=rol_usuario)    
    else:
        flash('Algo esta mal en sus datos digitados')
        return redirect(url_for('index'))


