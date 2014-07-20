from django.contrib import admin
from SabiaApp.models import Artigo
from SabiaApp.models import Fichamento
from SabiaApp.models import Marcacao
from SabiaApp.models import Usuario

admin.site.register(Artigo)
admin.site.register(Fichamento)
admin.site.register(Marcacao)
admin.site.register(Usuario)