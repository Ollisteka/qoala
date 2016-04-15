from django import forms

__author__ = 'Last G'


class TokenAuthForm(forms.Form):
    token = forms.CharField()


class PasswordAuthForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()


class RegisterForm(forms.Form):
    login = forms.CharField()
    name = forms.CharField()
    password = forms.CharField()