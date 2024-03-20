from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
from models.empleados import Dempleados
from utils.tokens import generador_id

@app.route("/empleados")
def empleados():
    if "nom_empleado" in session: 
        rol_usuario = session["rol"]
        if rol_usuario == "administrador":

            sql = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado`, `fecha_nacimiento_empleado`, `contacto_empleado`, `email_empleado`, `direccion_empleado`, `ciudad_empleado`,  `rol`, `fechahora_registroempleado`, `nombre_operador`, `apellido_operador`, `estado` FROM `empleados` WHERE estado ='ACTIVO'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
            return render_template('empleados/muestra_empleados.html', resulta=resultado)

        else:
            return redirect("/inicio")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))

@app.route("/editar_empleado/<string:doc_empleado>")
def editar_empleado(doc_empleado):
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador":

            bsq = "SELECT doc_empleado, nom_empleado, ape_empleado, fecha_nacimiento_empleado, contacto_empleado, email_empleado, direccion_empleado, ciudad_empleado, rol FROM empleados  WHERE doc_empleado = %s"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq,(doc_empleado))
            resultado = cursor.fetchall()
            print("los resultados", resultado)
            conn.commit()
            return render_template("empleados/editar_empleados.html", resul=resultado[0])
        
        else:
            return redirect("/inicio")
    else:
        flash('Por favor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    
@app.route("/actualizar_Empleado", methods=['POST'])
def actualizar_Empleado():
    if "nom_empleado" in session:
            
        rol_usuario = session["rol"]
        if rol_usuario == "administrador":



            doc = session["nom_empleado"]
            bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq)
            resultado = cursor.fetchone()
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]

            if request.method == 'POST':
                print("contenido del formulario", request.form)

                try:
                    doc_empleado = request.form['doc_empleado']
                    nom_empleado = request.form['nom_empleado']
                    ape_empleado = request.form['ape_empleado']
                    fecha_nacimiento = request.form['fecha_nacimiento']
                    contacto_empleado = request.form['contacto_empleado']
                    email_empleado = request.form['email_empleado']
                    direccion_empleado = request.form['direccion_empleado']
                    ciudad_empleado = request.form['ciudad_empleado']
                    rol = request.form['rol']  
                    Dempleados.modificar([doc_empleado, nom_empleado, ape_empleado, fecha_nacimiento, contacto_empleado, email_empleado, direccion_empleado, ciudad_empleado, rol, documento_registro, nombre_operador, apellido_operador])

                    datos_modificar = [doc_empleado, nom_empleado,ape_empleado, fecha_nacimiento, contacto_empleado, email_empleado, direccion_empleado, ciudad_empleado, rol]
                    print("los datos", datos_modificar)
                    resultado_modificacion = Dempleados.modificar(datos_modificar)
                    print("los datos modificados", resultado_modificacion)
                    return redirect('/empleados')
                except KeyError as e:
                    print("Error Keyerror", e)
                    flash('Error al procesar el formulario')
                    return redirect(url_for('index'))
            return render_template('muestra_empleados.html')
        
        else:
            return redirect("/inicio")

    else:
        flash('Por favor, inicia sesion para poder acceder')
        return redirect(url_for('index'))
    
    
@app.route("/buscador_empleados", methods=['POST', 'GET'])
def buscador_empleados():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            busqueda = request.form['buscadorEmpleados']
            sql = "SELECT `doc_empleado`, `nom_empleado`, `ape_empleado`, DATE(`fecha_nacimiento_empleado`), `contacto_empleado`, `email_empleado`, `direccion_empleado`, `ciudad_empleado`,  `rol`, DATE(`fechahora_registroempleado`), `nombre_operador`, `apellido_operador`, `estado` FROM `empleados` WHERE (estado ='ACTIVO') AND (doc_empleado LIKE %s OR nom_empleado LIKE %s)"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, ('%' + busqueda + '%', '%' + busqueda + '%'))
            resultado = cursor.fetchall()
            conn.close()
            return jsonify(result=resultado)

        else:
            return redirect("/inicio")
    else:
        flash('Por favor inicia sesión para poder acceder')
        return redirect(url_for('index'))

    
@app.route('/borrarEmpleado/<doc_empleado>', methods=['POST'])
def borrarEmpleado(doc_empleado):
    if "nom_empleado" in session:
            
        rol_usuario = session["rol"]
        if rol_usuario == "administrador":
            
            Dempleados.eliminar(doc_empleado)
            return redirect('/empleados')
        
        else:
            return redirect("/inicio")
        
    else:
        flash('Por favor, inicia sesion para poder acceder')
        return redirect(url_for('index'))