document.addEventListener("DOMContentLoaded", () => {
  const hello_elem = document.querySelector("#hello");

  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => response.json())
    .then((data) => {
        hello_elem.textContent = data.hello;
    })
});
