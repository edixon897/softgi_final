from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
from models.cotizaciones import cotizaciones




@app.route("/Cotizacion")
def Cotizacion():
    if "nom_empleado" in session: 
        msql= f"SELECT `cliente_cotizacion`, `nombre_cliente_cotizacion`,  `nombre_operador`, `apellido_operador`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion` FROM `cotizaciones`"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(msql)
        datos = cursor.fetchall()
        return render_template("cotizaciones/cotizaciones.html", datos=datos)
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))

        
@app.route("/CrearCotizacion")
def CrearCotizacion():
    if "nom_empleado" in session: 
        sql = "SELECT `doc_cliente`, `nom_cliente`, `ape_cliente`, `contacto_cliente`, `email_cliente`, `direccion_cliente`, `ciudad_cliente`, `tipo_persona` FROM clientes WHERE estado_cliente ='ACTIVO'"
        conn = mysql.connect()                    
        cursor = conn.cursor()
        cursor.execute(sql)                                          
        resultado = cursor.fetchall()
        return render_template('cotizaciones/crear.html', resulta=resultado)

@app.route('/buscarCliente', methods=['POST', 'GET'])
def buscarCliente():
    if "nom_empleado" in session:
        if request.method == 'POST':
            busqueda = request.form['busqueda']
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(f"SELECT `doc_cliente`, `nom_cliente`, `ape_cliente` FROM clientes WHERE estado_cliente='ACTIVO' AND (nom_cliente LIKE '%{busqueda}%' OR doc_cliente LIKE '%{busqueda}%' OR ape_cliente LIKE '%{busqueda}%')")
            resultados = cursor.fetchall()
            conn.close()
            return render_template('cotizaciones/crear.html', resulta=resultados) 
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))


@app.route('/crearCotizacion', methods=['POST'])
def crearCotizacion():
    if "nom_empleado" in session:
        if request.method == 'POST':
            doc = session["nom_empleado"]
            bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq)
            resultado = cursor.fetchone()
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]
            nombre_cliente_cotizacion = request.form['clienteCotizacion']
            if nombre_cliente_cotizacion:
                bsqd = f"SELECT `doc_cliente` FROM clientes WHERE `nom_cliente`='{nombre_cliente_cotizacion}'"
                cursor.execute(bsqd)
                resultado2 = cursor.fetchone()
                print(resultado2)
                if resultado2:
                    clienteCotizacion = resultado2[0]
                    
                else:
                    flash('Cliente no encontrado en la base de datos.')

                fechaInicioCotizacion = request.form['fechaInicioNuevoCliente']
                fechaFinCotizacion = request.form['fechaFinNuevoCliente']
                cotizaciones.crearCotizaciones([clienteCotizacion, documento_registro, nombre_operador, apellido_operador, fechaInicioCotizacion, fechaFinCotizacion, nombre_cliente_cotizacion])
                flash('Tu cliente fue creado con exito')
                return redirect(url_for('Cotizacion'))
                
            # Redirect or render appropriate page
            return redirect(url_for('CrearCotizacion'))
    else:
        flash('Por favor, inicia sesión para poder acceder')
        return redirect(url_for('home'))

