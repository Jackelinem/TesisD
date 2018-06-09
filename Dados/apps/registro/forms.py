from django import forms
from .models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model=Profesor

        fields = [
            'nombre',
            'apellido',
            'edad',
            'genero',
            'email',
            'contrasenia',
            'confirmpass',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Fecha nacimiento',
            'genero': 'Genero',
            'email': 'Email',
            'contrasenia': 'Contrasenia',
            'confirmpass': 'Confimar contrasenia',
        }
        widgest = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.CheckboxSelectMultiple(),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'contrasenia': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirmpass': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
