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
                var tr = $('<tr>');  // Crear una nueva fila para cada conjunto de datos
    
                for (var i = 0; i < row.length; i++) {
                    var value = row[i];
                    var td = $('<td>').text(value);  // Crear la celda y asignar el valor
    
                    // Aplicar estilos específicos a las columnas 2 y 3
                    if (i === 2 || i === 3) {
                        td.css({'color': '#6ad46a'});  // Estilo para la columna 2 y 3
                    }
    
                    // Comprobar si el valor es una fecha antes de formatear y si es la columna 5
                    if (i === 5 && isDate(value)) {
                        value = formatDate(value);
                        td.text(value);  // Actualizar el texto de la celda después de formatear la fecha
                    }
        
                        tr.append(td);  // Añadir la celda a la fila
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
// Función para verificar si un valor es una fecha
function isDate(value) {
    return !isNaN(Date.parse(value));
}

// Función para formatear la fecha y hora
function formatDate(dateString) {
    var date = new Date(dateString);
    var year = date.getFullYear();
    var month = ('0' + (date.getMonth() + 1)).slice(-2);
    var day = ('0' + date.getDate()).slice(-2);
    var hours = ('0' + date.getHours()).slice(-2);
    var minutes = ('0' + date.getMinutes()).slice(-2);
    var seconds = ('0' + date.getSeconds()).slice(-2);
    // Formato de fecha y hora YYYY-MM-DD HH:MM:SS
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}


