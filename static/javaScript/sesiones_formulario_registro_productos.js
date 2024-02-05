

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
    });

    if (nombre_producto && precio_venta && precio_compra && cantidad_producto && stockminimo && categorias && ubicacion) {
        if (precio_compra >= 0 && precio_venta >= 0 && cantidad_producto > 0 && stockminimo >= 0) {
            Swal.fire({
                icon: "success",
                text: "Registrando producto",
                width: "42%",
                height: "20%",
                timer: 1000,
                showConfirmButton: false
            });
            setTimeout(function() {
                form.submit();
            }, 1100);
        } else {
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "Valor negativo digitado",
                width: "50%",
                height: "20%",
                showConfirmButton: true
            });
        }
    } else {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Faltan campos por completar",
            width: "50%",
            height: "20%",
            showConfirmButton: true
        });
    }
};
