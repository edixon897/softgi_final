from flask import Flask, request, render_template, flash, redirect, url_for, session
from conexiondb import conexion, mysql, app

@app.route("/categorias")
def categorias():
    sql = "SELECT * FROM categorias WHERE estado_categorias ='ACTIVO'"
    conn = mysql.connect()                    
    cursor = conn.cursor()
    cursor.execute(sql)                                          
    resultado = cursor.fetchall()
    return render_template('/categorias/categoria.html', resulta=resultado)




