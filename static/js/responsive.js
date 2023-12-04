function responsive(x){
     if(x.matches){
        document.getElementsByClassName('login-bx')[0].classList.replace('w-25','w-100')
     }
     else{
        document.getElementsByClassName('login-bx')[0].classList.replace('w-100','w-25')
     }
}
var x=window.matchMedia('(max-width:600px)')

responsive(x)

x.addEventListener("change", function() {
    responsive(x);
  });