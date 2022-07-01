console.log("Hello");
let header = document.querySelector('header');

document.addEventListener('scroll',()=>{
    let scrollTop = window.scrollY;
    if(scrollTop >50 ){
        header.style.backgroundColor = '#daffb3'; 
    }else{
        header.style.backgroundColor = 'transparent'
    }


})