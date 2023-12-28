import sys
from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.productos import Dproductos




@app.route('/productos')
def productos():
        if "nom_empleado" in session: 
            sql = "SELECT `referencia_producto`, `nombre_producto`, `descripcion`, `categoria`, `cantidad_producto`, `stockminimo`, `proveedor`,  `precio_compra`, `precio_venta`, `ubicacion` FROM productos WHERE estado_producto ='ACTIVO'"
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
            ref_prod_1 = request.form['ref_prod_1']
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

            
            Dproductos.crearProductos([ref_prod_1, ref_prod_2, ref_prod_3, categoria, proveedores_activos, nom_proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante, tiempoRegistro, documento_registro, nombre_operador, apellido_operador])
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
                        

""" @app.route('/muestra_productos')
def muestra_Productos():
    if "nom_empleado" in session: 
        sql = f"SELECT ref_prod_1, ref_produ_2, ref_produ_3, nom_categoria, nom_proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante  FROM productos WHERE estado_producto = 'ACTIVO'" 
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("resultado", resultado)
        conn.commit()
        if (len(resultado) >= 1):
            return render_template("/productos/muestra_productos.html", resul=resultado)   # si hay resultados se muestran.
        else:
            resultado2 = "No hay productos registrados"
            return render_template("/productos/muestra_productos.html", resul2=resultado2)  # sino se muestra el mensaje de resultado2.
    else:
        flash('Algo está mal en los datos digitados')
        return redirect(url_for('index'))
"""







<<<<<<< HEAD
@app.route("/modificar_producto/<referencia_producto>")
def editar_producto(referencia_producto):
=======
@app.route("/modificar_producto/<id_producto>")
def editar_producto(id_producto):
    print("Entrando a editar un Producto")
>>>>>>> 0732cb5cb1a1d7ca4c7d74c1dc2276583f6c2346
    if "nom_empleado" in session: 
        sql = f"SELECT `id_producto`, `referencia_producto`, `ref_produ_2`, `ref_produ_3`, `nom_categoria`, `nom_proveedor`, `nombre_producto`, `precio_compra`, `precio_venta`, `cantidad_producto`, `descripcion`, `stockminimo`, `ubicacion`, `estante` FROM productos WHERE id_producto='{id_producto}'"

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("EStos son los datos que trae des la BDD", resultado)
        conn.commit()
        return render_template("productos/edita_productos.html", resul= resultado[0])
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('index'))      


@app.route('/modificar_Producto', methods=['POST'])
def modificar_Producto():
    print("entrando a modificar")
    if "nom_empleado" in session:
        doc = session["nom_empleado"]
        bsq = f"SELECT `doc_empleado`, `nom_empleado`, `ape_empleado` FROM empleados WHERE nom_empleado='{doc}'"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(bsq)
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
                referencia_producto = request.form['referencia_producto']
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

                datos_modificar = [id_producto, referencia_producto, ref_produ_2, ref_produ_3, nom_categoria, nom_proveedor, nombre_producto, precio_compra, precio_venta, cantidad_producto, descripcion, stockminimo, ubicacion, estante, documento_registro, nombre_operador, apellido_operador]

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

        # Resto del código...
    else:
        flash('Por favor, inicia sesión para poder acceder')
        return redirect(url_for('index'))

 

@app.route('/borra_produc/<idprod>')
def borra_produc(idprod):
    if "nom_empleado" in session: 
        Dproductos.borrar_producto(idprod)        # Eliminar productos
        return redirect("/muestra_productos")   
    else:
        flash('Algo esta mal en los datos digitados')
        return redirect(url_for('home'))
    
