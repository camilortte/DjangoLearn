from django.conf.urls import patterns, include, url
#from views import current_datetime, hours_ahead ,  saludador 
#from books.views import busqueda , busqueda2 , formss
from django.views.generic.simple import direct_to_template
from django.conf import settings
#import books , views    
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from books.views import AboutView
from django.views.generic import ListView
from books.models import Autor



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proyecto1.views.home', name='home'),
    # url(r'^Proyecto1/', include('Proyecto1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', 'views.current_datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'views.hours_ahead'),
    url(r'^saludame/$', 'views.saludador'),    
    url(r'^busqueda/$', 'books.views.busqueda'),
    url(r'^busqueda2/$', 'books.views.busqueda2'),
    url(r'^formu/$', 'books.views.formss'),
    url(r'^about/$', direct_to_template,{'template':'about.html'}), #Directamente
    url(r'^about2/', AboutView.as_view()),
    (r'^autor/$', ListView.as_view(
        model=Autor,template_name="autor.html",
    )),
)
