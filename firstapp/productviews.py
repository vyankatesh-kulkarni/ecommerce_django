from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp.form import ProductForm,Product,User,Category
from .models import Cart


def addProduct(request):
    p = ProductForm
    return render(request,'addProduct.html',{'form':p})

def insertproduct(request):
    p = ProductForm(request.POST)
    p.save()
    return redirect('/addProduct')

def productList(request):
    p = Product.objects.all()
    return render(request,"productlist.html",{'products':p})

def deleteProduct(request):
    id = request.GET.get('id')
    pr = Product.objects.get(id=id)
    pr.delete()
    return redirect('/productList')

def editeProduct(request):
    id = request.GET.get('id')
    p1 = Product.objects.get(id=id)
    p  = ProductForm(instance=p1)
    return render(request,"editProduct.html",{'info':p,'id':id})

def updateProduct(request):
    id = request.GET.get("id")
    p1 = Product.objects.get(id=id)
    p = ProductForm(request.POST,instance = p1)
    p.save()
    return redirect('/productList')

def addtoCart(request):
    pid    = request.GET.get('id')
    pd    = Product.objects.get(id=pid)
    email = request.session.get('userName')
    user  = User.objects.get(email = email)
    cr = Cart()
    cr.pid = pd
    cr.email = user 
    cr.save()
    return HttpResponse("success")

def cartList(request):
    email = request.session.get('userName')
    crlist = Cart.objects.filter(email = email)
    cl     = Category.objects.all()
    return render(request,'cartList.html',{'crlist':crlist,'cl':cl})


    