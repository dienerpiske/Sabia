from django.conf.urls import url, patterns
from django import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sabia.views.home', name='home'),
    url(r'^inicio/$', 'SabiaApp.views.inicio', name='inicio'),
    url(r'^home/$', 'SabiaApp.views.home', name='home'),
    #url(r'^novo_fichamento/(?P<id_artigo>\d+)/$', 'SabiaApp.views.novo_fichamento', name='novo_fichamento'),
    url(r'^artigo/(?P<id_artigo>\d+)/fichar/$', 'SabiaApp.views.novo_fichamento', name='novo_fichamento'),
    url(r'^fichamento/(?P<id_fichamento>\d+)/editar/$', 'SabiaApp.views.editar_fichamento', name='editar_fichamento'),
    url(r'^salvar_questao/$', 'SabiaApp.views.salvar_questao', name='salvar_questao'),
    url(r'^registra_novo/$', 'SabiaApp.views.registra_novo', name='registra_novo'),
    url(r'^novo_artigo/$', 'SabiaApp.views.novo_artigo', name='novo_artigo'),
    url(r'^fichamento/(?P<id_fichamento>\d+)/$', 'SabiaApp.views.mostra_fichamento', name='mostra_fichamento'),
    url(r'^artigo/(?P<id_artigo>\d+)/$', 'SabiaApp.views.mostra_artigo', name='mostra_artigo'),
    url(r'^cadastro_usuario/$', 'SabiaApp.views.cadastro_usuario', name='cadastro_usuario'),
        
    #url(r'^home/$', 'django.contrib.auth.views.login', name='home'),
    url(r'^home/$', 'django.contrib.auth.views.login', {'template_name':'SabiaApp/templates/meu_sabia.html'}),
    # Redireciona a pagina. Ao inves de ir pro admin, vai para meu_sabia.html 
    url(r'^logout_page/$', 'SabiaApp.views.logout_page', name="logout_page",),
)
