from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Sabia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^inicio/$', 'SabiaApp.views.inicio', name='inicio'),
    url(r'^main_page/$', 'SabiaApp.views.main_page', name='main_page'),
    url(r'^admin/', include(admin.site.urls)),
]
