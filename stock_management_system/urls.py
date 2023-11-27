from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from . import views

urlpatterns = [
    path("/", views.adminLogin, name="index"),
    path('/masterlogin',views.masterLogin,name="masterLogin"),
    path('/masterpanel',views.customerSection,name='masterpanel'),
    path('/supplier',views.supplierSection,name='supplier'),
    path('/products',views.productsPage,name='products'),
    path('/addproduct',views.addProduct,name='addproduct'),
    path('/purchase',views.purchaseSection,name='purchase'),
    path('/salespage',views.salesSection,name='salespage'),
    path('/service',views.serviceSection,name='service'),
    path('/serviceSales',views.serviceSales,name='serviceSales'),
    path('/alerts',views.alertsSection,name='alerts'),
    path('/mlogout',views.masterLogout,name='mlogout'),
    path('/logout',views.logout,name='logout')
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

