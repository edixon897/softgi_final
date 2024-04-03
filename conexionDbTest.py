from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from flask_socketio import SocketIO
from flaskext.mysql import MySQL
from flask_mail import Mail, Message
from email.mime.text import MIMEText
from email.message import EmailMessage


test = Flask(__name__)
mysql = MySQL()

test.secret_key = 'hfoy9ew87rwhdfs'

def conexion():
    try:
        test.config['MYSQL_DATABASE_SECRET_KEY'] = test.secret_key
        test.config['MYSQL_DATABASE_USER'] = 'root'
        test.config['MYSQL_DATABASE_PASSWORD'] = ''
        test.config['MYSQL_DATABASE_DB'] = 'db_test'
        test.config['MYSQL_DATABASE_HOST'] = 'localhost'
        test.config['MYSQL_DATABASE_PORT'] = 3306
        test.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
        print('Conexion con la base de datos es exitosa')
    except Exception as e:
                print(f"Error al conectar a la base de datos: {str(e)}")


conexion()
mysql.init_app(test)