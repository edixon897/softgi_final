$(document).ready(function () {
    // Cuando se hace clic en el botón para abrir el modal
    $("#openCrearCotizacionModal").click(function () {
        $("#crearCotizacionModal").css("display", "block");
    });

    // Cuando se hace clic fuera del modal, se cierra
    $(window).click(function (e) {
        if (e.target.id === "crearCotizacionModal") {
            $("#crearCotizacionModal").css("display", "none");
        }
    });
});
