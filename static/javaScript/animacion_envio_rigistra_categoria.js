function animacion_envio() {
    let form = document.querySelector('form');
    let nombre = document.getElementById('nombre').value;

    form.addEventListener("submit", function(event) {
        event.preventDefault()
    });

    if (nombre.length > 0) {

        Swal.fire({
            icon: "success",
            text: "Registrando categoria",
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
            text: "¡Falta por completar el campo categoria!",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    };
}