from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
from models.cotizaciones import Cotizaciones, cotizaciones
from models.devoluciones import Ddevoluciones
from utils.tokens import generador_id

@app.route("/muestraDevoluciones")
def muestraDevoluciones():
    if "nom_empleado" in session:
        msql= f"SELECT `id_devolucion`, `num_factura`, `documento_operador`, `nombre_operador`, `apellido_operador`, `cliente_devolucion`, `fecha_devolucion` FROM `devoluciones`"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(msql)
        datos = cursor.fetchall()
        return render_template("/devoluciones/muestra_devoluciones.html", datos=datos)
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))

#registro de devoluciones
@app.route("/crear_devolucion")
def crear_devolucion():
    if "nom_empleado" in session:
        return render_template('devoluciones/registrar_devolucion.html')

@app.route('/crear_devolucion', methods=['POST'])
def crearDevoluciones():
    if "nom_empleado" in session:
        doc = session["nom_empleado"]
        conn = mysql.connect()
        cursor = conn.cursor()

        # Obtener los detalles del empleado
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
        cursor.execute(bsq)
        resultado = cursor.fetchone()

        if resultado:
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]

            # Obtener detalles del formulario
            num_factura = request.form['num_factura']
            cliente_devolucion = request.form['cliente_devolucion']
            fecha_devolucion = request.form['fecha_devolucion']

            # Verificar existencia de datos
            bsqd_venta = f"SELECT num_factura FROM ventas WHERE num_factura='{num_factura}'"
            cursor.execute(bsqd_venta)
            resultado_venta = cursor.fetchone()

            bsqd_cliente = f"SELECT doc_cliente FROM clientes WHERE doc_cliente='{cliente_devolucion}'"
            cursor.execute(bsqd_cliente)
            resultado_cliente = cursor.fetchone()

            bsqd_empleado = f"SELECT doc_empleado FROM empleados WHERE doc_empleado='{documento_registro}'"
            cursor.execute(bsqd_empleado)
            resultado_empleado = cursor.fetchone()

            if resultado_venta and resultado_cliente and resultado_empleado:
                # Llamar a la función para crear la devolución
                Ddevoluciones.crear_devolucion([num_factura, cliente_devolucion, documento_registro, nombre_operador, apellido_operador, fecha_devolucion])
                return redirect('muestraDevoluciones')
            else:
                flash('Algunos datos no existen en la base de datos')
                return redirect(url_for('crearDevoluciones'))
        else:
            flash('No se encontró el empleado en la base de datos')
            return redirect(url_for('crearDevoluciones'))
    else:
        flash('Por favor inicia sesión para poder acceder')
        return redirect(url_for('index'))


#mostrar detalle de devolucion
@app.route('/detalledevoluciones')
def detallesDevoluciones():
    bsq = f"SELECT * FROM `detallesdevoluciones`"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(bsq)
    resultado = cursor.fetchall()
    return render_template('devoluciones/muestra_detalle_devoluciones.html', datos = resultado)

#editar detalle de devolucion
@app.route("/editarDetalleDevolucioncion/<id_DetalleDevolucion>")
def editarDetalleDevolucion(id_DetalleDevolucion):
    if "nom_empleado" in session:
        sql = f"SELECT * FROM `detalledevoluciones` WHERE `id_detalle_devolucion` = '{id_DetalleDevolucion}'"
        conn = mysql.connect()
        cursor = conn.cursor()                                   
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()
        return render_template("devoluciones/editar_detalle_devolucion.html", resul=resultado[0])
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
    
#Actualizar detalle de cotizacion
@app.route('/editarDetalleDevoluciones', methods=['POST', 'GET'])
def editarDetalleDevoluciones():
    if "nom_empleado" in session:
        conn = mysql.connect()
        cursor = conn.cursor()
        num_devolucion = request.form['num_devolucion']
        producto_devolucion = request.form['producto_devolucion']
        cantidad_proddevolucion = request.form['cantidad_proddevolucion']
        precio_proddevolucion = request.form['precio_proddevolucion']
        motivo_devolucion = request.form['motivo_devolucion']
        monto_total_devolucion = request.form['monto_total_devolucion']
        sql = f"SELECT `num_devolucion` FROM `devoluciones` WHERE `num_devolucion`='1'"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        num_devolucion  = resultado[1]
        bsql = f"SELECT `num_devolucion` FROM `devoluciones` WHERE id_devolucion='{num_devolucion}'"
        cursor.execute(bsql)
        resultado2 = cursor.fetchone() 
        producto_cotizacion = resultado2[0]
        datos = [num_devolucion, producto_cotizacion, producto_devolucion, cantidad_proddevolucion, precio_proddevolucion, motivo_devolucion, monto_total_devolucion   ]
        Cotizaciones.editarDetalleCotizaciones(datos)
        return redirect('detallesDevoluciones')
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))

#Borrar detalle de devolucion 
@app.route('/borraDetalleCotizacion/<id_detalleDevolucion>')
def borraDetalleDevolucion(id_detalleDevolucion):
    if "nom_empleado" in session:
        Ddevoluciones.eliminarDetalleDevolucion(id_detalleDevolucion)                       
        return redirect("/detallesDevoluciones")
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))

#crear detalle de cotizacion
@app.route('/detalleDevoluciones')
def detalleDevolucion():
    return render_template('devoluciones/detalle_devoluciones.html')

@app.route('/registroDetalleDevolucion', methods=['POST'])
def registroDetalleDevolucion():
     if "nom_empleado" in session:
        conn = mysql.connect()
        cursor = conn.cursor()
        producto_devolucion = request.form['producto_devolucion']
        cantidad_proddevolucion = request.form['cantidad_proddevolucion']
        precio_proddevolucion = request.form['precio_proddevolucion']
        motivo_devolucion = request.form['motivo_devolucion']
        monto_total_devolucion = request.form['monto_total_devolucion']
        sql = f"SELECT `id_devolucion` FROM `devoluciones` WHERE `id_devolucion`='0'"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        id_detalle_devolucion  = resultado[0]
        num_factura = request.form['num_factura']
        bsql = f"SELECT `num_factura` FROM `ventas` WHERE num_factura='{num_factura}'"
        cursor.execute(bsql)
        resultado2 = cursor.fetchone() 
        producto_devolucion = resultado2[0]
        datos = [id_detalle_devolucion, producto_devolucion, cantidad_proddevolucion, precio_proddevolucion, motivo_devolucion, monto_total_devolucion ]
        cotizaciones.crearDetalleCotizacion(datos)
        return redirect('Devolucion')
     else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
    

#editar cotizacion
@app.route("/modificar_devolucion/<id_devolucion>")
def editarDevolucion(id_devolucion):
    if "nom_empleado" in session:
        sql = f"SELECT * FROM devoluciones WHERE id_devolucion = '{id_devolucion}'"
        print(id_devolucion)
        conn = mysql.connect()
        cursor = conn.cursor()     #muestra toda la informacion y pone en los imputs
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
        conn.commit()
        return render_template("devoluciones/editar_devolucion.html", resul=resultado[0])
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))

@app.route('/actualizarDevolucion', methods=['POST'])
def atualizarDevolucion():
    if "nom_empleado" in session:
        email = session["email_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE email_empleado='{email}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsq)
        resultado = cursor.fetchone()
        documento_registro = resultado[0]
        nombre_operador = resultado[1]
        apellido_operador = resultado[2]
        cliente_devolucion = request.form['clienteDevolucion']
        bsqd = f"SELECT doc_cliente FROM clientes WHERE nom_cliente='{cliente_devolucion}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsqd)
        resultado2 = cursor.fetchone()
        cliente_devolucion = resultado2[0]
        id_c = request.form['id']
        fecha_devolucion = request.form['fecha_devolucion']
        datos_cotizaciones = [id_c, cliente_devolucion, documento_registro, nombre_operador, apellido_operador,fecha_devolucion, cliente_devolucion ]
        cotizaciones.editarCotizacion(datos_cotizaciones)
        return redirect('Devolucion')
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
