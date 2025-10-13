const mensaje =
  "Welcome to PokeCode! We hope you enjoy battling your favorite Pokémon one-on-one. Get ready to fight, now!";
let index = 0;
const velocity = 30; // milliseconds between each letter

function write() {
  if (index < mensaje.length) {
    document.getElementById("text").innerHTML += mensaje[index];
    index++;
    setTimeout(write, velocity);
  }
}
write();
