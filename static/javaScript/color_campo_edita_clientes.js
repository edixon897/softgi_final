
/*      Cambia el color de los inputs    */


function campo_lleno1() {
    var documento = document.getElementById("documento");
    var valor = documento.value;

    if (valor.length > 0) {
        documento.style.border = "1px solid #358CB4";
    } else {
        documento.style.border = "1px solid ##358CB4";
    }
}


function campo_lleno2() {
    var nombre = document.getElementById("nombre");
    var label = document.getElementById("label_nombre");
    var valor = nombre.value;

    if (valor.length > 0) {
        nombre.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        nombre.style.border = "1px solid #358CB4";
    }
}


function campo_lleno3() {
    var apellido = document.getElementById("apellido");
    var valor = apellido.value;
    var label = document.getElementById("label_apellido");

    if (valor.length > 0) {
        apellido.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        apellido.style.border = "1px solid #358CB4";
    }
}


function campo_lleno4() {
    var fecha = document.getElementById("fecha");
    var label = document.getElementById("label_fecha");
    var valor = fecha.value;

    if (valor.length > 0) {
        fecha.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        fecha.style.border = "1px solid #358CB4";
    }
}


function campo_lleno5() {
    var opt = document.getElementById("opt");
    var label = document.getElementById("label_otp");
    var valor = opt.value;

    if (valor.length > 0) {
        opt.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        opt.style.border = "1px solid #358CB4";
    }
}


function campo_lleno6() {
    var contacto = document.getElementById("contacto");
    var label = document.getElementById("label_contacto");
    var valor = contacto.value;

    if (valor.length > 0) {
        contacto.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        contacto.style.border = "1px solid #358CB4";
    }
}


function campo_lleno7() {
    var correo = document.getElementById("correo");
    var label = document.getElementById("label_correo");
    var valor = correo.value;

    if (valor.length > 0) {
        correo.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        correo.style.border = "1px solid #358CB4";
    }
}


function campo_lleno8() {
    var direccion = document.getElementById("direccion");
    var label = document.getElementById("label_direccion");
    var valor = direccion.value;

    if (valor.length > 0) {
        direccion.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        direccion.style.border = "1px solid #358CB4";
    }
}


function campo_lleno9() {
    var direccion = document.getElementById("ciudad");
    var label = document.getElementById("label_ciudad");
    var valor = ciudad.value;

    if (valor.length > 0) { 
        ciudad.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        ciudad.style.border = "1px solid #358CB4";
    }
}



/*  animaciones envio formulario */

function animacion_envio() {

    let form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault()
    });

    let input_principal = document.getElementById('documento').value;



    if (input_principal.length > 0) {

        
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
            text: "Guardando cambios",
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
                text: "El cliente debe ser mayor de 18 años para poder guardar los cambios.",
                width: "50%",
                height: "20%",
                showConfirmButton: true
            }); 
        }


    } else {
        
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Campo principal vacio",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    }

}