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
