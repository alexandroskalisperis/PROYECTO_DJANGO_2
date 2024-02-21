
// RELOJ ================ 
var myVar = setInterval(myTimer, 1000);

    function myTimer() {
        
        var d = new Date();
        var t = d.toLocaleTimeString();
        
        reloj=document.getElementById("reloj");
        reloj.innerHTML="&#x2bcc; La Plata || hora: "+ t + "|| fecha: "+ d.getDate()+" / "+ [d.getMonth()+1] +" / "+ d.getFullYear()+"&#x2bcc";
        
        
    }
