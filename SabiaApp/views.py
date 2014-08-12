# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.shortcuts import render_to_response, render
from SabiaApp.models import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth import authenticate, logout, login
from django.template import Context, loader, RequestContext
from django.contrib.auth.models import User
from django.db import IntegrityError

class FichamentoModelForm(ModelForm):
    class Meta:
        model = Fichamento

def redireciona(request):
    return HttpResponseRedirect(reverse('SabiaApp.views.inicio')) 
       
def islogado(request):
    if request.user.id is None:
        return HttpResponseRedirect(reverse('SabiaApp.views.inicio'))

def inicio(request):  
    return render_to_response('inicio.html')

@csrf_exempt 
def home(request):
    if request.user.id is None:
        if request.POST: 
            usuario = authenticate(username=request.POST['nomeUsuario'], password=request.POST['senhaUsuario'])
            
            if usuario is not None:           
                login(request, usuario)             
                artigos = Artigo.objects.all()
                fichamentos = Fichamento.objects.filter(usuario_id = request.user.id)    
                usuario = Usuario.objects.get(user_id=request.user.id)
                
                return render_to_response('meu_sabia.html',{'artigos' : artigos, 'fichamentos' : fichamentos, 'usuarioInfo' : usuario},context_instance=RequestContext(request,{}))
                                      
    else:
        artigos = Artigo.objects.all()
        fichamentos = Fichamento.objects.filter(usuario_id = request.user.id)    
        usuario = Usuario.objects.get(user_id=request.user.id)
        
        return render_to_response('meu_sabia.html',{'artigos' : artigos, 'fichamentos' : fichamentos, 'usuarioInfo' : usuario},context_instance=RequestContext(request,{}))
    
    return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))   

def acesso_negado(request):
    return render_to_response('acesso_negado.html')
        
def editar_fichamento(request, id_fichamento):
    if request.user.id is None:
        return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))  
    
    fichamento = Fichamento.objects.get(id = id_fichamento)
    return render_to_response('novo_fichamento.html',{'fichamento' : fichamento, 'artigo' : fichamento.artigo})

def novo_fichamento(request, id_artigo):
    if request.user.id is None:
        return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))  
    
    artigo = Artigo.objects.get(id=id_artigo)
    #usuario = Usuario.objects.get(id=request.user.id)
    fichamento = Fichamento(titulo_fichamento=artigo.titulo_artigo, likes_fichamento=0, artigo = artigo, usuario = request.user)
    fichamento.save()
    return HttpResponseRedirect(reverse('SabiaApp.views.editar_fichamento', args=[fichamento.id]))
    

def mostra_fichamento(request, id_fichamento):
    if request.user.id is None:
        return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))  
    fichamento = Fichamento.objects.get(id = id_fichamento)
    artigo = fichamento.artigo
    return mostra_artigo_fichamento(request, artigo, fichamento)

def mostra_artigo_fichamento(request, artigo, fichamento):
    if request.user.id is None:
        return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))  
    return render_to_response('mostra_artigo.html',{'artigo' : artigo, 'fichamento' : fichamento})

def mostra_artigo(request, id_artigo):
    if request.user.id is None:
        return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))  
    artigo = Artigo.objects.get(id = id_artigo)
    return render_to_response('mostra_artigo.html',{'artigo' : artigo})

@csrf_exempt 
def salvar_questao(request):
    if request.user.id is None:
       return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))  
    d = {}
    d.update(csrf(request))
    
    return HttpResponse(request.user.id)
    if request.POST:        
        doc = Fichamento()
        doc.titulo_topico = request.POST['formQuestao']
        doc.usuario_id = request.user.id
        doc.artigo_id = request.POST['idOculto']      
        doc.save()       
        return HttpResponseRedirect(reverse('SabiaApp.views.novo_fichamento', args=[request.POST['idOculto']]))
    #return render_to_response('novo_fichamento.html',doc)

@csrf_exempt
def registra_novo(request):   
    if request.user.id is None:
        return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))  
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
    if request.user.id is None:
        return HttpResponseRedirect(reverse('SabiaApp.views.acesso_negado'))  
    return render_to_response('novo_artigo.html')
 

@csrf_exempt
def cadastro_usuario(request):
    sucess_message = ''
    error_message = ''
    
    try:  
        if request.POST:
            usuario = User()
            usuario.first_name = request.POST['primeiroNome']
            usuario.last_name = request.POST['ultimoNome']
            usuario.username = request.POST['nomeUsuario']
            usuario.email = request.POST['emailUsuario']
            usuario.set_password(request.POST['senhaUsuario'])
            
            usuario.save()
            
            usuarioGenerico = Usuario()
            usuarioGenerico.user = usuario 
            usuarioGenerico.informacoes_usuario = request.POST['dadosAdicionais']
            usuarioGenerico.save()
            
            sucess_message = 'Usuário Cadastrado com Sucesso!'
    
    except IntegrityError:
        error_message = 'Usuário já existe!'
        return render(request,'cadastro_usuario.html',{'error_message' : error_message})
      
    return render(request,'cadastro_usuario.html',{'sucess_message' : sucess_message})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('../inicio/')

def login_page(request):
    return render_to_response('login.html')