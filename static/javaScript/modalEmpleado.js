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


$(document).ready(function () {
    // Cuando se hace clic en el botón para abrir el modal
    $("#abrirRecuperar").click(function () {
        $("#recuperarContradoModal").css("display", "block");
    });

    // Cuando se hace clic fuera del modal, se cierra
    $(window).click(function (e) {
        if (e.target.id === "recuperarContradoModal") {
            $("#recuperarContradoModal").css("display", "none");
        }
    });
});





