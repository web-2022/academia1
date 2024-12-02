function generateBalls(number) {
  const container = document.getElementById('rectangle-container');
  const feedback = document.getElementById('feedback');
  const audio = document.getElementById('audio-player');
  const containerWidth = container.offsetWidth;
  const containerHeight = container.offsetHeight;
  const ballRadius = 30; // Radio de las esferas (60px / 2)
  const positions = []; // Para almacenar las posiciones de las esferas

  // Limpia el contenedor y el feedback
  container.innerHTML = '';
  feedback.textContent = '';

  // Reproducir audio del número
  // audio.src = `https://example.com/numbers/${number}.mp3`; // Ruta de los audios
  // audio.play();

  // Generar pelotas sin intersección
  for (let i = 0; i < number; i++) {
      let x, y, isOverlapping;

      do {
          isOverlapping = false;

          // Generar coordenadas aleatorias
          x = Math.random() * (containerWidth - 2 * ballRadius);
          y = Math.random() * (containerHeight - 2 * ballRadius);

          // Verificar si las coordenadas se solapan con esferas existentes
          for (const pos of positions) {
              const dx = pos.x - x;
              const dy = pos.y - y;
              const distance = Math.sqrt(dx * dx + dy * dy);
              if (distance < 2 * ballRadius) {
                  isOverlapping = true;
                  break;
              }
          }
      } while (isOverlapping);

      // Guardar la posición de la nueva esfera
      positions.push({ x, y });

      // Crear la esfera
      const ball = document.createElement('div');
      ball.className = 'ball';
      ball.style.left = `${x}px`;
      ball.style.top = `${y}px`;
      container.appendChild(ball);
  }

  // Mostrar retroalimentación
  feedback.textContent = `¡Hay ${number} ${number === 1 ? 'pelota' : 'pelotas'}!`;
}