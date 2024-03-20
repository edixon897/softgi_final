// Obtener el elemento de entrada de fecha
var fechaInput = document.getElementById('fecha_compra_input');

// Escuchar el evento de cambio en el campo de fecha
fechaInput.addEventListener('change', function() {
    // Obtener la fecha seleccionada
    var fechaSeleccionada = new Date(this.value);
    
    // Obtener la fecha y hora actual en la zona horaria de Colombia (UTC-5)
    var fechaActual = new Date(new Date().toLocaleString("en-US", {timeZone: "America/Bogota"}));
    fechaActual.setHours(0, 0, 0, 0); // Establecer la hora a medianoche para ignorar la hora

    // Comparar la fecha seleccionada con la fecha actual
    if (fechaSeleccionada > fechaActual) {
        // Si la fecha seleccionada es mayor que la fecha actual, mostrar el mensaje de error
        document.getElementById('error_fecha').style.display = 'inline';
        // Restaurar la fecha seleccionada a la fecha actual
        this.valueAsDate = fechaActual;
    } else {
        // Si la fecha seleccionada es válida, ocultar el mensaje de error
        document.getElementById('error_fecha').style.display = 'none';
    }
});