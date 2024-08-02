const movies = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    for (const item of data.results) {
      list_item = document.createElement('li');
      list_item.textContent = item.title;
      movies.appendChild(list_item);
    }
  });
