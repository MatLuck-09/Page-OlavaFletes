const navToggleBtn = document.querySelector('.nav__toggle__btn');
const navItems = document.querySelector('.nav__items');

navToggleBtn.addEventListener('click', ()=> {
    navItems.classList.toggle('nav__items--hidden');
});