from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
   return render(request, 'index.html')

def terms(request):
     return render(request, 'terms.html')


def about(request):
    return render(request, 'about.html')

def handlelogin(request):
    if request.method=="POST":
        #firstname=request.POST.get("pass2")
        #lastname=request.POST.get("lname")
        uname=request.POST.get("uname")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"LOGIN SUCCESSFULL")
            return redirect('/')
        else:
            messages.error(request,"INCORRECT USERNAME AND PASSWORD")
            return redirect('/login')

    return render(request, 'login.html')


def handlesignup(request):
    if request.method=="POST":
        #firstname=request.POST.get("pass2")
        #lastname=request.POST.get("lname")
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        
        #print(uname,email,password,confirmpassword)
        if password!=confirmpassword:
            messages.warning(request, "Password Does not Match")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=uname):
               messages.info(request, "Username Already Exists")
               return redirect('/signup')
        except:
            pass     

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email Already Exists")
                return redirect('/signup')
        except:
            pass     



        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request, "Signup Successful")
        return redirect('/login')

    
    return render(request, 'signup.html')

   


   


