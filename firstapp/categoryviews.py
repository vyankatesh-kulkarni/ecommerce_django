from django.shortcuts import render,redirect
from firstapp.form import CategoryForm,Category,Product

def addCategory(request):
    c = CategoryForm
    return render(request,"addCategory.html",{'form':c})

def insertCategory(request):
    c = CategoryForm(request.POST)
    c.save()
    return redirect('/addCategory')

def Categorylist(request):
    c1 = Category.objects.all()
    return render (request,'Categorylist.html',{'category':c1})

def deleteCategory(request):
    cn = request.GET.get('cname')
    c1 = Category.objects.get(cname = cn)
    c1.delete()
    return redirect('/Categorylist')

def categoryproducts(request):
    cname = request.GET.get('cname')
    p1 = Product.objects.filter(cname = cname)
    c1 = Category.objects.all()
    return render(request,'index.html',{'categories':c1,'pl':p1})


