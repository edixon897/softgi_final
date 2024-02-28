// Función para abrir el modal
function abrirModal(contador) {
    // Cargar el contenido de editar_cantidad.html en el modalContenedor
    var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.innerHTML = "";

    var conten_registra_pago = document.getElementById("conten_registra_pago");
    conten_registra_pago.style.display = "block"

    var btn_enviar = document.getElementById('btn_enviar');
    btn_enviar.style.backgroundColor = "white"
    btn_enviar.style.color = "#358CB4"
    btn_enviar.style.border = "1px solid #358CB4"

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            modalContenedor.innerHTML = this.responseText;

            // Mostrar el modal
            modalContenedor.style.display = "block";
        }
    };

    xhttp.open("GET", "/abono_credito_2/" + contador, true);
    xhttp.send();
}

// Función para cerrar el modal
function cerrarModal() {
    var modalContenedor = document.getElementById("modalContenedor");
    modalContenedor.style.display = "none";

    var btn_enviar = document.getElementById('btn_enviar');
    btn_enviar.style.backgroundColor = "#358CB4"
    btn_enviar.style.color = "white"
    btn_enviar.style.border = "none"
}