
function buscarEnTiempoReal() {
    var input, filter, modulos, a, i, txtValue;

    input = document.getElementById("searchProduct");
    filter = input.value.toUpperCase();
    modulos = document.getElementById("modulos").getElementsByTagName("a");

    for (i = 0; i < modulos.length; i++) {
        a = modulos[i];
        txtValue = a.textContent || a.innerText;

        
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a.style.display = "";
        } else {
            a.style.display = "none";
        }
    }
};
/* const socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

socket.on('mostrar_modal', function(data) {
    document.getElementById('alertMessage').innerText = data.mensaje;
    document.getElementById('alertModal').style.display = 'block';
});

function cerrarModal() {
    document.getElementById('alertModal').style.display = 'none';
} */


document.getElementById("searchProduct").addEventListener("input", buscarEnTiempoReal);