$(document).ready(function () {
    // Cuando se hace clic en el botón para abrir el modal
    $("#abrirModalBtn").click(function () {
        $("#crearEmpleadoModal").css("display", "block");
    });

    // Cuando se hace clic fuera del modal, se cierra
    $(window).click(function (e) {
        if (e.target.id === "crearEmpleadoModal") {
            $("#crearEmpleadoModal").css("display", "none");
        }
    });
});