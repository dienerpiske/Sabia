from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sabia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^inicio/$', 'SabiaApp.views.inicio', name='inicio'),
    url(r'^home/$', 'SabiaApp.views.home', name='home'),
    url(r'^novo_fichamento/(?P<id_artigo>\d+)/$', 'SabiaApp.views.novo_fichamento', name='novo_fichamento'),
    url(r'^salvar_questao/$', 'SabiaApp.views.salvar_questao', name='salvar_questao'),
    url(r'^registra_novo/$', 'SabiaApp.views.registra_novo', name='registra_novo'),
    url(r'^novo_artigo/$', 'SabiaApp.views.novo_artigo', name='novo_artigo'),
    url(r'^mostra_artigo/(?P<id_artigo>\d+)/$', 'SabiaApp.views.mostra_artigo', name='mostra_artigo'),
    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += staticfiles_urlpatterns()