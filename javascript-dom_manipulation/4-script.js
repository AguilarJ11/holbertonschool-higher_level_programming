const add = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

add.addEventListener('click', () => {
  item = document.createElement('li');
  item.textContent = 'Item';
  list.appendChild(item);
});
