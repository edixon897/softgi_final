import datetime
import hashlib
from flask import Flask, request, render_template, session, flash, redirect, url_for
from conexiondb import conexion, mysql, app
from utils.recuContra import User, PasswordResetToken
from service.envio_correo import envio_correo
from utils.tokens import token_recuperar_contrasena




@app.route('/solicitarCambio_contraseña', methods=['GET', 'POST'])
def solicitarCambio_contraseña():
    if request.method == 'POST':
        email = request.form.get('email')
        cursor = mysql.get_db().cursor()
        msql = f"SELECT * FROM empleados  WHERE email_empleado  = '{email}'"
        cursor.execute(msql)
        usuario_data = cursor.fetchone()
        if usuario_data:
            usuario = User(id=usuario_data[0], email=usuario_data[5], nombre=usuario_data[1])
            cursor = mysql.get_db().cursor()
            # Verificar si hay registros en la tabla recuperarcontrasena para ese correo electrónico
            cursor.execute("SELECT * FROM recuperarcontrasena WHERE email_usuario = %s", (usuario.email,))
            existing_token = cursor.fetchone()
            token_recuperar = token_recuperar_contrasena()  #Token que se genera para cambio de contraseña
            # Si no existe un token para ese correo, crea uno nuevo
            expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=3)
            cursor.execute("INSERT INTO recuperarcontrasena (email_usuario, fechahora_solicitud, fechahora_termina, codigo, usuario,utilizado) VALUES (%s, %s, %s, %s, %s,%s)",
                            (usuario.email, datetime.datetime.now(), expiration_time, token_recuperar, usuario.id,'no')) 
            mysql.get_db().commit()
            envio_correo(usuario, token_recuperar)
            print(usuario, token_recuperar)
            flash('Se ha enviado un correo electrónico con instrucciones para restablecer la contraseña.', 'success')
            return redirect(url_for('index'))
        else:
            flash('No se encontró ninguna cuenta con ese correo electrónico.', 'danger')
    return render_template('envioEmail/recuperarContra.html')


@app.route('/recuperar_contraseña/<token_rctsn>', methods=['GET', 'POST'])
def recuperar_contraseña(token_rctsn):
    if request.method == 'POST':
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT  fechahora_termina, codigo, usuario FROM recuperarcontrasena WHERE codigo  = %s", (token_rctsn,))
        datos_db = cursor.fetchone()

        if not datos_db:
            flash('El token de confirmación no es válido.', 'danger')
            return redirect(url_for('solicitarCambio_contraseña'))
        
        usuario = datos_db[2]
        codigo = datos_db[1]
        expiration_time = datos_db[0]  
        current_time = datetime.datetime.now()
        if current_time > expiration_time:
            # El token ha caducado, mostrar un mensaje de error
            flash('El enlace de restablecimiento de contraseña ha caducado.', 'danger')
            return redirect(url_for('solicitarCambio_contraseña'))

        if request.method == 'POST':
            password = request.form.get('password')
            cifrado = hashlib.sha512(password.encode('utf-8')).hexdigest()
            cursor.execute("UPDATE empleados SET contrasena  = %s WHERE doc_empleado = %s", (cifrado, usuario))
            cursor.execute("UPDATE recuperarcontrasena SET utilizado='si' WHERE codigo = %s", (codigo))
            mysql.get_db().commit()
            flash('Tu contraseña ha sido restablecida.', 'success')
            return redirect(url_for('index'))
    return render_template('envioEmail/restablecerContra.html')

