

// Manejo de generación de pelotas y opciones
document.getElementById('generate-btn-5').addEventListener('click', () => generateBalls(5));


function generateBalls(maxBalls) {
  const circleContainer = document.getElementById('circle-container');
  const optionsContainer = document.getElementById('options-container');
  const feedback = document.getElementById('feedback');

  // Limpia el contenido previo
  circleContainer.innerHTML = '';
  optionsContainer.innerHTML = '';
  feedback.textContent = '';

  // Genera un número aleatorio de pelotas
  const numBalls = Math.floor(Math.random() * maxBalls) + 1;

  // Crea las pelotas y las posiciona aleatoriamente dentro del círculo
  for (let i = 0; i < numBalls; i++) {
    const ball = document.createElement('div');
    ball.className = 'ball';

    // Posición aleatoria dentro del círculo
    const angle = Math.random() * 2 * Math.PI;
    const radius = Math.random() * 40 + 20; // Ajustar para que no salgan fuera del círculo
    const x = 50 + radius * Math.cos(angle); // Posición X como porcentaje
    const y = 50 + radius * Math.sin(angle); // Posición Y como porcentaje

    ball.style.position = 'absolute';
    ball.style.left = `calc(${x}% - 25px)`; // Ajuste para centrar (50px es el tamaño del balón)
    ball.style.top = `calc(${y}% - 25px)`;

    circleContainer.appendChild(ball);
  }

  // Genera opciones de respuesta
  const options = new Set();
  options.add(numBalls);

  while (options.size < 4) {
    options.add(Math.floor(Math.random() * maxBalls) + 1);
  }

  // Ordena y muestra las opciones
  Array.from(options).sort(() => Math.random() - 0.5).forEach(option => {
    const button = document.createElement('button');
    button.textContent = option;
    button.className = 'btn btn-outline-primary option-btn';
    button.addEventListener('click', () => {
      if (option === numBalls) {
        feedback.textContent = '¡Correcto!';
        feedback.style.color = 'green';
        setTimeout(() => generateBalls(maxBalls), 2000); // Genera nuevas pelotas después de 2 segundos
      } else {
        feedback.textContent = 'Intenta de nuevo.';
        feedback.style.color = 'red';
      }
    });
    optionsContainer.appendChild(button);
  });
}

