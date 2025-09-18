from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(req):
    return render(req, 'AppExemplo/home.html')

def secHome(req):
    return render(req, "seguranca/secHome.html")

def registro(req):
    if req.method == 'POST':
        formulario = UserCreationForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("home-sec")
    else:
        formulario = UserCreationForm()
    contexto={'form': formulario}
    return render(req, 'seguranca/registro.html', contexto)

def segundaPagina(req):
    return render(req, 'AppExemplo/segundaPagina.html')