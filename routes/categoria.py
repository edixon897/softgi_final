import datetime
from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
from models.categoria import categoria

@app.route("/categorias")
def categorias():
    if "nom_empleado" in session:
        sql = "SELECT `id_categoria`, `nom_categoria` FROM categorias WHERE estado_categorias ='ACTIVO'"
        conn = mysql.connect()                    
        cursor = conn.cursor()
        cursor.execute(sql)                                          
        resultado = cursor.fetchall()
        return render_template('categoria/categoria.html', resulta=resultado)
    else:
        flash('Algo esta mal en sus datos digitados')
        return redirect(url_for('index'))

@app.route("/crearCategoria")
def crearCategoria(): 
    if "nom_empleado" in session:                                   
        return render_template('categoria/registrar.html')       
    else:
            flash('Algo esta mal en sus datos digitados')
            return redirect(url_for('index'))
        

@app.route("/registrar_categorias", methods=['POST'])
def registrar_categorias():
    if "nom_empleado" in session:
        nom = session["nom_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{nom}'"
        print(bsq)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsq)
        resultado = cursor.fetchone()
        print(resultado)
        documento_registro = resultado[0]
        nombre_operador = resultado[1]
        apellido_operador = resultado[2]
        nombre_categoria = request.form['nom_categoria']
        tiempo = datetime.datetime.now()

        categoria.crear_categoria([nombre_categoria, tiempo, documento_registro, nombre_operador, apellido_operador])
        return redirect('categorias')
    else:
        flash('Algo esta mal en sus datos digitados')
        return redirect(url_for('index'))

    

@app.route("/editarCategorias/<id_categoria>")  
def editarctegorias(id_categoria):
    if "nom_empleado" in session:
        idcategoria = id_categoria
        sql = f"SELECT * FROM categorias WHERE id_categoria = '{idcategoria}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()          
        return render_template("/categoria/editar.html", resul = resultado[0])
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
    


@app.route("/editar_categoria", methods=['POST', 'GET'])
def editacategoria():
    if "nom_empleado" in session:
        idcategoria = request.form['id_categoria']
        nombre_categoria = request.form['nom_categoria']
        categoria.modificar_categoria([idcategoria, nombre_categoria])
        return redirect('/categorias')
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
    


@app.route('/borracategoria/<id_categoria>')
def borracategoria(id_categoria):
    if "nom_empleado" in session:
        categoria.borrar_categoria (id_categoria)                      
        return redirect('/categorias')
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))


