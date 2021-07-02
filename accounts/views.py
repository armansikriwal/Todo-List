from django.core.checks import messages
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout


def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"enter valid details")
            return redirect("login")
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user already exists")
                return redirect("register")
            else:
                user= User.objects.create_user(first_name=first_name,last_name=last_name,password=password1,username=username)
                user.save()
                print("success")
                return redirect("/")
        else :
            messages.info(request,"password doesnt match")
            return redirect("register")
        return redirect("/")

    else:
        return render(request,"register.html")

def logout_view(request):
    logout(request)
    return  redirect("/")
