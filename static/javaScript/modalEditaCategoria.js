
function abrirModaledit_categoria(id_categoria) {
    $.ajax({
        url: `/editarCategorias/${id_categoria}`,
        type: 'GET',
        success: function(data) {
            $('#modalContainer').html(data); // Insertar el contenido del modal en el contenedor
            $('#editarCategoriaModal').show(); // Mostrar el modal
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
    
    /* $(window).click(function (e) {
        if (e.target.id === "editarCategoriaModal") {
            $("#editarCategoriaModal").hide();
        }
    }); */
}