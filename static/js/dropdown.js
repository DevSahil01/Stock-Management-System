


let dropdown=document.getElementById('dropdown')
let downangleIcon='M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z'
let upangleIcon="m7.247 4.86-4.796 5.481c-.566.647-.106 1.659.753 1.659h9.592a1 1 0 0 0 .753-1.659l-4.796-5.48a1 1 0 0 0-1.506 0z"
// let svgPath=dropdown.nextElementSibling.children[0].children[0]
// dropdown.addEventListener('click',()=>{
//     console.log(dropdown.nextElementSibling.children[0])
//     if(svgPath.getAttribute('d')===downangleIcon){
//         svgPath.setAttribute('d',upangleIcon)
//     }
//     else{
//         svgPath.setAttribute('d',downangleIcon)
//     }
// })

let optionList=document.getElementById('ulist')


let partyList=[]
for(let party of optionList.children){
    partyList.push(party.innerText)
}


function getSearchOption(name){
    let searchInput=document.getElementById('searchparty').value
    let party=new Set(partyList)
    let Result=party.length

    let listIndex=0
    optionList.innerHTML=''
    for (let p of party){
        let matchStr=p.toLowerCase()
        if(matchStr.match(searchInput.toLowerCase())){
            optionList.insertAdjacentHTML("afterbegin",
            `<li class="list-group-item option rounded-0" onclick="selectOption(event)"  >${p}</li>`)
            Result--;
            listIndex++;
        }
    }
    // console.log(noResult)
    if(Result===party.length){
        optionList.insertAdjacentHTML("afterbegin",
            `<li class="list-group-item rounded-0" >${name} name is not availaibe</li>`)
    }
    if(searchInput===''){
        console.log(partyList)
        optionList.innerHTML=''
        for(p of partyList){
            optionList.insertAdjacentHTML("afterbegin",
            `<li class="list-group-item option rounded-0"  onclick="selectOption(event)">${p}</li>`)
        }
    }
}

function selectOption(e){
    // dropdown.setAttribute('value',e.target.innerText)
    document.getElementById('party_name').value=e.target.innerText
    dropdown.innerText=e.target.innerText
    dropdown.click()
}


function autoSelectOption(e){
       let itemId=document.getElementById('item_ID')
       let cp=document.getElementsByName('cost_price')[0]
       let sp=document.getElementsByName('selling_price')[0]
       let options=document.getElementsByClassName('options')
       
       itemId.addEventListener('keyup',(e)=>{
             let value=parseInt(e.target.value)
             if(e.target.value!==''){
                  options[value-1].setAttribute('selected',true)
                  if(cp){
                      cp.value=options[value-1].getAttribute('data-cp')
                  }
                  sp.value=options[value-1].getAttribute('data-sp')
             }
             else{
                cp.value=''
                sp.value=''
             }
       })
       

}
autoSelectOption()



