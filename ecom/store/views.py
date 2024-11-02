from django.shortcuts import redirect, render
from .models import Product,Category
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

def about(request):
    return render(request,'about.html')

def login_user(request):

    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been login successfully")
            return redirect('home')
        else:
            messages.success(request,"Login was not successful,Try Again")
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')


def register_user(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #login user
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"You have Register successfully")
            return redirect('home')
        else:
            messages.success(request," Registeration was  unsuccessfully")
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})
    

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def category(request,foo):
    foo=foo.replace('-',' ')
    #grab cateogry from url
    try:
        #look up the category from the url
        category=Category.objects.get(name=foo)
        product=Product.objects.filter(Category=category)
        return render(request,'category.html',{'products':product,'category':category})



    except:
        messages.success(request,"Categories doesnt exist")
        return redirect('home')


