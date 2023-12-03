

let Noofpages=Math.ceil(document.getElementById('length').firstElementChild.innerText/10)
function Pagination(){
    let paginationNav=document.getElementById('pur_pagination')
    let salesPagination=document.getElementById('sale_pagination')
    let productPagination=document.getElementById('pr_pagination')

    if (paginationNav)
    for(let i=1;i<=Noofpages;i++){
        paginationNav.innerHTML+=`
        <li class="page-item"><a class="page-link" href="purchase?p=${i}&v=all">${i}</a></li>`
    }
    else if(salesPagination)
    for(let i=1;i<=Noofpages;i++){
        salesPagination.innerHTML+=`
        <li class="page-item"><a class="page-link" href="salespage?p=${i}">${i}</a></li>`
    }
    else if(productPagination){
        for(let i=1;i<=Noofpages;i++){
            productPagination.innerHTML+=`
            <li class="page-item"><a class="page-link" href="products?p=${i}">${i}</a></li>`
        }
    }
}
Pagination()

