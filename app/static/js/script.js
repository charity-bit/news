const iconify = document.querySelector('.iconify')
const navLinks = document.querySelector('#navlinks')

iconify.addEventListener('click',()=>{
    
    navLinks.classList.toggle('show-links')
})