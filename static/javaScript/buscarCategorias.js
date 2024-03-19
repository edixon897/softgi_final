function buscarCategorias() {
    var input, filter, table, tr, td, i, j, txtValue, noResults;

    input = document.getElementById("searchCategorias");
    filter = input.value.toUpperCase();
    table = document.getElementById("TablaCategorias");
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
};

document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("TablaCategorias");
    var rows = table.getElementsByTagName("tr");

    
    for (var i = 10; i < rows.length; i++) {
        rows[i].style.display = "none";
    }
});





/* Esconde los botones de eliminar y editar dependiendo el rol */

function verifica_input_rol() {
    let botones_credito_pago = document.getElementsByClassName('btns_centro');
    let isla_btns = document.getElementById('conten_btn_navegacion');
    let input_rol = document.getElementById('input_rol');
    let btn_crear = document.getElementById('abrirModalBtn');
    let valor = input_rol.value;

    if (valor === "administrador")  {
        for (let i = 0; i < botones_credito_pago.length; i++) {
            botones_credito_pago[i].style.visibility  = "visible";
        }
        
        btn_crear.style.display = "block"
    }else {
        isla_btns.style.width = "20%"
    }
    
}


document.addEventListener("DOMContentLoaded", function() {
    // Llama a la función para realizar la verificación inicial
    verifica_input_rol();
});