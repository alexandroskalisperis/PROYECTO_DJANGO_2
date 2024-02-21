addEventListener("DOMContentLoaded", inicio, false);
function inicio() {
    estrellas();
    setTimeout(enlace_1, 1000);
    setTimeout(enlace_2, 2000);
    setTimeout(enlace_3, 3000);
    setTimeout(enlace_4, 4000);
    
}
function enlace_1() {
    en_1 = document.getElementsByClassName("enlaces")[0];
    en_1.style.color = "white";
    en_1.style.animationDelay = "ease";
}
function enlace_2() {
    en_2 = document.getElementsByClassName("enlaces")[1];
    en_2.style.color = "white";
    
}
function enlace_3() {
    en_3 = document.getElementsByClassName("enlaces")[2];
    en_3.style.color = "white";
}
function enlace_4() {
    en_4 = document.getElementsByClassName("enlaces")[3];
    en_4.style.color = "white";
}

function estrellas() {
    count = 300;
    scene = document.querySelector("#body");
    i = 0;
    while( i < count)
    {
        star = document.createElement("i");
        x = Math.random()* window.innerWidth;
        y = Math.random()* window.innerHeight;
        duration = Math.random() * 100;
        size = Math.random() * 5;

        star.style.left= x + "px";
        star.style.top= y + "px";
        star.style.width= size + "px";
        star.style.height= size + "px";

        star.style.animationDuration =5 + duration + "s";
        star.style.animationDelay = duration + "s";

        scene.appendChild(star);
        i++
    }
    
}

