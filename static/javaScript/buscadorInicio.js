
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
        ventas.style.display = "block";
        cotizaciones.style.display = "block";
        compras_prove.style.display = "block";
        modulo_clientes.style.display = "block";
        modulo_empleados.style.display = "block";

    } else if (valor_input == "vendedor") {
        ventas.style.display = "block";
        cotizaciones.style.display = "block";
        modulo_clientes.style.display = "block";

    } else if (valor_input == "almacenista") {
        productos.style.display = "block";
        compras_prove.style.display = "block";
    }
    


}



document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    oculta_modulos();
    
});