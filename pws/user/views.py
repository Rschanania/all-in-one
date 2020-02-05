from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as authorize,logout as deauth

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages


def logout(request):
    if request.user.is_authenticated:
        deauth(request)
        messages.info(request,"You are succefully log out ")
        return redirect('/user/login')

    return redirect('/user/login')

def Home(request):
    return HttpResponse("Hello User")

def login(request):

    if request.method=="POST":
       # form=AuthenticationForm()
        uname=request.POST['username']
        upass=request.POST['password']
        user=authenticate(username=uname,password=upass)
        if user is  None:
            messages.info(request,'user or password is not correct')
            return redirect('/user/login')
        else:
            authorize(request,user)
            return redirect('/user/profile')
    else:
        if request.user.is_authenticated:
            return redirect('/user/profile')
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})

# Create your views here.
def register(request):
    form=UserCreationForm()
    if request.method=="POST": 
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO,"user successfully created ")
            return redirect('/user/login/')

    return render(request,'register.html',{'form':form})


def profile(request):
    if request.user.is_authenticated:
        print("hello")
        print(request.path)
        return render(request,'profile.html')
    else:
        messages.info(request,'YOu are not loged in ')
        return redirect('/user/login')