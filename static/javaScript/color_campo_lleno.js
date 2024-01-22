function campo_lleno1() {
    var documento = document.getElementById("documento");
    var valor = documento.value;

    if (valor.length > 0) {
        documento.style.border = "1px solid #05c673";
    } else {
        documento.style.border = "1px solid black";
    }
}


function campo_lleno2() {
    var nombre = document.getElementById("nombre");
    var valor = nombre.value;

    if (valor.length > 0) {
        nombre.style.border = "1px solid #05c673";
    } else {
        nombre.style.border = "1px solid black";
    }
}


function campo_lleno3() {
    var apellido = document.getElementById("apellido");
    var valor = apellido.value;

    if (valor.length > 0) {
        apellido.style.border = "1px solid #05c673";
    } else {
        apellido.style.border = "1px solid black";
    }
}


function campo_lleno4() {
    var fecha = document.getElementById("fecha");
    var valor = fecha.value;

    if (valor.length > 0) {
        fecha.style.border = "1px solid #05c673";
    } else {
        fecha.style.border = "1px solid black";
    }
}


function campo_lleno5() {
    var opt = document.getElementById("opt");
    var valor = opt.value;

    if (valor.length > 0) {
        opt.style.border = "1px solid #05c673";
    } else {
        opt.style.border = "1px solid black";
    }
}


function campo_lleno6() {
    var contacto = document.getElementById("contacto");
    var valor = contacto.value;

    if (valor.length > 0) {
        contacto.style.border = "1px solid #05c673";
    } else {
        contacto.style.border = "1px solid black";
    }
}


function campo_lleno7() {
    var correo = document.getElementById("correo");
    var valor = correo.value;

    if (valor.length > 0) {
        correo.style.border = "1px solid #05c673";
    } else {
        correo.style.border = "1px solid black";
    }
}


function campo_lleno8() {
    var direccion = document.getElementById("direccion");
    var valor = direccion.value;

    if (valor.length > 0) {
        direccion.style.border = "1px solid #05c673";
    } else {
        direccion.style.border = "1px solid black";
    }
}


function campo_lleno9() {
    var direccion = document.getElementById("ciudad");
    var valor = ciudad.value;

    if (valor.length > 0) { 
        ciudad.style.border = "1px solid #05c673";
    } else {
        ciudad.style.border = "1px solid black";
    }
}




/* Muestra mensaje de error */
function verifica_input() {
    var input_error = document.getElementById("input_error");
    var valorInput = input_error.value;

    if (valorInput == 1) {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "El usuario ya existe",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función handleInput para realizar la verificación inicial
    verifica_input();
});



/* Muestra animacion envio formulario */
function animacion_envio() {

    let form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault()
    });

    let documento = document.getElementById("documento").value;
    let nombre = document.getElementById("nombre").value;
    let apellido = document.getElementById("apellido").value;
    let fecha = document.getElementById("fecha").value;

    if ((documento.length > 0) && (nombre.length > 0) && (apellido.length > 0) && (fecha.length > 0)) {
        Swal.fire({
            icon: "success",
            text: "Registrando cliente",
            width: "42%",
            height: "20%",
            timer: 1000,
            showConfirmButton: false
        });

        setTimeout(function(){
            form.submit()
        },1100);

    } else {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Faltan campos por completar",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        }); 
    };
}