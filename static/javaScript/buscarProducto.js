var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda

$(document).ready(function() {
    // Guardar la tabla original cuando se carga el documento
    tablaOriginal = $('#Tabla_product tbody').html();

    $('#searchProductos').on('input', function() {
        var busqueda = $(this).val().trim();
        if (busqueda.length > 1) {
            buscarEnTiempoReal(busqueda);
        } else {
            restaurarTabla();
        }
    });

    // Manejar el evento cuando el campo de búsqueda se vacía
    $('#searchProductos').on('keyup', function(event) {
        if (event.keyCode === 8 && $(this).val().length === 0) {
            restaurarTabla();
        }
    });
});

function buscarEnTiempoReal(busqueda) {
    $.ajax({
        type: 'POST',
        url: '/buscador_productos',
        data: { 'searchProductos': busqueda },
        success: function(response) {
            actualizarTabla(response.result);
        },
        error: function(xhr, status, error) {
            console.error('Error al realizar la búsqueda:', error);
        }
    });
}

function restaurarTabla() {
    var tabla = $('#Tabla_product tbody');
    tabla.empty();
    tabla.append(tablaOriginal);
    // Asignar eventos onclick de nuevo después de restaurar la tabla
    asignarEventosClick();
}
function eliminarPruducto(doc_producto) {
    if (confirm('¿Seguro que deseas eliminar este producto?')) {
        $.ajax({
            type: 'POST',
            url: '/borra_produc/' + doc_producto,
            success: function(response) {
                // Si la eliminación es exitosa, actualiza la tabla
                var busqueda = $('#Tabla_product').val().trim();
                buscarEnTiempoReal(busqueda);
            },
            error: function(xhr, status, error) {
                console.error('Error al eliminar el proveedor:', error);
            }
        });
    }
}
function eliminarFilasDuplicadas(tabla) {
    var seen = {};
    tabla.find('tr').each(function() {
        var id = $(this).attr('id');
        if (seen[id]) $(this).remove();
        else seen[id] = true;
    });
}

function actualizarTabla(data) {
    var tabla = $('#Tabla_product tbody');
    tabla.empty();
    if (data.length > 0) {
        $.each(data, function(index, row) {
            var tr = $('<tr>'); // Crear una nueva fila para cada elemento en los datos
            $.each(row, function(key, value) {
                $('<td>').text(value).appendTo(tr); // Agregar cada valor como un elemento de celda a la fila
            });

            // Agregar botones a la fila
            var verDetalleBtn = $('<td class="btns_centr"><button onclick="abrirModal_2(\'' + row[0] + '\')"><i id="icono_3" class="lni lni-plus"></i></button></td>');
            tr.append(verDetalleBtn);

            var editarBtn = $('<td class="btns_centr"><button onclick="abrirModalEditCompra(\'' + row[0] + '\')" class="btn_editar"><i id="icono_ver_mas" class="lni lni-pencil"></i></button></td>');
            tr.append(editarBtn);

            var eliminarBtn = $('<td class="btns_centr"><button onclick="eliminarPruducto(\'' + row[0] + '\')"><i id="icono_2" class="lni lni-trash-can"></i></button></td>');
            tr.append(eliminarBtn);
            
            // Agregar la fila a la tabla
            tabla.append(tr);
        });
        // Asignar eventos onclick después de actualizar la tabla
        asignarEventosClick();
    } else {
        tabla.append('<tr><td colspan="7">No se encontraron resultados</td></tr>');
    }
}




function cerrarModal_2() {

    var conten_registra_pago = document.getElementById("conten_registra_pago");
        var modalContenedor = window.parent.document.getElementById("modalContenedor_2");
            

        setTimeout( function() {
            modalContenedor.style.opacity = "0";
        }, 15);

        setTimeout( function() {
            modalContenedor.style.display = "none";
        }, 215);
        

        setTimeout( function() {
            conten_registra_pago.style.background = "rgba(36, 36, 36, 0.0)";
        }, 80);

        setTimeout( function() {
            conten_registra_pago.style.display = "none";
        }, 400);

}

function validador_input() {
    let input_verificacion = document.getElementById('input_verificacion');
    let valor_input = input_verificacion.value;

    if (valor_input == 'stock_añadido_con_exito') {

        Swal.fire({
            icon: "success",
            text: "Stock añadido con exito",
            width: "42%",
            height: "20%",
            timer: 1700,
            showConfirmButton: false
        });

    }
}


function verifica_input_rol() {
    let btn_crear = document.getElementById('btn_crear');
    let isla_btns = document.getElementById('conten_btn_navegacion');
    let botones_credito_pago = document.getElementsByClassName('btns_centro');
    let input_rol = document.getElementById('input_rol');
    let valor = input_rol.value;

    if (valor === "administrador" || valor === "almacenista")  {
        for (let i = 0; i < botones_credito_pago.length; i++) {
            botones_credito_pago[i].style.visibility  = "visible";
        }

        btn_crear.style.display = "block"
    } else {
        isla_btns.style.width = "20%"
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    validador_input();
    verifica_input_rol();
});





/*  // Función para abrir el modal para aumentar cantidad de producto Cantidady no dejarlo cerrar al poner el cursor dentro del input
 function abrirModal(idProducto) {
    // Cargar el contenido de editar_cantidad.html en el modalContenedor
    var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.innerHTML = "";

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            modalContenedor.innerHTML = this.responseText;

            // Mostrar el modal
            modalContenedor.style.display = "block";
        }
    };

    xhttp.open("GET", "/editar_Cantidad/" + idProducto, true);
    xhttp.send();
}

// Función para cerrar el modal
function cerrarModal() {
    var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.style.display = "none";
}; */

function detenerPropagacion(event) {
    event.stopPropagation();
}

// Funcion para controlar la cantidad de items a mostrar
document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("Tabla_product");
    var rows = table.getElementsByTagName("tr");

    for (var i = 11; i < rows.length; i++) {
        rows[i].style.display = "none";
    }
});