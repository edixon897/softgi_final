var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda
    
        $(document).ready(function() {
            // Guardar la tabla original cuando se carga el documento
            tablaOriginal = $('#tablaVentas tbody').html();
            
            $('#buscador_ventas').on('input', function() {
                var busqueda = $(this).val().trim();
                if (busqueda.length > 0) {
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
            var tabla = $('#tablaVentas tbody');
            tabla.empty();  // Limpiar el contenido actual de la tabla
            tabla.html(tablaOriginal);  // Restaurar el HTML original guardado
            asignarEventosClick();  // Reasignar los eventos
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
                    for (var i = 0; i < row.length; i++) {
                        var value = row[i];
                        // Comprueba si el valor es una fecha antes de formatear
                          // Aplicar formato de fecha solo a las columnas conocidas que contienen fechas
                        if ((i === 4) && isDate(value)) {  // Asume que las columnas 1 y 3 contienen fechas
                            value = formatDate(value);
                        }
                        $('<td>').text(value).appendTo(tr);
                    }
                    // Mantener visible el botón de "Más detalles" incluso después de la búsqueda
                    $('<td class="btns_centro"><a href="#" class="ver_detalle"><i id="icono_ver_mas" class="lni lni-comments-alt-2"></i></a></td>').appendTo(tr);
                    tabla.append(tr);
                    var facturaBtn = $('<td class="btns_centro"><a href="/factura/' + row[0] + '"><i id="icono_ver_mas" class="lni lni-printer"></i></a></td>');
                    tr.append(facturaBtn);

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



/* Aumenta el tamaño del contenedor de las opciones */
function aumenta_tamaño_isla(){

    /* Desabilito el enlace */
    let link = document.getElementById('enlace_ventas_credito').addEventListener('click', function(event) {
        event.preventDefault();
    });

    /* Capturo y aumento el tamaño del contenedor */
    let conten_btns = document.getElementById('conten_btn_navegacion');
    conten_btns.style.width = "40%";

    /* Retraso el tiempo en q aparece el enlace */
    let enlace_entrante = document.getElementById('enlace_entrante');
    setTimeout( function() {
        enlace_entrante.style.display = "block"
    },199)
 
    /* Retraso el proceso del enlace */
    setTimeout( function() {
        window.location.href = "/muestra_ventas_credito"
    },200);

}








/* Muestra el nav laterar */

function abrir_nav() {
    let fondo = document.getElementById('section_sombra');
    let conten_desplegable = document.getElementById('conten_desplegable');
    let icono = document.getElementById('conten_icono_u');
    let nombre = document.getElementById('conten_nombre_2');
    let lado_1 = document.getElementById('lado_1');
    let lado_2 = document.getElementById('lado_2');
    let btn_cerrar = document.getElementById('conten_btn_cerrar');

    fondo.style.display = "block";
    setTimeout(function() {
        fondo.style.backgroundColor = "rgba(36, 36, 36, 0.6)";
    },50);

    setTimeout(function() {
        conten_desplegable.style.left = "85%";
    },400);

    setTimeout(function() {
        icono.style.opacity = "1";
    },750);

    setTimeout(function() {
        nombre.style.opacity = "1";
    },850);

    setTimeout(function() {
        lado_1.style.opacity = "1";
    },950);

    setTimeout(function() {
        lado_2.style.opacity = "1";
    },1050);

    setTimeout(function() {
        btn_cerrar.style.left = "-13%";
    },1150);

}

/* Cierra el nav lateral */

function cerrar_nav() {
    let fondo = document.getElementById('section_sombra');
    let conten_desplegable = document.getElementById('conten_desplegable');
    let icono = document.getElementById('conten_icono_u');
    let nombre = document.getElementById('conten_nombre_2');
    let lado_1 = document.getElementById('lado_1');
    let lado_2 = document.getElementById('lado_2');
    let btn_cerrar = document.getElementById('conten_btn_cerrar');


    setTimeout(function() {
        btn_cerrar.style.left = "140%";
    },50);

    setTimeout(function() {
        lado_2.style.opacity = "0";
    },150);

    setTimeout(function() {
        lado_1.style.opacity = "0";
    },250);

    setTimeout(function() {
        nombre.style.opacity = "0";
    },350);

    setTimeout(function() {
        icono.style.opacity = "0";
    },450);

    setTimeout(function() {
        conten_desplegable.style.left = "100%";
    },700);

    setTimeout(function() {
        fondo.style.backgroundColor = "rgba(36, 36, 36, 0.0)";
    },1050);

    setTimeout(function() {
        fondo.style.display = "none";
    },1410);

}


function detener_Propagacion(event) {
    event.stopPropagation();
}
