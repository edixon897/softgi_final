from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
from models.cotizaciones import cotizaciones
from utils.tokens import generador_id



@app.route("/Cotizacion")
def Cotizacion():
    if "nom_empleado" in session: 

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":

            msql = "SELECT `num_cotizacion`, `cliente_cotizacion`, `nombre_cliente_cotizacion`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_operador`, `apellido_operador` FROM `cotizaciones` WHERE estado= 'ACTIVO'"
            sql_clients = "SELECT `nom_cliente`, `ape_cliente` FROM clientes WHERE estado_cliente ='ACTIVO'"
            bsql = "SELECT `nombre_producto` FROM `productos` WHERE `estado_producto`='ACTIVO'"
            with mysql.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(msql)
                    datos = cursor.fetchall()

                    cursor.execute(sql_clients)
                    resultado = cursor.fetchall()

                    cursor.execute(bsql)
                    resultado2 = cursor.fetchall()
            return render_template("cotizaciones/cotizaciones.html", datos=datos, resulta=resultado, detal=resultado2)
        
        else:
            return redirect("/inicio")
    
    else:
        flash('Por favor, inicia sesión para poder acceder')
        return redirect(url_for('home'))

@app.route('/crearCotizacion', methods=['POST'])
def crearCotizacion():
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
            
            nombre_cliente_cotizacion = request.form['clienteCotizacion']
            if nombre_cliente_cotizacion:
                bsqd = f"SELECT `doc_cliente`, `contacto_cliente`, `email_cliente`, `direccion_cliente`, `ciudad_cliente` FROM clientes WHERE `nom_cliente`='{nombre_cliente_cotizacion}'"
                cursor.execute(bsqd)
                resultado2 = cursor.fetchone()

                if resultado2:
                    clienteCotizacion = resultado2[0]
                    contacto_cliente = resultado2[1]
                    correo_cliente = resultado2[2]
                    direcion_cliente = resultado2[3]
                    cuidad_cliente = resultado2[4]
                else:
                    flash('Cliente no encontrado en la base de datos.')
                    return redirect(url_for('CrearCotizacion'))
                    
                id_cotizacion = generador_id()
                fechaInicioCotizacion = request.form['fechaInicioNuevoCliente']
                fechaFinCotizacion = request.form['fechaFinNuevoCliente']
                
                referenciasProductos = request.form.getlist('referenciaProducto[]')
                cantidadesProductos = request.form.getlist('cantidadPorProducto[]')
                Cotiza = [id_cotizacion, clienteCotizacion, documento_registro, nombre_operador, apellido_operador, fechaInicioCotizacion, fechaFinCotizacion, nombre_cliente_cotizacion, direcion_cliente, correo_cliente, cuidad_cliente, correo_cliente]
                cotizaciones.crearCotizaciones(Cotiza)
                print(Cotiza)
                for i in range(len(referenciasProductos)):
                    referenciaProducto = referenciasProductos[i]
                    cantidadProducto = int(cantidadesProductos[i])
                    
                    bsqd = f"SELECT `id_producto`, `precio_venta` FROM `productos` WHERE `nombre_producto`='{referenciaProducto}'"
                    cursor.execute(bsqd)
                    resultadoReferencia = cursor.fetchone()
                    producto_cotizacion = resultadoReferencia[0]
                    valorunidadProdcotizacion = int(resultadoReferencia[1])
                    valortotalCantidaproductosCotizacion = cantidadProducto * valorunidadProdcotizacion
                    total= valortotalCantidaproductosCotizacion
                    datos = [id_cotizacion, producto_cotizacion, referenciaProducto, cantidadProducto, valorunidadProdcotizacion, valortotalCantidaproductosCotizacion, total]
                    cotizaciones.crearDetalleCotizacion(datos)
                    print(datos)
                
                flash('Tu cotizacion fue creada con exito')
                return redirect(url_for('Cotizacion'))
            
            flash('Por favor, selecciona un cliente.')
            return redirect(url_for('CrearCotizacion'))
        
        else:
            return redirect("/inicio")

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))


@app.route("/editarCotizacion/<id_cotizacion>", methods=['GET', 'POST'])
def editarCotizacion(id_cotizacion):
    if "nom_empleado" in session:

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            

            if request.method == 'GET':
                sql = """
                    SELECT
                        cotizaciones.fecha_inicio_cotizacion,
                        cotizaciones.fecha_fin_cotizacion,
                        cotizaciones.nombre_cliente_cotizacion,
                        detallecotizaciones.producto_cotizacion,
                        detallecotizaciones.nombre_producto,
                        detallecotizaciones.cantidad_productos_cotizacion,
                        detallecotizaciones.valorunidad_prodcotizacion,
                        cotizaciones.num_cotizacion
                    FROM cotizaciones
                    INNER JOIN detallecotizaciones ON cotizaciones.num_cotizacion = detallecotizaciones.num_cotizacion
                    WHERE cotizaciones.num_cotizacion = '{}'
                """.format(id_cotizacion)

                bsql = "SELECT `nombre_producto` FROM `productos` WHERE `estado_producto`='ACTIVO'"
                sql_clients = "SELECT `nom_cliente`, `ape_cliente` FROM clientes WHERE estado_cliente ='ACTIVO'"

                with mysql.connect() as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(sql)
                        datos = cursor.fetchall()

                        cursor.execute(bsql)
                        productos = cursor.fetchall()

                        cursor.execute(sql_clients)
                        cliente = cursor.fetchall()

                return render_template('/cotizaciones/editarCotizacion.html', datos=datos, productos=productos, cliente=cliente)

            elif request.method == 'POST':
                doc = session["nom_empleado"]
                bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"     
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(bsq)
                resultado = cursor.fetchone()
                documento_registro = resultado[0]
                nombre_operador = resultado[1]
                apellido_operador = resultado[2]
                fecha_inicio = request.form['fechaInicioEditarCliente']
                fecha_fin = request.form['fechaFinEditarCliente']
                cliente_seleccionado = request.form['clienteCotizacionEditar']
                if cliente_seleccionado:
                    bsqd = f"SELECT `doc_cliente` FROM clientes WHERE `nom_cliente`='{cliente_seleccionado}'"
                    cursor.execute(bsqd)
                    resultado2 = cursor.fetchone()

                    if resultado2:
                        clienteCotizacion = resultado2[0]
                    else:
                        flash('Su cotizacion fue editada con exito.')
                        return redirect(url_for('CrearCotizacion'))
                
                productos_seleccionados = []
                for i in range(len(request.form.getlist('nombreProd[]'))):
                    nombre_producto = request.form.getlist('nombreProd[]')[i]
                    cantidad_producto = request.form.getlist('cantidadProd[]')[i]
                    productos_seleccionados.append({'nombre_producto': nombre_producto, 'cantidad_producto': cantidad_producto})

                return jsonify({'status': 'success'})
            
        else:
            return redirect("/inicio")
        
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))

    
""" @app.route('/atualizarCotizacion', methods=['POST'])
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
        
        nombre_cliente_cotizacion = request.form['clienteCotizacionEditar']
        if nombre_cliente_cotizacion:
            bsqd = f"SELECT `doc_cliente` FROM clientes WHERE `nom_cliente`='{nombre_cliente_cotizacion}'"
            cursor.execute(bsqd)
            resultado2 = cursor.fetchone()

            if resultado2:
                clienteCotizacion = resultado2[0]
            else:
                flash('Cliente no encontrado en la base de datos.')
                return redirect(url_for('CrearCotizacion'))
                
            
            fechaInicioCotizacion = request.form['fechaInicioEditarCliente']
            fechaFinCotizacion = request.form['fechaFinEditarCliente']
            
            referenciasProductos = request.form.getlist('referenciaProductosEditar[]')
            cantidadesProductos = request.form.getlist('cantidad_productos_cotizacion[]')
            Cotiza = [clienteCotizacion, documento_registro, nombre_operador, apellido_operador, fechaInicioCotizacion, fechaFinCotizacion, nombre_cliente_cotizacion]
            cotizaciones.editarCotizacion(Cotiza)
            print(Cotiza)
            for i in range(len(referenciasProductos)):
                referenciaProducto = referenciasProductos[i]
                cantidadProducto = int(cantidadesProductos[i])
                
                bsqd = f"SELECT `id_producto`, `precio_venta` FROM `productos` WHERE `nombre_producto`='{referenciaProducto}'"
                cursor.execute(bsqd)
                resultadoReferencia = cursor.fetchone()
                producto_cotizacion = resultadoReferencia[0]
                valorunidadProdcotizacion = int(resultadoReferencia[1])
                valortotalCantidaproductosCotizacion = cantidadProducto * valorunidadProdcotizacion
                total= valortotalCantidaproductosCotizacion
                datos = [ producto_cotizacion, referenciaProducto, cantidadProducto, valorunidadProdcotizacion, valortotalCantidaproductosCotizacion, total]
                cotizaciones.editarDetalleCotizaciones(datos)
                print(datos)
            
            flash('Tu cliente fue creado con éxito')
            return redirect(url_for('Cotizacion'))
        
        flash('Por favor, selecciona un cliente.')
        return redirect(url_for('CrearCotizacion'))
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home')) """

@app.route('/borraCotizacion/<id_cotizacion>')
def borraCotizacion(id_cotizacion):
    if "nom_empleado" in session:

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":

            cotizaciones.eliminarCotizacion(id_cotizacion)                 
            return redirect("/Cotizacion")
        
        else:
            return redirect("/inicio")

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    


@app.route("/detalle/<id_cotizacion>")
def detalle(id_cotizacion):
    if "nom_empleado" in session:
            
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":

            sql = f"SELECT `nombre_producto`, `cantidad_productos_cotizacion`, `valorunidad_prodcotizacion`, `valortotal_cantidaproductos_cotizacion` FROM `detallecotizaciones` WHERE `num_cotizacion` = '{id_cotizacion}' AND `detalle_estado` = 'ACTIVO'"
            bsql =f"SELECT `num_cotizacion`, `cliente_cotizacion`, `nombre_operador`, `apellido_operador`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_cliente_cotizacion`, `direcion_cliente`, `correo_cliente`, `cuidad_cliente`, `contacto_cliente` FROM `cotizaciones` WHERE `num_cotizacion` = '{id_cotizacion}' AND `estado` = 'ACTIVO' "
            with mysql.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    resultado = cursor.fetchall()

                    cursor.execute(bsql)
                    cotiza = cursor.fetchall()

                    cursor.execute(bsql)
                    resultado2 = cursor.fetchall()
            total_cantidad = sum(row[3] for row in resultado)

            return render_template("cotizaciones/detalleCotizacion.html", datos=resultado, info=cotiza, total_cantidad=total_cantidad)
        
        else:
            return redirect("/inicio")

    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
