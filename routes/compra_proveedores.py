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

        doc = session["nom_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsq)                         # recibe la info y consulta los datos del operador
        resultado = cursor.fetchone()

        documento_operador = resultado[0]
        nombre_operador = resultado[1]
        apellido_operador = resultado[2]

        proveedor_compra = request.form['proveedor_compra']
        fecha_compra = request.form['fecha_compra']
        num_factura_proveedor = request.form['num_factura_proveedor']
        producto_compra = request.form['producto_compra']
        Cantidad_compra = request.form['cantidad_compra']
        cantidad_compra = int(Cantidad_compra)
        valor_unidad = request.form['valor_unidad']
        valor_total_unidad = (valor_unidad*cantidad_compra)
        tiempo_compra = datetime.datetime.now()

        lower = string.ascii_lowercase       
        upper = string.ascii_uppercase # generador de codigo 
        num = string.digits 
        chars = lower + upper + num
        codigo = random.sample(chars, 10)
        codigo_2 = ""  # variable que guarda el codigo
        for c in codigo:
            codigo_2+=c
        print(f"\n {codigo_2} \n")

        Dcompra_proveedores.registrar_compra([proveedor_compra, fecha_compra, documento_operador, nombre_operador, apellido_operador, tiempo_compra, num_factura_proveedor, codigo_2])   # se incerta los datos en la primera tabla
        
        
        sql = f"SELECT num_compra FROM comprasproveedores WHERE codigo_tabla = '{codigo_2}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        num_compra = cursor.fetchall()   # consulta el numero de compra de acuerdo al  codigo de esa tabla
        conn.commit()
        num = num_compra[0][0] # [[N]] ----> N 
        total = valor_unidad * cantidad_compra
        
        Dcompra_proveedores.registrar_detalles_compra([num, producto_compra, cantidad_compra, valor_unidad, valor_total_unidad, total ])   # se incerta los datos en la segunda tabla
        flash('¡Se registro con exito!')
        return redirect("/muestra_compra_proved")

    


# ------------- cancela compras -------

@app.route("/cancelar_compra_proveed/<num_compra>")
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
            f"SELECT d.`id_detalle_compra`, d.`detallenum_compra`, d.`producto_compra`, "
            f"d.`cantidad_producto_compra`, "
            f"d.`valorunidad_prodcompra`, "
            f"d.`valortotal_cantidadcomp`, "
            f"d.`totalpagar_compra`, "
            f"cp.`num_factura_proveedor` "
            f"FROM `detallecomprasproveedores` d "
            f"JOIN `comprasproveedores` cp ON d.`detallenum_compra` = cp.`num_compra` "
            f"WHERE d.`detallenum_compra` = '{num_compra}'"
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
            producto_compra = request.form['producto_compra']
            cantidad_compra = request.form['cantidad_compra']
            valor_unidad = request.form['valor_unidad']
            valor_total_unidad = (cantidad_compra*valor_unidad)
            
            Dcompra_proveedores.edita_detalles_compra([num_compra, producto_compra, cantidad_compra, valor_unidad, valor_total_unidad])

            return redirect("/muestra_compra_proved")
    
        else:
            return redirect("/inicio")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))



# ------------- buscador --------------

""" @app.route("/busca_compras_prov", methods=['POST', 'GET'])
def busca_compras_prov():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "almacenista":

            if request.method == 'POST':
                dato_busqueda = request.form['dato_busqueda']
                sql = f"SELECT `num_compra`, `proveedor_compra`, `documento_operador`, `nombre_operador`, `apellido_operador`, `date_compra`, `num_factura_proveedor` FROM `comprasproveedores` WHERE estado='activo' AND (num_compra LIKE '%{dato_busqueda}%' OR proveedor_compra LIKE '%{dato_busqueda}%')"
                conn = mysql.connect()
                cursor = conn.cursor()                  # muestra las compras a proveedores dependiendo de la busqueda
                cursor.execute(sql)
                resultado = cursor.fetchall()  
                conn.commit()
                return render_template("/compra_proveedores/muestra_compras_prove.html", resul=resultado)
            return redirect('muestra_compra_proved')
        
        else:
            return redirect("/inicio")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index')) """


# --------- muestra compras a proveedores -------

@app.route("/muestra_compra_proved")
def muestra_compra_proved():
    if "nom_empleado" in session:
        rol_usuario = session["rol"]
        if rol_usuario == "administrador" or rol_usuario == "almacenista":

            sql ="SELECT cp.`num_compra`, cp.`proveedor_compra`,  p.`nom_proveedor`, cp.`num_factura_proveedor`, CONCAT(cp.`nombre_operador`, ' ', cp.`apellido_operador`) AS nombre_completo, cp.`fecha_compra`, `direccion_proveedor` FROM `comprasproveedores` cp JOIN `proveedores` p ON cp.`proveedor_compra` = p.`doc_proveedor` WHERE cp.`estado` = 'ACTIVO'"
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
        
            sql =  f"""
                SELECT 
                    dc.detallenum_compra, 
                    dc.producto_compra, 
                    dc.cantidad_producto_compra, 
                    dc.valorunidad_prodcompra, 
                    dc.valortotal_cantidadcomp, 
                    dc.totalpagar_compra 
                FROM 
                    detallecomprasproveedores dc
                JOIN 
                    comprasproveedores cp ON dc.detallenum_compra = cp.num_compra
                WHERE 
                    dc.detallenum_compra = '{num_compra}' and num_compra = '{num_compra}'
            """
            conn = mysql.connect()
            cursor = conn.cursor()                  # muestra los detalles de compras a proveedores
            cursor.execute(sql)
            resultado = cursor.fetchall() 
            print("estos datos:", resultado) 
            conn.commit()
            return render_template("/compra_proveedores/detalles_compras/muestra_detalles.html", resul=resultado)

        else:
            return redirect("/inicio")
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
    
