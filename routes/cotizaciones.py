from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
from models.cotizaciones import cotizaciones
from utils.tokens import generador_id



@app.route("/Cotizacion")
def Cotizacion():
    if "nom_empleado" in session: 

        msql= f"SELECT `num_cotizacion`, `cliente_cotizacion`, `nombre_cliente_cotizacion`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion` FROM `cotizaciones` WHERE estado= 'ACTIVO'"

        msql= f"SELECT `cliente_cotizacion`, `nombre_cliente_cotizacion`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_operador`, `apellido_operador` FROM `cotizaciones`"

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
        sql = "SELECT `nom_cliente`, `ape_cliente` FROM clientes WHERE estado_cliente ='ACTIVO'"
        conn = mysql.connect()                    
        cursor = conn.cursor()
        cursor.execute(sql)                                          
        resultado = cursor.fetchall()
        bsql = f"SELECT `nombre_producto` FROM `productos` WHERE `estado_producto`='ACTIVO'"
        cursor.execute(bsql)
        resultado2 = cursor.fetchall() 
        return render_template('cotizaciones/crear.html', resulta=resultado, detalle=resultado2)
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))






@app.route('/crearCotizacion', methods=['POST'])
def crearCotizacion():
    if "nom_empleado" in session:
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

            if resultado2:
                clienteCotizacion = resultado2[0]
            else:
                flash('Cliente no encontrado en la base de datos.')
                return redirect(url_for('CrearCotizacion'))
                
            id_cotizacion = generador_id()
            fechaInicioCotizacion = request.form['fechaInicioNuevoCliente']
            fechaFinCotizacion = request.form['fechaFinNuevoCliente']
            
            referenciasProductos = request.form.getlist('referenciaProducto[]')
            cantidadesProductos = request.form.getlist('cantidadPorProducto[]')
            
            for i in range(len(referenciasProductos)):
                referenciaProducto = referenciasProductos[i]
                cantidadProducto = int(cantidadesProductos[i])
                
                bsqd = f"SELECT `id_producto`, `precio_venta` FROM `productos` WHERE `nombre_producto`='{referenciaProducto}'"
                cursor.execute(bsqd)
                resultadoReferencia = cursor.fetchone()
                producto_cotizacion = resultadoReferencia[0]
                valorunidadProdcotizacion = int(resultadoReferencia[1])
                valortotalCantidaproductosCotizacion = cantidadProducto * valorunidadProdcotizacion
                                
                datos = [id_cotizacion, producto_cotizacion, referenciaProducto, cantidadProducto, valorunidadProdcotizacion, valortotalCantidaproductosCotizacion]
                
                cotizaciones.crearDetalleCotizacion(datos)
                
            cotizaciones.crearCotizaciones([id_cotizacion, clienteCotizacion, documento_registro, nombre_operador, apellido_operador, fechaInicioCotizacion, fechaFinCotizacion, nombre_cliente_cotizacion])
            
            flash('Tu cliente fue creado con éxito')
            return redirect(url_for('Cotizacion'))
        
        flash('Por favor, selecciona un cliente.')
        return redirect(url_for('CrearCotizacion'))
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))


@app.route("/editarCotizacion/<id_cotizacion>")
def editarCotizacion(id_cotizacion):
    if "nom_empleado" in session:
        sql = f"SELECT * FROM cotizaciones WHERE num_cotizacion = '{id_cotizacion}'"
        conn = mysql.connect()
        cursor = conn.cursor()                                   
        cursor.execute(sql)
        resultado = cursor.fetchall()
        bsql = f"SELECT `nombre_producto` FROM `productos` WHERE `estado_producto`='ACTIVO'"
        cursor.execute(bsql)
        resultado2 = cursor.fetchall() 
        conn.commit()
        return render_template("cotizaciones/editarCotizacion.html", resul=resultado, detalle=resultado2)
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    
@app.route('/atualizarCotizacion', methods=['POST'])
def atualizarCotizacion():
    if "nom_empleado" in session:
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
        bsqd = f"SELECT doc_cliente FROM clientes WHERE nom_cliente='{nombre_cliente_cotizacion}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsqd)
        resultado2 = cursor.fetchone()
        clienteCotizacion = resultado2[0]
        id_c = request.form['id']
        fechaInicioCotizacion = request.form['fechaInicioCotizacion']
        fechaFinCotizacion = request.form['fechaFinCotizacion']
        datos_cotizaciones = [id_c, clienteCotizacion,documento_registro,nombre_operador,apellido_operador,fechaInicioCotizacion,fechaFinCotizacion, nombre_cliente_cotizacion ]
        cotizaciones.editarCotizacion(datos_cotizaciones)
        return redirect('Cotizacion')
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))

@app.route('/borraCotizacion/<id_cotizacion>')
def borraCotizacion(id_cotizacion):
    if "nom_empleado" in session:
        cotizaciones.eliminarCotizacion(id_cotizacion)                 
        return redirect("/Cotizacion")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    


@app.route("/detalle/<id_cotizacion>")
def detalle(id_cotizacion):
    if "nom_empleado" in session:
        sql = f"SELECT `nom_producto`, `cantidad_productos_cotizacion`, `valorunidad_prodcotizacion`, `valortotal_cantidaproductos_cotizacion` FROM `detallecotizaciones` WHERE `num_cotizacion` = '{id_cotizacion}' AND `detalle_estado` = 'ACTIVO'"
        conn = mysql.connect()
        cursor = conn.cursor()                                   
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()
        total_cantidad = sum(row[3] for row in resultado)

        return render_template("cotizaciones/detalleCotizacion.html", datos=resultado, total_cantidad=total_cantidad)
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
