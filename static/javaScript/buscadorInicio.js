
function buscarEnTiempoReal() {
    var input, filter, modulos, a, i, txtValue;

    input = document.getElementById("searchProduct");
    filter = input.value.toUpperCase();
    modulos = document.getElementById("modulos").getElementsByTagName("a");

    for (i = 0; i < modulos.length; i++) {
        a = modulos[i];
        txtValue = a.textContent || a.innerText;

        
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a.style.display = "";
        } else {
            a.style.display = "none";
        }
    }
};




function oculta_modulos() {
    let productos = document.getElementById('modulo_productos');
    let ventas = document.getElementById('modulo_ventas');
    let cotizaciones = document.getElementById('modulo_cotizaciones');
    let compras_prove = document.getElementById('modulo_compra_prove');
    let modulo_clientes = document.getElementById('modulo_clientes');
    let modulo_empleados = document.getElementById('modulo_empleados');


    let input_oculto = document.getElementById('input_oculta_rol');
    let valor_input = input_oculto.value;
    console.log(valor_input)

    if (valor_input == "administrador") {

        productos.style.display = "block";
        setTimeout( function() {
            productos.style.opacity = "1"
        }, 25)

        ventas.style.display = "block";
        setTimeout( function() {
            ventas.style.opacity = "1"
        }, 55)

        cotizaciones.style.display = "block";
        setTimeout( function() {
            cotizaciones.style.opacity = "1"
        }, 85)

        compras_prove.style.display = "block";
        setTimeout( function() {
            compras_prove.style.opacity = "1"
        }, 115)

        modulo_clientes.style.display = "block";
        setTimeout( function() {
            modulo_clientes.style.opacity = "1"
        }, 145)

        modulo_empleados.style.display = "block";
        setTimeout( function() {
            modulo_empleados.style.opacity = "1"
        }, 175)



    } else if (valor_input == "vendedor") {

        ventas.style.display = "block";
        setTimeout( function() {
            ventas.style.opacity = "1"
        }, 25)

        cotizaciones.style.display = "block";
        setTimeout( function() {
            cotizaciones.style.opacity = "1"
        }, 55)

        modulo_clientes.style.display = "block";
        setTimeout( function() {
            modulo_clientes.style.opacity = "1"
        }, 85)

    } else if (valor_input == "almacenista") {
        productos.style.display = "block";
        setTimeout( function() {
            productos.style.opacity = "1"
        }, 25)

        compras_prove.style.display = "block";
        setTimeout( function() {
            compras_prove.style.opacity = "1"
        }, 55)
    }
    
}



/* funcion que utiliza una ruta para mostrar ventas dependiendo de si es administrador o vendedor */
function valida_rol_ventas() {
    let modulo_ventas = document.getElementById('modulo_ventas');
    let input_validador = document.getElementById('input_valida_ventas');
    valor_input = input_validador.value;

    if (valor_input == "vendedor") {
        modulo_ventas.href = "/muestra_ventas_vendedor"
    }


}


document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    oculta_modulos();
    valida_rol_ventas();
    
});





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