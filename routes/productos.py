import sys
from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.productos import Dproductos




@app.route('/productos')
def productos():
        if "nom_empleado" in session: 
            sql = "SELECT * FROM productos WHERE estado_producto ='ACTIVO'"
            conn = mysql.connect()                    
            cursor = conn.cursor()
            cursor.execute(sql)                                          
            resultado = cursor.fetchall()
            return render_template('/productos/muestra_productos.html', resulta = resultado)
        else:
            flash('Porfavor inicia sesion para poder acceder')
            return redirect(url_for('index'))
        


@app.route('/crear_Producto', methods=['GET', 'POST'])
def crear_Producto():
    print("Entrando a crear_Producto")
    if "nom_empleado" in session:
        if request.method == 'POST':
            doc = session["nom_empleado"]
            bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq)
            resultado = cursor.fetchone()
            print("Voy por aca", resultado)
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]
            proveedores_activos= request.form['proveedor']
            print(proveedores_activos)
            sql = f"SELECT nom_proveedor FROM proveedores WHERE doc_proveedor='{proveedores_activos}' AND estado_proveedor = 'ACTIVO'"
            cursor.execute(sql)
            proveedores = cursor.fetchall()
            
            nom_proveedor = proveedores[0]
            print(nom_proveedor)
            referencia_producto = request.form['referencia_producto']
            ref_prod_2 = request.form['ref_prod_2']
            ref_prod_3 = request.form['ref_prod_3']
            categoria = request.form['categorias']
            nombre_producto = request.form['nombre_producto']
            precio_compra = request.form['precio_compra']
            precio_venta = request.form['precio_venta']
            cantidad_producto = request.form['cantidad_producto']
            descripcion = request.form['descripcion']
            stockminimo = request.form['stockminimo']
            ubicacion = request.form['ubicacion']
            estante = request.form['estante']
            tiempoRegistro = datetime.datetime.now()

            
            Dproductos.crearProductos([referencia_producto, ref_prod_2, ref_prod_3, categoria, proveedores_activos, nom_proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante, tiempoRegistro, documento_registro, nombre_operador, apellido_operador])
            return redirect(url_for('muestra_Productos'))
            
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT doc_proveedor, nom_proveedor FROM proveedores WHERE estado_proveedor = 'ACTIVO'"
        cursor.execute(sql)
        proveedores_activos = cursor.fetchall()

        sql = "SELECT id_categoria, nom_categoria FROM categorias WHERE  estado_categorias = 'ACTIVO'"
        cursor.execute(sql)
        categorias_activas = cursor.fetchall()

        print("Proveedor encontrado. Redirigiendo a la página de selección de proveedores.",proveedores_activos)
        print("Categorias", categorias_activas)
        return render_template('/productos/registrar_productos.html', proveedores=proveedores_activos, categorias=categorias_activas)
                        

@app.route('/muestra_productos')
def muestra_Productos():
    if "nom_empleado" in session: 
        sql = "SELECT  p.referencia_producto, p.ref_produ_2, p.ref_produ_3, c.nom_categoria, p.nom_proveedor, p.nombre_producto, p.precio_compra, p.precio_venta, p.cantidad_producto, p.descripcion, p.stockminimo, p.ubicacion, p.estante FROM productos p JOIN categorias c ON p.categoria = c.id_categoria WHERE p.estado_producto ='ACTIVO';" # se realiza un join para la consulta, con la unión de la tabla categoría para obtener el nombre de la categoría en lugar de su ID.
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()
        if (len(resultado) >= 1):
            return render_template("/productos/muestra_productos.html", resul=resultado)   # si hay resultados se muestran.
        else:
            resultado2 = "No hay productos registrados"
            return render_template("/productos/muestra_productos.html", resul2=resultado2)  # sino se muestra el mensaje de resultado2.
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
 



@app.route('/Busca_productos', methods=['POST'])
def busca_productos():
    dato_busqueda = request.form['dato_busqueda']
    sql = f"SELECT `id_producto`, `referencia_producto`, `categoria`, `proveedor`, `nombre_producto`, `precio_compra`, `precio_venta`, `cantidad_producto`, `descripcion`, `stockminimo`, `ubicacion`, `estante`, `estado_producto`, `nombre_proveedor` FROM `productos` WHERE estado_producto='activo' AND id_producto LIKE '%{dato_busqueda}%' OR estado_producto='activo' AND nombre_producto LIKE '%{dato_busqueda}%' OR estado_producto='activo' AND categoria LIKE '%{dato_busqueda}%' OR estado_producto='activo' AND 'descripcion' LIKE '%{dato_busqueda}'"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)             # puede buscar por doc_empleado,nom_empleado y ape_empleado
    resultado = cursor.fetchall()  
    conn.commit()
    return render_template("/productos/muestra_productos.html", resul=resultado)



@app.route("/modificar_producto/<referencia_producto>")
def editar_producto(referencia_producto):
    print("Entrando a editar un Producto")
    if "nom_empleado" in session: 
        sql = f"SELECT `referencia_producto`, `categoria`, nom_categoria, `proveedor`, `nom_proveedor`, `nombre_producto`, `precio_compra`, `precio_venta`, `cantidad_producto`, `descripcion`, `stockminimo`, `ubicacion`, `estante` FROM productos WHERE referencia_producto='{referencia_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()  
        conn.commit()
        return render_template("productos/edita_productos.html", resul= resultado[0])
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))      


@app.route('/modificar_Producto', methods=['POST', 'GET'])
def modificar_Producto():
    print("entrando a modificar")
    if "nom_empleado" in session:
        doc = session["nom_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsq)
        resultado = cursor.fetchone()
        print("Soy el empleado")
        documento_registro = resultado[0]
        nombre_operador = resultado[1]
        apellido_operador = resultado[2]
        referencia_producto = request.form['referencia_producto']
        categoria = request.form['categoria']
        proveedor = request.form['proveedor']
        nombre_producto = request.form['nombre_producto']
        precio_compra = request.form['precio_compra']
        precio_venta = request.form['precio_venta']
        cantidad_producto = request.form['cantidad_producto']
        descripcion = request.form['descripcion']
        stockminimo = request.form['stockminimo']
        ubicacion = request.form['ubicacion']
        estante = request.form['estante']
        Dproductos.modificar([referencia_producto, categoria, proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante, documento_registro, nombre_operador, apellido_operador])
        return redirect('/muestra_productos')
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))
 

@app.route('/borra_produc/<idprod>')
def borra_produc(idprod):
    if "nom_empleado" in session: 
        Dproductos.borrar_producto(idprod)        # Eliminar productos
        return redirect("/muestra_productos")   
    else:
        flash('Algo esta mal en los datos digitados')
        return redirect(url_for('home'))
    
