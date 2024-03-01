function abrirModal() {
    console.log("Abriendo modal");
    var modal = document.getElementById('modal');
    modal.style.display ='block';
}

function cerrarModal() {
    console.log("Cerrando modal");
    var modal = document.getElementById('modal');
    modal.style.display = 'none';
}

function registrar() {
    console.log("Entró a la función registrar");
// Obtener los valores ingresados en la ventana modal
var proveedorCompraElement = document.getElementById('proveedor_compra');
var fechaCompraElement = document.getElementById('fecha_compra');
var numFacturaProveedorElement = document.getElementById('num_factura_proveedor');
var productoCompraElement = document.getElementById('producto_compra');
var cantidadCompraElement = document.getElementById('cantidad_compra');
var valorUnidadElement = document.getElementById('valor_unidad');


// Verificar que los elementos existan antes de acceder a sus propiedades
if (proveedorCompraElement && fechaCompraElement && numFacturaProveedorElement && productoCompraElement && cantidadCompraElement && valorUnidadElement) {
    var proveedorCompra = proveedorCompraElement.value;
    var fechaCompra = fechaCompraElement.value;
    var numFacturaProveedor = numFacturaProveedorElement.value;
    var productoCompra = productoCompraElement.value;
    var cantidadCompra = cantidadCompraElement.value;
    var valorUnidad = valorUnidadElement.value;

// Realizar una solicitud al servidor para guardar los datos
guardarDatosEnBD(proveedorCompra, fechaCompra, numFacturaProveedor, productoCompra, cantidadCompra, valorUnidad);

// Cerrar la modal
document.getElementById('modal').style.display = 'none';
} else {
console.error('Alguno de los elementos no existe en el DOM.');
}
}

function agregarProducto() {
    // Crear campos dinámicamente y agregarlos al formulario
    var form = document.getElementById('compraForm');

    var div = document.createElement('div');
    div.innerHTML = '<label for="producto_compra_modal">Producto</label>' +
                    '<input type="text" name="productos[]" id="producto_compra_modal" placeholder="Producto" class="campo">' +
                    '<label for="cantidad_modal">Cantidad</label>' +
                    '<input type="number" name="cantidades[]" id="cantidad_modal" placeholder="Cantidad" class="campo">' +
                    '<label for="valor_unidad_modal">Valor por unidad</label>' +
                    '<input type="number" name="valores_unitarios[]" id="valor_unidad_modal" placeholder="Valor por unidad" class="campo">';

    form.appendChild(div);
}

function guardarDatosEnBD(proveedorCompra, fechaCompra, numFacturaProveedor, productoCompra, cantidadCompra, valorUnidad) {
// Obtener el token de seguridad CSRF si estás utilizando Flask-WTF
var csrfToken = document.getElementsByName('csrf_token')[0].value;

// Realizar una solicitud al servidor para guardar los datos
fetch('/guardar_datos_en_bd', {
method: 'POST',
headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken,  // Añade el token CSRF si estás utilizando Flask-WTF
},
body: JSON.stringify({
    proveedorCompra: proveedorCompra,
    fechaCompra: fechaCompra,
    numFacturaProveedor: numFacturaProveedor,
    productoCompra: productoCompra,
    cantidadCompra: cantidadCompra,
    valorUnidad: valorUnidad,
}),
})
.then(response => {
if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
}
return response.json();
})
.then(data => {
// Manejar la respuesta del servidor
console.log('Respuesta del servidor:', data);

// Cerrar la modal solo si la respuesta es exitosa
if (data.status === 'success') {
    document.getElementById('modal').style.display = 'none';
    // Puedes hacer otras acciones aquí después de cerrar la modal si es necesario
} else {
    console.error('Error en la respuesta del servidor:', data);
    // Puedes manejar el error de otra manera si es necesario
}
})
.catch((error) => {
console.error('Error en la solicitud fetch:', error);
});
}