from flask import Flask, request, render_template, flash, redirect, url_for
from conexiondb import conexion, mysql, app
import hashlib, datetime
import re
from models.registro import RegistroDeUsario
from utils.tokens import token_registro
from service.envio_correo import enviar_correo_confirmacion


@app.route('/registroUsario') 
def registroUsario(): 
    return render_template('registro/registro.html') 

@app.route('/registro', methods=['POST']) 
def registro_usuario(): 
    conn = mysql.connect() 
    cursor = conn.cursor() 
    doc_empleado = request.form['documento'] 
    nom_empleado = request.form['nombre']
    ape_empleado = request.form['apellido']
    direccion = request.form['direccion']
    contactoEmpleado = request.form['contactoEmpleado']
    ciudad = request.form['ciudad']
    fechaNacimiento = request.form['fechaNacimiento']
    email_empleado = request.form['correo']
    rol = request.form['rol']
    if not re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email_empleado):
        return render_template('/registro_usuario.html', flash="Correo electrónico inválido. Intente nuevamente.") 
    clave1 = request.form['contrasena'] 
    clave2 = request.form['confirmada']
    if clave1 == clave2: 
        cifrada = hashlib.sha512(clave1.encode("utf-8")).hexdigest()
        consul = f"SELECT * FROM empleados WHERE doc_empleado='{doc_empleado}' OR email_empleado='{email_empleado}'"
        cursor.execute(consul)
        resultado_1 = cursor.fetchone() 
        if resultado_1 is not None: 
            flash('Este usuario ya ha sido registrado')
            return redirect(url_for('index'))
        else: 
            mi_token2 = token_registro() 
            enviar_correo_confirmacion(nom_empleado, email_empleado, mi_token2)
            tiemporegistro = datetime.datetime.now()
            RegistroDeUsario.registrar([doc_empleado, nom_empleado, ape_empleado, fechaNacimiento, contactoEmpleado, email_empleado, direccion, ciudad, cifrada, rol, tiemporegistro])
            fecha_registro = datetime.datetime.now()
            tok = f"INSERT INTO tokens (doc_empleado, nom_empleado, email_empleado, token, confir_user, tiempo_registro) VALUES ('{doc_empleado}', '{nom_empleado}', '{email_empleado}','{mi_token2}', 'no confirmado', '{fecha_registro}' )" # Inserto o registro los datos en la base de datos en la tabla tokens
            cursor.execute(tok)
            conn.commit()
            conn.close()
            flash("Se envio un correo para confirmar tu registro, revisa la bandeja de entrada o spam")
            return redirect(url_for('index'))
    else:
        flash('la contraseña no coincide')
        return redirect(url_for('/registro_usuario'))

@app.route('/confirmar_correo/<token>', methods=['GET', 'POST'])
def confirmar_correo(token):
    if request.method == 'POST':
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT doc_empleado, nom_empleado, email_empleado, confir_user FROM tokens WHERE token = %s", (token,)) #ejecuto la consulta 
        usuario_data = cursor.fetchone() 
        if not usuario_data: 
                flash('El token de confirmación no es válido.', 'danger') 
                return redirect(url_for('index')) 

        email = usuario_data[2] 
        correo_confirmado = usuario_data[3]

        if correo_confirmado == 'confirmado':
            flash('El correo ya ha sido validado.', 'danger')
            return redirect(url_for('index'))
        if request.method == 'POST': 
            confi= request.form['confir'] 
            cursor.execute(f"UPDATE tokens SET confir_user = '{confi}' WHERE email_empleado = '{email}'") 
            mysql.get_db().commit()
            flash('Tu correo ha sido confirmado correctamente.', 'success')
            return redirect(url_for('index'))
        
    return render_template('registro/confirmaCuenta.html')

