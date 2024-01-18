

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


/* -------------------- cambia color de los inputs editados del formulario -------------------------- */


function cambia_color_1() {
    let referencia_producto = document.getElementById('referencia_producto');
    let label_1 = document.getElementById('label_1')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label_1.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label_1.style.color = "#358CB4"
    }
    
}


function cambia_color_2() {
    let referencia_producto = document.getElementById('ref_produ_2');
    let label_2 = document.getElementById('label_2')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label_2.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label_2.style.color = "#358CB4"
    }
    
}


function cambia_color_3() {
    let referencia_producto = document.getElementById('ref_produ_3');
    let label = document.getElementById('label_3')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_4() {
    let referencia_producto = document.getElementById('nom_proveedor');
    let label = document.getElementById('label_4')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_5() {
    let referencia_producto = document.getElementById('nom_categoria');
    let label = document.getElementById('label_5')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_6() {
    let referencia_producto = document.getElementById('nombre_producto');
    let label = document.getElementById('label_6')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_7() {
    let referencia_producto = document.getElementById('precio_compra');
    let label = document.getElementById('label_7')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_8() {
    let referencia_producto = document.getElementById('precio_venta');
    let label = document.getElementById('label_8')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_9() {
    let referencia_producto = document.getElementById('descripcion');
    let label = document.getElementById('label_9')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_10() {
    let referencia_producto = document.getElementById('cantidad_producto');
    let label = document.getElementById('label_10')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_11() {
    let referencia_producto = document.getElementById('stockminimo');
    let label = document.getElementById('label_11')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_12() {
    let referencia_producto = document.getElementById('ubicacion');
    let label = document.getElementById('label_12')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}


function cambia_color_13() {
    let referencia_producto = document.getElementById('estante');
    let label = document.getElementById('label_13')

    let longitud = referencia_producto.value;

    if (longitud > 0) {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }else {
        referencia_producto.style.border = "1px solid #358CB4"
        label.style.color = "#358CB4"
    }
    
}