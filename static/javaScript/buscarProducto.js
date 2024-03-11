function buscarProductos() {
    var input, filter, table, tr, td, i, j, txtValue, noResults;

    input = document.getElementById("searchProductos");
    filter = input.value.toUpperCase();
    table = document.getElementById("Tabla_product");
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


    
    if (Array.from(tr).every(row => row.style.display === "none")) {
        noResults.style.display = "block";
    }
};




function abrirModal_2(idProducto) {
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

    xhttp.open("GET", "/editar_Cantidad/" + idProducto, true);
    xhttp.send();
}


function cerrarModal_2() {

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








function validador_input() {
    let input_verificacion = document.getElementById('input_verificacion');
    let valor_input = input_verificacion.value;

    if (valor_input == 'stock_añadido_con_exito') {

        Swal.fire({
            icon: "success",
            text: "Stock añadido con exito",
            width: "42%",
            height: "20%",
            timer: 1700,
            showConfirmButton: false
        });

    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    validador_input();
});



function valida_digitacion() {
    let form = document.querySelector("form");
    let input_cantidad = document.getElementById('input_cantidad');
    let valor_input = input_cantidad.value;

    form.addEventListener("submit", function(event) {
        event.preventDefault();
    })

    if (valor_input <= 0) {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "La cantidad solicitada es menor o igual a cero",
            width: "50%",
            height: "30%",
            showConfirmButton: true
        });
    }
    else {
        form.submit();
    }
}







 // Función para abrir el modal
 function abrirModal(idProducto) {
    // Cargar el contenido de editar_cantidad.html en el modalContenedor
    var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.innerHTML = "";

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            modalContenedor.innerHTML = this.responseText;

            // Mostrar el modal
            modalContenedor.style.display = "block";
        }
    };

    xhttp.open("GET", "/editar_Cantidad/" + idProducto, true);
    xhttp.send();
}

// Función para cerrar el modal
function cerrarModal() {
    var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.style.display = "none";
};

function detenerPropagacion(event) {
    event.stopPropagation();
}