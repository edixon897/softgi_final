

function abrirModalEditCompra(id_producto) {
    $.ajax({
        url: `/modificar_Producto/${id_producto}`,
        type: 'GET',
        success: function(data) {
            $('#modalContainer').html(data); // Insertar el contenido del modal en el contenedor
            $('#ModalEditProducto').show(); // Mostrar el modal
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
    
    $(window).click(function (e) {
        if (e.target.id === "ModalEditProducto") {
            $("#ModalEditProducto").hide();
        }
    });
}