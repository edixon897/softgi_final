
var tablaOriginal;  // Variable para almacenar la tabla original antes de realizar la búsqueda
    
        $(document).ready(function() {
            // Guardar la tabla original cuando se carga el documento
            tablaOriginal = $('#TablaClientes tbody').html();
    
            $('#searchClientes').on('input', function() {
                var busqueda = $(this).val().trim();
                if (busqueda.length > 1) {
                    buscarEnTiempoReal(busqueda);
                } else {
                    restaurarTabla();
                }
            });
        });
        
        function buscarEnTiempoReal(busqueda) {
          $.ajax({
              type: 'POST',
              url: '/buscar_cliente',
              data: { 'searchClientes': busqueda },
              dataType: 'json', // Especifica que esperas una respuesta JSON
              success: function(response) {
                  console.log('Respuesta del servidor:', response);
                  if (response.result) {
                      actualizarTabla(response.result);
                  } else if (response.error) {
                      console.error('Error en la respuesta del servidor:', response.error);
                      // Maneja el error de forma adecuada
                  } else {
                      console.warn('Respuesta inesperada del servidor');
                  }
              },
              error: function(xhr, status, error) {
                  console.error('Error al realizar la búsqueda:', error);
              }
          });
      }
        
        function restaurarTabla() {
            // Eliminar filas duplicadas antes de restaurar la tabla original
            var tabla = $('#TablaClientes tbody');
            eliminarFilasDuplicadas(tabla);

            // Restaurar la tabla a su estado original
            tabla.empty();
            tabla.append(tablaOriginal);
            // Asignar eventos onclick de nuevo después de restaurar la tabla
            asignarEventosClick();
        }
        function eliminarFilasDuplicadas(tabla) {
            var seen = {};
            tabla.find('tr').each(function() {
                var txt = $(this).text();
                if (seen[txt]) $(this).remove();
                else seen[txt] = true;
            });
        }
        
        function actualizarTabla(data) {
          var tabla = $('#TablaClientes tbody');
          tabla.empty();
          if (data.length > 0) {
              $.each(data, function(index, row) {
                  var tr = $('<tr>');
                  $.each(row, function(key, value) {
                      $('<td>').text(value).appendTo(tr);
                  });
                  // Botones de editar y eliminar
                  var editarBtn = $('<td><button onclick="abrirModalEditar(\'' + row[0] + '\')"><i class="lni lni-pencil"></i></button></td>');
                  tr.append(editarBtn);
                  var eliminarBtn = $('<td><button onclick="eliminarProducto(\'' + row[0] + '\')"><i class="lni lni-trash-can"></i></button></td>');
                  tr.append(eliminarBtn);
                  tabla.append(tr);
              });
              asignarEventosClick();
          } else {
              tabla.append('<tr><td colspan="7">No se encontraron resultados</td></tr>');
          }
      }
    

// Función para verificar si un valor es una fecha
function isDate(value) {
    return !isNaN(Date.parse(value));
}

// Función para formatear la fecha 
function formatDate(dateString) {
    var date = new Date(dateString);
    var year = date.getFullYear();
    var month = ('0' + (date.getMonth() + 1)).slice(-2);
    var day = ('0' + date.getDate()).slice(-2);
    return year + '-' + month + '-' + day;
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






/*  Oculta funciones si es vendedor */
function verifica_input_rol() {
  let btn_eliminar = document.getElementsByClassName('btn_eliminar');
  let input_rol = document.getElementById('input_rol');
  let valor = input_rol.value;

  if (valor === "administrador")  {
      for (let i = 0; i < btn_eliminar.length; i++) {
          btn_eliminar[i].style.visibility  = "visible";
      }
  }
}

document.addEventListener("DOMContentLoaded", function() {
  // Llama a la función para realizar la verificación inicial
  verifica_input_rol();
});
