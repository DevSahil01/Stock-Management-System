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