from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from flask_socketio import SocketIO
from flaskext.mysql import MySQL
from flask_mail import Mail, Message
from email.mime.text import MIMEText
from email.message import EmailMessage


app = Flask(__name__)
mysql = MySQL()

app.secret_key = 'hfoy9ew87rwhdfsjerwojoafodsheurow843742rhw7298r3285962942tr8bds8834hwe683hiws73i2hi3r64eugsa8742k2'
def conexion():
    try:
        app.config['MYSQL_DATABASE_SECRET_KEY'] = app.secret_key
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = ''
        app.config['MYSQL_DATABASE_DB'] = 'softgi'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        app.config['MYSQL_DATABASE_PORT'] = 3306
        app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
    except Exception as e:
                print(f"Error al conectar a la base de datos: {str(e)}")

def servicion():
    try:                
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
        app.config['MAIL_PORT'] = 587  
        app.config['MAIL_USE_TLS'] = True 
        app.config['MAIL_USERNAME'] = 'jenasoft05@gmail.com'  
        app.config['MAIL_PASSWORD'] = 'moex wipe qghd ixuw' 
    except Exception as e:
                print(f"Error al intentar conectarse al servicio de envio de correo: {str(e)}")



servicion()
mail = Mail(app)
conexion()
mysql.init_app(app)