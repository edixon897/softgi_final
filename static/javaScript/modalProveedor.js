$(document).ready(function () {
    // Cuando se hace clic en el botón para abrir el modal
    $("#AbrirModal").click(function () {
        $("#crearCProveedorModal").css("display", "block");
    });

    // Cuando se hace clic fuera del modal, se cierra
    $(window).click(function (e) {
        if (e.target.id === "crearCProveedorModal") {
            $("#crearCProveedorModal").css("display", "none");
        }
    });
});
