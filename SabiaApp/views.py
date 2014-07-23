from django.forms import ModelForm
from django.shortcuts import render_to_response, render
from SabiaApp.models import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth import authenticate, logout, login
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User

class FichamentoModelForm(ModelForm):
    class Meta:
        model = Fichamento

def inicio(request):  
    return render_to_response('inicio.html')

@csrf_exempt 
def home(request):
   if request.user.id:
        artigos = Artigo.objects.all()
        fichamentos = Fichamento.objects.all()
        return render_to_response('meu_sabia.html',{'artigos' : artigos, 'fichamentos' : fichamentos})
        #return HttpResponse(request.user.id)
        
   if request.POST:       
        usuario = authenticate(username=request.POST['nomeUsuario'], password=request.POST['senhaUsuario'])
        
        if usuario is not None:                        
            artigos = Artigo.objects.all()
            fichamentos = Fichamento.objects.all()            
            return render_to_response('meu_sabia.html',{'artigos' : artigos, 'fichamentos' : fichamentos},context_instance=RequestContext(request,{}))
        else:
            return render(request,'inicio.html')
        
def editar_fichamento(request, id_fichamento):
    fichamento = Fichamento.objects.get(id = id_fichamento)
    return render_to_response('novo_fichamento.html',{'fichamento' : fichamento, 'artigo' : fichamento.artigo})

def novo_fichamento(request, id_artigo):
    artigo = Artigo.objects.get(id=id_artigo)
    usuario = Usuario.objects.get(id=1)
    fichamento = Fichamento(titulo_fichamento=artigo.titulo_artigo, likes_fichamento=0, artigo = artigo, usuario = usuario)
    fichamento.save()
    return render_to_response('novo_fichamento.html',{'fichamento' : fichamento, 'artigo' : fichamento.artigo})

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

@csrf_exempt
def cadastro_usuario(request):
    
    if request.POST:
        usuario = User()
        usuario.first_name = request.POST['primeiroNome']
        usuario.last_name = request.POST['ultimoNome']
        usuario.username = request.POST['nomeUsuario']
        usuario.email = request.POST['emailUsuario']
        usuario.set_password(request.POST['senhaUsuario'])
        
        usuario.save()
    
        return render(request,'cadastro_usuario.html',{'sucess_message' : 'OK'})
    else:
        return render_to_response('cadastro_usuario.html')

#def logout_page(request):
    #logout(request)
    #return render_to_response('inicio.html')