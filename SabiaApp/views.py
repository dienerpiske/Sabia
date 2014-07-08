from django.forms import ModelForm
from django.shortcuts import render_to_response
from SabiaApp.models import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

class FichamentoModelForm(ModelForm):
    class Meta:
        model = Fichamento
        
def inicio(request):  
    return render_to_response('index.html')

def main_page(request):  
    return render_to_response('main_page.html')

def novo_fichamento(request):
    return render_to_response('novo_fichamento.html')

@csrf_exempt 
def salvar_questao(request):
    d = {}
    d.update(csrf(request))
    if request.POST:        
        doc = Fichamento()
        doc.titulo_topico = request.POST['formQuestao']
        doc.usuario_id = '1'
        doc.artigo_id = '1'      
        doc = doc.save()       
        return render_to_response('novo_fichamento.html',doc)