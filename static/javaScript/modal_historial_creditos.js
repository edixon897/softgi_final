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

// Funcion para controlar la cantidad de items a mostrar
document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("tablaVentas");
    var rows = table.getElementsByTagName("tr");

    for (var i = 11; i < rows.length; i++) {
        rows[i].style.display = "none";
    }
});








/* Disminuye el tamaño del contenedor de las opciones */
function disminuye_tamaño_isla(){

    /* Desabilito el enlace */
    let link = document.getElementById('Muestra_ventas').addEventListener('click', function(event) {
        event.preventDefault();
    });

    /* Capturo y aumento el tamaño del contenedor */
    let conten_btns = document.getElementById('conten_btn_navegacion');
    conten_btns.style.width = "30%";

    /* Retraso el tiempo en q aparece el enlace */
    let enlace_salida = document.getElementById('enlace_salida');
    setTimeout( function() {
        enlace_salida.style.display = "none"
    },90)
 
    /* Retraso el proceso del enlace */
    setTimeout( function() {
        window.location.href = "/muestra_ventas"
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