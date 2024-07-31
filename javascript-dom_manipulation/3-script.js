const toggle = document.querySelector('#toggle_header');
const header = document.querySelector('header');

toggle.addEventListener("click", () => {
  if (header.classList.contains("green")) {
    header.classList.replace("green", "red");
  } else {
    header.classList.replace("red", "green");
  }
});
