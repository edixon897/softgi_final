from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app
import datetime
from models.clientes import Dclientes
from models.abonos import Dabonos, Abonos
from models.ventas import Dventas

#-------------------------------------------------------- Muestra Historial de abonos ----------------------------------------------------------------

@app.route("/historial_abonos/<contador>")
def historial_abonos(contador):
    if "nom_empleado" in session:
        
        sql = f"SELECT `abono`, `operador`, `fecha_abono` FROM `historial_credito` WHERE contador_ventacredito = '{contador}' ORDER BY contador DESC"
        conn = mysql.connect()
        cursor = conn.cursor()     #muestra toda la informacion
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()
        return render_template("/ventas_credito/historial_abonos.html",resul = resultado)

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))


#-------------------------------------------------------- abonos ventas a credito ----------------------------------------------------------------

@app.route("/abono_credito/<contador>")
def abono_credito(contador):
    if "nom_empleado" in session:

        # muestra el html
        return render_template("/ventas_credito/abono_venta.html",cont = contador)

    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))



# ------- recibe la info del FRONT-END -----

@app.route("/confirma_abono", methods = ['POST'])
def confirma_abono():
    if "nom_empleado" in session:

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
                Dventas.abono_completo(contador)
                return redirect("/muestra_ventas_credito")
            
            
            # 2 
            else:
                # se actualiza el credito restante
                Dventas.actualiza_credito_rest([credito_actual, contador])

                # se incerta en el historial el abono realizado
                Dventas.insert_historial_abn([contador, abono, documento_operador, tiempo_venta])
                return redirect("/muestra_ventas_credito")

        # 1
        else:
            mensaj = "¡Cantidd digitada mayor a la debida!"
            return render_template("/ventas_credito/abono_venta.html",cont = contador, mensaje = mensaj)
            
    else:
        flash('Porfavor inicia sesion para poder acceder')
        return redirect(url_for('home'))