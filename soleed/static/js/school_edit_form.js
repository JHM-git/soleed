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

const toggleElement = (e, target, cclass, target2, txt1, txt2) => {
  document.getElementById(target).classList.toggle(cclass);
  buttonChanger(target2, txt1, txt2);
  e = e || window.Event;
  e.preventDefault(); 
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
  let input = document.getElementById(source).textContent;
  let re = /[\]\[]/;
  if(input.search(re) === -1) {
    checkButton(input);
  } else  {
    let inputlst = input.replace(/[\'\,\[\]]/g, '').split(' ');
    for(let i=0; i < inputlst.length; i++) {
      checkButton(inputlst[i]);
    }
  }
}

const checkButton = (id) => {
  const item = document.getElementById(id)
  item.checked = true;
}

const multipleRadioToggler = (e, lst1, lst2, cclass) => {
  for(let i=0; i < lst1.length; i++) {
    if(document.getElementById(lst1[i]).checked && document.getElementById(lst2[i]).classList.contains(cclass)===false) {
      simplyToggleElement(e, lst2[i], cclass);
    } else if(document.getElementById(lst2[i]).classList.contains(cclass) && document.getElementById(lst1[i]).checked===false) {
      simplyToggleElement(e, lst2[i], cclass);
    }
  }
}

const noDefault = (e) => {
  e = e || window.Event;
  e.preventDefault();
}

window.addEventListener('load', radioChecker('school-religious'))
window.addEventListener('load', radioChecker('edu-offer-lst'))
