from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='event.html'),
    url(r'^event/$', views.event, name='event.html'),
    url(r'^location/$', views.location, name='location.html'),
    url(r'^business/$', views.business, name='business.html'),
]
