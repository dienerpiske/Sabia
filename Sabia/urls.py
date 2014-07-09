from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Sabia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^inicio/$', 'SabiaApp.views.inicio', name='inicio'),
    url(r'^main_page/$', 'SabiaApp.views.main_page', name='main_page'),
    url(r'^novo_fichamento/(?P<id_artigo>\d+)/$', 'SabiaApp.views.novo_fichamento', name='novo_fichamento'),
    url(r'^salvar_questao/$', 'SabiaApp.views.salvar_questao', name='salvar_questao'),
    url(r'^registra_novo/$', 'SabiaApp.views.registra_novo', name='registra_novo'),
    url(r'^insere_artigo/$', 'SabiaApp.views.insere_artigo', name='insere_artigo'),
    url(r'^admin/', include(admin.site.urls)),
]
