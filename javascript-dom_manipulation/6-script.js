const character_name = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/11/?format=json')
  .then(response => response.json())
  .then(data => character_name.textContent = data.name);