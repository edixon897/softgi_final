from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
from models.cotizaciones import cotizaciones
from utils.tokens import generador_id
from num2words import num2words


@app.route("/Cotizacion")
def Cotizacion():
    if "nom_empleado" in session: 

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":

            msql = "SELECT `num_cotizacion`, `cliente_cotizacion`, `nombre_cliente_cotizacion`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_operador`, `apellido_operador` FROM `cotizaciones` WHERE estado = 'ACTIVO'"
            with mysql.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(msql)
                    datos = cursor.fetchall()

            return render_template("cotizaciones/cotizaciones.html", datos=datos)
        
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
                Cotiza = [id_cotizacion, clienteCotizacion, documento_registro, nombre_operador, apellido_operador, fechaInicioCotizacion, fechaFinCotizacion, nombre_cliente_cotizacion, direcion_cliente, correo_cliente, cuidad_cliente, contacto_cliente]
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


@app.route("/editarCotizacion/<id_cotizacion>", methods=['GET'])
def editarCotizacion(id_cotizacion):
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            sql = """
                SELECT
                    cotizaciones.fecha_inicio_cotizacion,
                    cotizaciones.fecha_fin_cotizacion,
                    cotizaciones.nombre_cliente_cotizacion,
                    detallecotizaciones.producto_cotizacion,
                    detallecotizaciones.nombre_producto,
                    detallecotizaciones.cantidad_productos_cotizacion,
                    detallecotizaciones.valorunidad_prodcotizacion,
                    cotizaciones.num_cotizacion,
                    detallecotizaciones.`id_detalle_cotizacion`
                FROM cotizaciones
                INNER JOIN detallecotizaciones ON cotizaciones.num_cotizacion = detallecotizaciones.num_cotizacion
                WHERE cotizaciones.num_cotizacion = '{}' AND  detallecotizaciones.num_cotizacion = '{}' AND `detalle_estado`='ACTIVO' AND  `estado`='ACTIVO'
            """.format(id_cotizacion,  id_cotizacion)

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

            
        else:
            return redirect("/inicio")
        
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
        fecha_inicio = request.form['fechaInicioEditarCliente']
        fecha_fin = request.form['fechaFinEditarCliente']
        cliente_seleccionado = request.form.get('clienteCotizacionEditar')
        id_cotizacion = request.form['id_cotizacion']

        clienteCotizacion = None  # Inicializar las variables con un valor predeterminado
        contacto_cliente = None
        correo_cliente = None 
        direcion_cliente = None  
        cuidad_cliente = None

        if cliente_seleccionado:
            bsqd = f"SELECT `doc_cliente`, `contacto_cliente`, `email_cliente`, `direccion_cliente`, `ciudad_cliente` FROM clientes WHERE `nom_cliente`='{cliente_seleccionado}'"
            cursor.execute(bsqd)
            resultado2 = cursor.fetchone()
            

            if resultado2:
                clienteCotizacion = resultado2[0]
                contacto_cliente = resultado2[1]
                correo_cliente = resultado2[2]
                direcion_cliente = resultado2[3]
                cuidad_cliente = resultado2[4]
            else:
                flash('El cliente seleccionado no existe.')
                return redirect(url_for('CrearCotizacion'))
        
        editarCotiza = [
            id_cotizacion, 
            clienteCotizacion, 
            documento_registro, 
            nombre_operador, 
            apellido_operador, 
            fecha_inicio, 
            fecha_fin, 
            cliente_seleccionado, 
            direcion_cliente, 
            correo_cliente, 
            cuidad_cliente, 
            contacto_cliente
            ]
        
        cotizaciones.editarCotizacion(editarCotiza)
    
        referenciasProductos = request.form.getlist('nombreProd[]')
        cantidadesProductos = request.form.getlist('cantidadProd[]')

        for i in range(len(referenciasProductos)):
            nombre_producto = referenciasProductos[i]
            cantidad_producto = int(cantidadesProductos[i])  # Convertir a entero

            bsqd = f"SELECT `id_producto`, `precio_venta` FROM `productos` WHERE `nombre_producto`='{nombre_producto}'"
            mylsql = f"SELECT `id_detalle_cotizacion` FROM `detallecotizaciones` WHERE `num_cotizacion`={id_cotizacion} AND `nombre_producto`='{nombre_producto}'"

            with mysql.connect() as conn:
                with conn.cursor() as cursor:
                    # Consulta para obtener la información del producto
                    cursor.execute(bsqd)
                    resultadoReferencia = cursor.fetchone()

                    if resultadoReferencia:
                        producto_cotizacion = resultadoReferencia[0]
                        valorunidadProdcotizacion = resultadoReferencia[1]

                        # Consulta para obtener el ID de detalle de cotización del producto en la cotización actual
                        cursor.execute(mylsql)
                        detalle_cotizacion = cursor.fetchone()

                        # Verificar si se encontró un detalle de cotización para el producto actual
                        if detalle_cotizacion:
                            id_detalle_cotizacion = detalle_cotizacion[0]
                            valortotalCantidaproductosCotizacion = cantidad_producto * valorunidadProdcotizacion
                            total = valortotalCantidaproductosCotizacion

                            # Actualizar el detalle de cotización existente
                            datos = [id_detalle_cotizacion, producto_cotizacion, nombre_producto, cantidad_producto, valorunidadProdcotizacion, valortotalCantidaproductosCotizacion, total, id_detalle_cotizacion]
                            cotizaciones.editarDetalleCotizaciones(datos)
                            print('Actualizacion de datos', datos)
                        else:
                            # Insertar un nuevo detalle de cotización
                            valortotalCantidaproductosCotizacion = cantidad_producto * valorunidadProdcotizacion
                            total = valortotalCantidaproductosCotizacion
                            datos = [id_cotizacion, producto_cotizacion, nombre_producto, cantidad_producto, valorunidadProdcotizacion, valortotalCantidaproductosCotizacion, total]
                            cotizaciones.crearDetalleCotizacion(datos)
                            print('Registro de datos', datos)

        flash('La cotización ha sido actualizada exitosamente.')
        return redirect(url_for('Cotizacion'))
        
    else:
        flash('Por favor inicia sesión para poder acceder')
        return redirect(url_for('home'))


@app.route('/borraCotizacion/<id_cotizacion>', methods=['POST'])
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

@app.route('/borraDetallleCotizacion/<int:id_cotizacion>', methods=['POST'])
def borraDetallleCotizacion(id_cotizacion):
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            cotizaciones.eliminarDetalleCotizacion(id_cotizacion)
            return 'Producto eliminado correctamente', 200
        else:
            return 'No tienes permiso para realizar esta acción', 403
   
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    

@app.route("/detalle/<id_cotizacion>")
def detalle(id_cotizacion):
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            sql = f"SELECT `nombre_producto`, `cantidad_productos_cotizacion`, `valorunidad_prodcotizacion`, `valortotal_cantidaproductos_cotizacion` FROM `detallecotizaciones` WHERE `num_cotizacion` = '{id_cotizacion}' AND `detalle_estado` = 'ACTIVO'"
            bsql = f"SELECT `num_cotizacion`, `cliente_cotizacion`, `nombre_operador`, `apellido_operador`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_cliente_cotizacion`, `direcion_cliente`, `correo_cliente`, `cuidad_cliente`, `contacto_cliente` FROM `cotizaciones` WHERE `num_cotizacion` = '{id_cotizacion}' AND `estado` = 'ACTIVO' "

            with mysql.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    resultado = cursor.fetchall()

                    cursor.execute(bsql)
                    cotiza = cursor.fetchall()

            # Aca se convertir el total de la cantidad a palabras
            total_cantidad = sum(row[3] for row in resultado)
            # Se asegúra de que total_cantidad sea un entero antes de pasarlo a num2words
            total_cantidad_entero = int(total_cantidad)
            total_cantidad_palabras = num2words(total_cantidad_entero, lang='es')
  

            return render_template("cotizaciones/detalleCotizacion.html", datos=resultado, info=cotiza, total_cantidad=total_cantidad, total_cantidad_palabras=total_cantidad_palabras)
        else:
            return redirect("/inicio")
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
    

@app.route('/buscar_ProductoCotizacion', methods=['POST'])
def buscar_ProductoCotizacion():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            if request.method == 'POST':
                busqueda = request.form.get('busqueda', '')
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(f"SELECT `nombre_producto` FROM `productos` WHERE `estado_producto`='ACTIVO' AND `nombre_producto` LIKE '%{busqueda}%'")
                resultados = cursor.fetchall()
                conn.close()
                return jsonify(result=resultados)
        else:
            return redirect("/inicio")
    else:
        flash('Por favor, inicia sesión para poder acceder')
        return redirect(url_for('index'))
    
    
@app.route('/buscar_cotizacion', methods=['POST'])
def buscar_cotizacion():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            if request.method == 'POST':
                busqueda = request.form.get('busqueda', '')
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT num_cotizacion, cliente_cotizacion, nombre_cliente_cotizacion, fecha_inicio_cotizacion, fecha_fin_cotizacion, nombre_operador FROM cotizaciones WHERE estado='ACTIVO' AND nombre_cliente_cotizacion LIKE %s", ('%' + busqueda + '%',))
                resultados = cursor.fetchall()
                conn.close()
                return jsonify(result=resultados)
        else:
            return redirect("/inicio")
    else:
        flash('Por favor, inicia sesión para poder acceder')
        return redirect(url_for('index'))
    
@app.route('/modalCrear')
def modalCrear():
    if "nom_empleado" in session: 

        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            sql_clients = "SELECT `nom_cliente`, `ape_cliente` FROM clientes WHERE estado_cliente ='ACTIVO'"
            with mysql.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_clients)
                    resultado = cursor.fetchall()
            return  render_template("cotizaciones/crearCotizacion.html", resulta = resultado)
        else:
            return redirect("/inicio")
    
    else:
        flash('Por favor, inicia sesión para poder acceder')
        return redirect(url_for('home'))

