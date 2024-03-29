/* -------------------- Desplazamiento del formulario -------------------------- */


let boton_continuar_1 = document.getElementById('btn-continuar_1');

boton_continuar_1.addEventListener("click", function () {
    let sesion_formulari_2 = document.getElementById('sesion_formulari_2');
    let barra_progreso_2 = document.getElementById('barra_progreso_2');
    let sesion_boton_2 = document.getElementById('sesion_boton_2');

    sesion_formulari_2.style.right = "0%";
    sesion_boton_2.style.right = "0%";
    barra_progreso_2.style.background = "#358CB4"
    
});


let boton_volver_1 = document.getElementById('btn-volver_1');

boton_volver_1.addEventListener("click", function() {
    let sesion_formulari_2 = document.getElementById('sesion_formulari_2');
    let barra_progreso_2 = document.getElementById('barra_progreso_2');
    let sesion_boton_2 = document.getElementById('sesion_boton_2');

    sesion_formulari_2.style.right = "-100%";
    sesion_boton_2.style.right = "-200%";
    barra_progreso_2.style.background = "white"
    
});




let boton_continuar_2 = document.getElementById('btn-continuar_2');

boton_continuar_2.addEventListener("click", function() {
    let sesion_formulari_3 = document.getElementById('sesion_formulari_3');
    let barra_progreso_3 = document.getElementById('barra_progreso_3');
    let sesion_boton_3 = document.getElementById('sesion_boton_3');

    sesion_formulari_3.style.right = "0%";
    sesion_boton_3.style.right = "0%";
    barra_progreso_3.style.background = "#358CB4"
})


let boton_volver_2 = document.getElementById('btn-volver_2');

boton_volver_2.addEventListener("click", function() {
    let sesion_formulari_3 = document.getElementById('sesion_formulari_3');
    let barra_progreso_3 = document.getElementById('barra_progreso_3');
    let sesion_boton_3 = document.getElementById('sesion_boton_3');

    sesion_formulari_3.style.right = "-100%";
    sesion_boton_3.style.right = "-200%";
    barra_progreso_3.style.background = "white"
    
});


/*  animaciones envio formulario */

function animacion_envio() {
    let form = document.querySelector('form');
    let nombre_producto = document.getElementById('nombre_producto').value;
    let categorias = document.getElementById('categorias').value;
    let ubicacion = document.getElementById('ubicacion').value;
    let precio_compra = parseFloat(document.getElementById('precio_compra').value);
    let precio_venta = parseFloat(document.getElementById('precio_venta').value);
    let cantidad_producto = parseInt(document.getElementById('cantidad_producto').value);
    let stockminimo = parseInt(document.getElementById('stockminimo').value);

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Verificar si el precio de venta es menor o igual al precio de compra
        if (precio_venta <= precio_compra){
            Swal.fire({
                icon: "error",
                title: "Error",
                text : "El precio de Venta No puede ser igual o inferior al precio de Compra",
                width: "50%",
                height: "20%",
                showConfirmButton: true
            });
            document.getElementById('precio_venta').focus();
            return; // Detiene el envío del formulario
        }

        // Si la validación pasa, mostrar el mensaje de éxito
        Swal.fire({
            icon: "success",
            text: "Registrando producto",
            width: "42%",
            height: "20%",
            timer: 1000, // Tiempo de duración del mensaje
            showConfirmButton: false
        });

        // Enviar el formulario después de un tiempo
        setTimeout(function() {
            form.submit();
        }, 1100);
    });

    // Si hay campos obligatorios que faltan o valores incorrectos, mostrar mensajes de error
    if (!nombre_producto || !precio_venta || !precio_compra || !cantidad_producto || !stockminimo || !categorias || !ubicacion ||
        precio_compra < 0 || precio_venta < 0 || cantidad_producto <= 0 || stockminimo < 0) {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Por favor, verifique los campos y corrija cualquier error antes de enviar el formulario.",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
        return; // Detiene el envío del formulario
    }
}

 // Función para formatear un número como moneda colombiana
 function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

// Función para formatear el valor del input cuando cambia
/* function formatInputValue(inputId) {
    let input = document.getElementById(inputId);
    let value = input.value.replace(/\./g, ''); // Eliminar puntos existentes
    input.value = formatNumber(value);
}

// Event listener para formatear el valor del input cuando cambia
document.getElementById('precio_venta').addEventListener('input', function() {
    formatInputValue('precio_venta');
});

document.getElementById('precio_compra').addEventListener('input', function() {
    formatInputValue('precio_compra');
}); */

/* ----- Control para no ingresar numeros negativos ---------------- */

document.getElementById('estante').addEventListener('input', function(event) {
    let estante_input = event.target;
    let valor = parseInt(estante_input.value);
    if (valor < 0) {
        estante_input.setCustomValidity('No se permiten números negativos');
    } else {
        estante_input.setCustomValidity('');
    }
});

document.getElementById('stockminimo').addEventListener('input', function(event) {
    let estante_input = event.target;
    let valor = parseInt(estante_input.value);
    if (valor < 0) {
        estante_input.setCustomValidity('No se permiten números negativos, en el campo cantidad minima');
    } else {
        estante_input.setCustomValidity('');
    }
});

document.getElementById('cantidad_producto').addEventListener('input', function(event) {
    let estante_input = event.target;
    let valor = parseInt(estante_input.value);
    if (valor < 0) {
        estante_input.setCustomValidity('No se permiten números negativos, en el campo cantidad de producto');
    } else {
        estante_input.setCustomValidity('');
    }
});




