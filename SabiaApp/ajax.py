import detectlanguage
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from SabiaApp.models import Artigo
from SabiaApp.models import Fichamento
from django.template.loader import render_to_string
from SabiaApp.bing import MicrosoftTranslatorClient


@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message' : 'message from server'})

@dajaxice_register
def traduzir(request, texto, de, para):
    detectlanguage.configuration.api_key = "f2d7fc33a7f3cb0b045d83b6a4c36ad9"
    #msg = detectlanguage.simple_detect(texto)
    client = MicrosoftTranslatorClient('sabialiedufes', 'HyJ6rFaIeEPd9q7ZjrWaixrKIUuAXuxIAroGL6YpRl8=')
    t =  client.TranslateText(texto, de, para)
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

