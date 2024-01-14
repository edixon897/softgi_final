function campo_lleno1() {
    var documento = document.getElementById("documento");
    var valor = documento.value;

    if (valor.length > 0) {
        documento.style.border = "1px solid #358CB4";
    } else {
        documento.style.border = "1px solid ##358CB4";
    }
}


function campo_lleno2() {
    var nombre = document.getElementById("nombre");
    var label = document.getElementById("label_nombre");
    var valor = nombre.value;

    if (valor.length > 0) {
        nombre.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        nombre.style.border = "1px solid #358CB4";
    }
}


function campo_lleno3() {
    var apellido = document.getElementById("apellido");
    var valor = apellido.value;
    var label = document.getElementById("label_apellido");

    if (valor.length > 0) {
        apellido.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        apellido.style.border = "1px solid #358CB4";
    }
}


function campo_lleno4() {
    var fecha = document.getElementById("fecha");
    var label = document.getElementById("label_fecha");
    var valor = fecha.value;

    if (valor.length > 0) {
        fecha.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        fecha.style.border = "1px solid #358CB4";
    }
}


function campo_lleno5() {
    var opt = document.getElementById("opt");
    var label = document.getElementById("label_otp");
    var valor = opt.value;

    if (valor.length > 0) {
        opt.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        opt.style.border = "1px solid #358CB4";
    }
}


function campo_lleno6() {
    var contacto = document.getElementById("contacto");
    var label = document.getElementById("label_contacto");
    var valor = contacto.value;

    if (valor.length > 0) {
        contacto.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        contacto.style.border = "1px solid #358CB4";
    }
}


function campo_lleno7() {
    var correo = document.getElementById("correo");
    var label = document.getElementById("label_correo");
    var valor = correo.value;

    if (valor.length > 0) {
        correo.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        correo.style.border = "1px solid #358CB4";
    }
}


function campo_lleno8() {
    var direccion = document.getElementById("direccion");
    var label = document.getElementById("label_direccion");
    var valor = direccion.value;

    if (valor.length > 0) {
        direccion.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        direccion.style.border = "1px solid #358CB4";
    }
}


function campo_lleno9() {
    var direccion = document.getElementById("ciudad");
    var label = document.getElementById("label_ciudad");
    var valor = ciudad.value;

    if (valor.length > 0) { 
        ciudad.style.border = "1px solid #358CB4";
        label.style.color = "#358CB4"
    } else {
        ciudad.style.border = "1px solid #358CB4";
    }
}