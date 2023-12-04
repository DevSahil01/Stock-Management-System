function checkMobileNo(){
    mobField=document.getElementById('mob')
    if(mobField){

        mobField.addEventListener('keyup',(e)=>{
            if(e.target.value.length>10){
                document.getElementById('mob_warning').innerText='Mobile no should not be greater than 10 Digits'
                // mobField.setAttribute('readOnly',true)
            }
            else{
                document.getElementById('mob_warning').innerText=''
            }
        })
    }
}
checkMobileNo()




function showAlert(){
    let msg=document.getElementById('alert-msg')
    let alert=document.getElementById('alert')
    if(msg.innerText.trim()!==''){
        alert.classList.replace('d-none','d-block')
        setTimeout(() => {
            msg.innerText=""
            alert.classList.replace('d-block','d-none')
        }, 4000);
    }
    else{
        alert.classList.replace('d-block','d-none')
    }

}
showAlert()