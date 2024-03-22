$(document).ready(function () {
    // Cuando se hace clic en el botón para abrir el modal
    $("#abrirModalBtn").click(function () {
        console.log("abre modal")
        $("#crearProveedorModal").css("display", "block");
    });

    // Cuando se hace clic fuera del modal, se cierra
    $(window).click(function (e) {
        if (e.target.id === "crearProveedorModal") {
            $("#crearProveedorModal").css("display", "none");
        }
    });
});


/* Funcion que oculta el editar y eliminar para el rol almacenista */

function verifica_input_rol() {
    let botones = document.getElementsByClassName('btns_centro');
    let input_rol = document.getElementById('input_rol');
    let valor = input_rol.value;

    if (valor === "administrador")  {
        for (let i = 0; i < botones.length; i++) {
            botones[i].style.visibility  = "visible";
        }

        btn_crear.style.display = "block"
    }
}

document.addEventListener("DOMContentLoaded", function() {
    verifica_input_rol()
})