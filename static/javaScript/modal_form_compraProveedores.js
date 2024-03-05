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

var contadorProductos = 0;

function agregarProducto() {
    contadorProductos++;
    // Crear campos dinámicamente y agregarlos al formulario
    var form = document.getElementById('compraForm');

    var div = document.createElement('div');
    div.innerHTML = '<label for="producto_compra_modal_'+ contadorProductos +'">Producto</label>' +
                    '<input type="text" name="producto_compra[]" id="producto_compra_modal_'+ contadorProductos +'" placeholder="Producto" class="campo">' +
                    '<label for="cantidad_modal_'+ contadorProductos +'">Cantidad</label>' +
                    '<input type="number" name="cantidad_compra[]" id="cantidad_modal_'+ contadorProductos +'" placeholder="Cantidad" class="campo">' +
                    '<label for="valor_unidad_modal_'+ contadorProductos +'">Valor por unidad</label>' +
                    '<input type="number" name="valor_unidad[]" id="valor_unidad_modal_'+ contadorProductos +'" placeholder="Valor por unidad" class="campo">';

    form.appendChild(div);
    console.log(producto_compra);
    console.log(cantidad_compra);
    console.log(valor_unidad);

}
