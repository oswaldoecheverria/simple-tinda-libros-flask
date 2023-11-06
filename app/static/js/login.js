(function () {
    const body = document.querySelector('body');
    body.classList.add('text-center')
}) ();

/*
Se va a agregar la clase textcenter para que 
centre todo el texto a todo el cuerpo del 
documento, especificamente a la etiqueta body 

1. Agregamos en una contante el cuerpo 
const body = document.querySelector('body');

2. Diremos que le agregamos a la listas de la
clase en body text-center
body.classList.add('text-center')

3. Necesitamos que esto se ejecute cuando 
el documento sea cargado.
La funcion que vamos a ejecutar es igual 
al jquery.ready que cuando el documento esta listo 
realizara una serie de acciones  

(function () {
    const body = document.querySelector('body');
    body.classList.add('text-center')
}) ();

*/