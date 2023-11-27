import hashlib, datetime
import re
from models.registro import manejoUsuarios
from utils.tokens import token_registro
from service.envio_correo import enviar_correo_confirmacion
from conexiondb import *

@app.route('/registroUsario') 
def registroUsario(): 
    return render_template('registro/registro.html') 


@app.route('/registro', methods=['POST']) 
def registro_usuario(): 
    conn = mysql.connect() 
    cursor = conn.cursor() 
    doc_empleado = request.form['documento'] 
    nom_empleado = request.form['nombre']
    ape_empleado = request.form['apellido']#
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
            return redirect(url_for('home'))
        else: 
            mi_token2 = token_registro() 
            enviar_correo_confirmacion(nom_empleado, email_empleado, mi_token2)
            tiemporegistro = datetime.datetime.now()
            todoRegistro =[doc_empleado, nom_empleado, ape_empleado, fechaNacimiento, contactoEmpleado, email_empleado, direccion, ciudad, cifrada, rol, tiemporegistro]
            manejoUsuarios.registroUsuarios(todoRegistro)
            fecha_registro = datetime.datetime.now()
            tok = f"INSERT INTO tokens (doc_empleado, nom_empleado, email_empleado, token, confir_user, tiempo_registro) VALUES ('{doc_empleado}', '{nom_empleado}', '{email_empleado}','{mi_token2}', 'no confirmado', '{fecha_registro}' )" # Inserto o registro los datos en la base de datos en la tabla tokens
            cursor.execute(tok)
            conn.commit()
            conn.close()
            flash("Se envio un correo para confirmar tu registro, revisa la bandeja de entrada o spam")
            return render_template('login.html')
    else:
        flash('la contraseña no coincide')
        return redirect(url_for('/registro_usuario'))
