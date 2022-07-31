from django import forms
from .models import User
from django.forms import ModelForm

#class RegisterForm(forms.Form):
 #   name = forms.CharField(label='Имя')
 #   email = forms.EmailField(label='Емейл')
 #   password = forms.CharField(label='Пароль')


# creating forms from models
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "password"]
