import hashlib
from conexiondb import *

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
        bsql_emp = f"SELECT * FROM empleados WHERE doc_empleado='{documento}' AND estado='activo'"
        cursor.execute(bsql_emp) 
        resultado = cursor.fetchone()
        if resultado is not None:
            session["doc_empleado"] = resultado[0]
            return render_template('registro/registro.html')
        else:
            flash('Algo está mal en tus credenciales o tu correo no ha sido confirmado.', 'success')
            return redirect(url_for('index'))
    return  redirect(url_for('index'))



