from django.shortcuts import render,redirect
from firstapp.models import Category,Product,User,Feedback
from django.http import HttpResponse
from firstapp.form import FeedbackForm
#from firstapp.models import User

# Create your views here.
def datapage(request):
    c1 = Category.objects.all()
    p1 = Product.objects.all()
    return render(request,"index.html",{'categories':c1,'pl':p1})

def addUser(request):
    return render(request,'addUser.html')

def homepage(request):
    return redirect('/')

def login(request):
    return render(request,'login.html')

def loginuser(request):
    email = request.POST.get('uname')
    password   = request.POST.get('pwd')
    if email =='admin' and password =='admin':
        request.session['admin'] =email
        return redirect('/')
    try:
        ul = User.objects.get(email = email)
        if email == ul.email and password == ul.password:
            request.session['userName'] = email
            return redirect('/')
        else:
            return render(request,'login.html',{'msg':'invalid username or password'})
    except:
        return render(request,"login.html",{'msg':"invalid username or password"})


def logoutUser(request):
    ls = list(request.session.keys())
    for i in ls:
        del request.session[i]
    return redirect('/')

def feedback(request):
    f = FeedbackForm
    return render(request,"feedback.html",{'form':f})

def search(request):
    c1 = Category.objects.all()
    p1 = Product.objects.all()
    print("data ",p1)
    return render(request,"search.html",{'categories':c1,'pl':p1})

    #return render(request,"search.html",{'pl':pl,'cl':cl})
    #return render(request,'search.html')

def searchProduct(request):
    product = request.POST.get('product')
    print("pprrr" ,product)
    pl  = Product.objects.filter(Pname = product)
    print("Search Data ",pl)

    cl = Category.objects.all()
    return render(request,"index.html",{'pl':pl,})
    


        


     
    


    