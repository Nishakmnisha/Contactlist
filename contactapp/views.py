from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LogInForm,ContactForm,ContactUpdateForm
from contactapp import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Contact
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'index.html')
class Register(View):
    def get(self,request):
        reg=RegisterForm()
        return render(request,'reg.html',{'reg':reg})
    def post(self,request):
        reg=RegisterForm(request.POST)
        if reg.is_valid():
            fname=reg.cleaned_data.get("first_name")
            lname=reg.cleaned_data.get("last_name")
            uname=reg.cleaned_data.get("username")
            password=reg.cleaned_data.get("password")
            User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password)
            messages.success(request,"registered successfully!")
            return redirect('home')
class LoginView(View):
    def get(self,request):
        form=LogInForm()
        return render(request,"log.html",{'form':form})
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(request,"WELCOME")
            return redirect('home')
        else:
            messages.error (request,"Invalid Credentials")
            return redirect("log")
class LogOutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Please login to add your contact!")
        return redirect('log')
class AddContactView(View):
    def get(self,request):
        form=ContactForm()
        return render(request,'add.html',{'form':form})
    def post(self,request):
        if request.user.is_authenticated:
            form=ContactForm(request.POST)
            if form.is_valid():
                email=form.cleaned_data.get("email")
                address=form.cleaned_data.get("address")
                tele=form.cleaned_data.get("Telephone")
                phone_number=form.cleaned_data.get("phone_number")
                user=request.user
                Contact.objects.create(user=user,email=email,address=address,Telephone=tele,phone_number=phone_number)
                messages.success(request,"Contact added successfully!")
                return redirect("home")
            else:
                messages.warning(request,"Invalid Credentials!")
                return redirect("add")
        else:
            messages.warning(request,"you must login first!")
            return redirect('log')
class ContactListView(View):
    def get(self,request):
        user=request.user
        if user.is_authenticated:
            cont=Contact.objects.filter(user=request.user)
            return render(request,'list.html',{'cont':cont})
        else:
            messages.warning(request,"you must login first!")
            return redirect('log')
class ContactDeleteView(View):
    def get(self,request,*args,**kwargs):
        user=request.user
        contact=Contact.objects.get(user=request.user)
        contact.delete()
        return redirect("list")
class ContactDeleteView(View):
    def get(self,request,*args,**kwargs):
        user=request.user
        contact=Contact.objects.get(user=request.user)
        contact.delete()
        return redirect("list")
class ContactUpdateView(View):
    def get(self,request,*args,**kwargs):
        user=request.user
        contact=Contact.objects.get(user=request.user)
        form=ContactUpdateForm(instance=contact)
        return render(request,"update.html",{'form':form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        contact=Contact.objects.get(user=request.user)
        form=ContactUpdateForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('list')