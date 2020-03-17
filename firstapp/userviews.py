from django.shortcuts import render,redirect
from firstapp.form import UserForm,User

def addUser(request):
    u = UserForm
    return render(request,"aduser.html",{'form':u})

def insertUser(request):
    u = UserForm(request.POST)
    u.save()
    return redirect('/addUser')

def userlist(request):
    u1 = User.objects.all()
    return render(request,"userlist.html",{'users':u1})

def deleteuser(request):
    us = request.GET.get("email")
    em = User.objects.get(email = us)
    em.delete()
    return redirect('/userlist')

def editeuser(request):
    email = request.GET.get('email')
    e1 = User.objects.get(email = email)
    e = UserForm(instance=e1)
    return render(request,'editeuser.html',{'info':e,'email':email})

def updateUser(request):
    email = request.GET.get('email') 
    u1 = User.objects.get(email=email)
    u = UserForm(request.POST,instance=u1)
    u.save()
    return redirect('/userlist')




