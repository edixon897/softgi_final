
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



document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    oculta_modulos();
    
});