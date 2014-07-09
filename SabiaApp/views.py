from django.forms import ModelForm
from django.shortcuts import render_to_response
from SabiaApp.models import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class FichamentoModelForm(ModelForm):
    class Meta:
        model = Fichamento
        
def inicio(request):  
    return render_to_response('index.html')

def main_page(request):  
    return render_to_response('main_page.html')

def novo_fichamento(request, id_artigo):
    artigo = Artigo.objects.get(id = id_artigo)
    return render_to_response('novo_fichamento.html',{'artigo' : artigo})

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
        artigo.save()       
            
        return HttpResponseRedirect(reverse('SabiaApp.views.novo_fichamento', args=[artigo.id]))

def insere_artigo(request):
    return render_to_response('insere_artigo.html')