import detectlanguage
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from SabiaApp.models import Artigo
from SabiaApp.models import Fichamento
from SabiaApp.models import Marcacao
from django.template.loader import render_to_string
from SabiaApp.bing import MicrosoftTranslatorClient

@dajaxice_register
def criarmarcacao(request, id_fichamento,titulo,texto):
    print("1")
    fichamento = Fichamento.objects.get(id=id_fichamento)
    marcacao = Marcacao(titulo_marcacao = titulo, texto_marcacao = texto, fichamento = fichamento)
    marcacao.save()
    return crialgmarcacao(fichamento)

@dajaxice_register
def salvarmarcacao(request, id, titulo, texto):
    marcacao = Marcacao.objects.get(id=id)
    marcacao.titulo_marcacao = titulo
    marcacao.texto_marcacao = texto
    marcacao.save()
    return crialgmarcacao(marcacao.fichamento)

@dajaxice_register
def removermarcacao(request, id):
    marcacao = Marcacao.objects.get(id=id)
    fichamento = marcacao.fichamento
    marcacao.delete()
    return crialgmarcacao(fichamento)
    
def crialgmarcacao(fichamento):
    marcacoes = fichamento.marcacao_set.all()
    listgroup = render_to_string('div_lg_marcacao.html', {'marcacoes': marcacoes})
    return simplejson.dumps({'listgroup': listgroup})

@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message' : 'message from server'})

@dajaxice_register
def traduzir(request, texto, de, para):
    detectlanguage.configuration.api_key = "f2d7fc33a7f3cb0b045d83b6a4c36ad9"
    msg = detectlanguage.simple_detect(texto)
    client = MicrosoftTranslatorClient('sabialiedufes', 'HyJ6rFaIeEPd9q7ZjrWaixrKIUuAXuxIAroGL6YpRl8=')
    t =  client.TranslateText(texto, msg, para)
    return simplejson.dumps({'texto' : t})

@dajaxice_register
def searchfichamentos(request, busca):
    fichamentos = Fichamento.objects.all().filter(titulo_fichamento__icontains=busca)
    listgroup = render_to_string('div_lg_fichamento.html', {'fichamentos': fichamentos})
    return simplejson.dumps({'listgroup': listgroup})

@dajaxice_register
def searchartigos(request, busca):
    artigos = Artigo.objects.all().filter(texto_artigo__icontains=busca)
    listgroup = render_to_string('div_lg_artigo.html', {'artigos': artigos})
    return simplejson.dumps({'listgroup': listgroup})

@dajaxice_register
def salvartitulofichamento(request, id_f, titulo_f):
    fichamento = Fichamento.objects.get(id=id_f)
    fichamento.titulo_fichamento = titulo_f
    fichamento.save()
    
@dajaxice_register
def gostarfichamento(request, id_f):
    fichamento = Fichamento.objects.get(id=id_f)
    likes = fichamento.likes_fichamento + 1
    fichamento.likes_fichamento = likes
    fichamento.save()
    return simplejson.dumps({'likes': likes})