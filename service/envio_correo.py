from conexiondb import servicion, mail, conexion
from flask import Flask, render_template, url_for
from flask_mail import  Message
from utils.recuContra import User



def enviar_correo_confirmacion(nombre, email, token):
    confirm_url = url_for('confirmar_correo', token=token, email=email, _external=True)
    render_html = render_template('envioEmail/registro.html', nombre=nombre, correo_url=confirm_url)
    msg = Message('Confirmación de correo electrónico', sender='jenasoft05@gmail.com', recipients=[email]) 
    msg.html =  render_html 
    mail.send(msg)
    
def envio_correo(user, token_rctsn):
    token_url = url_for('recuperar_contraseña', token_rctsn=token_rctsn, user=user, _external=True)
    print(token_url)
    rendered_html = render_template('envioEmail/restablecerEmail.html', user=user, token_url=token_url)
    msg = Message('Recuperación de contraseña', sender='jenasoft05@gmail.com', recipients=[user.email])
    msg.html = rendered_html
    mail.send(msg)