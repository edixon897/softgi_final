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