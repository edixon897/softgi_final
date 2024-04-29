
/* Funcion que tiene el modal */
function modal_info() {

    Swal.fire({
        title: "Info",
        text: "Para imprimir la factura, pulsa la tecla Ctrol + P",
        icon: "info"
      });

}

/* Vigilante que activa el modal al cargarse el html */
document.addEventListener("DOMContentLoaded", function() {
    modal_info()
})