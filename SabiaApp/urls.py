from django.conf.urls import url, patterns

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

    
)
