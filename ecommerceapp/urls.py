
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),

    path('signup',views.signup,name='signup'),

    path('signin',views.signin,name='signin'),

    path('register',views.register,name='register'),

    path('user_login',views.user_login,name='user_login'),

    path('logout',views.logout,name='logout'),

    # path('search',views.search,name='search'),

    path('show_all',views.show_all,name='show_all'),

    path('category/<int:id>',views.category,name='category'),


    path('product_detail/<int:id>',views.product_detail,name='product_detail'),

    path('add_cart/<int:id>',views.add_cart,name='add_cart'),

    path('cart',views.cart,name='cart'),

    path('zip',views.zip,name='zip'),

    path('remove_cart/<int:id>',views.remove_cart,name='remove_cart'),

    path('remove_cart_all',views.remove_cart_all,name='remove_cart_all'),

    path('checkout',views.checkout,name='checkout'),
    
    path('shipping_address',views.shipping_address,name='shipping_address'),
    

    path('place_order/<int:id>',views.place_order,name='place_order'),

    path('dashboard',views.dashboard,name='dashboard'),

    path('dashboard_profile',views.dashboard_profile,name='dashboard_profile'),

    path('dash_edit_profile',views.dash_edit_profile,name='dash_edit_profile'),

    path('edit',views.edit,name='edit'),

    path('dash_address_book',views.dash_address_book,name='dash_address_book'),

    path('track_order',views.track_order,name='track_order'),

    path('my_order',views.my_order,name='my_order'),

    path('manage_order/<int:id>',views.manage_order,name='manage_order'),




    path('admin_dash',views.admin_dash,name='admin_dash'),

    path('dash_category',views.dash_category,name='dash_category'),

    path('add_category',views.add_category,name='add_category'),

    path('del_category/<int:id>',views.del_category,name='del_category'),

    
    path('dash_product',views.dash_product,name='dash_product'),

    path('add_product',views.add_product,name='add_product'),


    path('edit_product/<int:id>',views.edit_product,name='edit_product'),

    path('edit_pro/<int:id>',views.edit_pro,name='edit_pro'),
    

    path('show_product',views.show_product,name='show_product'),

    path('show_order',views.show_order,name='show_order'),

    path('status/<int:id>',views.status,name='status'),




    path('show_order_product/<int:id>',views.show_order_product,name='show_order_product'),

    path('show_user',views.show_user,name='show_user'),


    path('user_carts/<int:id>',views.user_carts,name='user_carts'),
    

    


    

    

    

    

    

    


    

    

    
   

   
]

   

