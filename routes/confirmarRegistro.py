from flask import Flask, request, render_template, session, flash, redirect, url_for
from conexiondb import conexion, mysql, app

@app.route('/confirmar_correo/<token>', methods=['GET', 'POST'])
def confirmar_correo(token): 
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT doc_empleado, nom_empleado, email_empleado, confir_user FROM tokens WHERE token = %s", (token,))  
    usuario_data = cursor.fetchone() 
    if not usuario_data:  
            flash('El token de confirmación no es válido.', 'danger') 
            return redirect(url_for('routes/index')) 

    email = usuario_data[2] 
    correo_confirmado = usuario_data[3] 

    if correo_confirmado == 'confirmado':
        flash('El correo ya ha sido validado.', 'danger')#
        return redirect(url_for('routes/index'))
    
    if request.method == 'POST': 
        confi= request.form['confir'] 
        cursor.execute(f"UPDATE tokens SET confir_user = '{confi}' WHERE email_empleado = '{email}'") 
        mysql.get_db().commit()
        flash('Tu correo ha sido confirmado correctamente.', 'success')
        return redirect(url_for('routes/index'))
    
    return render_template('envioEmail/confirmaCuenta.html')
