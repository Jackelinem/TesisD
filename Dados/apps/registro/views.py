from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ProfesorForm
from .models import Profesor
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse


# Create your views here.
def home(request):
    return render(request, 'home.html')

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
