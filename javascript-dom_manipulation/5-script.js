const update_text = document.querySelector('#update_header');
const header = document.querySelector('header');

update_text.addEventListener('click', () => {
    header.textContent = 'New Header!!!'
})
