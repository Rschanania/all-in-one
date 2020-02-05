from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login as authorize ,logout as deauth


def login(request):
    form=AuthenticationForm()
    if request.method=="POST":
        uname=request.POST['username']
        upass=request.POST['password']
        user=authenticate(username=uname,password=upass)
        if user is None:
            messages.info(request,"Username or password is Not correct ")
            return redirect('/user/login')
        else:
            authorize(request,user)
            return redirect('/user/profile')
    else:
        if request.user.is_authenticated:
            return redirect('/user/profile')       

    return render(request,'user/login.html',{"form":form})
    #return HttpResponse("Hello login")

def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            #messages.info(request,"Registraion successfull Enjoy ")
            messages.add_message(request,messages.INFO,"Registraion successfull Enjoy")
            form.save()
            return redirect('/user/login')
        
            
    return render(request,'user/register.html',{'form':form})

def logout(request):
    if request.user.is_authenticated:
        deauth(request)
        messages.info(request,"logot sucessfully")
        return redirect('/user/login')
    return redirect('/user/login')
def profile(request):
    if request.user.is_authenticated:
        return render(request,'user/profile.html')
    else:
        messages.info(request,"You are not authenticates")
        return redirect('/user/login/')


