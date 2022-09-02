from multiprocessing import context
from operator import countOf
import os
import random
from django.shortcuts import redirect, render
from . models import *

from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    product=Product.objects.all()
    category = Category.objects.all()
    
    context={
        'x':product,
        'category' : category,
    }
    
    return render(request,'index.html',context)




def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']   
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        psw=request.POST['psw']
        cpsw=request.POST['cpsw']

        if psw==cpsw:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=email,
                    email=email,
                    password=psw) 
                user.save()
            u=User.objects.get(id=user.id) 
            member=Member(phone=phone,user=u)
            member.save()
            return redirect('signin')

        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            return redirect('signup')
    else:
        return redirect('signup')



def user_login(request):
    if request.method=='POST':
        email=request.POST['email']
        psw=request.POST['psw']
        user=auth.authenticate(username=email,password=psw)
        request.session["uid"]=user.id
        

        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_dash')
            else:
                login(request,user)
                return redirect('index')


@login_required(login_url='signin')
def category(request,id):
    category = Category.objects.get(id=id)
    product = Product.objects.filter(Category_Name=category)

    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        
        
    }
    return render(request,'shop-full.html',context)



# def search(request):
#     if request.method=='POST':
#         search = request.POST['search']
#         category = Category.objects.filter(Category_Name=search)

#         product = Product.objects.all()
#         # category = Category.objects.all()
#         crt=Cart.objects.filter(user=request.user)
#         crt_count = crt.count()

#         sub_total=0 
#         grand_total = 0
#         shipping =50
#         for i in crt:
#             sub_total =  sub_total + i.product_qty * i.product.Product_Price 


#         grand_total =  sub_total + shipping
 

#         context = {
#             'pro'  : product, 
#             'crt' : crt,
#             'crt_count' : crt_count,
#             'sub_total' : sub_total,
#             'shipping'  : shipping,
#             'grand_total' : grand_total,
#             'category' : category,
        
        
#         }
#         return render(request,'shop-full.html',context)





        
    


@login_required(login_url='signin')
def show_all(request):
   
    product = Product.objects.all()
    category = Category.objects.all()
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 

    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        
        
    }
    return render(request,'shop-full.html',context)



@login_required(login_url='signin')
def product_detail(request,id):
    product=Product.objects.filter(id=id)
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 
      


    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        
        
    }


    return render(request,'product-detail.html',context) 



@login_required(login_url='signin')
def add_cart(request,id):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        product=Product.objects.get(id=id)

        qty=request.POST['qty']

        ct=Cart(user=user,product=product,product_qty=qty)
        ct.save()
        return redirect('cart')


@login_required(login_url='signin')
def cart(request):
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping

    context = {
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        
    }


    return render(request,'cart.html',context)    

def zip(request):
    if request.method=='POST':
        zipcode=request.POST['zip']
        if Zip.objects.filter(zip_code=zipcode).exists():
            messages.info(request, 'Delery avilable')
            return redirect('cart') 
        else:
            messages.info(request, 'Delery is not avilable')
            return redirect('cart')





def remove_cart(request,id):
    crt=Cart.objects.get(id=id)
    crt.delete()
    return redirect('cart')

def remove_cart_all(request):
    crt=Cart.objects.filter(user=request.user)
    crt.delete()
    return redirect('cart')
    

@login_required(login_url='signin')
def checkout(request):
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()
    ship = Shipping_address.objects.filter(user=request.user)

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 
    orderitem = Order_Item.objects.filter(user=request.user)
    shipadd = ""
    for i in ship:
        shipadd = str(i.Full_name)+" , " + str(i.House)+" , "  + str(i.Area)+" , "+ str(i.Landmark)+" , " + str(i.Town)+" , " + str(i.State)+" , " + str(i.Zip)+" , " + str(i.Phone)



    context = {
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'ship'    :   ship,
        'orderitem'  : orderitem,
        'shipadd'  : shipadd,
        
    }

    return render(request,'checkout.html',context)   


@login_required(login_url='signin')
def shipping_address(request):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        if Shipping_address.objects.filter(user=request.user).exists():
            ship1 =Shipping_address.objects.get(user=request.user)
            ship1.user=user
            ship1.Full_name = request.POST['fullname']
            ship1.Phone = request.POST['phone']
            ship1.House = request.POST['house']
            ship1.Area = request.POST['area']
            ship1.Landmark = request.POST['landmark']
            ship1.Town = request.POST['town']
            ship1.State = request.POST['state']
            ship1.Zip = request.POST['zip']
            ship1.save()
            return redirect('checkout')
        else:
            ship=Shipping_address()
            ship.user=user
            ship.Full_name = request.POST['fullname']
            ship.Phone = request.POST['phone']
            ship.House = request.POST['house']
            ship.Area = request.POST['area']
            ship.Landmark = request.POST['landmark']
            ship.Town = request.POST['town']
            ship.State = request.POST['state']
            ship.Zip = request.POST['zip']
            ship.save()
            return redirect('checkout')
        

@login_required(login_url='signin')
def place_order(request,id):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)

        ship=Shipping_address.objects.get(id=id)
        
        neworder= Order()

        neworder.user = user
        neworder.shipping_address = ship

        neworder.payment_mode = request.POST['payment']

        cart = Cart.objects.filter(user=request.user)
        crt_total_price = 0

        for i in cart:
            crt_total_price = crt_total_price +  i.product_qty * i.product.Product_Price 


        neworder.total_price = crt_total_price

        trackno = 'ananthu'+str(random.randint(1111111,9999999))

        while Order.objects.filter(tracking_no=trackno ) is None:
            trackno = 'ananthu'+str(random.randint(1111111,9999999))

        neworder.tracking_no = trackno
        neworder.save()
        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            Order_Item.objects.create(
                user = request.user,
                order = neworder,
                product = item.product,
                price  = item.product.Product_Price,
                quanty = item.product_qty

            )
        Cart.objects.filter(user=request.user).delete()

        messages.success(request,"Your order has been placed successfully")

        return redirect ('my_order')
               
    

@login_required(login_url='signin')
def dashboard(request):
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()
    ship = Shipping_address.objects.filter(user=request.user)

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
 
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    shipadd = ""
    for i in ship:
        shipadd = str(i.Full_name)+" , " + str(i.House)+" , "  + str(i.Area)+" , "+ str(i.Landmark)+" , " + str(i.Town)+" , " + str(i.State)+" , " + str(i.Zip)+" , " + str(i.Phone)



    context = {
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'ship'    :   ship,
        'orderitem'  : orderitem,
        'shipadd'  : shipadd,
        'order_count' : order_count,
    }
    return render(request,'dashboard.html',context)

@login_required(login_url='signin')
def dashboard_profile(request): 
    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'phone':ph,
        'order_count':order_count,
    }

    return render(request,'dash-my-profile.html',context)


@login_required(login_url='signin')
def dash_edit_profile(request):
    
    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'phone':ph,
        'order_count':order_count,
    }


    return render(request,'dash-edit-profile.html',context)


@login_required(login_url='signin')
def edit(request):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        pho=Member.objects.get(user=request.user)
        pho.phone=request.POST['phone']
        user.save()
        pho.save()
        return redirect('dash_edit_profile')     

@login_required(login_url='signin')
def dash_address_book(request):
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()
    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 

    ship = Shipping_address.objects.filter(user=request.user)
    address = ""
    reg = ""
    for i in ship:
        address = str(i.House)+" , "  + str(i.Area)+" , "+ str(i.Landmark)+" , " + str(i.Town)+" , " + str(i.State) +" , " + str(i.Zip)
        reg = str(i.Town)+" , " + str(i.State) 

    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'address':address,
        'reg':reg,
        'ph' :ph,

       
        'order_count':order_count,
    }
    return render(request,'dash-address-book.html',context)

@login_required(login_url='signin')
def track_order(request):

    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()


    context = {
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'order_count' :order_count,
        
    }
    return render(request,'dash-track-order.html',context)

    
@login_required(login_url='signin')
def my_order(request):
    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    order_count = orderitem.count()
    category = Category.objects.all()
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'phone':ph,
        'order_count':order_count,
        'orderitem' :orderitem,
    }
    return render(request,'dash-my-order.html',context)

    
@login_required(login_url='signin')
def manage_order(request,id):

    phone=Member.objects.get(user=request.user) 
    ph=phone.phone
    crt=Cart.objects.filter(user=request.user)
    crt_count = crt.count()

    sub_total=0 
    grand_total = 0
    shipping =50
    for i in crt:
      sub_total =  sub_total + i.product_qty * i.product.Product_Price 


    grand_total =  sub_total + shipping
    orderitem = Order_Item.objects.filter(user=request.user)
    ship = Shipping_address.objects.filter(user=request.user)
    shipadd = ""
    for i in ship:
        shipadd = str(i.Full_name)+" , " + str(i.House)+" , "  + str(i.Area)+" , "+ str(i.Landmark)+" , " + str(i.Town)+" , " + str(i.State)+" , " + str(i.Zip)+" , " + str(i.Phone)
        fullname =str(i.Full_name)
    
    order_count = orderitem.count()
    category = Category.objects.all()
    manageorder = Order_Item.objects.get(id=id)
    total=0
    total=(manageorder.price *manageorder.quanty) + shipping
    context = {
        'pro'  : product, 
        'crt' : crt,
        'crt_count' : crt_count,
        'sub_total' : sub_total,
        'shipping'  : shipping,
        'grand_total' : grand_total,
        'category' : category,
        'phone':ph,
        'order_count':order_count,
        'orderitem' :orderitem,
        'manageorder' :manageorder,
        'total' :total,
        'shipadd' :shipadd,
        'fullname' : fullname,
    }
    return render(request,'dash-manage-order.html',context) 



@login_required(login_url='signin')
def admin_dash(request):
    if not request.user.is_staff:
        return redirect('signin')
    return render(request,'administrator/index.html') 

@login_required(login_url='signin')
def dash_category(request):
    category=Category.objects.all()
    context={
        'category':category,

    }
    return render(request,'administrator/category.html',context)

@login_required(login_url='signin')
def add_category(request):
    if request.method=='POST':
        cat=Category()
        cat.Category_Name = request.POST['category']
        cat.save()
        return redirect('dash_category')

@login_required(login_url='signin')
def del_category(request,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    return redirect('dash_category')




@login_required(login_url='signin')
def dash_product(request):
    cat=Category.objects.all()
    context ={
        'cat' :cat,

         }

    return render(request,'administrator/products.html',context)

@login_required(login_url='signin')
def add_product(request):
    if request.method=='POST':
        c = request.POST['cat']
        cat=Category.objects.get(id=c)
        pro=Product()
        pro.Category_Name =cat
        pro.Product_Name = request.POST['pname']
        pro.Product_Description = request.POST['desp']
        pro.Product_Price = request.POST['price']
        pro.Product_Delprice = request.POST['delprice']
        if len(request.FILES) != 0:
            pro.Product_Image = request.FILES['file']
        pro.save()

    return redirect('show_product')


def edit_product(request,id):
    

    cat=Category.objects.all()
    product=Product.objects.get(id=id)
    context ={
        'cat' :cat,
        'product' :product,

         }
        
    return render(request,'administrator/edit_product.html',context)

@login_required(login_url='signin')
def edit_pro(request,id):

    if request.method=='POST':
        c = request.POST['cat']
        cat=Category.objects.get(id=c)
        pro=Product.objects.get(id=id)
       
        pro.Category_Name = cat
        
        pro.Product_Name = request.POST['pname']
        pro.Product_Description = request.POST['desp']
        pro.Product_Price = request.POST['price']
        pro.Product_Delprice = request.POST['delprice']
        if len(request.FILES) != 0:
            if len(pro.Product_Image) > 0  :
                os.remove(pro.Product_Image.path)
            pro.Product_Image = request.FILES['file']
            
        pro.save()
        return redirect('show_product')



@login_required(login_url='signin')
def show_product(request):

    product=Product.objects.all()
    context= {
        'product' : product,

    }

    return render(request,'administrator/show_product.html',context)

@login_required(login_url='signin')
def show_order(request):
    order = Order.objects.all()
    context = {
        'order' :order,
    }
    return render(request,'administrator/show_order.html',context)

@login_required(login_url='signin')
def status(request,id):
    if request.method=='POST':
        order = Order.objects.get(id=id)
        print(order)
        order.status = request.POST['st']
        order.save()
        return redirect('show_order')
          






@login_required(login_url='signin')
def show_order_product(request,id):
    items=Order_Item.objects.filter(order=id)
    order =Order.objects.get(id=id)
    context={
       'items' : items,
       'order' :order,
    }
    return render(request,'administrator/show_order_product.html',context)   



def show_user(request):

    users = User.objects.all()
    return render(request,'administrator/show_users.html',{'users':users})   


def user_carts(request,id):
    us = User.objects.get(id=id)
    
    carts=Cart.objects.filter(user=us)
    context = {
        'carts' : carts,
    }
    

    return render(request,'administrator/view_carts.html',context)  


def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('index')
      