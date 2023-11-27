from conexiondb import *


def enviar_correo_confirmacion(nombre, email, token):
    confirm_url = url_for('confirmar_correo', token=token, email=email, _external=True)
    render_html = render_template('correoMsj.html', nombre=nombre, correo_url=confirm_url)
    msg = Message('Confirmación de correo electrónico', sender='jenasoft05@gmail.com', recipients=[email]) 
    msg.html =  render_html 
    mail.send(msg)