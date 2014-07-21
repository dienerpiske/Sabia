from django.forms import ModelForm
from django.shortcuts import render_to_response, render
from SabiaApp.models import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios

class FichamentoModelForm(ModelForm):
    class Meta:
        model = Fichamento

def inicio(request):  
    return render_to_response('inicio.html')

def home(request):
    artigos = Artigo.objects.all()
    fichamentos = Fichamento.objects.all()
    return render_to_response('meu_sabia.html',{'artigos' : artigos, 'fichamentos' : fichamentos})

def editar_fichamento(request, id_artigo, id_fichamento):
    fichamento = Fichamento.objects.get(id = id_fichamento)
    return render_to_response('novo_fichamento.html',{'fichamento' : fichamento, 'artigo' : fichamento.artigo})

def novo_fichamento(request, id_artigo):
    id_fichamento = 1 # criar novo fichamento e passar o id
    return editar_fichamento(request, id_artigo, id_fichamento)

def mostra_fichamento(request, id_fichamento):
    fichamento = Fichamento.objects.get(id = id_fichamento)
    artigo = fichamento.artigo
    return mostra_artigo_fichamento(request, artigo, fichamento)

def mostra_artigo_fichamento(request, artigo, fichamento):
    return render_to_response('mostra_artigo.html',{'artigo' : artigo, 'fichamento' : fichamento})

def mostra_artigo(request, id_artigo):
    artigo = Artigo.objects.get(id = id_artigo)
    return render_to_response('mostra_artigo.html',{'artigo' : artigo})

@csrf_exempt 
def salvar_questao(request):
    d = {}
    d.update(csrf(request))
    if request.POST:        
        doc = Fichamento()
        doc.titulo_topico = request.POST['formQuestao']
        doc.usuario_id = '1'
        doc.artigo_id = request.POST['idOculto']      
        doc.save()       
        return HttpResponseRedirect(reverse('SabiaApp.views.novo_fichamento', args=[request.POST['idOculto']]))
    #return render_to_response('novo_fichamento.html',doc)

@csrf_exempt
def registra_novo(request):    
    art = {}
    art.update(csrf(request))
    
    if request.POST:        
        artigo = Artigo()
        artigo.texto_artigo = request.POST['formArtigo']
        artigo.titulo_artigo = request.POST['formTitulo']  
        artigo.tags_artigo = request.POST['formTags']          
        artigo.save()       
            
        return HttpResponseRedirect(reverse('SabiaApp.views.mostra_artigo', args=[artigo.id]))

def novo_artigo(request):
    return render_to_response('novo_artigo.html')