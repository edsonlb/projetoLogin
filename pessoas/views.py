# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoas.forms import PessoaForm, LoginForm, cadastroForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
from pessoas.models import Pessoa
from django.core.mail import send_mail

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
    form = cadastroForm()
    return render(request,'cadastro.html',{'form':form})

def cadastro_validar(request):
    if request.method == 'POST':
        form = cadastroForm(request.POST)

        if form.is_valid():
            pessoa = Pessoa(
                username=form.data['login'], 
                email=form.data['email'],
                is_active=False
            )
            pessoa.set_password(form.data['senha'])
            pessoa.save()
            
            if send_mail('Campo assunto Aqui', 'Valide o seu email: http://unifran-78230.sae1.nitrousbox.com/token/'+str(pessoa.pk), 'testeunifran@bol.com.br',
    [pessoa.email], fail_silently=False):
                # Se der erro ele avisa aqui.
                # Retornar tela de sucesso! Vc Consegue fazer e tb arrumar esses códigos?
                return render(request,'cadastro.html',{'form':form})

def token(request, numero):
    pessoa = Pessoa.objects.get(pk=numero)
    pessoa.is_active = True
    pessoa.save()
    return HttpResponseRedirect('/login/')

