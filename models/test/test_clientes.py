from models.clientes import Dclientes
from conexionDbTest import *

def test_crear_cliente():
    con = mysql.connect()
    cur = con.cursor()
    sql="DELETE FROM clientes WHERE doc_cliente='12345'"
    cliente=['12345',"Joaquin","Perez",'1981-09-04','3123185701','javiper@gmail.com','carrera 21# 15b-35','Buga','Natural','','','','','']
    Dclientes.crear_cliente(cliente)
    