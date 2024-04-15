from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,"home.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['password']
        myuser=authenticate(username=username,password=userpassword)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return render(request,"index.html")
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,"signin.html")

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password != confirm_password:
            messages.warning(request,"Password is not Matching")
            return render(request,'signup.html')
        
        try:
            if User.objects.get(username=email):
                messages.info(request,"Email Already Taken")
                return render(request,"signup.html")
        except Exception as identifier:
            pass

        user=User.objects.create_user(email,email,password)
        user.save()
        messages.info(request,"User created")
        return render(request,"signin.html")
    return render(request,"signup.html")

def logout(request):
    return render(request,'signin.html')