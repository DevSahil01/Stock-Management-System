from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.conf import settings
from .models import Customer
from .models import Supplier
from .models import Items
from .models import Purchase
from .models import Service
from django.db import connection
from .forms import productForm
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse

#Main admin panel login
def adminLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        branch=request.POST['branch']
        print(username,password)
        
        # user=User.objects.create_user(username=username,password=password,is_staff=True)
        # user.save()
        # redirect('index')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('purchase')
        else:
           return render(request,'login.html',{'message':"Invalid username or password"})
            
    else:
        return render(request,'login.html',{'message':''})

@login_required(login_url='index')
def masterLogin(request):
    masterCredentials={
        "Andheri(E)":{
            "username":"sahil",
            "password":"1234",
        }
        ,
        "Andheri(W)":{
            "username":"vivek",
            "password":"4567"
        }
    }
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        branch=request.POST['branch']
        try:
            if masterCredentials[branch]["username"]==username and masterCredentials[branch]['password']==password:
                return redirect('masterpanel')
            else:
                return render(request,'MasterpageLogin.html',{'message':'invalid credentials'})
        except:
                return render(request,'MasterpageLogin.html',{'message':'Select Branch'})

    else:
        return render(request,'MasterpageLogin.html',{'message':''})

@login_required(login_url='index')   
def customerSection(request):
    custData=Customer.objects.all()
    if request.method=="POST":
        cust_name=request.POST['cust_Name']
        cust_mob=request.POST['cust_mob']
        cust_add=request.POST['cust_add']
        alreadyExists=False
        for cust in custData:
            if(cust.name==cust_name):
                alreadyExists=True

        if alreadyExists==False:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO customer(name,mobile,address) VALUES (%s,%s,%s)",[cust_name,cust_mob,cust_add])
                return redirect('masterpanel')
            except:
                return render(request,'customer.html',{'message':"Server Error",'customerData':custData})
        else:
                return render(request,'customer.html',{'message':"Customer Already Exists",
                                                       'customerData':custData})

    else:
        return render(request,'customer.html',{'customerData':custData})

@login_required(login_url='index')
def supplierSection(request):
    splrData=Supplier.objects.all()
    if request.method=="POST":
        splr_name=request.POST['splr_name']
        splr_mobile=request.POST['splr_mobile']
        splr_add=request.POST['splr_add']
        alredyExists=False
        
        for supplier in splrData:
            if(supplier.name==splr_name or supplier.mobile==splr_mobile):
                alredyExists=True

        if alredyExists==False:
            try:
                with connection.cursor() as cur:
                    cur.execute("INSERT INTO supplier (name,mobile,address) VALUES (%s,%s,%s) ",[splr_name,splr_mobile,splr_add])
                    return redirect('supplier')
            except:
                return render(request,'supplier.html',{'message':"Server Error !"})
        else:
            return render(request,'supplier.html',{'message':'Supplier Already Exists',
                                                   'supplierData':splrData})
        

    else:
        
        return render(request,'supplier.html',{'supplierData':splrData})

@login_required(login_url='index')   
def productsPage(request):
        PN=1#page no

        try:
            PN=request.GET['p']
        except:
            PN=1
        EC=10*int(PN)#End count
        IC=EC-9#initial count
        itemData=Items.objects.all()
        print(settings.MEDIA_URL)
        return render(request,'product.html',{'itemData':itemData[IC-1:EC-1],'media_url':settings.MEDIA_URL,'datalength':len(itemData)})

@login_required(login_url='index')
def addProduct(request):
    if request.method=="POST":
        form =productForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')

    else:
        return render(request,'addproduct.html')
    
@login_required(login_url='index')
def purchaseSection(request):
    if request.method=="POST":
        date=request.POST['date']
        pay_method=request.POST['pay_method']
        billno=request.POST['bill_no']
        party_name=request.POST['party_name']
        p_name=request.POST['item_name']
        quantity=request.POST['quantity']
        cost_price=request.POST['cost_price']
        selling_price=request.POST['selling_price']
        amount_paid=request.POST['amount_paid']
        payable_amount=request.POST['payable_amount']
        due_date=request.POST['due_date']
        if pay_method=='cash':
            amount_paid=int(quantity)*int(cost_price)
            payable_amount=0

        with connection.cursor() as cursor:
            cursor.execute('CALL InsertPurchase(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',[party_name,p_name,billno,date,quantity,cost_price,selling_price,amount_paid,payable_amount,due_date])
            return redirect('purchase')

    else:
        filter='all'
        PN=1#page no

        try:
            filter=request.GET['v']
            PN=request.GET['p']
        except:
            filter='all'
            PN=1
        EC=10*int(PN)#End count
        IC=EC-9#initial count
        print(IC,EC,PN)

        suppliers=Supplier.objects.all()
        itemData=Items.objects.all()
        if filter=='all':

            #other ways entries.objects.values(<column_name>)
            #other ways entries.objects.values_list(<column_name>)
            with connection.cursor() as cursor:
                cursor.execute('''SELECT p.bill_no,s.name,p.Date,i.name,p.quantity,p.amount,pd.paid,cd.payable,cd.due_date
                    FROM purchase p
                    JOIN supplier s ON s.id=p.supplier_id
                    JOIN items i on i.id=p.item_id
                    JOIN paid pd on pd.purchase_id=p.id
                    JOIN creditors cd ON cd.purchase_id=p.id ''')
                purchaseData=cursor.fetchall()
                # for p in purchaseData:
                #     print(p)
            return render(request,'purchase.html',{'suppliers':suppliers,'itemdata':list(itemData),'purchasedata':purchaseData[IC-1:EC-1],'datalength':len(purchaseData)})
        else:
            with connection.cursor() as cursor:
                cursor.execute('''SELECT p.bill_no,s.name,p.Date,i.name,p.quantity,p.amount,pd.paid,cd.payable,cd.due_date
                    FROM purchase p
                    JOIN supplier s ON s.id=p.supplier_id
                    JOIN items i on i.id=p.item_id
                    JOIN paid pd on pd.purchase_id=p.id
                    JOIN creditors cd ON cd.purchase_id=p.id ORDER BY cd.payable DESC''')
                purchaseData=cursor.fetchall()
                # for p in purchaseData:
                #     print(p)
            return render(request,'purchase.html',{'suppliers':suppliers,'itemdata':list(itemData),'purchasedata':purchaseData[IC-1:EC-1],'datalength':len(purchaseData)})




# @login_required(login_url='index')
def salesSection(request):
    customers=Customer.objects.all()
    itemData=Items.objects.only('name')
    PN=1#page no
    try:
            PN=request.GET['p']
    except:
            PN=1
    EC=10*int(PN)#End count
    IC=EC-9#initial count
    print(IC,EC,PN)
    if request.method=="POST":
        try:
            startdate=request.POST['start_date']
            endDate=request.POST['end_date']
            with connection.cursor() as cursor:
                cursor.execute('''SELECT s.id,c.name,s.Date,i.name,s.quantity,s.amount,rd.received,db.receivable,db.due_date
                FROM sales s
                JOIN customer c ON c.id=s.customer_id
                JOIN items i on i.id=s.item_id
                JOIN received rd on rd.sales_id=s.id
                JOIN debtors db ON db.sales_id=s.id BETWEEN %s AND %s''',[startdate,endDate])
            salesData=cursor.fetchall()
            return render(request,'sales.html',{'customers':customers,
                                                'itemdata':itemData,
                                                'salesdata':salesData})

        except Exception as e:
            
            date=request.POST['date']
            pay_method=request.POST['pay_method']
            billno=request.POST['bill_no']
            cust_name=request.POST['cust_name']
            p_name=request.POST['item_name']
            quantity=request.POST['quantity']
            selling_price=request.POST['selling_price']
            amt_recieved=request.POST['amt_recieved']
            receivable_amt=request.POST['receivable_amt']
            due_date=request.POST['due_date']


            if pay_method=='cash':
                amt_recieved=int(quantity)*int(selling_price)
                receivable_amt=0
            with connection.cursor() as cursor:
                cursor.execute("CALL InsertSales(%s, %s, %s, %s, %s, %s, %s,%s);",[cust_name,p_name,date,quantity,selling_price,amt_recieved,receivable_amt,due_date])
                return redirect('salespage')
    else:
        
        with connection.cursor() as cursor:
            cursor.execute('''SELECT s.id,c.name,s.Date,i.name,s.quantity,s.amount,rd.received,db.receivable,db.due_date
            FROM sales s
            JOIN customer c ON c.id=s.customer_id
            JOIN items i on i.id=s.item_id
            JOIN received rd on rd.sales_id=s.id
            JOIN debtors db ON db.sales_id=s.id''')
        salesData=cursor.fetchall()
        return render(request,'sales.html',{'customers':customers,
                                            'itemdata':itemData,
                                            'salesdata':salesData[IC-1:EC-1],
                                             'datalength':len(salesData)})

@login_required(login_url='index')
def serviceSection(request):
    serviceData=Service.objects.all()
    if request.method=='POST':
        name=request.POST['service_name']
        category=request.POST['ser_cat']
        subcategory=request.POST['ser_subcat']
        price=request.POST['price']
        alreadyExists=False
        for service in serviceData:
             if service.name==name:
                 alreadyExists=True
        if alreadyExists==False:
            try:
                with connection.cursor() as cur:
                    cur.execute("INSERT INTO service (name, category,subcategory,price,material_id) VALUES (%s, %s, %s,%s,NULL)",[name,category,subcategory,price])
                    return redirect('service')
            except:
                return render(request,'service.html',{'message':'server Error'})
        else:
            return render(request,'service.html',{'message':"Service already Exist",
                                                  'servicedata':serviceData})

    else:
        return render(request,'service.html',{'servicedata':serviceData})


@login_required(login_url='index')
def serviceSales(request):
    if request.method=='POST':
        date=request.POST['date']
        cust_name=request.POST['cust_name']
        ser_name=request.POST['service_name']
        quantity=request.POST['quantity']
        selling_price=request.POST['selling_price']
        amt_recieved=request.POST['amt_recieved']
        receivable_amt=request.POST['receivable_amt']
        due_date=request.POST['due_date']
        with connection.cursor() as cursor:
            cursor.execute("CALL InsertServiceSales(%s, %s, %s, %s, %s, %s, %s,%s);",[cust_name,ser_name,date,quantity,selling_price,amt_recieved,receivable_amt,due_date])
            return redirect('serviceSales')
        
    else:
        customers=Customer.objects.all()
        serviceData=Service.objects.all()
        with connection.cursor() as cursor:
            cursor.execute('''SELECT s.id,c.name,s.Date,svc.name,s.quantity,s.amount,rd.received,db.receivable,db.due_date
FROM service_sales s
JOIN customer c ON c.id=s.customer_id
JOIN service svc on svc.id=s.service_id
JOIN received rd on rd.service_id=s.id
JOIN debtors db ON db.service_id=s.id''')
        serviceSalesData=cursor.fetchall()
        return render(request,'servicesales.html',{'customers':customers,
                                                   'servicedata':serviceData,
                                                    'serviceSalesdata':serviceSalesData})


def alertsSection(request):
    with connection.cursor() as cursor:
       cursor.execute('SELECT i.name, s.name, s.mobile, p.Date, c.payable, c.due_date FROM creditors c JOIN purchase p ON p.id=c.purchase_id JOIN items i ON i.id=p.item_id JOIN supplier s ON s.id=p.supplier_id WHERE DATE(due_date) BETWEEN CURDATE() AND CURDATE() + INTERVAL 3 DAY;')
       creditorAlerts=cursor.fetchall()
       cursor.execute('SELECT i.name, c.name, c.mobile, s.Date, d.receivable, d.due_date FROM debtors d JOIN sales s ON s.id=d.sales_id JOIN items i ON i.id=s.item_id JOIN customer c ON c.id=s.customer_id WHERE DATE(due_date) BETWEEN CURDATE() AND CURDATE() + INTERVAL 3 DAY;')
       debatorAlerts=cursor.fetchall()
       cursor.execute('SELECT svc.name, c.name, c.mobile,  s.Date, d.receivable, d.due_date FROM debtors d JOIN service_sales s ON s.id=d.service_id JOIN service svc ON svc.id=s.service_id JOIN customer c ON c.id=s.customer_id WHERE DATE(due_date) BETWEEN CURDATE() AND CURDATE() + INTERVAL 3 DAY;')
       serviceSalesAlerts=cursor.fetchall()
    return render(request,'alerts.html',{'creditoralerts':creditorAlerts,
                                         'debtoralerts':debatorAlerts,
                                         'servicesalesAlerts':serviceSalesAlerts})

def logout(request):
    auth.logout(request)
    return redirect('index')

def masterLogout(request):
    return redirect('purchase')

