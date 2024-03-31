
function loadDataForEdit(cotizacionId) {
    fetch(`/editarCotizacion/${cotizacionId}`)
        .then(response => response.json())
        .then(data => {
            // Función para formatear la fecha en 'YYYY-MM-DD'
            function formatFecha(fecha) {
                var fechaObj = new Date(fecha);
                return fechaObj.toISOString().split('T')[0];
            }

            // Formatea y asigna los valores a los campos del modal
            document.getElementById('fechaInicioEditar').value = formatFecha(data.fecha_inicio_cotizacion);
            document.getElementById('fechaFinEditar').value = formatFecha(data.fecha_fin_cotizacion);

            // Llena el campo del cliente
            var clienteSelect = document.getElementById('clienteCotizacionEditar');
            clienteSelect.value = data.cliente_id; // Asigna el valor del ID del cliente

            // Llena la tabla de productos seleccionados
            var productosSeleccionadosTable = document.getElementById('productosSeleccionadosEditar');

            // Limpia la tabla antes de agregar nuevos productos
            productosSeleccionadosTable.innerHTML = '';

            data.detalle.forEach(detalle => {
                var row = productosSeleccionadosTable.insertRow();
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);

                cell1.innerHTML = detalle.nombre_producto;
                // Añadir campo de entrada para editar la cantidad
                cell2.innerHTML = `<input type="number" name="cantidad_productos_cotizacion[]" value="${detalle.cantidad_productos_cotizacion}" min="1">`;
                // Añadir botón para eliminar la fila
                cell3.innerHTML = `<button type="button" class="eliminar-button" onclick="eliminarFila(this)">Eliminar</button>`;
            });

            // Agrega la funcionalidad de búsqueda y selección en tiempo real para productos
            var searchProductosEditar = document.getElementById('searchProductosEditar');
            searchProductosEditar.addEventListener('input', filterProductss);

            // Llena la tabla de productos disponibles
            var productTable = document.getElementById('productTable');
            productTable.innerHTML = '';

            data.productos.forEach(producto => {
                var row = productTable.insertRow();
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);

                cell1.innerHTML = producto.nombre_producto;
                cell2.innerHTML = `<button type="button" class="select-button" onclick="selectProducts('${producto.nombre_producto}')">Seleccionar</button>`;
            });
        })
        .catch(error => console.error('Error:', error));
}

/* function filterProducts() {

    var searchTerm = searchProductosEditar.value.toLowerCase();

    
    $('.product-rows').each(function() {
        var productName = $(this).find('td:first').text().toLowerCase();

        
        if (productName.includes(searchTerm)) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}
 */
function eliminarFila(button) {
    var row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}



function filterProductss() {
    // Obtener el valor del campo de búsqueda
    var searchTerm = $('#searchProductosEditar').val().toLowerCase();

    // Filtrar las filas de la tabla
    $('.product-rows').each(function() {
        var productName = $(this).find('td:first').text().toLowerCase();
        
        // Mostrar u ocultar la fila según si coincide con el término de búsqueda
        if (productName.includes(searchTerm)) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}

function selectProducts(productName) {
    // Obtener la tabla de productos seleccionados
    var productosSeleccionadosTable = document.getElementById('productosSeleccionadosEditar');

    // Verificar si el producto ya está en la tabla
    var productoExistente = false;
    var filas = productosSeleccionadosTable.getElementsByTagName('tr');
    for (var i = 0; i < filas.length; i++) {
        var nombreProductoSeleccionado = filas[i].getElementsByTagName('td')[0].innerText;
        if (nombreProductoSeleccionado === productName) {
            // Si el producto ya está en la tabla, incrementa la cantidad
            var cantidadInput = filas[i].getElementsByTagName('input')[0];
            cantidadInput.value = parseInt(cantidadInput.value) + 1;
            productoExistente = true;
            break;
        }
    }

    if (!productoExistente) {
        // Si el producto no está en la tabla, agrégalo
        var row = productosSeleccionadosTable.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);

        cell1.innerHTML = productName;
        // Añadir campo de entrada para la cantidad
        cell2.innerHTML = `<input type="number" name="cantidad_productos_cotizacion[]" value="1" min="1">`;
        // Añadir botón para eliminar la fila
        cell3.innerHTML = `<button type="button" class="eliminar-button" onclick="eliminarFila(this)">Eliminar</button>`;
    }
}
