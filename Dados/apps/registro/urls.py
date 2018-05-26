
from . import views

from django.urls import path, include
from django.conf.urls import url
from apps.registro.views import index, registro

""" nombre del url y el otro parametro esla vista"""

app_name = 'registro'

urlpatterns = [
    path('index/', index, name='index'),

]
