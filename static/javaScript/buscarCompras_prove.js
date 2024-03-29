var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda

$(document).ready(function() {
    // Guardar la tabla original cuando se carga el documento
    tablaOriginal = $('#tabla_compraProveedor tbody').html();

    $('#buscador_2').on('input', function() {
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
        url: '/buscador_compraproveedor',
        data: { 'BuscaCompraProveedores': busqueda },
        success: function(response) {
            actualizarTabla(response.result);
        },
        error: function(xhr, status, error) {
            console.error('Error al realizar la búsqueda:', error);
        }
    });
}
function eliminarCompraAproveedor(num_compra) {
    if (confirm('¿Seguro que deseas eliminar este empleado?')) {
        $.ajax({
            type: 'POST',
            url: '/cancelar_compra_proveed/' + num_compra,
            success: function(response) {
                // Si la eliminación es exitosa, actualiza la tabla
                var busqueda = $('#buscador_2').val().trim();
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
    var tabla = $('#tabla_compraProveedor tbody');
    tabla.empty();
    tabla.append(tablaOriginal);
}

function actualizarTabla(data) {
    var tabla = $('#tabla_compraProveedor tbody');
        tabla.empty();
            if (data.length > 0) {
                $.each(data, function(index, row) {
                    var tr = $('<tr>');
                    // Comenzamos desde 1 para omitir el primer campo
                    for (var i =1; i < row.length; i++) {
                        var value = row[i];
                        if (isDate(value)) {
                            value = formatDate(value);
                        }
                        $('<td>').text(value).appendTo(tr);
                    }
                    // Agregar los botones a la fila
                    var verDetalleBtn = $('<td class="btns_centro"><button onclick="abrirModalEditCompra(\'' + row[0] + '\')" class="btn_editar"> <i id="icono_ver_mas" class="lni lni-pencil"></i></button></td>');
                    tr.append(verDetalleBtn);
                    var eliminarProveedorBtn = $('<td class="btns_centro"><button onclick="eliminarCompraAproveedor(\'' + row[0] + '\')" class="btn_eliminar"><i id="icono_3" class="lni lni-trash-can"></i></button></td>');
                    tr.append(eliminarProveedorBtn);
                    var masDeTalles = $('<td class="btns_centro"><a href="muestra_detalles_com/' + row[0] + '"><i id="icono_3" class="lni lni-circle-plus"></i></a></td>');
                    tr.append(masDeTalles);

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

// Función para formatear la fecha en el formato AAAA-MM-DD
function formatDate(dateString) {
    var date = new Date(dateString);
    var year = date.getFullYear();
    var month = ('0' + (date.getMonth() + 1)).slice(-2);
    var day = ('0' + date.getDate()).slice(-2);
    return year + '-' + month + '-' + day;
}



document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("tabla_compraProveedor");
    var rows = table.getElementsByTagName("tr");
  
    var visibleRowCount = 11; // Número de filas visibles inicialmente
  
    // Ocultar filas que están más allá del número de filas visibles
    for (var i = visibleRowCount; i < rows.length; i++) {
      rows[i].style.display = "none";
    }
  
    // Función para mostrar más filas cuando se hace scroll
    function mostrarMasFilas() {
      var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
      var windowHeight = window.innerHeight;
      var tableBottom = table.offsetTop + table.offsetHeight;
  
      if (scrollTop + windowHeight >= tableBottom) {
        // Mostrar las filas ocultas
        for (var i = visibleRowCount; i < rows.length; i++) {
          rows[i].style.display = "none";
        }
  
        // Actualizar el número de filas visibles
        visibleRowCount = rows.length;
      }
    }
  
    // Asignar el evento de scroll a la función mostrarMasFilas
    window.addEventListener("scroll", mostrarMasFilas);
  });