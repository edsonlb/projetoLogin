# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoas.forms import PessoaForm, LoginForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def validar(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            pessoa = authenticate(username=form.data['login'], password=form.data['senha'])
            
            if pessoa is not None:
                if pessoa.is_active:
                    meu_login(request, pessoa)
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def logoff(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required()
def dashboard(request):
    return render(request,'dashboard.html')

def cadastro(request):
    form = PessoaForm()
    return render(request,'cadastro.html',{'form':form})

