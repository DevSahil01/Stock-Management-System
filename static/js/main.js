const productSubCat={
    'stationary':['pencil','eraser','geometry box','sharpner','pen','notebook'],
    'gifts':['toys','articles','idol'],
    'service':['xerox','project','print'],
    'cosmetics':['neckless','makeup'],
    'general':['dhaga','plastic'],
    'other':['other']
}

const serviceSubCat={
    'print':['xerox','print'],
    'project':['thermocol house','project book']
}

///show alert 

function showAlert(arg_msg,type){
    let msg=document.getElementById('alert-msg')
    let alert=document.getElementById('alert')
    msg.innerText=arg_msg
    if(msg.innerText!==''){
        alert.classList.replace('d-none','d-block')
        if(!alert.classList.contains(`alert-${type}`)){
            alert.classList.replace(alert.classList[1],`alert-${type}`)
        }
        setTimeout(() => {
            msg.innerText=""
            alert.classList.replace('d-block','d-none')
        }, 4000);
    }
    else{
        alert.classList.replace('d-none','d-block')
    }

}




function setSubcatOptions(cat){
    let subcatOption=document.getElementById('subcategory')
    // let p_subcat=[]
    p_subcat=productSubCat[cat]
    subcatOption.innerHTML="<option value=''  selected >Select sub-category</option>"

    for (p of p_subcat ){
        subcatOption.insertAdjacentHTML("beforeEnd",
        `<option value=${p} ><p class='text-primary'>${p}</p></option>
        `)
    } 
}


function getProductCat(){
    let p_cat=document.getElementById('category').options[document.getElementById('category').selectedIndex].value
  
    switch(p_cat){
        case 'stationary':
            setSubcatOptions('stationary');
            break;
        case 'gifts':
            setSubcatOptions('gifts');
            break;
        case 'cosmetics':
            setSubcatOptions('cosmetics');
            break;
        case 'service':
            setSubcatOptions('service');
            break;
        case 'general':
            setSubcatOptions('general');
            break;
        case 'other':
            setSubcatOptions('other');
            break;
                
    }
}

function setSerSubcatOptions(cat){
    let subcatOption=document.getElementById('ser_subcat')
    // let p_subcat=[]
    p_subcat=serviceSubCat[cat]
    subcatOption.innerHTML="<option value='' selected>Select sub-category</option>"

    for (p of p_subcat ){
        subcatOption.insertAdjacentHTML("beforeEnd",
        `<option value=${p}>${p}</option>
        `)
    } 
}

function getServiceCat(){
    let ser_cat=document.getElementById('ser_cat').options[document.getElementById('ser_cat').selectedIndex].value

    switch(ser_cat){
        case 'print':
            setSerSubcatOptions('print')
            break;
        case 'project':
            setSerSubcatOptions('project')
            break;
    }
}

serviceData=document.getElementById("service_name")
serviceDataObj={}
if(serviceData){

    for( service of serviceData.children){
        Object.assign(serviceDataObj,{[service.value]:[service.getAttribute('data-cat'),service.getAttribute('data-subcat')]})
     }

}
function getServiceSubcat(){
    let subcatOpt=document.getElementById('ser_subcat').options[document.getElementById('ser_subcat').selectedIndex].value
    let p_cat=document.getElementById('ser_cat').options[document.getElementById('ser_cat').selectedIndex].value
    
    serviceFilterList=[]
    

    for(service of Object.keys(serviceDataObj)){
        // console.log(itemDataObj[item].includes(subcatOpt))
        if(serviceDataObj[service].includes(subcatOpt) && serviceDataObj[service].includes(p_cat)){
             serviceFilterList.push(service)
            // console.log(item)
        }
    }

    //set items dropdown list
    if(serviceFilterList.length!==0){
        serviceData.innerHTML='<option value="" selected>Select Service</option>'
        for(service of serviceFilterList){
            serviceData.insertAdjacentHTML('beforeend',
            ` <option data-cat="${serviceDataObj[service][0]}" data-subcat="${serviceDataObj[service][1]}"
            value="${service}">${service}</option>`)
        }
    }
    else{
        serviceData.innerHTML='<option value="" selected>select proper category and subcategory</option>'
    }

}








function changeIcon(){
    let dropdown=document.getElementById('dropdown')
    console.log(dropdown.children[1])
}

itemData=document.getElementById("item_name")
itemDataObj={}
if(itemData){

    for( item of itemData.children){
        Object.assign(itemDataObj,{[item.value]:[item.getAttribute('data-cat'),item.getAttribute('data-subcat'),item.getAttribute('data-cp'),item.getAttribute('data-sp')]})
     }
}
console.log(itemDataObj)


function getProductSubcat(){
    let subcatOpt=document.getElementById('subcategory').options[document.getElementById('subcategory').selectedIndex].value
    let p_cat=document.getElementById('category').options[document.getElementById('category').selectedIndex].value
    
    itemFilterList=[]
    
    for(item of Object.keys(itemDataObj)){
        // console.log(itemDataObj[item].includes(subcatOpt))
        if(itemDataObj[item].includes(subcatOpt) && itemDataObj[item].includes(p_cat)){
             itemFilterList.push(item)
            // console.log(item)
        }
    }

    //set items dropdown list
    if(itemFilterList.length!==0){
        itemData.innerHTML='<option value="" selected>Select Item</option>'
        for(item of itemFilterList){
            itemData.insertAdjacentHTML('beforeend',
            ` <option data-cat="${itemDataObj[item][0]}" data-subcat="${itemDataObj[item][1]}"
            data-sp="${itemDataObj[item][3]}" data-cp="${itemDataObj[item][2]}"
            value="${item}" class="options" >${item}</option>`)
        }
    }
    else{
        itemData.innerHTML='<option value="" selected>select proper category and subcategory</option>'
    }

}
function setCPSP(e){
     let item_ID=document.getElementById('item_name').selectedIndex
     let cp=document.getElementsByName('cost_price')[0]
     let sp=document.getElementsByName('selling_price')[0]
     let options=document.getElementsByClassName('options')
     if(cp){
         cp.value=options[item_ID-1].getAttribute('data-cp')
     }
     sp.value=options[item_ID-1].getAttribute('data-sp')
}


function getDate(){
    var today=new Date()
    var day=today.getDate()
    if(parseInt(day)<10){
        day='0'+day
    }
    console.log((today.getMonth()+1)+"-"+today.getFullYear()+"-"+day)
    document.getElementById('date_in').value=today.getFullYear()+"-"+(today.getMonth()+1)+"-"+day
}

function GetPayMethod(){
    let pay_method=document.getElementById('pay_method').options[document.getElementById('pay_method').selectedIndex].value
    let credit_row=document.getElementById('credit_row')
    if(pay_method==='credits'){
         credit_row.classList.remove('d-none')
    }
    else{
        credit_row.classList.add('d-none')
    }
}





function showTotal(){
    let quantity=0
    let priceTag=document.getElementById('price')
    let price=priceTag
    
    document.getElementsByName('quantity')[0].addEventListener('keyup',(e)=>{
        quantity=e.target.value
    })
    
    priceTag.addEventListener('keyup',(e)=>{
            price=e.target.value
        })

   document.onclick=function(){
     document.getElementsByName('total')[0].value=quantity*priceTag.value
   }

   let pay_method=document.getElementById('pay_method').options[document.getElementById('pay_method').selectedIndex].value
   let main_amt=document.getElementById('main_amt')
  
   
    main_amt.addEventListener('keyup',(e)=>{
          let payable_amount=document.getElementsByName('total')[0].value-e.target.value
          
             if(payable_amount>=0){
                 document.getElementById('pay_amt').value=payable_amount;
             }
             else{
                showAlert("The paid amount should not be greater than total",'warning')
                document.getElementById('pay_amt').value=0;
             }
          
    })


}
showTotal()


// function showtableInsight(){
    
// }
// showtableInsight()






window.onload=function(){
    getDate()
}




