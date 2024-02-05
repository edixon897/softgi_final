function buscarVENTAS() {
    var input, filter, table, tr, td, i, j, txtValue, noResults;

    input = document.getElementById("buscador_ventas");
    filter = input.value.toUpperCase();
    table = document.getElementById("tablaVentas");
    tr = table.getElementsByTagName("tr");
    noResults = document.getElementById("noResults");


    noResults.style.display = "none";


    for (i = 0; i < tr.length; i++) {
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

        
        tr[i].style.display = encontrado ? "" : "none";
    }

    
    if (Array.from(tr).every(row => row.style.display === "none")) {
        noResults.style.display = "block";
    }
}