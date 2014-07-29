from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
import SabiaApp

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    (r'^sabia/', include('SabiaApp.urls')),
    (dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/profile/', include(admin.site.urls)),
    url(r'^$', 'SabiaApp.views.redireciona'),
)

urlpatterns += staticfiles_urlpatterns()