addEventListener("DOMContentLoaded", inicio, false);
function inicio() {
    document.getElementById("div_general").addEventListener("mouseover", reaccion_1, false);
    document.getElementById("div_general").addEventListener("mouseleave", reaccion_2, false);
       
}

function reaccion_1() {
    titulo_hover = document.getElementById("titulo_1");
    mover_1 = document.getElementsByClassName("div_interno_izquierdo_1")[0];
    enlace_1 = document.getElementById("vinculo_1");
    numero_1 = document.getElementById("numero_temp_1");

    mover_2 = document.getElementsByClassName("div_interno_izquierdo_2")[0];
    enlace_2 = document.getElementById("vinculo_2");
    numero_2 = document.getElementById("numero_temp_2");

    mover_3 = document.getElementsByClassName("div_interno_izquierdo_3")[0];
    enlace_3 = document.getElementById("vinculo_3");
    numero_3 = document.getElementById("numero_temp_3");

    mover_4 = document.getElementsByClassName("div_interno_derecho_1")[0];
    enlace_4 = document.getElementById("vinculo_4");
    numero_4 = document.getElementById("numero_temp_4");

    mover_5 = document.getElementsByClassName("div_interno_derecho_2")[0];
    enlace_5 = document.getElementById("vinculo_5");
    numero_5 = document.getElementById("numero_temp_5");

    mover_6 = document.getElementsByClassName("div_interno_derecho_3")[0];
    enlace_6 = document.getElementById("vinculo_6");
    numero_6 = document.getElementById("numero_temp_6");

    titulo_hover.style.color = "yellow";
    titulo_hover.style.transition = "2s ease";
    titulo_hover.style.textShadow = "-5px 20px 5px black";
    titulo_hover.style.transform = "perspective(250px)";

    mover_1.style .left = "10%";
    mover_1.style .transition = "2s ease";
    enlace_1.style.color = "yellow";
    enlace_1.style.textShadow = "0px 10px 5px black";
    enlace_1.style.transition = "2s ease";
    numero_1.style.color = "yellow";
    numero_1.style.textShadow = "10px 10px 5px black";
    numero_1.style.fontSize = "20px";
    numero_1.style.transition = "2s ease";
    
    mover_2.style.left = "10%";
    mover_2.style.transition = "2s ease";
    enlace_2.style.color = "yellow";
    enlace_2.style.textShadow = "0px 10px 5px black";
    enlace_2.style.transition = "2s ease";
    numero_2.style.color = "yellow";
    numero_2.style.textShadow = "10px 10px 5px black";
    numero_2.style.fontSize = "20px";
    numero_2.style.transition = "2s ease";

    mover_3.style.left = "10%";
    mover_3.style.transition = "2s ease";
    enlace_3.style.color = "yellow";
    enlace_3.style.textShadow = "0px 10px 5px black";
    enlace_3.style.transition = "2s ease";
    numero_3.style.color = "yellow";
    numero_3.style.textShadow = "10px 10px 5px black";
    numero_3.style.fontSize = "20px";
    numero_3.style.transition = "2s ease";

    mover_4.style.left = "10%";
    mover_4.style.transition = "2s ease";
    enlace_4.style.color = "yellow";
    enlace_4.style.textShadow = "0px 10px 5px black";
    enlace_4.style.transition = "2s ease";
    numero_4.style.color = "yellow";
    numero_4.style.textShadow = "10px 10px 5px black";
    numero_4.style.fontSize = "20px";
    numero_4.style.transition = "2s ease";

    mover_5.style.left = "10%";
    mover_5.style.transition = "2s ease";
    enlace_5.style.color = "yellow";
    enlace_5.style.textShadow = "0px 10px 5px black";
    enlace_5.style.transition = "2s ease";
    numero_5.style.color = "yellow";
    numero_5.style.textShadow = "10px 10px 5px black";
    numero_5.style.fontSize = "20px";
    numero_5.style.transition = "2s ease";

    mover_6.style.left = "10%";
    mover_6.style.transition = "2s ease";
    enlace_6.style.color = "yellow";
    enlace_6.style.textShadow = "0px 10px 5px black";
    enlace_6.style.transition = "2s ease";
    numero_6.style.color = "yellow";
    numero_6.style.textShadow = "10px 10px 5px black";
    numero_6.style.fontSize = "20px";
    numero_6.style.transition = "2s ease";
}

function reaccion_2() {
    titulo_hover.style.color = "white";
    titulo_hover.style.transition = "1s ease";
    titulo_hover.style.textShadow = "10px 10px 5px black";


    mover_1.style.left = "10%";
    enlace_1.style.color = "white";
    enlace_1.style.textShadow = "10px 10px 5px black";
    numero_1.style.color = "transparent";
    numero_1.style.textShadow = "none";
    
    mover_2.style.left = "30%";
    enlace_2.style.color = "white";
    enlace_2.style.textShadow = "10px 10px 5px black";
    numero_2.style.color = "transparent";
    numero_2.style.textShadow = "none";

    mover_3.style.left = "50%";
    enlace_3.style.color = "white";
    enlace_3.style.textShadow = "10px 10px 5px black";
    numero_3.style.color = "transparent";
    numero_3.style.textShadow = "none";

    mover_4.style.left = "50%";
    enlace_4.style.color = "white";
    enlace_4.style.textShadow = "-10px 10px 5px black";
    numero_4.style.color = "transparent";
    numero_4.style.textShadow = "none";

    mover_5.style.left = "30%";
    enlace_5.style.color = "white";
    enlace_5.style.textShadow = "-10px 10px 5px black";
    numero_5.style.color = "transparent";
    numero_5.style.textShadow = "none";

    mover_6.style.left = "10%";
    enlace_6.style.color = "white";
    enlace_6.style.textShadow = "-10px 10px 5px black";
    numero_6.style.color = "transparent";
    numero_6.style.textShadow = "none";
}




   
