document.addEventListener('DOMContentLoaded', () => {
    const updateHeaderDiv = document.getElementById('update_header');
    const headerElement = document.querySelector('header');
  
    updateHeaderDiv.addEventListener('click', () => {
      headerElement.textContent = 'New Header!!!';
    });
  });
  