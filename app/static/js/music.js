const muteBtn = document.getElementById("muteBtn");
const audio = document.getElementById("backgroundMusic");

// Set audio source and properties
if (musicSrc && musicSrc.trim() !== "") {
  audio.src = musicSrc;
  audio.volume = 0.1;
  audio.muted = true; // Start muted by default
  audio.loop = true; // Enable loop

  // Try to play (browsers may require user interaction first)
  audio.play().catch((error) => {
    console.log("Audio playback delayed (user interaction required):", error);
  });
}

// Toggle mute button
muteBtn.addEventListener("click", () => {
  if (audio.muted) {
    audio.muted = false;
    muteBtn.textContent = "🔊";
    audio.play().catch((error) => {
      console.log("Error playing audio:", error);
    });
  } else {
    audio.muted = true;
    muteBtn.textContent = "🔇";
  }
});
