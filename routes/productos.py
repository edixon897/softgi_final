import sys
from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.productos import Dproductos




@app.route('/crear_Producto', methods=['GET', 'POST'])
def crear_Producto():
    global codigo_barras_global
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
            categorias_activas = request.form['categorias']
            sql =f"SELECT nom_categoria FROM categorias WHERE id_categoria= '{categorias_activas}' AND estado_categorias = 'ACTIVO'"
            cursor.execute(sql)
            categorias = cursor.fetchall()
            nom_categoria = categorias[0]
            ref_produ_1 = request.form['ref_produ_1']
            ref_produ_2 = request.form['ref_prod_2']
            ref_produ_3 = request.form['ref_prod_3']
        
            nombre_producto = request.form['nombre_producto']
            precio_compra = request.form['precio_compra']
            precio_venta = request.form['precio_venta']
            cantidad_producto = request.form['cantidad_producto']
            descripcion = request.form['descripcion']
            stockminimo = request.form['stockminimo']
            ubicacion = request.form['ubicacion']
            estante = request.form['estante']
            tiempoRegistro = datetime.datetime.now()

            
            Dproductos.crearProductos([ref_produ_1, ref_produ_2, ref_produ_3, categorias_activas, nom_categoria, proveedores_activos, nom_proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante, tiempoRegistro, documento_registro, nombre_operador, apellido_operador])
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
        sql = f"SELECT id_producto, ref_produ_1, ref_produ_2, ref_produ_3, nom_categoria, nom_proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante  FROM productos WHERE estado_producto = 'ACTIVO'" 
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("resultado", resultado)
        conn.commit()
        if (len(resultado) >= 1):
            return render_template("/productos/muestra_productos.html", resul=resultado) 
        # si hay resultados se muestran.
        else:
            resultado2 = "No hay productos registrados"
            return render_template("/productos/muestra_productos.html", resul2=resultado2)  # sino se muestra el mensaje de resultado2.
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
    

@app.route('/buscar_producto', methods=['GET', 'POST'])
def buscar():
    if "nom_empleado" in session:
        busqueda = request.form['buscar']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM productos WHERE estado_producto='ACTIVO' AND (nombre_producto LIKE '%{busqueda}%' OR ref_produ_1 LIKE '%{busqueda}%' OR ref_produ_2 LIKE '%{busqueda}%' OR ref_produ_3 LIKE '%{busqueda}%'  OR descripcion LIKE '%{busqueda}%')")
        resultados = cursor.fetchall()
        conn.close()
        return render_template('productos/muestra_productos', result = resultados)
    else:
        flash('Por favor inicia sesion')
        return redirect(url_for('index'))


@app.route("/modificar_Producto/<int:id_producto>")
def editar_producto(id_producto):
    if "nom_empleado" in session: 
        sql = "SELECT id_producto, ref_produ_1, ref_produ_2, ref_produ_3, nom_categoria, nom_proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante FROM productos WHERE id_producto=%s"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, (id_producto,))
        resultado = cursor.fetchall()
        print("Este es el resultado:", resultado)
        conn.commit()

        if resultado:

            sql = "SELECT nom_proveedor FROM proveedores WHERE estado_proveedor = 'ACTIVO'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            proveedores = cursor.fetchall()
            conn.commit()

            sql = "SELECT nom_categoria FROM categorias WHERE  estado_categorias = 'ACTIVO'"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            categorias = cursor.fetchall()
            conn.commit()
            
            return render_template("productos/edita_productos.html", resul=resultado[0], prove = proveedores, cate = categorias)
        else:
            flash('No se encontró el producto')
    
    return redirect(url_for('index'))







@app.route('/modificar_Producto', methods=['POST'])
def modificar_Producto():
    print("entrando a modificar")
    if "nom_empleado" in session:
        doc = session["nom_empleado"]
        sql = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchone()
        print("Soy el empleado", resultado)
        documento_registro = resultado[0]
        nombre_operador = resultado[1]
        apellido_operador = resultado[2]

        if request.method == 'POST':
            # Imprime el contenido completo de request.form
            print("Contenido del formulario:", request.form)

            try:
                id_producto = request.form['id_producto']
                ref_produ_1 = request.form['ref_produ_1']
                ref_produ_2 = request.form['ref_produ_2']
                ref_produ_3 = request.form['ref_produ_3']
                nom_categoria = request.form['nom_categoria']
                nom_proveedor = request.form['nom_proveedor']
                nombre_producto = request.form['nombre_producto']
                precio_compra = request.form['precio_compra']
                precio_venta = request.form['precio_venta']
                cantidad_producto = request.form['cantidad_producto']
                descripcion = request.form['descripcion']
                stockminimo = request.form['stockminimo']
                ubicacion = request.form['ubicacion']
                estante = request.form['estante']

                datos_modificar = [id_producto, ref_produ_1, ref_produ_2, ref_produ_3, nom_categoria, nom_proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante, documento_registro, nombre_operador, apellido_operador]

                # Imprime los datos que estás pasando a Dproductos.modificar
                print("Datos a modificar:", datos_modificar)

                # Modificar Dproductos.modificar para devolver algo si es necesario
                resultado_modificacion = Dproductos.modificar(datos_modificar)

                # Imprime el resultado de Dproductos.modificar
                print("Resultado de la modificación:", resultado_modificacion)

                return redirect('/muestra_productos')

            except KeyError as e:
                print("Error KeyError:", e)
                flash('Error al procesar el formulario. Por favor, inténtalo de nuevo.')
                return redirect(url_for('index'))
        return render_template('muestra_productos.html')

    else:
        flash('Por favor, inicia sesión para poder acceder')
        return redirect(url_for('index'))


@app.route('/borra_produc/<string:id_producto>', methods=['GET', 'POST'])
def borra_produc(id_producto):
    print(id_producto)
    print("aca voy")
    if "nom_empleado" in session: 
        Dproductos.borrar_producto(id_producto)  
        print("aca voy", id_producto)    
        return redirect('/muestra_productos')   
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
    