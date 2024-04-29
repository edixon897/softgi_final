
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
            data: JSON.stringify({ 'buscarClientes': busqueda }),
            contentType: 'application/json',  // Especificar el tipo de contenido
            dataType: 'json',  // Esperar una respuesta en formato JSON
            success: function(response) {
                console.log('Respuesta del servidor:', response);
                if (response.result) {
                    actualizarTabla(response.result);
                } else if (response.error) {
                    console.error('Error en la respuesta del servidor:', response.error);
                } else {
                    console.warn('Respuesta inesperada del servidor');
                }
            },
            error: function(xhr, status, error) {
                console.error('Error al realizar la búsqueda:', error);
            }
        });
    }

    function eliminarCliente(documento) {
        if (confirm('¿Seguro que deseas eliminar este cliente?')) {
            $.ajax({
                type: 'POST',
                url: '/borracliente/' + documento,
                success: function(response) {
                    // Comprobar si hay algún término de búsqueda presente
                    var busqueda = $('#TablaClientes').val().trim();
                    
                        // Si hay un término de búsqueda, realiza de nuevo la búsqueda
                        buscarEnTiempoReal(busqueda);
                    
                },
                error: function(xhr, status, error) {
                    console.error('Error al eliminar el cliente:', error);
                }
            });
        }
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
                for (var i = 0; i < row.length; i++) {
                    var value = row[i];
                    // Comprueba si el valor es una fecha antes de formatear
                      // Aplicar formato de fecha solo a las columnas conocidas que contienen fechas
                    if ((i === 3) && isDate(value)) {  // Asume que las columnas 1 y 3 contienen fechas
                        value = formatDate(value);
                    }
                    $('<td>').text(value).appendTo(tr);
                }
                // Botones de editar y eliminar
                var editarBtn = $('<td><button onclick="abrirModalEditar(\'' + row[0] + '\')"><i id="icono_2" class="lni lni-pencil"></i></button></td>');
                tr.append(editarBtn);
                var eliminarBtn = $('<td><button onclick="eliminarCliente(\'' + row[0] + '\')"><i id="icono_2" class="lni lni-trash-can"></i></button></td>');
                tr.append(eliminarBtn);
                tabla.append(tr);
            });
        } else {
            tabla.append('<tr><td colspan="7">No se encontraron resultados</td></tr>');
        }
    }
    
    
    


// Función para verificar si un valor es una fecha
function isDate(value) {
    var date = new Date(value);
    return !isNaN(date.getTime());
}



function formatDate(dateString) {
    var date = new Date(dateString); // Convierte la cadena de fecha en un objeto Date
    var year = date.getFullYear(); // Obtiene el año
    var month = ('0' + (date.getMonth() + 1)).slice(-2); // Obtiene el mes y lo ajusta a dos dígitos
    var day = ('0' + date.getDate()).slice(-2); // Obtiene el día y lo ajusta a dos dígitos
    return year + '-' + month + '-' + day; // Combina los componentes en el formato deseado
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
