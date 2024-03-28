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


function verifica_input_rol() {
    let btn_crear = document.getElementById('btn_crear');
    let isla_btns = document.getElementById('conten_btn_navegacion');
    let botones_credito_pago = document.getElementsByClassName('btns_centro');
    let input_rol = document.getElementById('input_rol');
    let valor = input_rol.value;

    if (valor === "administrador" || valor === "almacenista")  {
        for (let i = 0; i < botones_credito_pago.length; i++) {
            botones_credito_pago[i].style.visibility  = "visible";
        }

        btn_crear.style.display = "block"
    } else {
        isla_btns.style.width = "20%"
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    validador_input();
    verifica_input_rol();
});





/*  // Función para abrir el modal para aumentar cantidad de producto Cantidady no dejarlo cerrar al poner el cursor dentro del input
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
}; */

function detenerPropagacion(event) {
    event.stopPropagation();
}

// Funcion para controlar la cantidad de items a mostrar
document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("Tabla_product");
    var rows = table.getElementsByTagName("tr");

    for (var i = 11; i < rows.length; i++) {
        rows[i].style.display = "none";
    }
});