from django.shortcuts import render, get_object_or_404
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
        else:
            contexto = {'form': formulario, 'mensagem': 'Preenche direito jumento!'}
            return render(req, 'contatos/cadastraContato.html', contexto)
        
class updateContatosView(View):
    def get(self, req, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        formulario = ContatoModel2Form(instance=pessoa)
        contexto = {'pessoa': formulario}
        return render(req, 'contatos/atualizaContato.html', contexto)
    
    def post(self, req, pk, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ContatoModel2Form(req.POST, instance=pessoa)
        if formulario.is_valid():
            pessoa = formulario.save()
            pessoa.save()
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
        else:
            contexto = {'pessoa': formulario, 'mensagem': 'Preenche direito jumento!'}
            return render(req, 'contatos/atualizaContato.html', contexto)

class deleteContatosView(View):
    def get(self, req, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = {'pessoa': pessoa}
        return render(req, 'contatos/excluiContato.html', contexto)
    
    def post(self, req, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))