

const nextPage = (e, number) => {
  let currentPage = document.getElementById('form-sec' + number);
  let nextPage = document.getElementById('form-sec' + (number + 1));
  if (!nextPage) {
    console.log('No more pages!')
  };
  console.log('This is page ' + number)
  currentPage.style.display = 'none';
  nextPage.style.display = 'block';
  e = e || window.Event;
  e.preventDefault();
}

const previousPage = (e, number) => {
  let currentPage = document.getElementById('form-sec' + number);
  let previousPage = document.getElementById('form-sec' + (number - 1));
  if (!previousPage) {
    console.log('There is no more!')
  };
  currentPage.style.display = 'none';
  previousPage.style.display = 'block';
  e = e || window.Event;
  e.preventDefault();
}