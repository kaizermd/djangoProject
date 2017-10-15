"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
#from django.conf.urls import patterns, url
#from app.forms import BootstrapAuthenticationForm

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from app.forms import BootstrapAuthenticationForm
from app.views import home, contact, about, artists, artistsdetails
from django.contrib.auth.views import login, logout
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^artists$', artists, name='artists'), 
    url(r'^artists/(?P<name>[A-Za-z]+)$', artistsdetails, name='artistsdetails'),
    url(r'^$', home, name='home'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about', about, name='about'),
    url(r'^login/$',
        login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        logout,
        {
            'next_page': '/',
        },
        name='logout')
    ]

#urlpatterns = patterns('',
#    # Examples:
#    url(r'^$', 'app.views.home', name='home'),
#    url(r'^contact$', 'app.views.contact', name='contact'),
#    url(r'^about', 'app.views.about', name='about'),
#    url(r'^login/$',
#        'django.contrib.auth.views.login',
#        {
#            'template_name': 'app/login.html',
#            'authentication_form': BootstrapAuthenticationForm,
#            'extra_context':
#            {
#                'title':'Log in',
#                'year':datetime.now().year,
#            }
#        },
#        name='login'),
#    url(r'^logout$',
#        'django.contrib.auth.views.logout',
#        {
#            'next_page': '/',
#        },
#        name='logout'),

#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#)
