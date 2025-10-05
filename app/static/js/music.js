const muteBtn=document.getElementById("muteBtn");
const audio=document.getElementById("backgroundMusic");
audio.src=musicSrc;
audio.volume=0.1;
audio.muted=true;
audio.play();

audio.play().catch(error => {
    console.log("Error al reproducir:", error);
});

muteBtn.addEventListener("click", () => {
    if(audio.muted) {
        audio.muted = false;
        muteBtn.textContent = "🔊";
        audio.play();
    } else {
        audio.muted = true;
        muteBtn.textContent = "🔇";
    }
});