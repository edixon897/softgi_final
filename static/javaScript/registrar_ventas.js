function verifica_input() {
    let input_error = document.getElementById('input_error');
    let valor_input = input_error.value;

    if (valor_input == 1) {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "No hay productos seleccionados",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    } else if (valor_input == 2) {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Identificacion del operador invalida",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    } else if (valor_input == 3) {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "El cliente no existe en la base de datos",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    } else if (valor_input == "listo_credito") {
        Swal.fire({
            icon: "success",
            text: "Venta a credito realizada",
            width: "42%",
            height: "20%",
            timer: 1500,
            showConfirmButton: false
        });
    } else if (valor_input == "Venta_realizada_normal") {
        Swal.fire({
            icon: "success",
            text: "Venta realizada",
            width: "42%",
            height: "20%",
            timer: 1500,
            showConfirmButton: false
        });
    } else if (valor_input == "No_hay_productos_seleccionados_para_eliminar") {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "No hay productos seleccionados para eliminar",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    }
}




function verifica_input_2() {
    let input_error_2 = document.getElementById('input_error_2');
    let valor_input = input_error_2.value;

    if (valor_input == "La_cantidad_solicitada_es_menor_a_la_disponible") {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "La cantidad solicitada del producto es mayor a la disponible",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    }  else if (valor_input == "La_cantidad_solicitada_es_menor_o_igual_a_cero") {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "La cantidad solicitada es menor o igual a cero",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    } else if (valor_input == "El_cliente_ya_existe_en_la_base_de_datos") {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "El cliente ya existe en la base de datos",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    } else if (valor_input == "Se_vaciaron_todos_los_productos_seleccionados") {
        Swal.fire({
            icon: "success",
            text: "Se vaciaron todos los productos seleccionados",
            width: "42%",
            height: "20%",
            timer: 1500,
            showConfirmButton: false
        });
    }
}

function valida_rol_ventas() {
    let Muestra_ventas = document.getElementById('Muestra_ventas');
    let input_validador = document.getElementById('input_valida_ventas');
    valor_input = input_validador.value;

    if (valor_input == "vendedor") {
        Muestra_ventas.href = "/muestra_ventas_vendedor"
    }
}



document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    verifica_input();
    verifica_input_2();
    valida_rol_ventas();
});



function verifica_tipo_venta() {
    let venta_tipo = document.getElementById('venta_tipo');
    let valor_venta_tipo = venta_tipo.value;
    

    if (valor_venta_tipo == "venta_normal") {

        let forma_pago = document.getElementById('forma_pago');
        forma_pago.style.display = "block"

        let conten_input_2 = document.getElementById('conten_input_2');
        conten_input_2.style.width = "50%"

        let conten_input_1 = document.getElementById('conten_input_1');
        conten_input_1.style.width = "50%"

    } else {
        let forma_pago = document.getElementById('forma_pago');
        forma_pago.style.display = "none"

        let conten_input_2 = document.getElementById('conten_input_2');
        conten_input_2.style.width = "100%"

        let conten_input_1 = document.getElementById('conten_input_1');
        conten_input_1.style.width = "0%"

    }
}



function valida_campos() {
    let doc_operador = document.getElementById('doc_operador').value;
    let doc_cliente = document.getElementById('doc_cliente').value;
    let form = document.querySelector("form");

    form.addEventListener('submit', function(event) {
        event.preventDefault()
    });

    if (doc_operador && doc_cliente) {
        form.submit()
    } else {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Faltan campos por completar",
            width: "50%",
            height: "20%",
            timer: 1500,
            showConfirmButton: false
        });
    }
    
}


/* BUSCADOR */
var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda

    $(document).ready(function() {
        // Guardar la tabla original cuando se carga el documento
        tablaOriginal = $('#tabla tbody').html();

        $('#buscador').on('input', function() {
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
            url: '/buscarProductosVentas',
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
        // Restaurar la tabla a su estado original
        $('#tabla tbody').html(tablaOriginal);
    }

    function actualizarTabla(data) {
        var tabla = $('#tabla tbody');
        tabla.empty();
        if (data.length > 1) {
            $.each(data, function(index, row) {
                var tr = $('<tr>');
                $.each(row, function(key, value) {
                    $('<td>').text(value).appendTo(tr);
                });
                // Agregar los enlaces y botones correspondientes a la última columna de la fila
                $('<td>').html('<a href="#" class="abrir-modal" data-id="' + row[0] + '"><i id="icono_select_2" class="lni lni-layers"></i></a>').appendTo(tr);
                $('<td>').html('<a href="/selector_una_cantidad/' + row[0] + '"><i id="icono_select_1" class="lni lni-select-cursor"></i></a>').appendTo(tr);
                tabla.append(tr);
            });
        } else {
            tabla.append('<tr><td colspan="6">No se encontraron resultados</td></tr>');
        }

        // Vincular eventos click a los enlaces con clase "abrir-modal"
        $('.abrir-modal').off('click').on('click', function(e) {
            e.preventDefault();
            var idProducto = $(this).data('id');
            abrirModal_2(idProducto);
        });
    }




/* function buscarProductos() {
    var input, filter, table, tr, td, i, j, txtValue, noResults;

    input = document.getElementById("buscador");
    filter = input.value.toUpperCase();
    table = document.getElementById("tabla");
    tr = table.getElementsByTagName("tr");
    noResults = document.getElementById("noResults");

    noResults.style.display = "none";

    for (i = 0; i < tr.length; i++) {
        if (!tr[i].getElementsByTagName("td").length) {
            // Si no hay celdas td, es decir, es un encabezado, se salta la iteración.
            continue;
        }
        td = tr[i].getElementsByTagName("td");
        var encontrado = false;

        for (j = 0; j < td.length; j++) {
            if (td[j]) {
                txtValue = td[j].textContent || td[j].innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    encontrado = true;
                    break;
                }
            }
        }

        // Ocultar o mostrar la fila según si se encontró o no la coincidencia.
        tr[i].style.display = encontrado ? "" : "none";
    }

    // Mostrar el mensaje de "No se encontraron resultados" si todas las filas están ocultas.
    if (Array.from(tr).every(row => row.style.display === "none")) {
        noResults.style.display = "block";
    }
}



document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("tabla");
    var rows = table.getElementsByTagName("tr");

    
    for (var i = 10; i < rows.length; i++) {
        rows[i].style.display = "none";
    }
}); */




// Función para abrir el modal
/* function abrirModal(idProducto) {
    // Cargar el contenido de editar_cantidad.html en el modalContenedor
    var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.innerHTML = "";

    var btn_enviar = document.getElementById('btn_enviar');
    btn_enviar.style.backgroundColor = "white"
    btn_enviar.style.color = "#358CB4"
    btn_enviar.style.border = "1px solid #358CB4"

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            modalContenedor.innerHTML = this.responseText;

            // Mostrar el modal
            modalContenedor.style.display = "block";
        }
    };

    xhttp.open("GET", "/m_selector_cantidad_p/" + idProducto, true);
    xhttp.send();
} */

// Función para cerrar el modal
/* function cerrarModal() {
    var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.style.display = "none";

    var btn_enviar = document.getElementById('btn_enviar');
    btn_enviar.style.backgroundColor = "#358CB4"
    btn_enviar.style.color = "white"
    btn_enviar.style.border = "none"
} */





function abrirModal_2(idProducto) {
    // Cargar el contenido de editar_cantidad.html en el modalContenedor

    var btn_enviar = document.getElementById('btn_enviar');
    btn_enviar.style.backgroundColor = "white"
    btn_enviar.style.color = "#358CB4"
    btn_enviar.style.border = "1px solid #358CB4"

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

    xhttp.open("GET", "/m_selector_cantidad_p/" + idProducto, true);
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


        var btn_enviar = document.getElementById('btn_enviar');
        btn_enviar.style.backgroundColor = "#358CB4"
        btn_enviar.style.color = "white"
        btn_enviar.style.border = "none"
}



function abrirModal_3() {
    // Cargar el contenido de editar_cantidad.html en el modalContenedor

    var btn_enviar = document.getElementById('btn_enviar');
    btn_enviar.style.backgroundColor = "white"
    btn_enviar.style.color = "#358CB4"
    btn_enviar.style.border = "1px solid #358CB4"

    var icono_cedula = document.getElementById('icono_cedula')
    icono_cedula.style.display = "none"

    var modalContenedor = document.getElementById("modalContenedor_3");
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

    xhttp.open("GET", "/crearClientes_2", true);
    xhttp.send();
}



function cerrarModal_3() {
    /* var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.style.display = "none"; */

    var conten_registra_pago = document.getElementById("conten_registra_pago");
    var modalContenedor = window.parent.document.getElementById("modalContenedor_3");
            
    var icono_cedula = document.getElementById('icono_cedula')
    icono_cedula.style.display = "block"

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


        var btn_enviar = document.getElementById('btn_enviar');
        btn_enviar.style.backgroundColor = "#358CB4"
        btn_enviar.style.color = "white"
        btn_enviar.style.border = "none"
}




function detenerPropagacion(event) {
    event.stopPropagation();
}



