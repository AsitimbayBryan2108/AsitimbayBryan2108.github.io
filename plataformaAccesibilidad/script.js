// script.js

document.addEventListener('DOMContentLoaded', () => {
    const contrasteButton = document.getElementById('modo-contraste');
    const aumentarTextoButton = document.getElementById('aumentar-texto');
    const disminuirTextoButton = document.getElementById('disminuir-texto');
    const selectorIdioma = document.getElementById('selector-idioma');
    const contenidoDinamico = document.getElementById('contenido-dinamico');

    // Modo Alto Contraste
    contrasteButton.addEventListener('click', () => {
        document.body.classList.toggle('alto-contraste');
    });

    // Cambiar tamaño de texto
    aumentarTextoButton.addEventListener('click', () => {
        document.body.style.fontSize = '120%';
    });

    disminuirTextoButton.addEventListener('click', () => {
        document.body.style.fontSize = '100%';
    });

    // Traducción dinámica
    selectorIdioma.addEventListener('change', (e) => {
        const idioma = e.target.value;

        // Hacer una solicitud fetch al archivo lang.json
        fetch('lang.json')
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Error al cargar el archivo lang.json');
                }
                return response.json();
            })
            .then((data) => {
                const traducciones = data[idioma];
                if (traducciones) {
                    // Cambiar los textos de la página con las traducciones
                    contenidoDinamico.querySelector('h2').textContent = traducciones.titulo;
                    contenidoDinamico.querySelector('p').textContent = traducciones.mensaje;
                } else {
                    console.error('Traducción no encontrada para el idioma seleccionado');
                }
            })
            .catch((error) => {
                console.error('Error al cargar el archivo JSON:', error);
            });
    });
});
