let card_description = document.querySelectorAll('.product_descr')
let card_name = document.querySelectorAll('.product_name')
let images = document.querySelectorAll('img')

card_description.forEach(text => {
  let max_length = 0
  if (window.innerWidth < 320) {
    card_description.remove;
  }
  if (window.innerWidth < 550) {
    max_length = 10
  }
  else if (window.innerWidth < 600) {
    max_length = 20
  }
  else if (window.innerWidth < 1000) {
    max_length = 25
  }
  else if (window.innerWidth < 1200) {
    max_length = 50
  }
  else if (window.innerWidth < 1400) {
    max_length = 80
  }
  else if (window.innerWidth < 1800) {
    max_length = 90
  }
  else if (window.innerWidth > 1800) {
    max_length = 115
  }
  
  if (text.innerHTML.trim().length > max_length) {
    let cutten_text = text.innerHTML.trim().slice(0,[max_length]);
    text.innerHTML = cutten_text + '...';
  }
});

//control lenght name of product in catalog
card_name.forEach(text => {
  let max_length = 0
  if (window.innerWidth < 550) {
    max_length = 10
  }
  else if (window.innerWidth < 600) {
    max_length = 10
  }
  else if (window.innerWidth < 1000) {
    max_length = 11
  }
  else if (window.innerWidth < 1000) {
    max_length = 12
  }
  else if (window.innerWidth < 1200) {
    max_length = 14
  }
  else if (window.innerWidth < 1400) {
    max_length = 18
  }
  else if (window.innerWidth < 1800) {
    max_length = 20
  }
  else if (window.innerWidth > 1800) {
    max_length = 25
  }
  
  console.log(max_length, text.innerHTML.length, text.innerHTML)
  if (text.innerHTML.trim().length > max_length) {
    let cutten_text = text.innerHTML.trim().slice(0,[max_length]);
    text.innerHTML = cutten_text.trim() + '...';
  }
});
