from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    return render(req, 'AppExemplo/home.html')

def segundaPagina(req):
    return render(req, 'AppExemplo/segundaPagina.html')