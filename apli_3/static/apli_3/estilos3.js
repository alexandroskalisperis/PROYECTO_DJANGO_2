addEventListener("DOMContentLoaded", movimiemto_perros, false);
function movimiemto_perros() {
    document.getElementsByName("boton_like")[0].addEventListener("mouseover", mov_1, false);
    document.getElementsByName("boton_like")[0].addEventListener("mouseout", mov_2, false);

    document.getElementsByName("boton_like")[1].addEventListener("mouseover", mov_3, false);
    document.getElementsByName("boton_like")[1].addEventListener("mouseout", mov_4, false);

    document.getElementsByName("boton_like")[2].addEventListener("mouseover", mov_5, false);
    document.getElementsByName("boton_like")[2].addEventListener("mouseout", mov_6, false);
}

function mov_1() {
    perro_1 = document.getElementById("imagen_perro_1");
    perro_1.style.transform = "rotate(15deg)";
    perro_1.style.transition = "0.3s ease";
    perro_1.style.width = "37%";
}

function mov_2() {
    perro_1.style.transform = "rotate(0deg)";
    perro_1.style.transition = "0.3s ease";
    perro_1.style.width = "35%";
}

function mov_3() {
    perro_2 = document.getElementById("imagen_perro_2");
    perro_2.style.transform = "rotate(15deg)";
    perro_2.style.transition = "0.3s ease";
    perro_2.style.width = "37%";
}

function mov_4() {
    perro_2.style.transform = "rotate(0deg)";
    perro_2.style.transition = "0.3s ease";
    perro_2.style.width = "35%";
}

function mov_5() {
    perro_3 = document.getElementById("imagen_perro_3");
    perro_3.style.transform = "rotate(15deg)";
    perro_3.style.transition = "0.3s ease";
    perro_3.style.width = "37%";
}

function mov_6() {
    perro_3.style.transform = "rotate(0deg)";
    perro_3.style.transition = "0.3s ease";
    perro_3.style.width = "35%";
}

