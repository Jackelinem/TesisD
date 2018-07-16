from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import formset_factory
from django.template import RequestContext
from django.forms.formsets import formset_factory
from django.views import View
from .forms import ProfesorForm, EstudiantesForm, CursoForm,AnioLectivoForm,\
    TipoPreguntaForm, EvaluacionForm, PreguntasForm ,RespuestasForm, RespuestasFormset

from .models import Profesor,Pregunta,Respuesta, Estudiante,Curso, AnioLectivo
from django.urls import reverse_lazy, reverse
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .forms import (BookModelForm,AuthorFormset)

#****************************************************
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Profile
from .forms import FamilyMemberFormSet


class ProfileList(ListView):
    model = Profile


class ProfileCreate(CreateView):
    model = Profile
    fields = ['question', 'tipo','evaluacion']


class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    fields = ['question', 'tipo','evaluacion']
    success_url = reverse_lazy('registro:profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Profile
    success_url = '/'
    fields = ['question', 'tipo','evaluacion']


class ProfileFamilyMemberUpdate(UpdateView):
    model = Profile
    fields = ['question', 'tipo','evaluacion']
    success_url = reverse_lazy('registro:profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST, instance=self.object)
        else:
            data['familymembers'] = FamilyMemberFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberUpdate, self).form_valid(form)


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-list')






































# Create your views here.
def home(request):
    return render(request, 'home.html')


class PreguntasList(ListView):
    model = Pregunta


class PreguntasCreate (CreateView):
    model= Pregunta
    fields = ['pregunta','codigo_tip','codigo_eval']

#RespuestasFormset
class PreguntasyRespuestas(CreateView):
    model = Pregunta
    fields = ['pregunta','codigo_tip','codigo_eval']
    success_url = reverse_lazy('registro:estudiantes')

    def get_context_data(self, **kwargs):

        data = super(PreguntasyRespuestas, self).get_context_data(**kwargs)
        if self.request.POST:
            data['answers'] = RespuestasFormset(self.request.POST)
        else:
            data['answers'] = RespuestasFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        answers = context['answers']
        with transaction.atomic():
            self.object = form.save()

            if answers.is_valid():
                answers.instance = self.object
                answers.save()
        return super(PreguntasyRespuestas, self).form_valid(form)


class PreguntasUpdate(UpdateView):
    model = Pregunta
    success_url = '/'
    fields = ['pregunta','codigo_tip','codigo_eval']




class PreguntasyRespuestasUpdate(UpdateView):
    model = Pregunta
    fields = ['pregunta','codigo_tip','codigo_eval']
    success_url = reverse_lazy('registro:estudiantes')

    def get_context_data(self, **kwargs):
        data = super(PreguntasyRespuestasUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['answers'] = RespuestasFormset(self.request.POST, instance=self.object)
        else:
            data['answers'] = RespuestasFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        answers = context['answers']
        with transaction.atomic():
            self.object = form.save()

            if answers.is_valid():
                answers.instance = self.object
                answers.save()
        return super(PreguntasyRespuestasUpdate, self).form_valid(form)



def create_book_with_authors(request):

    template_name = 'registrarPreguntas.html'
    if request.method == 'GET':
        bookform = BookModelForm(request.GET or None)
        formset = AuthorFormset(queryset=Respuesta.objects.none())

    elif request.method == 'POST':
        print('jsjak')
        bookform = BookModelForm(request.POST)
        formset = AuthorFormset(request.POST)
        if bookform.is_valid() and formset.is_valid():
            # first save this pregunta, as its reference will be used in `respuestas`


            pregunta = bookform.save()
            for form in formset:
                respuesta = form.save(commit=False)

                respuesta.pregunta = pregunta

                respuesta.save()
                def __str__(self):
                    return str(self.respuesta)
            return redirect('registro:estudiantes')
    return render(request, template_name, {
        'bookform': bookform,
        'formset': formset,
    })
























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


#Registro de nuevas preguntas

def registrarPreguntas(request):

    if request.method == 'POST':

        form = PreguntasForm(request.POST)
        if form.is_valid() :
            form.save()
        return HttpResponseRedirect(reverse('registro:listarProfesor'))
    else:
        form = PreguntasForm()
    return render(request, 'registrarPreguntas.html', {'formPreguntas': PreguntasForm})



def registrarRespuestas(request):

    #template_name = 'registrarRespuestas.html'
    #heading_message = 'Formset Demo'


    #if request.method == 'GET':

    formset = RespuestasFormset
    if request.method=='POST':

        formset = RespuestasFormset(request.POST)
        if formset.is_valid():
            respuestas = formset.save(commit=False)

            for respuesta in respuestas:
                respuesta.save()
                #respuesta =  form.cleaned_data.get('respuesta')

                #

                #codigo_pre =  form.cleaned_data.get('codigo_pre')
                #if respuesta:
                   # Respuesta(respuesta=respuesta).save()

                #if validacion:
                 #   Respuesta(validacion=validacion).save()
               # if codigo_pre:
                   # Respuesta(codigo_pre=codigo_pre).save()
        return redirect(reverse('registro:listarProfesor'))
                #respuesta = form.cleaned_data.get('respuesta')

    return render(request, 'registrarRespuestas.html', {'formset': formset})







def create_book_normal(request):
    template_name = 'registrarRespuestas.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = RespuestasFormset(request.GET or None)
    elif request.method == 'POST':

        formset = RespuestasFormset(request.POST)
        print('formSet')
        if formset.is_valid():
            print('is_valid')
            for form in formset:
                respuesta = form.cleaned_data.get('respuesta')

                validacion = form.cleaned_data.get('validacion')

                codigo_pre = form.cleaned_data.get('codigo_pre')
                # save book instance
                if respuesta:
                    Respuesta(respuesta=respuesta).save()
                if validacion:
                    Respuesta(validacion=validacion).save()
                if codigo_pre:
                    Respuesta(codigo_pre=codigo_pre).save()

            return redirect('registro:listarProfesor')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


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
