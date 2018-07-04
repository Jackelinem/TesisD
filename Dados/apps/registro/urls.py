

from django.urls import path
from .views import home, registrarProfesor, listarProfesores
#from .users.views import  RegisterView, login
 #   ProfesoresList, ProfesorCreate,


""" nombre del url y el otro parametro esla vista"""

app_name = 'registro'

urlpatterns = [



    path('registrar/',registrarProfesor, name='registrar'),
    path('listar/', listarProfesores, name='listarProfesor'),
    #path('listarProfesores/', ProfesoresList.as_view(), name='listProfesores'),
    #path('createProfesor/', ProfesorCreate.as_view(), name='createProfesor'),
    #path('updateProfesor/<int:id>/', ProfesorUpdate.as_view(), name='updateProfesor'),

]
