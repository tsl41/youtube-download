const text = "Paste full URL to start download";
const interval = 4000; // Interval between each full text update in milliseconds
const container = document.querySelector('.intro-text');
let currentIndex = 0;

function animateText() {
  if (currentIndex <= text.length) {
    container.textContent = text.substring(0, currentIndex);
    currentIndex++;
    setTimeout(animateText, 100);
  } else {
    currentIndex = 0;
    setTimeout(animateText, interval);
  }
}

animateText();
