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
            text: "La cantidad solicitada del producto es menor a la disponible",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    }
}



document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    verifica_input();
    verifica_input_2();
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