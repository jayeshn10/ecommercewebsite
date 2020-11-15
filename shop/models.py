from datetime import date
from decimal import Decimal

from django.db import models


# Create your models here.


class Shopproduct(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_img = models.ImageField(upload_to="productimg")
    product_desc = models.TextField()
    product_pdate = models.DateField()

    def __str__(self):
        return self.product_name


class contactdata(models.Model):
    fname = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=50, default="")
    phone = models.BigIntegerField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.email


class gallery(models.Model):
    img_name = models.CharField(max_length=30)
    img_title = models.CharField(max_length=40, default="")
    img_disc = models.TextField(max_length=500, default="")
    img_src = models.ImageField(upload_to='gallerypics')
    img_src_max = models.ImageField(upload_to='gallerypics/gallerypicsmax', default="")

    def __str__(self):
        return self.img_name


class blogmod(models.Model):
    blog_title = models.CharField(max_length=40)
    blog_img = models.ImageField(upload_to='blogimage')
    blog_img_max = models.ImageField(upload_to='blogimage/blogmaximg', default="")
    blog_disc = models.TextField(max_length=1000)
    blog_disc_max = models.TextField(max_length=2000, default="")

    def __str__(self):
        return self.blog_title


class order(models.Model):
    cust_name = models.CharField(max_length=50)
    cust_email = models.EmailField()
    cust_phone = models.BigIntegerField()
    cust_address = models.CharField(max_length=500)
    cust_city = models.CharField(max_length=200)
    cust_state = models.CharField(max_length=200)
    cust_zip_code = models.BigIntegerField()
    order_payment_type = models.CharField(max_length=50)
    order_payment_status = models.CharField(max_length=200)
    order_status = models.CharField(max_length=200)
    order_item_num = models.IntegerField()
    order_grand_total = models.FloatField()

    def __str__(self):
        return str(self.id)


class orderiteminfo(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    order_item_name = models.CharField(max_length=50)
    order_item_qty = models.IntegerField()
    order_item_price = models.FloatField()
    order_item_total_price = models.FloatField()

    def __str__(self):
        return str(self.id)



