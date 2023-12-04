let sidebar=document.getElementById('sidebar')
let menu=document.getElementById('menu')
let menuIcon='http://127.0.0.1:8000/static/Images/square.png'
let closeIcon='http://127.0.0.1:8000/static/Images/cancel.png'
function collpaseSideBar(){
     if(menu.src===closeIcon){
         menu.src=menuIcon
         sidebar.classList.replace('d-flex','d-none')
     }
     else{
        menu.src=closeIcon
        sidebar.classList.replace('d-none','d-flex')
     }
     
}
function myFunction(x) {
    console.log('apply')
    if (x.matches) { // If media query matches
       if (document.getElementsByClassName('form')[0])document.getElementsByClassName('form')[0].classList.replace('w-50','w-100')
       sidebar.classList.add('position-absolute')
       menu.classList.add('position-absolute')
       if(menu.src=closeIcon){

          collpaseSideBar()
       }
    } else {
        if (document.getElementsByClassName('form')[0])document.getElementsByClassName('form')[0].classList.replace('w-100','w-50')
        sidebar.classList.remove('position-absolute')
      //  menu.classList.remove('position-absolute')
    }
  }
  
  // Create a MediaQueryList object
  var x = window.matchMedia("(max-width: 600px)")
  
  // Call listener function at run time
  myFunction(x);
  
  // Attach listener function on state changes
  x.addEventListener("change", function() {
    myFunction(x);
  });