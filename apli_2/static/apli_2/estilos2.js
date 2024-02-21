// ======================================= RELOJ ==========================================
var myVar = setInterval(myTimer, 1000);

    function myTimer() {
        
        var d = new Date();
        var t = d.toLocaleTimeString();
        
        reloj=document.getElementById("reloj");
        reloj.innerHTML="&#x2bcc; La Plata || hora: "+ t + "|| fecha: "+ d.getDate()+" / "+ [d.getMonth()+1] +" / "+ d.getFullYear()+"&#x2bcc";
        
        
    }

addEventListener("DOMContentLoaded", inicio, false);
function inicio() {
    document.getElementsByClassName("div_1_seccion")[0].addEventListener("mouseover",modi1,false);
    document.getElementsByClassName("div_1_seccion")[0].addEventListener("mouseout",modi2,false);
    document.getElementsByClassName("div_1_seccion")[1].addEventListener("mouseover",modi3,false);
    document.getElementsByClassName("div_1_seccion")[1].addEventListener("mouseout",modi4,false);

    document.getElementsByClassName("div_2_seccion")[0].addEventListener("mouseover",modi5,false);
    document.getElementsByClassName("div_2_seccion")[0].addEventListener("mouseout",modi6,false);
    document.getElementsByClassName("div_2_seccion")[1].addEventListener("mouseover",modi7,false);
    document.getElementsByClassName("div_2_seccion")[1].addEventListener("mouseout",modi8,false);
}
function modi1() {
    div_1 = document.getElementsByClassName("div_1_seccion")[0];
    div_2 = document.getElementsByClassName("div_1_seccion")[1];
    div_3 = document.getElementsByClassName("div_2_seccion")[0];
    div_4 = document.getElementsByClassName("div_2_seccion")[1];

    div_1.style.boxShadow = "violet 0px 0px 25px";
    div_1.style.transition = "1s ease";
    
    div_2.style.width = "300px";
    div_2.style.height = "200px";
    div_2.style.opacity = "0.5";
    div_2.style.transition = "1s ease";

    div_3.style.width = "300px";
    div_3.style.height = "200px";
    div_3.style.opacity = "0.5";
    div_3.style.marginLeft = "19%";
    div_3.style.transition = "1s ease";

    div_4.style.width = "300px";
    div_4.style.height = "200px";
    div_4.style.opacity = "0.5";
    div_4.style.marginLeft = "15%";
    div_4.style.transition = "1s ease";
}
function modi2() {
    div_1 = document.getElementsByClassName("div_1_seccion")[0];
    div_2 = document.getElementsByClassName("div_1_seccion")[1];
    div_3 = document.getElementsByClassName("div_2_seccion")[0];
    div_4 = document.getElementsByClassName("div_2_seccion")[1];

    div_1.style.boxShadow = "none";
    div_1.style.transition = "1s ease";
    
    div_2.style.width = "350px";
    div_2.style.height = "250px";
    div_2.style.opacity = "1";
    div_2.style.transition = "1s ease";

    div_3.style.width = "350px";
    div_3.style.height = "250px";
    div_3.style.opacity = "1";
    div_3.style.marginLeft = "15%";
    div_3.style.transition = "1s ease";

    div_4.style.width = "350px";
    div_4.style.height = "250px";
    div_4.style.opacity = "1";
    div_4.style.marginLeft = "15%";
    div_4.style.transition = "1s ease";
}
function modi3() {
    div_1 = document.getElementsByClassName("div_1_seccion")[0];
    div_2 = document.getElementsByClassName("div_1_seccion")[1];
    div_3 = document.getElementsByClassName("div_2_seccion")[0];
    div_4 = document.getElementsByClassName("div_2_seccion")[1];

    div_2.style.boxShadow = "violet 0px 0px 25px";

    div_1.style.width = "300px";
    div_1.style.height = "200px";
    div_1.style.opacity = "0.5";
    div_1.style.marginLeft = "19%";
    div_1.style.transition = "1s ease";

    div_3.style.width = "300px";
    div_3.style.height = "200px";
    div_3.style.opacity = "0.5";
    div_3.style.marginLeft = "19%";
    div_3.style.transition = "1s ease";

    div_4.style.width = "300px";
    div_4.style.height = "200px";
    div_4.style.opacity = "0.5";
    div_4.style.marginLeft = "15%";
    div_4.style.transition = "1s ease";
}
function modi4() {
    div_1 = document.getElementsByClassName("div_1_seccion")[0];
    div_2 = document.getElementsByClassName("div_1_seccion")[1];
    div_3 = document.getElementsByClassName("div_2_seccion")[0];
    div_4 = document.getElementsByClassName("div_2_seccion")[1];

    div_1.style.marginLeft = "15%";
    div_1.style.width = "350px";
    div_1.style.height = "250px";
    div_1.style.opacity = "1";
    div_1.style.transition = "1s ease";

    div_2.style.boxShadow = "none";
    div_2.style.transition = "1s ease";

    div_3.style.width = "350px";
    div_3.style.height = "250px";
    div_3.style.opacity = "1";
    div_3.style.marginLeft = "15%";
    div_3.style.transition = "1s ease";

    div_4.style.width = "350px";
    div_4.style.height = "250px";
    div_4.style.opacity = "1";
    div_4.style.marginLeft = "15%";
    div_4.style.transition = "1s ease";
}
function modi5() {
    div_1 = document.getElementsByClassName("div_1_seccion")[0];
    div_2 = document.getElementsByClassName("div_1_seccion")[1];
    div_3 = document.getElementsByClassName("div_2_seccion")[0];
    div_4 = document.getElementsByClassName("div_2_seccion")[1];

    div_1.style.width = "300px";
    div_1.style.height = "200px";
    div_1.style.opacity = "0.5";
    div_1.style.marginLeft = "19%";
    div_1.style.transition = "1s ease";

    div_2.style.width = "300px";
    div_2.style.height = "200px";
    div_2.style.opacity = "0.5";
    div_2.style.transition = "1s ease";

    div_3.style.boxShadow = "violet 0px 0px 25px";
    div_3.style.transition = "1s ease";

    div_4.style.width = "300px";
    div_4.style.height = "200px";
    div_4.style.opacity = "0.5";
    div_4.style.transition = "1s ease";
   
}
function modi6() {
    div_1 = document.getElementsByClassName("div_1_seccion")[0];
    div_2 = document.getElementsByClassName("div_1_seccion")[1];
    div_3 = document.getElementsByClassName("div_2_seccion")[0];
    div_4 = document.getElementsByClassName("div_2_seccion")[1];

    div_1.style.width = "350px";
    div_1.style.height = "250px";
    div_1.style.opacity = "1";
    div_1.style.marginLeft = "15%";
    div_1.style.transition = "1s ease";

    div_2.style.width = "350px";
    div_2.style.height = "250px";
    div_2.style.opacity = "1";
    div_2.style.marginLeft = "15%";
    div_2.style.transition = "1s ease";

    div_3.style.boxShadow = "none";

    div_4.style.width = "350px";
    div_4.style.height = "250px";
    div_4.style.opacity = "1";
    div_4.style.transition = "1s ease";
}
function modi7() {
    div_1 = document.getElementsByClassName("div_1_seccion")[0];
    div_2 = document.getElementsByClassName("div_1_seccion")[1];
    div_3 = document.getElementsByClassName("div_2_seccion")[0];
    div_4 = document.getElementsByClassName("div_2_seccion")[1];

    div_1.style.width = "300px";
    div_1.style.height = "200px";
    div_1.style.opacity = "0.5";
    div_1.style.marginLeft = "19%";
    div_1.style.transition = "1s ease";

    div_2.style.width = "300px";
    div_2.style.height = "200px";
    div_2.style.opacity = "0.5";
    div_2.style.transition = "1s ease";

    div_3.style.width = "300px";
    div_3.style.height = "200px";
    div_3.style.opacity = "0.5";
    div_3.style.marginLeft = "19%";
    div_3.style.transition = "1s ease";

    div_4.style.boxShadow = "violet 0px 0px 25px";
    div_4.style.transition = "1s ease";
}
function modi8() {
    div_1 = document.getElementsByClassName("div_1_seccion")[0];
    div_2 = document.getElementsByClassName("div_1_seccion")[1];
    div_3 = document.getElementsByClassName("div_2_seccion")[0];
    div_4 = document.getElementsByClassName("div_2_seccion")[1];
    
    div_1.style.width = "350px";
    div_1.style.height = "250px";
    div_1.style.opacity = "1";
    div_1.style.marginLeft = "15%";
    div_1.style.transition = "1s ease";

    div_2.style.width = "350px";
    div_2.style.height = "250px";
    div_2.style.opacity = "1";
    div_2.style.transition = "1s ease";

    div_3.style.width = "350px";
    div_3.style.height = "250px";
    div_3.style.opacity = "1";
    div_3.style.marginLeft = "15%";
    div_3.style.transition = "1s ease";

    div_4.style.boxShadow = "none";
    div_4.style.transition = "1s ease";
}
// =============================================================================================================================

