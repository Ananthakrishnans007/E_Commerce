from django.contrib import admin
from . models import*

# Register your models here.
admin.site.register(Category) 

admin.site.register(Product)
 
admin.site.register(Cart) 

admin.site.register(Zip) 

admin.site.register(Shipping_address) 

admin.site.register(Order) 

admin.site.register(Order_Item) 



