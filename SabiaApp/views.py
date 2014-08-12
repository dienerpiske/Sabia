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
from django.contrib.auth.decorators import login_required

def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

@csrf_exempt 
@login_required()
def home(request):
    artigos = Artigo.objects.all()
    fichamentos = Fichamento.objects.filter(usuario_id = request.user.id)
    return render_to_response('meu_sabia.html',{'artigos' : artigos, 'fichamentos' : fichamentos, 'user' : request.user, 'usuario' : request.user.usuario_set.all()[0]},context_instance=RequestContext(request,{}))

@login_required()
def editar_fichamento(request, id_fichamento):
    fichamento = Fichamento.objects.get(id = id_fichamento)
    if request.user.id == fichamento.usuario.id:
        return render_to_response('novo_fichamento.html',{'fichamento' : fichamento, 'artigo' : fichamento.artigo, 'user' : request.user})
    return HttpResponseRedirect(reverse('SabiaApp.views.acessoNegado'))

@login_required()
def novo_fichamento(request, id_artigo):
    artigo = Artigo.objects.get(id=id_artigo)
    #usuario = Usuario.objects.get(id=request.user.id)
    fichamento = Fichamento(titulo_fichamento=artigo.titulo_artigo, likes_fichamento=0, artigo = artigo, usuario = request.user)
    fichamento.save()
    return HttpResponseRedirect(reverse('SabiaApp.views.editar_fichamento', args=[fichamento.id]), { 'user' : request.user})
    
def mostra_fichamento(request, id_fichamento):
    fichamento = Fichamento.objects.get(id = id_fichamento)
    artigo = fichamento.artigo
    return mostra_artigo_fichamento(request, artigo, fichamento)

def mostra_artigo_fichamento(request, artigo, fichamento):
    return render_to_response('mostra_artigo.html',{'artigo' : artigo, 'fichamento' : fichamento, 'user' : request.user})

def mostra_artigo(request, id_artigo):
    artigo = Artigo.objects.get(id = id_artigo)
    return render_to_response('mostra_artigo.html',{'artigo' : artigo, 'user' : request.user})

@login_required()
@csrf_exempt 
def salvar_questao(request):
    d = {}
    d.update(csrf(request))
    
    return HttpResponse(request.user.id)
    if request.POST:        
        doc = Fichamento()
        doc.titulo_topico = request.POST['formQuestao']
        doc.usuario_id = request.user.id
        doc.artigo_id = request.POST['idOculto']      
        doc.save()       
        return HttpResponseRedirect(reverse('SabiaApp.views.novo_fichamento', args=[request.POST['idOculto']]), {'user' : request.user})
    #return render_to_response('novo_fichamento.html',doc)

@login_required()
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
            
        return HttpResponseRedirect(reverse('SabiaApp.views.mostra_artigo', args=[artigo.id]),{'user' : request.user})

@login_required()
def novo_artigo(request):
    return render_to_response('novo_artigo.html', {'user' : request.user})
 
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
            perfil = usuario.usuario_set.all()[0]
            perfil.lattes = request.POST['lattes']
            perfil.informacoes_usuario = request.POST['dadosAdicionais']
            perfil.save()
            sucess_message = 'Usuário Cadastrado com Sucesso!'
    
    except IntegrityError:
        error_message = 'Usuário já existe!'
        return render(request,'cadastro_usuario.html',{'error_message' : error_message, 'user' : request.user})
      
    return render(request,'cadastro_usuario.html',{'sucess_message' : sucess_message, 'user' : request.user})

def acessoNegado(request):
    return render_to_response("acesso_negado.html", {'user' : request.user})

def doLogout(request):
    logout(request)
    return HttpResponseRedirect('/sabia/')