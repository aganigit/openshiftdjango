from django.conf.urls import patterns, include, url
from django.conf import settings

from contact_form import views, forms

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'francichef.views.home', name='home'),
    url(r'^', include('sito.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include("contact_form.urls", namespace="contact_form")),
)

if settings.DEBUG:  
        urlpatterns += patterns('',  
                                #REMOVE IT in production phase  
                                (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
                                {'document_root': settings.MEDIA_ROOT})
                              )
