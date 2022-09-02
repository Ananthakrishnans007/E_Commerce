from distutils.command.upload import upload
from itertools import product
from pyexpat import model
from unicodedata import category
from venv import create
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Member(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)  
    phone = models.TextField()



class Category(models.Model):
    Category_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Category_Name


class Product(models.Model):
    Category_Name = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    Product_Name = models.CharField(max_length=150)
    Product_Image = models.ImageField(upload_to='product',null=True)
    Product_Description = models.TextField()
    Product_Price = models.IntegerField()
    Product_Delprice = models.IntegerField()

    def __str__(self):
        return self.Product_Name 


class Zip(models.Model):
    zip_code = models.IntegerField()

    def __str__(self):
        return self.zip_code


    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    product =  models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name



class Shipping_address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    Full_name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=12)
    House  = models.CharField(max_length=255)
    Area = models.CharField(max_length=60)
    Landmark = models.CharField(max_length=60)
    Town =  models.CharField(max_length=60)
    State =  models.CharField(max_length=60)
    Zip = models.IntegerField()
    
    def __str__(self):
        return self.Full_name


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    shipping_address = models.ForeignKey(Shipping_address,on_delete=models.CASCADE) 
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=255,null=False)
   
    Order_statuses = (
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),

    )
    
    status =models.CharField(max_length=150,choices=Order_statuses,default='Pending')
    tracking_no = models.CharField(max_length=150,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    

  
class Order_Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    order = models.ForeignKey(Order,on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    quanty = models.IntegerField(null=False)   

    
    







