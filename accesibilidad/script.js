// script.js
document.addEventListener('DOMContentLoaded', () => {
    const btnContraste = document.getElementById('modo-contraste');
    const btnAumentarTexto = document.getElementById('aumentar-texto');
    const btnCambiarIdioma = document.getElementById('cambiar-idioma');

    // Alternar modo de alto contraste
    btnContraste.addEventListener('click', () => {
        document.body.classList.toggle('alto-contraste');
    });

    // Alternar aumento de tamaño de texto
    btnAumentarTexto.addEventListener('click', () => {
        document.body.classList.toggle('texto-grande');
    });

    // Cambiar entre español e inglés
    btnCambiarIdioma.addEventListener('click', () => {
        const esEspanol = document.documentElement.lang === 'es';

        // Cambiar texto según el idioma
        document.documentElement.lang = esEspanol ? 'en' : 'es';

        document.getElementById('titulo').textContent = esEspanol
            ? 'Welcome to the Accessible Site'
            : 'Bienvenidos al Sitio Accesible';
        document.getElementById('link-inicio').textContent = esEspanol ? 'Home' : 'Inicio';
        document.getElementById('link-acerca').textContent = esEspanol ? 'About' : 'Acerca';
        document.getElementById('link-contacto').textContent = esEspanol ? 'Contact' : 'Contacto';
        document.getElementById('contenido-principal').textContent = esEspanol
            ? 'Main Content'
            : 'Contenido Principal';
        document.getElementById('descripcion').textContent = esEspanol
            ? 'This page is designed to be accessible to all users.'
            : 'Esta página está diseñada para ser accesible a todos los usuarios.';
        document.getElementById('texto-contacto').textContent = esEspanol
            ? 'Contact: '
            : 'Contacto: ';
        document.getElementById('correo').textContent = 'soporte@accesible.com';
        btnCambiarIdioma.textContent = esEspanol ? 'Switch to Spanish' : 'Cambiar a Inglés';
    });
});
