from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.services.as_view(), name='Varsinaissuomen palvelut'),
    #url(r'^services$', views.services.as_view(), name='Varsinaissuomen palvelut'),
]
