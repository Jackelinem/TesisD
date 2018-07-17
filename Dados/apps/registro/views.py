from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import formset_factory
from django.template import RequestContext
from django.forms.formsets import formset_factory
from django.views import View
from .forms import ProfesorForm, EstudiantesForm, CursoForm,AnioLectivoForm,\
    TipoPreguntaForm, EvaluacionForm

from .models import Profesor, Estudiante,Curso, AnioLectivo
from django.urls import reverse_lazy, reverse

#****************************************************
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Preguntas
from .forms import RespuestasFormSet

#*******CRUD de preguntas y Respuestas***

class PreguntasList(ListView):
    model = Preguntas


class PreguntasCreate(CreateView):
    model = Preguntas
    fields = ['question', 'tipo','evaluacion']


class RespuestasCreate(CreateView):
    model = Preguntas
    fields = ['question', 'tipo','evaluacion']
    success_url = reverse_lazy('registro:preguntas-list')

    def get_context_data(self, **kwargs):
        data = super(RespuestasCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['answers'] = RespuestasFormSet(self.request.POST)
        else:
            data['answers'] = RespuestasFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        answers = context['answers']
        with transaction.atomic():
            self.object = form.save()

            if answers.is_valid():
                answers.instance = self.object
                answers.save()
        return super(RespuestasCreate, self).form_valid(form)


class PreguntasUpdate(UpdateView):
    model = Preguntas
    success_url = '/'
    fields = ['question', 'tipo','evaluacion']


class RespuestasUpdate(UpdateView):
    model = Preguntas
    fields = ['question', 'tipo','evaluacion']
    success_url = reverse_lazy('registro:preguntas-list')

    def get_context_data(self, **kwargs):
        data = super(RespuestasUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['answers'] = RespuestasFormSet(self.request.POST, instance=self.object)
        else:
            data['answers'] = RespuestasFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        answers = context['answers']
        with transaction.atomic():
            self.object = form.save()

            if answers.is_valid():
                answers.instance = self.object
                answers.save()
        return super(RespuestasUpdate, self).form_valid(form)

class PreguntasDelete(DeleteView):
    model = Preguntas
    success_url = reverse_lazy('registro:preguntas-list')

























# Create your views here.
def home(request):
    return render(request, 'home.html')


#Registrar un nuevo estudiante
def registrarEstudiantes(request):
    if request.method == 'POST':
        form = EstudiantesForm(request.POST)
        if form.is_valid():
            form.save()
            print("save")
        return HttpResponseRedirect(reverse('registro:listarProfesor'))
    else:
        form = EstudiantesForm()
    return render(request, 'registrarEstudiantes.html', {'formEstudiantes': EstudiantesForm})


#Registrar un nuevo curso
def registrarCursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            print("save curso")
        return HttpResponseRedirect(reverse('registro:listarProfesor'))
    else:
        form = EstudiantesForm()
    return render(request, 'registrarCurso.html', {'formCursos': CursoForm})


#Registro de un nuevo anio lectivo
def registrarAnioLectivo(request):
    if request.method == 'POST':
        form = AnioLectivoForm(request.POST)
        if form.is_valid():
            form.save()
            print("save curso")
        return HttpResponseRedirect(reverse('registro:listarProfesor'))
    else:
        form = AnioLectivoForm()
    return render(request, 'registrarAnioLectivo.html', {'formAnioLectivo': AnioLectivoForm})


#Registro de nuevas categoria de preguntas
def registrarTipoPregunta(request):
    if request.method == 'POST':
        form = TipoPreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            print("save curso")
        return HttpResponseRedirect(reverse('registro:listarProfesor'))
    else:
        form = TipoPreguntaForm()
    return render(request, 'registrarTipoPreguntas.html', {'formTipoPregunta': TipoPreguntaForm})

#registro de una nueva evaluacion
def registrarEvaluacion(request):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
            print("save curso")
        return HttpResponseRedirect(reverse('registro:listarProfesor'))
    else:
        form = EvaluacionForm()
    return render(request, 'registrarEvaluacion.html', {'formEvaluacion': EvaluacionForm})


class registrarCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'registarCurso.html'
    success_url = reverse_lazy('listProfesores')


def registrarProfesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            print("save")
        return HttpResponseRedirect(reverse('registro:index'))
    else:
        form = ProfesorForm()
    return render(request, 'register.html', {'formProfesor': ProfesorForm})


def listarProfesores(request):
    profesor = Profesor.objects.all()
    contexto = {'profesores': profesor}
    return render(request, 'listarProfesores.html', contexto)


def profesorEditar(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'GET':
        form = ProfesorForm(instance=profesor)
    else:
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            print('estudiante guardado')
        return redirect('registro:listarProfesor')
    return render(request, 'test.html', {'formProfesor': form})


class ProfesoresList(ListView):
    model = Profesor
    template_name = 'listarProfesores.html'


class ProfesorCreate(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'test.html'
    success_url = reverse_lazy('listProfesores')


class ProfesorUpdate(UpdateView):
    model = Profesor
    template_name = 'test.html'
    success_url = reverse_lazy('listProfesores')
