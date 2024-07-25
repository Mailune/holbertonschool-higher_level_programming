document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    const characterDiv = document.getElementById('character');
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        characterDiv.textContent = data.name;
      })
      .catch(error => console.error('Error:', error));
  });
  