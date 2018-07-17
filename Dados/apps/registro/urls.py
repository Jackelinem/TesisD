from django.urls import path
from .views import home, registrarProfesor, listarProfesores,\
    registrarEstudiantes,registrarCursos, registrarAnioLectivo, \
    registrarEvaluacion, registrarTipoPregunta, ProfesorCreate
#from .users.views import  RegisterView, login
 #   ProfesoresList

from . import views
from django.conf.urls import url
""" nombre del url y el otro parametro esla vista"""

app_name = 'registro'

urlpatterns = [

    #urls para los registros
    path('registrar/',registrarProfesor, name='registrar'), #profesores
    path('estudiantes/', registrarEstudiantes, name='estudiantes'),#registrar estudiantes
    path('cursos/',registrarCursos, name='cursos'),# agregar cursos
    path('anioLectivo/',registrarAnioLectivo, name='anioLectivo'), #registrar nuevo anio lectivo
    path('tipoP/', registrarTipoPregunta, name='tipoP'),  # registrar nuevo anio lectivo
    path('evaluacion/', registrarEvaluacion, name='evaluacion'),  # registrar nueva evaluacion
    #path('preguntas/', registrarPreguntas, name='preguntas'),  # registrar nuevas preguntas
    #path('respuestas/', registrarRespuestas, name='respuestas'),  # registrar nuevas preguntas


    path('listar/', listarProfesores, name='listarProfesor'),
    #path('listarProfesores/', ProfesoresList.as_view(), name='listProfesores'),
    #path('createProfesor/', ProfesorCreate.as_view(), name='createProfesor'),
    #path('updateProfesor/<int:id>/', ProfesorUpdate.as_view(), name='updateProfesor'),


    #Urls para el crud de las preguntas y respuestas
    url(r'^$', views.PreguntasList.as_view(), name='preguntas-list'),
    path('preguntas/add', views.RespuestasCreate.as_view(), name='preguntas-add'),
    url(r'preguntas/(?P<pk>[0-9]+)/$', views.RespuestasUpdate.as_view(), name='preguntas-update'),
    url(r'preguntas/(?P<pk>[0-9]+)/delete/$', views.PreguntasDelete.as_view(), name='preguntas-delete'),


]
