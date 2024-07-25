document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const listMovies = document.getElementById('list_movies');
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        const films = data.results;
        films.forEach(film => {
          const listItem = document.createElement('li');
          listItem.textContent = film.title;
          listMovies.appendChild(listItem);
        });
      })
      .catch(error => console.error('Error:', error));
  });
  