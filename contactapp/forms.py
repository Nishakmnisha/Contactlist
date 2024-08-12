from django import forms
from django.contrib.auth.models import User
from .models import Contact
class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password"]     
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"first_name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"last_name"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"})
        }   
class LogInForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"})
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["email","address","Telephone","phone_number"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}),
            "address":forms.TextInput(attrs={"class":"form-control","placeholder":"Address"}),
            "Telephone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Telephone"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control","placeholder":"phone_number"})
        }
class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["email","address","Telephone","phone_number"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}),
            "address":forms.TextInput(attrs={"class":"form-control","placeholder":"Address"}),
            "Telephone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Telephone"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control","placeholder":"phone_number"}),
        }