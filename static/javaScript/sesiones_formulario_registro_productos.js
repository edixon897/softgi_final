
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