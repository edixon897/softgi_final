from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.clientes import Dclientes


@app.route("/clientes")
def clientes():
    if "nom_empleado" in session: 
            
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":

            sql = "SELECT * FROM clientes WHERE estado_cliente ='ACTIVO'"
            conn = mysql.connect()                    
            cursor = conn.cursor()
            cursor.execute(sql)                                          
            resultado = cursor.fetchall()
            return render_template('clientes/clientes.html', resulta=resultado)


        else:
            return redirect("/inicio")
        
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))

@app.route("/crearClientes")
def crearClientes():
    if "nom_empleado" in session:      

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":

            return render_template('clientes/registrar.html')

        else:
            return redirect("/inicio")

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    
@app.route("/crear_cliente", methods=['POST'])
def crear_cliente():
    if "nom_empleado" in session:

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":


            doc = session["nom_empleado"]
            bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq)
            resultado = cursor.fetchone()
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]
            doc_cliente = request.form['doc_cliente']
            nom_cliente = request.form['nom_cliente']
            ape_cliente = request.form['ape_cliente']
            fecha_nacimiento_cliente = request.form['fecha_nacimiento_cliente']
            contacto_cliente = request.form['contacto_cliente']
            email_cliente = request.form['email_cliente']
            direccion_cliente = request.form['direccion_cliente']
            ciudad_cliente = request.form['ciudad_cliente']
            tipo_persona = request.form['tipopersona']                 
            tiempo = datetime.datetime.now()
            if not Dclientes.buscar_cliente(doc_cliente):
                Dclientes.crear_cliente([doc_cliente, nom_cliente, ape_cliente, fecha_nacimiento_cliente, contacto_cliente, email_cliente, direccion_cliente, ciudad_cliente, tipo_persona, tiempo, documento_registro, nombre_operador, apellido_operador])
                return redirect('/clientes')
            else:
                """ mensaje="Cliente ya existe"
                cliente =[doc_cliente, nom_cliente, ape_cliente, contacto_cliente, email_cliente, direccion_cliente, ciudad_cliente, tipo_persona]
                return render_template('clientes/clientes.html', mensaje=mensaje, cliente=cliente) """
                mensaje = 1
                return render_template('clientes/registrar.html', mensaje=mensaje)


        else:
            return redirect("/inicio")
        
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    

@app.route("/editarClientes/<documento>")
def edit_cliente(documento):
    if "nom_empleado" in session:

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":

            sql = f"SELECT * FROM clientes WHERE doc_cliente = '{documento}'"
            conn = mysql.connect()
            cursor = conn.cursor()                                    
            cursor.execute(sql)
            resultado = cursor.fetchall()
            conn.commit()
            return render_template("clientes/editar.html", resul=resultado[0])
        else:
            return redirect("/inicio")
        
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))

@app.route("/Actualizar_clie", methods=['POST','GET'])
def Actualizar_clie():
    if "nom_empleado" in session:
        
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":


            doc = session["nom_empleado"]
            bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq)
            resultado = cursor.fetchone()
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]
            doc_cliente = request.form['doc_cliente']
            nom_cliente = request.form['nom_cliente']
            ape_cliente = request.form['ape_cliente']
            fecha_nacimiento_cliente = request.form['fecha_nacimiento_cliente']
            contacto_cliente = request.form['contacto_cliente']
            email_cliente = request.form['email_cliente']
            direccion_cliente = request.form['direccion_cliente']
            ciudad_cliente = request.form['ciudad_cliente']
            tipo_persona = request.form['tipo_persona']  
            Dclientes.modificar_cliente([doc_cliente, nom_cliente, ape_cliente, fecha_nacimiento_cliente, contacto_cliente, email_cliente, direccion_cliente, ciudad_cliente, tipo_persona, documento_registro, nombre_operador, apellido_operador])
            return redirect('/clientes')
        
        else:
            return redirect("/inicio")

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))

@app.route('/buscar_cliente', methods=['POST', 'GET'])
def buscar_cliente():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":

            if request.method == 'POST':
                busqueda = request.form['busqueda']
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM clientes WHERE estado_cliente='ACTIVO' AND (nom_cliente LIKE '%{busqueda}%' OR doc_cliente LIKE '%{busqueda}%' OR ape_cliente LIKE '%{busqueda}%')")
                resultados = cursor.fetchall()
                conn.close()
                return render_template('clientes/clientes.html', resulta=resultados) 
            
        else:
            return redirect("/inicio")

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    
@app.route('/borracliente/<documento>')
def borrarcliente(documento):
    if "nom_empleado" in session:

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            
            Dclientes.borrar_cliente(documento)
            return redirect('/clientes')
    
        else:
            return redirect("/inicio")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))



""" Registra clientes en modulo ventas  """

@app.route("/crearClientes_2")
def crearClientes_2():
    if "nom_empleado" in session:

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor": 

            return render_template('clientes/registrar_clientes_2.html')  
        
        else:
            return redirect("/inicio")  
        
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    




@app.route("/crear_cliente_2", methods=['POST'])
def crear_cliente_2():
    if "nom_empleado" in session:
            
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor": 

            doc = session["nom_empleado"]
            bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq)
            resultado = cursor.fetchone()
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]
            doc_cliente = request.form['doc_cliente']
            nom_cliente = request.form['nom_cliente']
            ape_cliente = request.form['ape_cliente']
            fecha_nacimiento_cliente = request.form['fecha_nacimiento_cliente']
            contacto_cliente = ""
            email_cliente = ""
            direccion_cliente = ""
            ciudad_cliente = ""
            tipo_persona = request.form['tipopersona']                 
            tiempo = datetime.datetime.now()
            if not Dclientes.buscar_cliente(doc_cliente):
                Dclientes.crear_cliente([doc_cliente, nom_cliente, ape_cliente, fecha_nacimiento_cliente, contacto_cliente, email_cliente, direccion_cliente, ciudad_cliente, tipo_persona, tiempo, documento_registro, nombre_operador, apellido_operador])
                return redirect('/verCrear_ventas')
            else:
                """ mensaje="Cliente ya existe"
                cliente =[doc_cliente, nom_cliente, ape_cliente, contacto_cliente, email_cliente, direccion_cliente, ciudad_cliente, tipo_persona]
                return render_template('clientes/clientes.html', mensaje=mensaje, cliente=cliente) """
                


            # Muestra el documento del operador
            documento_operador = session["documento_operador"]


            # consulta los productos del inventario
            sql = "SELECT `id_producto`, `ref_produ_1`, `nombre_producto`, `precio_venta`, `cantidad_producto` FROM `productos` WHERE `estado_producto`= 'ACTIVO'"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql)
            productos_inven = cursor.fetchall()
            conn.commit()

            # consulta los productos seleccionados para venta
            sql = "SELECT `contador`, `nombre_producto`, `precio_venta`, `cantidad_adquirida`, `total` FROM `carritoventas`"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql)
            productos_carr = cursor.fetchall()
            conn.commit()

            # Realiza la suma de el total de todos los productos seleccionados
            sql = "SELECT SUM(total) FROM carritoventas"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql) 
            Suma_total = cursor.fetchall()
            conn.commit()

            mensaje_error = "El_cliente_ya_existe_en_la_base_de_datos"

            # le asigno el 0 si la suma es none
            if Suma_total[0][0] is not None:
                return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = Suma_total[0][0], operador = documento_operador, mensaje_2 = mensaje_error) 
            else:
                return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = 0, operador = documento_operador, mensaje_2 = mensaje_error) 
            
        else:
            return redirect("/inicio")
            
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))