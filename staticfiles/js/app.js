let deferredPrompt;

window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  deferredPrompt = e;
  const installBtn = document.getElementById("installBtn");
  if (installBtn) {
    installBtn.style.display = "block";
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const installBtn = document.getElementById("installBtn");
  if (installBtn) {
    installBtn.addEventListener("click", async () => {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        console.log(`Install outcome: ${outcome}`);
        deferredPrompt = null;
        installBtn.style.display = "none";
      }
    });
  }
});
