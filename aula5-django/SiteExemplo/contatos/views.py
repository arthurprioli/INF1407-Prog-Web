from django.shortcuts import render
from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

from django.views.generic.base import View

# Create your views here.
class listaContatosView(View):
    def get(self, req, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = { 'pessoas': pessoas, }
        return render(
            req,
            'contatos/listaContatos.html',
            contexto
        )

class insereContatosView(View):
    def get(self, req, *args, **kwargs):
        contexto = {'form': ContatoModel2Form}
        return render(req, "contatos/cadastraContato.html", contexto)

    def post(self, req, *args, **kwargs):
        formulario = ContatoModel2Form(req.POST)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))