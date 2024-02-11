
function filterProducts() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById('searchProductos');
    filter = input.value.toUpperCase();
    table = document.getElementById('productTable');
    tr = table.getElementsByTagName('tr');
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName('td')[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = ''; 
            } else {
                tr[i].style.display = 'none'; 
            }
        }
    }
}


function selectProduct(productName) {
    var tableBody = document.getElementById('productosSeleccionados').getElementsByTagName('tbody')[0];


    var existingRow = findRowByProductName(tableBody, productName);

    if (existingRow) {

        var cantidadInput = existingRow.querySelector('.cantidad-input');
        cantidadInput.value = parseInt(cantidadInput.value) + 1;
    } else {
        
        var row = tableBody.insertRow();

        var cell1 = row.insertCell(0);
        cell1.textContent = productName;

        var cell2 = row.insertCell(1);
        var cantidadInput = document.createElement('input');
        cantidadInput.type = 'number';
        cantidadInput.name = 'cantidadPorProducto[]';
        cantidadInput.className = 'cantidad-input';
        cantidadInput.value = 1; 
        cantidadInput.addEventListener('input', updateTotalQuantity);
        cell2.appendChild(cantidadInput);

        var cell3 = row.insertCell(2);
        var removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.textContent = 'Eliminar';
        removeButton.onclick = function () {
            tableBody.removeChild(row);
            updateTotalQuantity();
        };
        cell3.appendChild(removeButton);
        var referenciaProductoInput = document.createElement('input');
        referenciaProductoInput.type = 'hidden';
        referenciaProductoInput.name = 'referenciaProducto[]';
        referenciaProductoInput.value = productName;
        cell3.appendChild(referenciaProductoInput);
    }

    updateTotalQuantity();
}


function findRowByProductName(tableBody, productName) {
    
    var rows = tableBody.getElementsByTagName('tr');
    for (var i = 0; i < rows.length; i++) {
        var cell1 = rows[i].getElementsByTagName('td')[0];
        if (cell1 && cell1.textContent === productName) {
            return rows[i];
        }
    }
    return null;
}

// Función que actualizar la cantidad total de productos seleccionados
function updateTotalQuantity() {
    var cantidadProductoSeleccionado = document.getElementById('cantidadProductoSeleccionado');
    var cantidadInputs = document.querySelectorAll('.cantidad-input');
    var totalQuantity = Array.from(cantidadInputs).reduce((total, input) => total + (input.value ? parseInt(input.value) : 0), 0);
    cantidadProductoSeleccionado.value = totalQuantity;
}


$(document).ready(function () {
    // Establecer el número inicial de productos a mostrar
    var productosMostrados = 2;

    // Ocultar las filas que están más allá del límite inicial
    $(".product-row:gt(" + (productosMostrados - 1) + ")").hide();

    // Manejar el clic en el botón "Cargar más productos"
    $("#loadMoreButton").click(function () {
        // Mostrar las siguientes 4 filas
        $(".product-row:lt(" + productosMostrados + ")").show();
        // Actualizar el número de productos mostrados
        productosMostrados += 1;

        // Ocultar el botón si no hay más productos por mostrar
        if (productosMostrados >= $(".product-row").length) {
            $("#loadMoreButton").hide();
        }
    });
});

$(document).ready(function () {
    // Establecer el número inicial de productos a mostrar
    var productosMostrados = 2;

    // Ocultar las filas que están más allá del límite inicial
    $(".product-row:gt(" + (productosMostrados - 1) + ")").hide();

    // Manejar el clic en el botón "Cargar más productos"
    $("#loadMoreButton").click(function () {
        // Mostrar las siguientes 2 filas
        $(".product-row:lt(" + productosMostrados + ")").show();
        // Actualizar el número de productos mostrados
        productosMostrados += 2;

        
    });
});