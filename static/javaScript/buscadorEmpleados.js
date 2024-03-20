var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda

$(document).ready(function() {
    // Guardar la tabla original cuando se carga el documento
    tablaOriginal = $('#TablaEmpleados tbody').html();

    $('#searchClientes').on('input', function() {
        var busqueda = $(this).val().trim();
        if (busqueda.length > 4) {
            buscarEnTiempoReal(busqueda);
        } else {
            restaurarTabla();
        }
    });
});

function buscarEnTiempoReal(busqueda) {
    $.ajax({
        type: 'POST',
        url: '/buscador_empleados',
        data: { 'buscadorEmpleados': busqueda },
        success: function(response) {
            actualizarTabla(response.result);
        },
        error: function(xhr, status, error) {
            console.error('Error al realizar la búsqueda:', error);
        }
    });
}
function eliminarEmpleado(doc_empleado) {
    if (confirm('¿Seguro que deseas eliminar este empleado?')) {
        $.ajax({
            type: 'POST',
            url: '/borrarEmpleado/' + doc_empleado,
            success: function(response) {
                // Si la eliminación es exitosa, actualiza la tabla
                var busqueda = $('#TablaEmpleados').val().trim();
                buscarEnTiempoReal(busqueda);
            },
            error: function(xhr, status, error) {
                console.error('Error al eliminar el proveedor:', error);
            }
        });
    }
}

function restaurarTabla() {
    // Eliminar filas duplicadas antes de restaurar la tabla original
    var tabla = $('#TablaEmpleados tbody');
    tabla.empty();
    tabla.append(tablaOriginal);
}

function actualizarTabla(data) {
    var tabla = $('#TablaEmpleados tbody');
        tabla.empty();
            if (data.length > 0) {
                $.each(data, function(index, row) {
                    var tr = $('<tr>');
                    // Comenzamos desde 1 para omitir el primer campo
                    for (var i =0; i < row.length; i++) {
                        $('<td>').text(row[i]).appendTo(tr);
                    }
                    // Agregar los botones a la fila
                    var verDetalleBtn = $('<td class="btns_centro"><button onclick="abrirModalEditarEmpleado(\'' + row[0] + '\')" class="btn_editar"><i id="icono_2" class="lni lni-pencil"></i></button></td>');
                    tr.append(verDetalleBtn);
                    var eliminarProveedorBtn = $('<td class="btns_centro"><button onclick="eliminarEmpleado(\'' + row[0] + '\')" class="btn_eliminar"><i id="icono_3" class="lni lni-trash-can"></i></button></td>');
                    tr.append(eliminarProveedorBtn);
                    tabla.append(tr);
                });
            } else {
                tabla.append('<tr><td colspan="8">No se encontraron resultados</td></tr>');
    }
}


