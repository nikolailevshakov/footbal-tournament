from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Емейл')
    password = forms.CharField(label='Пароль')
