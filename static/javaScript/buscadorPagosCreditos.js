var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda

$(document).ready(function() {
    // Guardar la tabla original cuando se carga el documento
    tablaOriginal = $('#tablaVentas tbody').html();

    $('#buscador_ventas').on('input', function() {
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
        url: '/buscador_creditos_pagados',
        data: { 'dato_busqueda': busqueda },
        success: function(response) {
            actualizarTabla(response.result);
        },
        error: function(xhr, status, error) {
            console.error('Error al realizar la búsqueda:', error);
        }
    });
}

function restaurarTabla() {
    // Eliminar filas duplicadas antes de restaurar la tabla original
    var tabla = $('#tablaVentas tbody');
    tabla.empty();
    tabla.append(tablaOriginal);
}

function actualizarTabla(data) {
    var tabla = $('#tablaVentas tbody');
        tabla.empty();
            if (data.length > 0) {
                $.each(data, function(index, row) {
                    var tr = $('<tr>');
                    // Comenzamos desde 1 para omitir el primer campo
                    for (var i = 1; i < row.length; i++) {
                        $('<td>').text(row[i]).appendTo(tr);
                    }
                    // Agregar los botones a la fila
                    var verDetalleBtn = $('<td class="btns_centro"><a href="#" onclick="abrirModal_2(\'' + row[0] + '\')"><i id="icono_3" class="lni lni-stats-up"></i></a></td>');
                    tr.append(verDetalleBtn);
                    tabla.append(tr);
                });
            } else {
                tabla.append('<tr><td colspan="8">No se encontraron resultados</td></tr>');
    }
}


