
from django.contrib import admin
from django.urls import path
from .import views,categoryviews,userviews,productviews
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.datapage),
    path('register',views.addUser),
    path('Homepage',views.homepage),
    path('login',views.login),
    path('loginuser',views.loginuser),
    path('logout',views.logoutUser),
    path('feedback',views.feedback),

    path('addCategory',categoryviews.addCategory),
    path('insertCategory',categoryviews.insertCategory),
    path('Categorylist',categoryviews.Categorylist),
    path('deleteCategory',categoryviews.deleteCategory),
    path('categoryproducts',categoryviews.categoryproducts),

    path('addUser',userviews.addUser),
    path('insertUser',userviews.insertUser),
    path('userlist',userviews.userlist),
    path('deleteuser',userviews.deleteuser),
    path('editeuser',userviews.editeuser),
    path('updateUser',userviews.updateUser),

    path('addProduct',productviews.addProduct),
    path('insertproduct',productviews.insertproduct),
    path('productList',productviews.productList),
    path('deleteProduct',productviews.deleteProduct),
    path('editeProduct',productviews.editeProduct),
    path('updateProduct',productviews.updateProduct),
    path('addtoCart',productviews.addtoCart),
    path('cartList',productviews.cartList),

    path('search',views.search),
    path('searchProduct',views.searchProduct)

    

    
]
