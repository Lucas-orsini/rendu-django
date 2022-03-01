from django.db import models

# Create your models here.
class Product(models.Model):
    productname =models.CharField(max_length=500)
    productprice = models.IntegerField()
    productimage = models.CharField(max_length=100000)
    productdescription = models.CharField(max_length=800)
    productquantity = models.IntegerField()
    