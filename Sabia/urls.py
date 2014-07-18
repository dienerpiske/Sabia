from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Sabia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^inicio/$', 'SabiaApp.views.inicio', name='inicio'),
    url(r'^home/$', 'SabiaApp.views.home', name='home'),
    url(r'^novo_fichamento/(?P<id_artigo>\d+)/$', 'SabiaApp.views.novo_fichamento', name='novo_fichamento'),
    url(r'^salvar_questao/$', 'SabiaApp.views.salvar_questao', name='salvar_questao'),
    url(r'^registra_novo/$', 'SabiaApp.views.registra_novo', name='registra_novo'),
    url(r'^novo_artigo/$', 'SabiaApp.views.novo_artigo', name='novo_artigo'),
    url(r'^mostra_artigo/(?P<id_artigo>\d+)/$', 'SabiaApp.views.mostra_artigo', name='mostra_artigo'),
    url(r'^admin/', include(admin.site.urls)),
]
