import random
import string
from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.ventas import Dventas, Ventas



#-------------------------------------------------------- abonos ventas a credito ----------------------------------------------------------------

@app.route("/abono_credito_2/<contador>")
def abono_credito_2(contador):
    if "email_empleado" in session:

        # muestra el html
        return render_template("/ventas_credito/abono_venta.html",cont = contador)

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))




"""   --------------recibe la info del FRONT-END------------  """

@app.route("/confirma_abono_2", methods = ['POST'])
def confirma_abono_2():
    if "email_empleado" in session:

        contador = request.form['contador']
        abono = request.form['abono']
        documento_operador = session["doc_empleado"]    

        # combierto el texto a numero
        abono = int(abono)
        
        # conuslto el credito restante
        sql = f"SELECT `credito_restante` FROM `ventas_credito` WHERE contador = '{contador}'"
        conn = mysql.connect()
        cursor = conn.cursor()    
        cursor.execute(sql)
        credito_restante = cursor.fetchall()
        conn.commit()

        # 1 - valido si la cantidad digitada es menor a la debida
        if (credito_restante[0][0] >= abono):

            credito_actual = (credito_restante[0][0] - abono)
            tiempo_venta = datetime.datetime.now()

            # 2 - valido si la resta = 0
            if (credito_actual == 0):

                # se cambia el estado de ACTIVO a CANCELADO
                Ventas.abono_completo(contador)
                return redirect("/muestra_ventas_credito")
            
            
            # 2 
            else:
                # se actualiza el credito restante
                Ventas.actualiza_credito_rest([credito_actual, contador])

                # se incerta en el historial el abono realizado
                Ventas.insert_historial_abn([contador, abono, documento_operador, tiempo_venta])
                return redirect("/muestra_ventas_credito")

        # 1
        else:
            mensaj = "¡Cantidd digitada mayor a la debida!"
            return render_template("/ventas_credito/abono_venta.html",cont = contador, mensaje = mensaj)
            
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))

























#-------------------------------------------------------- Historial de ventas ----------------------------------------------------------------

@app.route("/muestra_ventas")
def muestra_ventas():
    if "nom_empleado" in session: 
        sql = "SELECT  `num_factura`, `cliente_factura`, `nombre_operador`, `apellido_operador`, `fechahora_venta`, `forma_pago` FROM `ventas` ORDER BY num_factura DESC"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return render_template("/ventas/muestra_ventas.html", resul = resultado)
    
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))
    
    
@app.route("/muestra_detalles_ventas/<num_factura>")
def muestra_detalles_ventas(num_factura):
    if "nom_empleado" in session: 
        sql = f"SELECT `num_factura_venta`, `producto_factura`, `cantidad_productos_factura`, `total_pagar_factura` FROM `detalleventas` WHERE num_factura_venta = '{num_factura}'"
        conn = mysql.connect()
        cursor = conn.cursor()     #muestra toda la informacion de detalles
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return render_template('ventas/detalle_ventas.html', resul = resultado)
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))


# -------------------------------- Buscador ventas a credito ---------------------

@app.route("/buscador_venta_c", methods = ['POST'])
def buscador_venta_c():
    if "nom_empleado" in session: 
        # recibe la info
        busqueda = request.form['dato_busqueda']
        sql = f"SELECT `contador`, `cliente`, `productos`, `credito_total`, `credito_restante`, `operador`, `fecha_venta` FROM `ventas_credito`  WHERE estado ='ACTIVO' AND cliente LIKE '%{busqueda}%' OR estado='ACTIVO' AND operador LIKE '%{busqueda}%'"
        conn = mysql.connect()
        cursor = conn.cursor()     #muestra toda la informacion de la busqueda
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return render_template("/ventas_credito/muestra_ventas.html",resul = resultado)
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))

#-------------------------------------------------------- Historial de ventas a credito ----------------------------------------------------------------

@app.route("/muestra_ventas_credito")
def muestra_ventas_credito():
    if "nom_empleado" in session: 
        sql = "SELECT `contador`, `cliente`, `productos`, `credito_total`, `credito_restante`, `operador`, `fecha_venta` FROM `ventas_credito` WHERE estado = 'ACTIVO'"
        conn = mysql.connect()
        cursor = conn.cursor()     #muestra toda la informacion
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return render_template("/ventas_credito/muestra_ventas.html",resul = resultado)
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))


#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------- <<<< REALIZA LA VENTA >>> --------------------------------------------------

@app.route("/confirma_venta", methods = ['POST'])
def confirma_venta():
    if "nom_empleado" in session: 

#-------------------------------------------- informacion por si hay un error -----------

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

#--------------------------------------------------------------------

        # valido si hay productos o no
        sql = f"SELECT `id_producto` FROM carritoventas"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        busqueda = cursor.fetchall()
        conn.commit()

        # 1 - valido que la venta no este vacia - 
        if ((len(busqueda)) > 0):

            # recibo la info del FRONT-END
            doc_operador = request.form['doc_operador']
            doc_cliente = request.form['doc_cliente']
            forma_de_pago = request.form['forma_de_pago']
            tipo_de_venta = request.form['tipo_de_venta']

            # consulto info del operador
            sql = f"SELECT * FROM `empleados` WHERE doc_empleado = '{doc_operador}'"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql)
            info_operador = cursor.fetchall()
            conn.commit()

            # 2 - valido que el operador exista
            if ((len(info_operador)) > 0):

                # consulto info cliente
                sql = f"SELECT * FROM `clientes` WHERE estado_cliente = 'ACTIVO' AND doc_cliente = '{doc_cliente}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                info_cliente = cursor.fetchall()
                conn.commit()

                # 3 - valido que el cliente exista
                if ((len(info_cliente)) > 0):

                    # captura el timpo
                    tiempo_venta = datetime.datetime.now()

                    # Agrupo el nombre de todos los productos
                    sql = "SELECT GROUP_CONCAT(CONCAT(nombre_producto, ' - ', cantidad_adquirida) SEPARATOR ',   ') AS concatenado FROM carritoventas;"
                    conn = mysql.connect()
                    cursor = conn.cursor()     
                    cursor.execute(sql)
                    productos_fac = cursor.fetchall()
                    conn.commit()

                    # 4 ----------- Validacion tipo de venta --------------
                    if (tipo_de_venta == "venta_normal"):

                        # consulto el nombre y apellido del operador
                        sql = f"SELECT `nom_empleado`, `ape_empleado` FROM `empleados` WHERE doc_empleado = '{doc_operador}'"
                        conn = mysql.connect()
                        cursor = conn.cursor()     
                        cursor.execute(sql)
                        nombre_apell_operador = cursor.fetchall()
                        conn.commit()

                        # paso de [[]] a []
                        nom_ape_operador = nombre_apell_operador[0]

                        # generador de codigo 
                        lower = string.ascii_lowercase       
                        upper = string.ascii_uppercase 
                        num = string.digits 
                        chars = lower + upper + num
                        codigo = random.sample(chars, 20)
                        codigo_2 = ""  # variable que guarda el codigo
                        for c in codigo:
                            codigo_2+=c
                        
                        # Insertacion de datos en tabla ventas
                        Dventas.crear_venta([doc_cliente, doc_operador, tiempo_venta, forma_de_pago, codigo_2, nom_ape_operador[0], nom_ape_operador[1]])

                        # consulto el num_factura en tabla ventas
                        sql = f"SELECT `num_factura` FROM `ventas` WHERE codigo_tabla = '{codigo_2}'"
                        conn = mysql.connect()
                        cursor = conn.cursor()     
                        cursor.execute(sql)
                        num_factura = cursor.fetchall()
                        conn.commit()

                        #consulto el numero de productos seleccionados
                        sql = "SELECT SUM(cantidad_adquirida) FROM `carritoventas`"
                        conn = mysql.connect()
                        cursor = conn.cursor()     
                        cursor.execute(sql)
                        cantidad_productos = cursor.fetchall()
                        conn.commit()

                        # Insertacion en la tabla detalleventas 
                        Dventas.crearDetalleventa([num_factura[0][0], productos_fac[0][0], cantidad_productos[0][0], Suma_total[0][0], Suma_total[0][0]])

                        #  Elimino toda la info del carritoventas
                        sql = "DELETE FROM `carritoventas`"
                        conn = mysql.connect()
                        cursor = conn.cursor()     
                        cursor.execute(sql)
                        conn.commit()

                        # consulta los productos seleccionados para venta
                        sql = "SELECT `contador`, `nombre_producto`, `precio_venta`, `cantidad_adquirida`, `total` FROM `carritoventas`"
                        conn = mysql.connect()
                        cursor = conn.cursor()     
                        cursor.execute(sql)
                        productos_carr_2 = cursor.fetchall()
                        conn.commit()

                        mensaje_exitoso = "Venta_realizada_normal" #¡Venta realizada!
                        return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr_2, Total = 0, operador = documento_operador, mensaje = mensaje_exitoso) 



                    # 4
                    else:

                        Dventas.crear_venta_credito([doc_cliente, productos_fac[0][0], Suma_total[0][0], Suma_total[0][0], doc_operador, tiempo_venta, ])

                        #  Elimino toda la info del carritoventas
                        sql = "DELETE FROM `carritoventas`"
                        conn = mysql.connect()
                        cursor = conn.cursor()     
                        cursor.execute(sql)
                        conn.commit()

                                                # consulta los productos seleccionados para venta
                        sql = "SELECT `contador`, `nombre_producto`, `precio_venta`, `cantidad_adquirida`, `total` FROM `carritoventas`"
                        conn = mysql.connect()
                        cursor = conn.cursor()     
                        cursor.execute(sql)
                        productos_carr_2 = cursor.fetchall()
                        conn.commit()

                        mensaje_exitoso = "listo_credito" #¡Venta a credito realizada!
                        return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr_2, Total = 0, operador = documento_operador, mensaje = mensaje_exitoso)




                # 3
                else:
                    mensaje_error = 3#¡El cliente no existe en la base de datos!
                    return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = Suma_total[0][0], operador = documento_operador, mensaje = mensaje_error) 

            # 2
            else:
                mensaje_error = 2 #¡Identificacion del operador invalida!
                return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = Suma_total[0][0], operador = documento_operador, mensaje = mensaje_error) 
        #  1 
        else:
            # envio mensaje del error
            mensaje_error = 1#¡No hay productos seleccionados!
            # muestra el HTML registrar_venta
            return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = 0, operador = documento_operador, mensaje = mensaje_error) 
            
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))
    
#-------------------------------------------------------- Cancelador ventas a credito ----------------------------------------------------------------

@app.route("/cancela_venta_c/<contador>")
def cancela_venta_c(contador):
    if "nom_empleado" in session:

        # funciona al validar q se pago completo el credito 
        print(f" porque nooooo\n{contador}\n")
        #Ventas.venta_cancelada_cred(contador)
        sql = f"UPDATE `ventas_credito` SET `estado`='PAGADA' WHERE contador = '{contador}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        conn.commit()
        return redirect("/muestra_ventas_credito")

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))
    
#---------------------------------------- Elimina Todos los productos seleccionados -------------------------------------------
@app.route("/elimina_todo_seleccionado_p")
def elimina_todo_seleccionado_p():
    if "nom_empleado" in session:

        # consulto todos los contadores de carrito_ventas
        sql = "SELECT `contador` FROM `carritoventas`"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        contadores = cursor.fetchall()
        conn.commit()

        # 1 - Valido que aigan productos para eliminar
        if ((len(contadores)) > 0):

            # saco la consulta de [[]] 2 listas a una sola []
            contador_2 = contadores[0]

            # realizo el FOR que elimine uno por uno
            for i in range(len(contador_2)):



                # consulto el id_producto 
                sql = f"SELECT `id_producto` FROM `carritoventas` WHERE contador = '{contador_2[i]}'" # <---- i es el CONTADOR
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                id_pro = cursor.fetchall()
                conn.commit()
                id_producto = id_pro[0][0]

                # consulto el stock disponible que tiene el producto 
                sql = f"SELECT `cantidad_producto` FROM `productos` WHERE id_producto = '{id_producto}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                stock_disponible = cursor.fetchall()
                conn.commit()

                # consulto la cantidad seleccionada del producto en el carrito ventas
                sql = f"SELECT `cantidad_adquirida` FROM `carritoventas` WHERE id_producto = '{id_producto}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                cantidad_adquirida = cursor.fetchall()
                conn.commit()

                # sumo al stock disponible la cantidad que adquirida
                stock_disponible = (stock_disponible[0][0] + cantidad_adquirida[0][0])

                # inserto el nuevo stock en la base de datos
                sql = f"UPDATE `productos` SET `cantidad_producto` = '{stock_disponible}' WHERE id_producto = '{id_producto}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                conn.commit()

                # borro el producto seleccionado de la tabla carrito_ventas
                sql = f"DELETE FROM `carritoventas` WHERE id_producto = '{id_producto}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                conn.commit()

            return redirect("/verCrear_ventas")


        # 1
        else:

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

            mensaje_error = "No_hay_productos_seleccionados_para_eliminar" #¡No hay productos seleccionados para eliminar!
            return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = 0, operador = documento_operador, mensaje = mensaje_error) 



    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))


#---------------------------------------- Elimina productos 1 por 1 seleccionados -------------------------------------------
@app.route("/elimina_p_select/<contador>")
def elimina_p_select(contador):
    if "nom_empleado" in session:

        # consulto el id_producto 
        sql = f"SELECT `id_producto` FROM `carritoventas` WHERE contador = '{contador}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        id_pro = cursor.fetchall()
        conn.commit()
        id_producto = id_pro[0][0]

        # consulto el stock disponible que tiene el producto 
        sql = f"SELECT `cantidad_producto` FROM `productos` WHERE id_producto = '{id_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        stock_disponible = cursor.fetchall()
        conn.commit()

        # consulto la cantidad seleccionada del producto en el carrito ventas
        sql = f"SELECT `cantidad_adquirida` FROM `carritoventas` WHERE id_producto = '{id_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        cantidad_adquirida = cursor.fetchall()
        conn.commit()

        # sumo al stock disponible la cantidad que adquirida
        stock_disponible = (stock_disponible[0][0] + cantidad_adquirida[0][0])

        # inserto el nuevo stock en la base de datos
        sql = f"UPDATE `productos` SET `cantidad_producto`='{stock_disponible}' WHERE id_producto = '{id_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        conn.commit()

        # borro el producto seleccionado de la tabla carrito_ventas
        sql = f"DELETE FROM `carritoventas` WHERE id_producto = '{id_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        conn.commit()

        return redirect("/verCrear_ventas")

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))

    


#---------------------------------------- Selector de 1 cantidad solo producto para Ventas -------------------------------------------
@app.route("/selector_una_cantidad/<id_producto>")
def selector_una_cantidad(id_producto):
    if "nom_empleado" in session:

        cantidad_adquirida = 1

        # consulto la cantidad disponible del prodcuto
        sql = f"SELECT `cantidad_producto` FROM `productos` WHERE id_producto = '{id_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        stock = cursor.fetchall()
        conn.commit()

         # 1 - valido si la cantidad digitada es menor a la disponible 
        if (stock[0][0] > cantidad_adquirida) or (stock[0][0] == 1 and cantidad_adquirida == 1):

            # consulto la informacion del producto
            sql = f"SELECT `nombre_producto`, `precio_venta`, `cantidad_producto` FROM `productos` WHERE id_producto = '{id_producto}'"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql)
            info_producto = cursor.fetchall()
            conn.commit()

            # saco la consulta de [[]] 2 listas a una sola []
            info_producto_2 = info_producto[0] 

            # actualizo el stock disponible del producto
            stock_disponible = (info_producto_2[2] - cantidad_adquirida)
            sql = f"UPDATE `productos` SET `cantidad_producto` = '{stock_disponible}' WHERE id_producto = '{id_producto}'"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql)
            conn.commit()

            # 2 consulto si la cantidad  adquirida en el carrito ventas
            sql = f"SELECT `cantidad_adquirida` FROM `carritoventas` WHERE id_producto = {id_producto}"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql)
            cantidad_carrito = cursor.fetchall()
            conn.commit()

            print(f"\n {id_producto} {cantidad_carrito} \n")
            
            # 2 - valido si ya esta seleccionado el producto
            if ((len(cantidad_carrito)) > 0):
                

                # sumamos la cantidad ya seleccionado con lo digitado
                cantidad_total_adqui = (cantidad_carrito[0][0] + cantidad_adquirida)

                # saco el nuevo total a pagar
                total = (cantidad_total_adqui * info_producto_2[1])

                # actualizo la info del registro de carrito venta
                sql = f"UPDATE `carritoventas` SET `cantidad_adquirida`='{cantidad_total_adqui}',`total`='{total}' WHERE id_producto = '{id_producto}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                conn.commit()

                return redirect("/verCrear_ventas")



            # 2
            else:

                # inserto los datos en la tabla Carrito ventas
                sql = f"INSERT INTO `carritoventas`(`id_producto`, `nombre_producto`, `precio_venta`, `cantidad_adquirida`, `total`) VALUES ('{id_producto}','{info_producto_2[0]}','{info_producto_2[1]}','{cantidad_adquirida}','{info_producto_2[1]}')"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                conn.commit()

                return redirect("/verCrear_ventas")

        # 1
        else:

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

            mensaje_error = "La_cantidad_solicitada_es_menor_a_la_disponible" #¡La cantidad solicitada es menor a la disponible!

            if Suma_total[0][0] is not None:            
                return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = Suma_total[0][0], operador = documento_operador, mensaje_2 = mensaje_error) 
            else:
                return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = 0, operador = documento_operador, mensaje_2 = mensaje_error) 


    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))


#---------------------------------------- Selector de productos para Ventas -------------------------------------------
@app.route("/m_selector_cantidad_p/<id_producto>")
def m_selector_cantidad_p(id_producto):
    if "nom_empleado" in session:

        sql = f"SELECT `nombre_producto`, `precio_venta`, `cantidad_producto` FROM `productos` WHERE id_producto = '{id_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        info_producto = cursor.fetchall()
        conn.commit()

        # muestra el html producto_seleccionado donde se digitara la cantidad a comprar del producto
        return render_template('ventas/producto_seleccionado.html',id_p = id_producto, nom_p = info_producto[0])

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))
    


# ------------ Recibe la informacion del FRON-END ---------------------

@app.route("/confirma_p_seleccionado", methods = ['POST'])
def confirma_p_seleccionado():
    if "nom_empleado" in session:
        
        # informacion del FRONT-END
        id_producto = request.form['id_producto']
        nombre_producto = request.form['nombre_producto']
        precio_unidad = request.form['precio_unidad']           
        stock_disponible = request.form['Stock_disponible']
        cantidad_digitada = request.form['cantidad_digitada']

        # covierto los valores de texto a numeros 
        precio_unidad = float(precio_unidad)
        stock_disponible = int(stock_disponible)
        cantidad_digitada = int(cantidad_digitada)

        # consulto la cantidad disponible del prodcuto
        sql = f"SELECT `cantidad_producto` FROM `productos` WHERE id_producto = '{id_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()     
        cursor.execute(sql)
        stock = cursor.fetchall()
        conn.commit()


        # 1 - valido si la cantidad digitada es menor a la disponible 
        if (stock[0][0] > cantidad_digitada) or (stock[0][0] == 1 and cantidad_digitada == 1):
            
            sql = f"SELECT `cantidad_adquirida` FROM `carritoventas` WHERE id_producto = '{id_producto}'"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql)
            cantidad_carrito = cursor.fetchall()
            conn.commit()
            
            # 2 - valido si ya esta seleccionado el producto
            if ((len(cantidad_carrito)) > 0):

                # Actualizo el stock disponible del producto 
                stock_disponible = (stock_disponible - cantidad_digitada)

                # Actualizo el stock en la base de datos
                sql = f"UPDATE `productos` SET `cantidad_producto` = '{stock_disponible}' WHERE id_producto = '{id_producto}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                conn.commit()

                # sumamos la cantidad ya seleccionado con lo digitado
                cantidad_total_adqui = (cantidad_carrito[0][0] + cantidad_digitada)

                # saco el nuevo total a pagar
                total = (cantidad_total_adqui * precio_unidad)

                # actualizo la info del registro de carrito venta
                sql = f"UPDATE `carritoventas` SET `cantidad_adquirida`='{cantidad_total_adqui}',`total`='{total}' WHERE id_producto = '{id_producto}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                conn.commit()

                return redirect("/verCrear_ventas")


            # 2 inserta normal
            else:
                # Saco el total a pagar por la catidad digitada
                total = (precio_unidad * cantidad_digitada)

                # Actualizo el stock disponible del producto 
                stock_disponible = (stock_disponible - cantidad_digitada)

                # Actualizo el stock en la base de datos
                sql = f"UPDATE `productos` SET `cantidad_producto` = '{stock_disponible}' WHERE id_producto = '{id_producto}'"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                conn.commit()

                # inserto los datos en la tabla Carrito ventas
                sql = f"INSERT INTO `carritoventas`(`id_producto`, `nombre_producto`, `precio_venta`, `cantidad_adquirida`, `total`) VALUES ('{id_producto}','{nombre_producto}','{precio_unidad}','{cantidad_digitada}','{total}')"
                conn = mysql.connect()
                cursor = conn.cursor()     
                cursor.execute(sql)
                conn.commit()

                return redirect("/verCrear_ventas")
        
        # 1
        else:
            sql = f"SELECT `nombre_producto`, `precio_venta`, `cantidad_producto` FROM `productos` WHERE id_producto = '{id_producto}'"
            conn = mysql.connect()
            cursor = conn.cursor()     
            cursor.execute(sql)
            info_producto = cursor.fetchall()
            conn.commit()

            mensaje_error = "¡Cantidad dijitada mayor a la disponible en el stock!"
        
            return render_template('ventas/producto_seleccionado.html',id_p = id_producto, nom_p = info_producto[0], mensaje_Error = mensaje_error)


    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))

#---------------------------------------- Buscador de productos en Ventas -------------------------------------------
@app.route("/Busca_produc_ven", methods = ['POST'])
def Busca_produc_ven():
    if "nom_empleado" in session:

        busqueda = request.form['id_nombre']

        # Muestra el documento del operador
        documento_operador = session["documento_operador"]

        # consulta los productos del inventario segun la busqueda realizada
        sql = f"SELECT `id_producto`, `ref_produ_1` , `nombre_producto`, `precio_venta`, `cantidad_producto` FROM `productos`  WHERE estado_producto ='ACTIVO' AND referencia_producto LIKE '%{busqueda}%' OR estado_producto='ACTIVO' AND nombre_producto LIKE '%{busqueda}%'"
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

        # le asigno el 0 si la suma es none
        if Suma_total[0][0] is not None:
            return render_template('ventas/registrar_venta.html', prod = productos_inven, prod_carr = productos_carr, Total = Suma_total[0][0], operador = documento_operador) 
        else:
             return render_template('ventas/registrar_venta.html', prod = productos_inven, prod_carr = productos_carr, Total = 0, operador = documento_operador) 
 

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))


#--------------------------------------------- Muestra registro de venta----------------------------------------------
@app.route("/verCrear_ventas")
def verCrear_ventas():
    if "nom_empleado" in session:

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

            # le asigno el 0 si la suma es none
            if Suma_total[0][0] is not None:
                return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = Suma_total[0][0], operador = documento_operador) 
            else:
                return render_template('ventas/registrar_ventas.html', prod = productos_inven, prod_carr = productos_carr, Total = 0, operador = documento_operador) 
        