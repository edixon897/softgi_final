// Función para abrir el modal
function abrirModal(contador) {
    // Cargar el contenido de editar_cantidad.html en el modalContenedor
    var modalContenedor = document.getElementById("modalContenedor");
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

    xhttp.open("GET", "/abono_credito_2/" + contador, true);
    xhttp.send();
}

// Función para cerrar el modal
function cerrarModal() {
    /* var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.style.display = "none"; */

    var conten_registra_pago = document.getElementById("conten_registra_pago");
        var modalContenedor = window.parent.document.getElementById("modalContenedor");
            

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




function abrirModal_2(contador) {
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

    xhttp.open("GET", "/historial_abono/" + contador, true);
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





function verifica_input() {

    let valor_input = document.getElementById('input_error').value;

    if (valor_input == "¡Cantidd_digitada_mayor_a_la_debida!") {

        Swal.fire({
            icon: "error",
            title: "Error",
            text: "La cantidad digitada es mayor a la debida",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });

    } else if (valor_input == "menor_igual_cero") {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "La cantidad digitada es igual a 0 o menor",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    } else if (valor_input == "El_credito_fue_pagado_exitosamente_por_completo") {
        Swal.fire({
            icon: "success",
            text: "El credito fue pagado exitosamente por completo",
            width: "42%",
            height: "20%",
            timer: 2000,
            showConfirmButton: false
        });
    }   else if (valor_input == "Pago_parcial_registrado_exitosamente") {
        Swal.fire({
            icon: "success",
            text: "Pago parcial registrado exitosamente",
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
    valida_rol_ventas();
});



