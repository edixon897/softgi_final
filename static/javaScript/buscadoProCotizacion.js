var tablaOriginal; 

$(document).ready(function() {
    // Guardar la tabla original cuando se carga el documento
    tablaOriginal = $('#productTable tbody').html();

    $('#searchProductos').on('input', function() {
        var busqueda = $(this).val().trim();
        if (busqueda.length > 3) {
            buscarProductosEnTiempoReal(busqueda);
        } else {
            restaurarTabla();
        }
    });
});

function buscarProductosEnTiempoReal(busqueda) {
    $.ajax({
        type: 'POST',
        url: '/buscar_ProductoCotizacion',
        data: { 'busqueda': busqueda },
        success: function(response) {
            actualizarTabla(response.result);
            $('#productTable').show(); // Mostrar la tabla después de la búsqueda
        },
        error: function(xhr, status, error) {
            console.error('Error al realizar la búsqueda:', error);
        }
    });
}

function restaurarTabla() {
    // Restaurar la tabla original
    var tabla = $('#productTable tbody');
    tabla.empty();
    tabla.append(tablaOriginal);
    $('#productTable').hide(); // Ocultar la tabla cuando no hay búsqueda
}

function actualizarTabla(data) {
    var tabla = $('#productTable tbody');
    tabla.empty();
    if (data.length > 0) {
        $.each(data, function(index, row) {
            var tr = $('<tr>');
            $('<td>').text(row[0]).appendTo(tr);
            var selectButton = $('<td><button type="button" class="select-button" onclick="selectProduct(\'' + row[0] + '\')">Seleccionar</button></td>');
            tr.append(selectButton);
            tabla.append(tr);
        });
    } else {
        tabla.append('<tr><td colspan="2">No se encontraron resultados</td></tr>');
    }
}


/* document.addEventListener("DOMContentLoaded", function() {
    // Verificar si el cuerpo de la tabla está vacío
    var tableBody = document.querySelector("#productosSeleccionados tbody");
    if (tableBody.innerHTML.trim() === "") {
        // Si está vacío, ocultar el contenedor de la tabla
        document.querySelector(".table-container").style.display = "none";
    } else {
        // Si hay datos, mostrar el contenedor de la tabla
        document.querySelector(".table-container").style.display = "block";
    }
}); */

