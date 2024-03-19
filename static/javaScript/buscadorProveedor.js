var tablaOriginal;  

$(document).ready(function() {
    // Guardar la tabla original cuando se carga el documento
    tablaOriginal = $('#tablaProveedor tbody').html();

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
        url: '/buscador_proveedores',
        data: { 'buscar_proveedor': busqueda },
        success: function(response) {
            actualizarTabla(response.result);
        },
        error: function(xhr, status, error) {
            console.error('Error al realizar la búsqueda:', error);
        }
    });
}

function restaurarTabla() {
    // Restaurar la tabla original
    var tabla = $('#tablaProveedor tbody');
    tabla.empty();
    tabla.append(tablaOriginal);
}

function eliminarProveedor(idProveedor) {
    if (confirm('¿Seguro que deseas eliminar este proveedor?')) {
        $.ajax({
            type: 'POST',
            url: '/borraProveedor/' + idProveedor,
            success: function(response) {
                // Si la eliminación es exitosa, actualiza la tabla
                var busqueda = $('#buscador_ventas').val().trim();
                buscarEnTiempoReal(busqueda);
            },
            error: function(xhr, status, error) {
                console.error('Error al eliminar el proveedor:', error);
            }
        });
    }
}

function actualizarTabla(data) {
    var tabla = $('#tablaProveedor tbody');
    tabla.empty();
    if (data.length > 0) {
        $.each(data, function(index, row) {
            var tr = $('<tr>');
            for (var i = 0; i < row.length; i++) {
                $('<td>').text(row[i]).appendTo(tr);
            }
            var verDetalleBtn = $('<td><button style="" onclick="abrirModalEditarProveedor(\'' + row[0] + '\')" class="btn_editar"><i id="icono_2" class="lni lni-pencil"></i></button></td>');
            tr.append(verDetalleBtn);
            var eliminarProveedorBtn = $('<td class="btns_centro"><button onclick="eliminarProveedor(\'' + row[0] + '\')" class="btn_eliminar"><i id="icono_3" class="lni lni-trash-can"></i></button></td>');
            tr.append(eliminarProveedorBtn);
            tabla.append(tr);
        });
    } else {
        tabla.append('<tr><td colspan="8">No se encontraron resultados</td></tr>');
    }
}


function abrirModalEditarProveedor(documento) {
    $.ajax({
        url: `/actializarProveedor/${documento}`,
        type: 'GET',
        success: function(data) {
            $('#modalContainer').html(data); // Inserto el contenido del modal en el contenedor
            $('#editarProveedorModal').show(); // Mostrar el modal
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
    
    $(window).click(function (e) {
        if (e.target.id === "editarProveedorModal") {
            $("#editarProveedorModal").hide();
        }
    });
}


document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("tablaProveedor");
    var rows = table.getElementsByTagName("tr");

    
    for (var i = 11; i < rows.length; i++) {
        rows[i].style.display = "none";
    }
});


