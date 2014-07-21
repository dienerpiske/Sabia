from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from SabiaApp.models import Artigo
from SabiaApp.models import Fichamento
from django.template.loader import render_to_string

@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})

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

