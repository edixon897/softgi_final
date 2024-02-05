function animacion_envio() {
    let form = document.querySelector('form');
    let nombre = document.getElementById('nombre').value;
    let principal_input = document.getElementById('id_categoria').value;

    form.addEventListener("submit", function(event) {
        event.preventDefault()
    });

    if (nombre.length > 0 && principal_input > 0) {

        Swal.fire({
            icon: "success",
            text: "Guardando cambios",
            width: "42%",
            height: "20%",
            timer: 1000,
            showConfirmButton: false
        });

        setTimeout( function() {
            form.submit()
        }, 1100)

    }else{
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "¡Falta campos por completar!",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    };
}