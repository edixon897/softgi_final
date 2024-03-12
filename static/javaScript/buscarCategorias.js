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
