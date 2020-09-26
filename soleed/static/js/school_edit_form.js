const nextPage = (e, number) => {
  let currentPage = document.getElementById('form-sec' + number);
  let nextPage = document.getElementById('form-sec' + (number + 1));
  if (!nextPage) {
    console.log('No more pages!')
  };
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

const toggleElement = (target, cclass, target2, txt1, txt2) => {
  document.getElementById(target).classList.toggle(cclass);
  buttonChanger(target2, txt1, txt2);
}

const buttonChanger = (target, txt1, txt2) => {
  let text = document.getElementById(target).textContent;
  if(text === txt1) {
    text = txt2;
    document.getElementById(target).textContent = text;
  } else {
    text = txt1;
    document.getElementById(target).textContent = text;
  }
}

const simplyToggleElement = (e, target, cclass) => {
  document.getElementById(target).classList.toggle(cclass);
  e = e || window.Event;
  e.preventDefault(); 
}

const changeCSSClass = (target, cclass) => {
  document.getElementById(target).className = cclass;
}

const testFunction = () => {
  console.log('Working!');
}

const radioToggler = (id, id2, target, cclass, cclass2) => {
  if(document.getElementById(id).checked) {
    changeCSSClass(target, cclass);
  } else if(document.getElementById(id2).checked) {
    changeCSSClass(target, cclass2);
  }
}

const radioChecker = (source) => {
  if(typeof(source) === 'string') {
    let value = document.getElementById(source).textContent;
    checkButton(value);
  }
}

const checkButton = (id) => {
  const item = document.getElementById(id)
  item.checked = true;
}

window.addEventListener('load', radioChecker('school-religious'))
