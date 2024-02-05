
/* Cambia color campo lleno */

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
    // Llama a la función para realizar la verificación inicial
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

        // Obtener la fecha de nacimiento del campo de entrada
        let fechaNacimiento = new Date(document.getElementById("fecha").value);

        // Obtener fecha actual
        let fechaActual = new Date();

        // Calcular la edad del usuario
        let edad = fechaActual.getFullYear() - fechaNacimiento.getFullYear();

        // Verificar si el usuario aún no ha cumplido años este año
        if (fechaActual.getMonth() < fechaNacimiento.getMonth() || (fechaActual.getMonth() === fechaNacimiento.getMonth() && fechaActual.getDate() < fechaNacimiento.getDate())) {
            edad--;
        }

        // Verificar si el usuario es mayor o igual a 18 años
        if (edad >= 18) {

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
        // Si es menor de 18 años, mostrar un mensaje de error

            Swal.fire({
                icon: "error",
                title: "Error",
                text: "El cliente debe ser mayor de 18 años para registrarse.",
                width: "50%",
                height: "20%",
                showConfirmButton: true
            }); 
        }

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


/* Manejo de sesiones formulario */

function desplaza_form() {
    let conten_FORM_2 = document.getElementById("conten_FORM_2");
    let sesion_buttons_2 = document.getElementById("sesion_buttons_2");
    let barra_progreso_2 = document.getElementById("barra_progreso_3");

    conten_FORM_2.style.left = "0%";
    sesion_buttons_2.style.left = "0%";
    barra_progreso_2.style.background = "#358CB4"
}

function desplaza_form_regreso() {
    let conten_FORM_2 = document.getElementById("conten_FORM_2");
    let sesion_buttons_2 = document.getElementById("sesion_buttons_2");
    let barra_progreso_2 = document.getElementById("barra_progreso_3");

    conten_FORM_2.style.left = "100%";
    sesion_buttons_2.style.left = "200%";
    barra_progreso_2.style.background = "white"
}

