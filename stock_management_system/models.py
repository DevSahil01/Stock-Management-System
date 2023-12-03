from django.db import models
from django.contrib.auth import get_user_model





User=get_user_model()

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Supplier(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class Items(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='productImages')
    category = models.CharField(max_length=100, blank=True, null=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.IntegerField(blank=True, null=True)
    cost_price = models.IntegerField(blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Paid(models.Model):
    purchase = models.ForeignKey('Purchase', models.DO_NOTHING, blank=True, null=True)
    paid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paid'


class Purchase(models.Model):
    bill_no = models.IntegerField(blank=True, null=True)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase'


class Received(models.Model):
    sales = models.ForeignKey('Sales', models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey('ServiceSales', models.DO_NOTHING, blank=True, null=True)
    received = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'received'


class Sales(models.Model):
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'


class Service(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    material = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceSales(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    service = models.ForeignKey(Service, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_sales'


class Stock(models.Model):
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'