
from . import views

from django.urls import path, include
from django.conf.urls import url
from .views import index, registrarProfesor, login, listarProfesores, profesorEditar

""" nombre del url y el otro parametro esla vista"""

app_name = 'registro'

urlpatterns = [
    path('',index, name='index'),
    path('registrar',registrarProfesor, name='registrar'),
    path('listar', listarProfesores, name='listarProfesor'),

    path('login',login, name='login'),

]
