function buscarClientes() {
    var input, filter, table, tr, td, i, j, txtValue, noResults;

    input = document.getElementById("searchClientes");
    filter = input.value.toUpperCase();
    table = document.getElementById("TablaClientes");
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

document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("TablaClientes");
    var rows = table.getElementsByTagName("tr");
  
    var visibleRowCount = 10; // Número de filas visibles inicialmente
  
    // Ocultar filas que están más allá del número de filas visibles
    for (var i = visibleRowCount; i < rows.length; i++) {
      rows[i].style.display = "none";
    }
  
    // Función para mostrar más filas cuando se hace scroll
    function mostrarMasFilas() {
      var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
      var windowHeight = window.innerHeight;
      var tableBottom = table.offsetTop + table.offsetHeight;
  
      if (scrollTop + windowHeight >= tableBottom) {
        // Mostrar las filas ocultas
        for (var i = visibleRowCount; i < rows.length; i++) {
          rows[i].style.display = "none";
        }
  
        // Actualizar el número de filas visibles
        visibleRowCount = rows.length;
      }
    }
  
    // Asignar el evento de scroll a la función mostrarMasFilas
    window.addEventListener("scroll", mostrarMasFilas);
  });