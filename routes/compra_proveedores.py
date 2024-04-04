import random
import string
import sys
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.compra_proveedores import Dcompra_proveedores

# ------------- registra compras  --------------


@app.route("/Registrar_compra_p", methods=['POST'])
def Registrar_compra_p():
    if "nom_empleado" in session:
        # Obtener datos del operador de sesión
        doc = session["nom_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsq)
        resultado = cursor.fetchone()

        documento_operador = resultado[0]
        nombre_operador = resultado[1]
        apellido_operador = resultado[2]

        # Obtener datos de la compra
        num_factura_proveedor = request.form['num_factura_proveedor']
        proveedor_compra = request.form['proveedor_compra']
        fecha_compra = request.form['fecha_compra']

        # Generar un código aleatorio para la compra
        codigo_2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        

        # Insertar datos de la compra en la tabla de comprasproveedores
       
        tiempo_compra = datetime.datetime.now()
        Dcompra_proveedores.registrar_compra([proveedor_compra, fecha_compra, documento_operador, nombre_operador, apellido_operador, tiempo_compra, num_factura_proveedor, codigo_2])



        sql = f"SELECT num_compra FROM comprasproveedores WHERE codigo_tabla = '{codigo_2}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        num_compra = cursor.fetchall()   
        conn.commit()
        num = num_compra[0][0] 

        productos = request.form.getlist('producto_compra[]')
        cantidades = request.form.getlist('cantidad_compra[]')
        valores = request.form.getlist('valor_unidad[]')

        for i in range(len(productos)):
            cantidad = cantidades[i]
            valor = valores[i]
            total = float(valor) * int(cantidad)
            Dcompra_proveedores.registrar_detalles_compra([num, productos[i], cantidad, valor, total, total])
            
        flash('¡Se registraron los productos con éxito!')
        
        return redirect("/muestra_compra_proved")
    else:
        flash('No se ha iniciado sesión')
        return redirect("/login")


# ------------- cancela compras -------

@app.route("/cancelar_compra_proveed/<num_compra>", methods=['POST'])
def cancelar_compra_proveed(num_compra):
    if "nom_empleado" in session:

        Dcompra_proveedores.cacela_compra(num_compra)
        return redirect("/muestra_compra_proved")

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))



# ------- editar detalles de compras a proveedores -----

@app.route("/edita_compras_provee/<num_compra>")
def edita_compras_provee(num_compra):
    if "nom_empleado" in session:
        sql = (
            f"SELECT cp.`num_compra`, "
            f"cp.`proveedor_compra`, "
            f"p.`nom_proveedor`, "
            f"cp.`fecha_compra`, "
            f"cp.`num_factura_proveedor`, "
            f"cp.`estado`, "
            f"dcp.`id_detalle_compra`, "
            f"dcp.`detallenum_compra`, "
            f"dcp.`producto_compra`, "
            f"dcp.`cantidad_producto_compra`, "
            f"dcp.`valorunidad_prodcompra`, "
            f"dcp.`valortotal_cantidadcomp`, "
            f"dcp.`totalpagar_compra` "
            f"FROM `comprasproveedores` cp "
            f"INNER JOIN `detallecomprasproveedores` dcp ON cp.`num_compra` = dcp.`detallenum_compra` "
            f"INNER JOIN `proveedores` p ON cp.`proveedor_compra` = p.`doc_proveedor` "
            f"WHERE cp.`num_compra` = '{num_compra}'"
        )
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("Resultado de la consulta:", resultado)

        if resultado:  # Verifica si la tupla no está vacía
            conn.commit()
            return render_template("/compra_proveedores/edita_compras_prove.html", resul=resultado[0])
        else:
            flash('Compra no encontrada')
            return redirect(url_for('muestra_compra_proved'))

    else:
        flash('Por favor, inicia sesión para poder acceder')
        return redirect(url_for('index'))



@app.route("/actualiza_compra_provee", methods=['POST'])
def actualiza_compra_provee():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "almacenista":

            num_compra = request.form['num_compra']
            detallenum_compra = request.form['detallenum_compra']
            producto_compra = request.form['producto_compra']
            cantidad_compra = int(request.form['cantidad_compra'])
            valorunidad_prodcompra = float(request.form['valorunidad_prodcompra'])
            valor_total_unidad = cantidad_compra * valorunidad_prodcompra

            fecha_compra = request.form['fecha_compra']
            num_factura_proveedor = request.form['num_factura_proveedor']
            
            Dcompra_proveedores.edita_detalles_compra((num_compra, detallenum_compra, producto_compra, cantidad_compra, valorunidad_prodcompra, valor_total_unidad, fecha_compra, num_factura_proveedor))



            return redirect("/muestra_compra_proved")

            return redirect("/muestra_compra_proved")
    
        else:
            return redirect("/inicio")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))






@app.route("/muestra_compra_proved")
def muestra_compra_proved():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "almacenista":

            sql ="SELECT cp.`num_compra`, cp.`num_factura_proveedor`, cp.`proveedor_compra`,  p.`nom_proveedor`,  CONCAT(cp.`nombre_operador`, ' ', cp.`apellido_operador`) AS nombre_completo, cp.`fecha_compra`, `direccion_proveedor` FROM `comprasproveedores` cp JOIN `proveedores` p ON cp.`proveedor_compra` = p.`doc_proveedor` WHERE cp.`estado` = 'ACTIVO'"
            sql_proveedor = "SELECT doc_proveedor, nom_proveedor FROM proveedores WHERE estado_proveedor = 'ACTIVO'"
            with mysql.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    datos = cursor.fetchall()
                    cursor.execute(sql_proveedor)
                    Proveedor = cursor.fetchall()
        return render_template("/compra_proveedores/muestra_compras_prove.html", resul=datos, prove = Proveedor) 
    
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    

# ------------- muestra detalles de compras a proveedores ----------

@app.route("/muestra_detalles_com/<num_compra>")
def muestra_detalles_com(num_compra):
    if "nom_empleado" in session:
        rol_usuario = session["rol"]

        if rol_usuario == "administrador" or rol_usuario == "almacenista":
        
            sql =  f"SELECT `num_factura_proveedor`, `fecha_compra` FROM `comprasproveedores`  WHERE  num_compra = '{num_compra}' "

            bsql = f"SELECT  `detallenum_compra`, `producto_compra`, `cantidad_producto_compra`, `valorunidad_prodcompra`, `valortotal_cantidadcomp` FROM `detallecomprasproveedores` WHERE `detallenum_compra` = '{num_compra}'  "

            
            with mysql.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    resultado = cursor.fetchall()

                    cursor.execute(bsql)
                    detalle = cursor.fetchall()

                    cursor.execute(sql)
                    compra = cursor.fetchall()
            total_cantidad = sum(row[4] for row in detalle)

            return render_template("/compra_proveedores/detalles_compras/muestra_detalles.html", resul=detalle, result1=compra, total=total_cantidad)

        else:
            return redirect("/inicio")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    


@app.route("/buscador_compraproveedor", methods=['POST', 'GET'])
def buscador_compraproveedor():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "vendedor":
            busqueda = request.form['BuscaCompraProveedores']
            sql = "SELECT cp.`num_compra`, cp.`num_factura_proveedor`, cp.`proveedor_compra`,  p.`nom_proveedor`,  CONCAT(cp.`nombre_operador`, ' ', cp.`apellido_operador`) AS nombre_completo, cp.`fecha_compra`, `direccion_proveedor` FROM `comprasproveedores` cp JOIN `proveedores` p ON cp.`proveedor_compra` = p.`doc_proveedor` WHERE (cp.`estado`='ACTIVO') AND (p.`nom_proveedor` LIKE %s OR cp.`num_factura_proveedor` LIKE %s)"
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