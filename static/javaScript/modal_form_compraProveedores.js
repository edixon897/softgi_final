$(document).ready(function () {
    // Cuando se hace clic en el botón para abrir el modal
    $("#botonAbrirModalBtn").click(function () {
        console.log('ejecutado')
        $("#crearCompraModal").css("display", "block");
    });

    // Cuando se hace clic fuera del modal, se cierra
    $(window).click(function (e) {
        if (e.target.id === "crearCompraModal") {
            $("#crearCompraModal").css("display", "none");
        }
    });
});

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

    var modal = document.getElementById('modal-content');
    modal.scrollTop = modal.scrollHeight;
    console.log(producto_compra);
    console.log(cantidad_compra);
    console.log(valor_unidad);

};

