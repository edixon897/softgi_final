function buscarCotizacion() {
    var input, filter, table, tr, td, i, txtValue, noResults;

    input = document.getElementById("searchProduct");
    filter = input.value.toUpperCase();
    table = document.getElementById("cotizacionTable");
    tr = table.getElementsByTagName("tr");
    noResults = document.getElementById("noResults");

    
    noResults.style.display = "none";

    
    for (i = 0; i < tr.length; i++) {
        if (!tr[i].getElementsByTagName("td").length) {
            // Si no hay celdas td, es decir, es un encabezado, se salta la iteración.
            continue;
        }
        td = tr[i].getElementsByTagName("td");
        var encontrado = false;

        for (j = 0; j < td.length; j++) {
            if (td[j]) {
                txtValue = td[j].textContent || td[j].innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    encontrado = true;
                    break;
                }
            }
        }

        // Ocultar o mostrar la fila según si se encontró o no la coincidencia.
        tr[i].style.display = encontrado ? "" : "none";
    }

    
    if (Array.from(tr).every(row => row.style.display === "none")) {
        noResults.style.display = "block";
    }
}






/* Esconde los botones de eliminar y editar dependiendo el rol */

function verifica_input_rol() {
    let botones_credito_pago = document.getElementsByClassName('btn_eliminar');
    let input_rol = document.getElementById('input_rol');
    let btn_crear = document.getElementById('abrirModalBtn');
    let valor = input_rol.value;

    if (valor === "administrador" || valor === "almacenista")  {
        for (let i = 0; i < botones_credito_pago.length; i++) {
            botones_credito_pago[i].style.visibility  = "visible";
        } 
    }
    
}


document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    verifica_input_rol();
});






