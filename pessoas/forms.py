# coding: utf-8
from django import forms
from pessoas.models import Pessoa

class PessoaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Pessoa

class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    
class cadastroForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.CharField(max_length=100, required=True)