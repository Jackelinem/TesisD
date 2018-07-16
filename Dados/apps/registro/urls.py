from django.urls import path
from .views import home, registrarProfesor, listarProfesores,\
    registrarEstudiantes,registrarCursos, registrarAnioLectivo, \
    registrarEvaluacion, registrarTipoPregunta, registrarPreguntas,\
    registrarRespuestas,create_book_normal, ProfesorCreate, PreguntasyRespuestas, create_book_with_authors
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
    path('preguntas/', registrarPreguntas, name='preguntas'),  # registrar nuevas preguntas
    path('respuestas/', registrarRespuestas, name='respuestas'),  # registrar nuevas preguntas

   # path('respuesta/', views.PreguntasyRespuestas.as_view(), name='questionsAnswers'),
    #url('preguntas-update/(?P<pk>[0-9]+)/$', views.PreguntasUpdate.as_view(), name='preguntas-update'),


    path('listar/', listarProfesores, name='listarProfesor'),
    #path('listarProfesores/', ProfesoresList.as_view(), name='listProfesores'),
    #path('createProfesor/', ProfesorCreate.as_view(), name='createProfesor'),
    #path('updateProfesor/<int:id>/', ProfesorUpdate.as_view(), name='updateProfesor'),

   # path('create', create_book_with_authors, name='create'),

    url(r'^$', views.ProfileList.as_view(), name='profile-list'),
    path('profile/add', views.ProfileFamilyMemberCreate.as_view(), name='profile-add'),
    url(r'profile/(?P<pk>[0-9]+)/$', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
    url(r'profile/(?P<pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),

]
