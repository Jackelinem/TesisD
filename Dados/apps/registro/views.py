from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  ProfesorForm
from  .models import Profesor

# Create your views here.
def index(request):
    return render(request,'index.html')

def registrarProfesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            print("save")
        return redirect('registro:index')
    else:
        form = ProfesorForm()
    return render(request,'test.html',{'formProfesor':ProfesorForm})

def listarProfesores(request):
    profesor= Profesor.objects.all()
    contexto ={'profesores': profesor}
    return render (request,'listarProfesores.html',contexto)


def profesorEditar(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method=='GET':
        form = ProfesorForm(instance=profesor)
    else:
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
        return redirect('registro:listarProfesor')
    return render(request, 'test.html',{'formProfesor': form})



def login(request):
    return render(request,'login' )
