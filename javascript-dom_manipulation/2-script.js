const header_red = document.querySelector('#red_header');
const header = document.querySelector('header');

header_red.addEventListener('click', () => {
  header.classList.add('red');
});
