$(document).ready(function () {
    // Cuando se hace clic en el botón para abrir el modal
    $("#icono_ver_mas").click(function () {
        console.log('ejecutado')
        $("#actualizarproveedorModal").css("display", "block");
    });

    // Cuando se hace clic fuera del modal, se cierra
    $(window).click(function (e) {
        if (e.target.id === "actualizarproveedorModal") {
            $("#actualizarproveedorModal").css("display", "none");
        }
    });
});
