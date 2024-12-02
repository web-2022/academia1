
// Eslogan

const typingContainer = document.querySelector('.typing-container');
const typingAnimationDuration = 5000; // Duración de la animación de escritura
const pauseDuration = 3000; // Pausa antes de reiniciar la animación

function startTypingAnimation() {
  typingContainer.style.borderRight = '3px solid #007bff'; // Resetea el cursor
  typingContainer.style.width = '0'; // Reinicia el ancho
  typingContainer.style.animation = 'none'; // Detiene la animación

  // Espera un momento para aplicar la animación de escritura de nuevo
  setTimeout(() => {
    typingContainer.style.animation = `typing ${typingAnimationDuration}ms steps(40, end) forwards, blink-cursor 0.7s steps(1) ${typingAnimationDuration}ms forwards`;
    
    // Espera a que termine la animación y luego oculta el cursor
    setTimeout(() => {
      typingContainer.style.borderRight = 'none'; // Elimina el borde del cursor al final
    }, typingAnimationDuration);
  }, 100); // Pequeño retraso para permitir que se aplique la propiedad "none"
}

// Inicia la primera animación
startTypingAnimation();

// Configura el intervalo para repetir la animación
setInterval(() => {
  startTypingAnimation();
}, typingAnimationDuration + pauseDuration); // Espera que termine la animación más la pausa

//Fin de slogan