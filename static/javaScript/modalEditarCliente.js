function abrirModalEditar(documento) {
    $.ajax({
        url: `/obtenerFormularioEditar/${documento}`,
        type: 'GET',
        success: function(data) {
            $('#modalContainer').html(data); // Insertar el contenido del modal en el contenedor
            $('#editarClienteModal').show(); // Mostrar el modal
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
    
    $(window).click(function (e) {
        if (e.target.id === "editarClienteModal") {
            $("#editarClienteModal").hide();
        }
    });
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
          rows[i].style.display = "";
        }
  
        // Actualizar el número de filas visibles
        visibleRowCount = rows.length;
      }
    }
  
    // Asignar el evento de scroll a la función mostrarMasFilas
    window.addEventListener("scroll", mostrarMasFilas);
  });


  