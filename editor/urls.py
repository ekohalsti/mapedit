from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^palvelut.json$', views.palvelut_json, name='palvelut_json'),
]
