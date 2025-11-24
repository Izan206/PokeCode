function typeWriter(elementId, velocity = 30) {
  const el = document.getElementById(elementId);
  const mensaje = el.getAttribute("data-text");
  let index = 0;

  function write() {
    if (index < mensaje.length) {
      el.innerHTML += mensaje[index];
      index++;
      setTimeout(write, velocity);
    }
  }

  write();
}

typeWriter("text");
