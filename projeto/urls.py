from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoas.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'login'),
    url(r'^validar/$', 'validar'),
    url(r'^logoff/$', 'logoff'),
    url(r'^dashboard/$', 'dashboard'),
                       
    url(r'^cadastro/$', 'cadastro'), 
    url(r'^cadastro_validar/$', 'cadastro_validar'),
    url(r'^token/(?P<numero>\d+)/$', 'token'),
)

