var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda
    
        $(document).ready(function() {
            // Guardar la tabla original cuando se carga el documento
            tablaOriginal = $('#tablaVentas tbody').html();
    
            $('#buscador_ventas').on('input', function() {
                var busqueda = $(this).val().trim();
                if (busqueda.length > 1) {
                    buscarEnTiempoReal(busqueda);
                } else {
                    restaurarTabla();
                }
            });
        });
        
        function buscarEnTiempoReal(busqueda) {
            $.ajax({
                type: 'POST',
                url: '/buscarVentas',
                data: { 'Busqueda': busqueda },
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
            eliminarFilasDuplicadas(tabla);

            // Restaurar la tabla a su estado original
            tabla.empty();
            tabla.append(tablaOriginal);
            // Asignar eventos onclick de nuevo después de restaurar la tabla
            asignarEventosClick();
        }
        function eliminarFilasDuplicadas(tabla) {
            var seen = {};
            tabla.find('tr').each(function() {
                var txt = $(this).text();
                if (seen[txt]) $(this).remove();
                else seen[txt] = true;
            });
        }
        
        function actualizarTabla(data) {
            var tabla = $('#tablaVentas tbody');
            tabla.empty();
            if (data.length > 0) {
                $.each(data, function(index, row) {
                    var tr = $('<tr>');
                    $.each(row, function(key, value) {
                        $('<td>').text(value).appendTo(tr);
                    });
                    // Mantener visible el botón de "Más detalles" incluso después de la búsqueda
                    $('<td class="btns_centro"><a href="#" class="ver_detalle"><i id="icono_ver_mas" class="lni lni-comments-alt-2"></i></a></td>').appendTo(tr);
                    tabla.append(tr);
                });
                // Asignar eventos onclick después de actualizar la tabla
                asignarEventosClick();
            } else {
                tabla.append('<tr><td colspan="7">No se encontraron resultados</td></tr>');
            }
        }
    
        function asignarEventosClick() {
            $('.ver_detalle').on('click', function(e) {
                e.preventDefault();
                var num_factura = $(this).closest('tr').find('td:first').text(); // Obtener el número de factura de la fila actual
                abrirModal_2(num_factura);
            });
        }





function abrirModal_2(id) {
    // Cargar el contenido de editar_cantidad.html en el modalContenedor
    var modalContenedor = document.getElementById("modalContenedor_2");
    modalContenedor.innerHTML = "";

    var conten_registra_pago = document.getElementById("conten_registra_pago");
    conten_registra_pago.style.display = "block"


    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            modalContenedor.innerHTML = this.responseText;

            // Mostrar el modal
            modalContenedor.style.display = "block";
            setTimeout( function() {
                conten_registra_pago.style.background = "rgba(36, 36, 36, 0.4)";
            }, 400);
            setTimeout( function() {
                modalContenedor.style.opacity = "1";
            }, 255);
        }
    };

    xhttp.open("GET", "/muestra_detalles_ventas/" + id, true);
    xhttp.send();
}



function cerrarModal_2() {
    /* var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.style.display = "none"; */

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



function detenerPropagacion(event) {
    event.stopPropagation();
}



document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("tablaVentas");
    var rows = table.getElementsByTagName("tr");

    
    for (var i = 11; i < rows.length; i++) {
        rows[i].style.display = "none";
    }
});