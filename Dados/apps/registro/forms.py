from django import forms
from django.forms import inlineformset_factory, ModelForm
from .models import (
    Profesor, Estudiante, Curso,
    AnioLectivo,TipoPregunta,Evalucion,
    )

from .models import Preguntas, Respuestas


#Formulario de las preguntas
class PreguntasForm(ModelForm):
    class Meta:
        model = Preguntas
        exclude = ()

#Formulario de las respuestas
class RespuestasForm(ModelForm):
    class Meta:
        model = Respuestas
        exclude = ()

RespuestasFormSet = inlineformset_factory(Preguntas, Respuestas,
                                            form=RespuestasForm, extra=1)

#Formulario del profesor
class ProfesorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        required=False,
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y',
                               attrs={'class': 'form-control', 'placeholder': 'dd-mm-AAAA (Ej. 01-01-1995)',
                                      'id': 'datetime-input', 'tabindex': '1'}))
    class Meta:
        model=Profesor
        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'genero',
            'email',
            'contrasenia',
            'confirmpass',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha_nacimiento': 'Fecha nacimiento',
            'genero': 'Genero',
            'email': 'Email',
            'contrasenia': 'Contrasenia',
            'confirmpass': 'Confimar contrasenia',
        }
        widgest = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.CheckboxSelectMultiple(),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'contrasenia': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirmpass': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

#Formulario del estudiante
class EstudiantesForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        required=False,
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y',
                               attrs={'class': 'form-control', 'placeholder': 'dd-mm-AAAA (Ej. 01-01-1995)',
                                      'id': 'datetime-input', 'tabindex': '1'}))
    class Meta:
        model=Estudiante

        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'genero',
            'email',
            'contrasenia',
            'confirmpass',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha_nacimiento':'fecha_nacimiento',
            'genero': 'Genero',
            'email': 'Email',
            'contrasenia': 'Contrasenia',
            'confirmpass': 'Confimar contrasenia',
        }
        widgest = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control style-select', 'tabindex':'1'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'contrasenia': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirmpass': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

#Formlario del curso
class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso

        fields = [
            'nombre',
            'descripcion',
            ]

        labels = {
            'nombre':'Curso:',
            'descripcion':'Paralelo:'
        }

        widgest ={

            'nombre': forms.Select(attrs={'class': 'form-control style-select', 'tabindex': '1'}),
            'descripcion':forms.Select(attrs={'class': 'form-control style-select', 'tabindex': '2'}),
        }

#Formulario del anio lectivo
class AnioLectivoForm(forms.ModelForm):
    anioLectivoInicio = forms.DateField(
        label='Inicio del periodo escolar',
        required=False,
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y',
                               attrs={'class': 'form-control', 'placeholder': 'dd-mm-AAAA (Ej. 01-01-1995)',
                                      'id': 'datetime-input', 'tabindex': '1'}))
    anioLectivoFin = forms.DateField(
        label='Fin del periodo escolar',
        required=False,
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y',
                               attrs={'class': 'form-control', 'placeholder': 'dd-mm-AAAA (Ej. 01-01-1995)',
                                      'id': 'datetime-input', 'tabindex': '2'}))
    class Meta:
        model = AnioLectivo
        fields = "__all__"

#Formulario tipo pregunta
class TipoPreguntaForm(forms.ModelForm):
 class Meta:
        model = TipoPregunta
        fields = "__all__"

#Formulario de la evalucion
class EvaluacionForm(forms.ModelForm):
 class Meta:
        model = Evalucion
        fields = "__all__"

