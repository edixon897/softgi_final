var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda

$(document).ready(function() {
    // Guardar la tabla original cuando se carga el documento
    tablaOriginal = $('#cotizacionTable tbody').html();

    $('#searchCotizacion').on('input', function() {
        var busqueda = $(this).val().trim();
        if (busqueda.length > 2) {
            buscarCotizacionesEnTiempoReal(busqueda);
        } else {
            restaurarTabla();
        }
    });
});

function buscarCotizacionesEnTiempoReal(busqueda) {
    $.ajax({
        type: 'POST',
        url: '/buscar_cotizacion', // Corregido para que coincida con la ruta en Flask
        data: { 'busqueda': busqueda }, // Corregido el nombre del parámetro para que coincida con el nombre en Flask
        success: function(response) {
            actualizarTabla(response.result);
        },
        error: function(xhr, status, error) {
            console.error('Error al realizar la búsqueda:', error);
        }
    });
    
}

function eliminarCotizacion(doc_empleado) {
    if (confirm('¿Seguro que deseas eliminar esta cotizacion?')) {
        if (doc_empleado) {
            $.ajax({
                type: 'POST',
                url: '/borraCotizacion/' + doc_empleado,
                success: function(response) {
                    // Si la eliminación es exitosa, actualiza la tabla
                    var busqueda = $('#searchCotizacion').val().trim();
                    buscarCotizacionesEnTiempoReal(busqueda);
                },
                error: function(xhr, status, error) {
                    console.error('Error al eliminar la cotizacion:', error);
                    alert('Error al eliminar la cotizacion. Por favor, inténtalo de nuevo más tarde.');
                }
            });
        } else {
            console.error('ID de empleado no válido.');
            alert('Cotizacion no válido. Por favor, seleccione una cotizacion válido para eliminar.');
        }
    }
}


function restaurarTabla() {
    // Restaura la tabla original
    $('#cotizacionTable tbody').html(tablaOriginal);
}

function actualizarTabla(data) {
    var tabla = $('#cotizacionTable tbody');
    tabla.empty();
    if (data.length > 0) {
        $.each(data, function(index, row) {
            var tr = $('<tr>');
            for (var i = 1; i < row.length; i++) {
                // Verificamos si el valor es una fecha y la formateamos
                var value = row[i];
                if (isDate(value)) {
                    value = formatDate(value);
                }
                $('<td>').text(value).appendTo(tr);
            }
            // Botón para editar (ver detalle)
            var verDetalleBtn = $('<td class="btns_centro"><a href="/editarCotizacion/' + row[0] + '"><i id="icono_ver_mas" class="lni lni-pencil"></i></a></td>');
            tr.append(verDetalleBtn);
            //Boton para detalle cotizacion
            var verDetalleBtn = $('<td class="btns_centro"><a href="/nuevo_detalle/' + row[0] + '"> <i id="icono_3" class="lni lni-circle-plus"></i></a></td>');
            tr.append(verDetalleBtn);
            // Botón para eliminar
            var eliminarEmpleadoBtn = $('<td class="btns_centro btn_eliminar"><button onclick="eliminarCotizacion(\'' + row[0] + '\')" ><i id="icono_3" class="lni lni-trash-can"></i></button></td>');
            tr.append(eliminarEmpleadoBtn);
            // Botón para imprimir
            var imprimirBtn = $('<td class="btns_centro"><a href="/detalle/' + row[0] + '"><i id="btn_print" class="lni lni-printer"></i></a></td>');
            tr.append(imprimirBtn);
            // Agregamos la fila a la tabla
            tabla.append(tr);
        });
    } else {
        // Si no se encuentran resultados, muestra un mensaje
        tabla.append('<tr><td colspan="8">No se encontraron resultados</td></tr>');
    }
}

// Función para verificar si un valor es una fecha
function isDate(value) {
    return !isNaN(Date.parse(value));
}

// Función para formatear la fecha en el formato AAAA-MM-DD
function formatDate(dateString) {
    var date = new Date(dateString);
    var year = date.getFullYear();
    var month = ('0' + (date.getMonth() + 1)).slice(-2);
    var day = ('0' + date.getDate()).slice(-2);
    return year + '-' + month + '-' + day;
}






/* Esconde los botones de eliminar y editar dependiendo el rol */

function verifica_input_rol() {
    let botones_credito_pago = document.getElementsByClassName('btn_eliminar');
    let input_rol = document.getElementById('input_rol');
    let btn_crear = document.getElementById('abrirModalBtn');
    let valor = input_rol.value;

    if (valor === "administrador" || valor === "almacenista")  {
        for (let i = 0; i < botones_credito_pago.length; i++) {
            botones_credito_pago[i].style.visibility  = "visible";
        } 
    }
    
}


document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    verifica_input_rol();
});






