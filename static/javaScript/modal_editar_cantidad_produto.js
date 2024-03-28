/* ---------- Funciones del Modal Editar Cantidad de Porducto */

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


/* -------- Funcion que evita que el usuario ingrese cantidad negativa 'Cero o menor que Cero' */
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
            text: "La cantidad ingresada, es menor o igual a cero, verifique",
            width: "50%",
            height: "30%",
            showConfirmButton: true
        });
    }
    else {
        form.submit();
    }
}

