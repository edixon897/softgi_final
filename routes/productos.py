from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.productos import Dproductos




@app.route('/productos')
def productos():
        return render_template('/productos/muestra_productos.html')
    
        
@app.route('/crear_producto', methods=['POST', 'GET'])
def crearProducto():
    if "doc_empleado" in session:
        conn = mysql.connect()
        cursor = conn.cursor() 
        sql = "SELECT `nom_categoria` FROM `categorias` WHERE estado_categorias ='ACTIVO'"
        cursor.execute(sql)                                          
        categoriaResul = cursor.fetchall()

        sql = f"SELECT doc_proveedor, nom_proveedor FROM proveedores WHERE estado_proveedor = 'ACTIVO'"
        cursor.execute(sql)
        resultado2 = cursor.fetchall()
        if request.method == 'POST':
            email = session["doc_empleado"]
            bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE doc_empleado='{email}'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(bsq)
            resultado = cursor.fetchone()
            documento_registro = resultado[0]
            nombre_operador = resultado[1]
            apellido_operador = resultado[2]
            proveedor = request.form['proveedor']
           
            referencia_producto = request.form['referencia_producto']
            categoria = request.form['categoria']
            nombreProveedor = resultado2[1]
            
            nombre_producto = request.form['nombre_producto']
            precio_compra = request.form['precio_compra']
            precio_venta = request.form['precio_venta']
            cantidad_producto = request.form['cantidad_producto']
            descripcion = request.form['descripcion']
            stockminimo = request.form['stockminimo']
            ubicacion = request.form['ubicacion']
            estante = request.form['estante']
            tiempoRegistro = datetime.datetime.now()
            estado = 'ACTIVO'
            Dproductos.crearProductos([ referencia_producto, categoria, proveedor, nombreProveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante, tiempoRegistro, documento_registro, nombre_operador, apellido_operador,  estado])
            return redirect('/muestra_productos')
        
        
        return render_template('/productos/registrar_productos.html', result = categoriaResul, result2 = resultado2)
    else:
        flash('Algo esta mal en los datos digitados')
        return redirect(url_for('index'))




@app.route('/muestra_productos')
def muestra_Productos():
    if "doc_empleado" in session:
        sql = "SELECT  p.referencia_producto, c.nom_categoria, p.proveedor, p.nombre_proveedor, p.nombre_producto, p.precio_compra, p.precio_venta, p.cantidad_producto, p.descripcion, p.stockminimo, p.ubicacion, p.estante FROM productos p JOIN categorias c ON p.categoria = c.id_categoria WHERE p.estado_producto ='ACTIVO';" # se realiza un join para la consulta, con la unión de la tabla categoría para obtener el nombre de la categoría en lugar de su ID.
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
def Busca_productos():
    dato_busqueda = request.form['dato_busqueda']
    sql = f"SELECT `id_producto`, `referencia_producto`, `categoria`, `proveedor`, `nombre_producto`, `precio_compra`, `precio_venta`, `cantidad_producto`, `descripcion`, `stockminimo`, `ubicacion`, `estante`, `estado_producto`, `nombre_proveedor` FROM `productos` WHERE estado_producto='activo' AND id_producto LIKE '%{dato_busqueda}%' OR estado_producto='activo' AND nombre_producto LIKE '%{dato_busqueda}%' OR estado_producto='activo' AND categoria LIKE '%{dato_busqueda}%' OR estado_producto='activo' AND 'descripcion' LIKE '%{dato_busqueda}'"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)             # puede buscar por doc_empleado,nom_empleado y ape_empleado
    resultado = cursor.fetchall()  
    conn.commit()
    return render_template("/productos/muestra_productos.html", resul=resultado)



@app.route("/modificar_producto/<id_producto>")
def editar_producto(id_producto):
    if "doc_empleado" in session:
        sql = f"SELECT * FROM productos WHERE id_producto='{id_producto}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()  
        conn.commit()
        return render_template("/productos/edita_productos.html", resul= resultado)
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('home'))      


@app.route('/modificar_producto', methods=['POST', 'GET'])
def modificarProducto():
     if "doc_empleado" in session:
        email = session["email_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE email_empleado='{email}'"
        print(bsq)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsq)
        resultado = cursor.fetchone()
        documento_registro = resultado[0]
        nombre_operador = resultado[1]
        apellido_operador = resultado[2]
        nombreProveedor = request.form['nombreProveedor']
        sql = f"SELECT doc_proveedor FROM proveedores WHERE nom_proveedor= '{nombreProveedor}'"
        cursor.execute(sql)
        resultado2 = cursor.fetchone()
        print(resultado2)
        id_producto = request.form['id_producto']
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
        Dproductos.modificar([id_producto, referencia_producto, categoria, proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante, documento_registro, nombre_operador, apellido_operador, nombreProveedor])
        return redirect('/muestra_productos')
     else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('home'))
 

@app.route('/borra_produc/<idprod>')
def borra_produc(idprod):
    if "email_empleado" in session:
        Dproductos.borrar_producto(idprod)        # Eliminar productos
        return redirect("/muestra_productos")   
    else:
        flash('Algo esta mal en los datos digitados')
        return redirect(url_for('home'))
    
