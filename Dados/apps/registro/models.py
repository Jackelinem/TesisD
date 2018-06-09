from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    confirmpass = models.CharField(max_length=50)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    confirmpass = models.CharField(max_length=50)

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class AnioLectivo(models.Model):
    anioLectivo= models.DateField()

class EstudianteCurso(models.Model):
    cupos = models.IntegerField()
    codigo_alec = models.ForeignKey(AnioLectivo, on_delete=models.CASCADE)
    codigo_est = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    codigo_profe = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    codigo_cur = models.ForeignKey(Curso, on_delete=models.CASCADE)

class TipoPregunta(models.Model):
    tipo = models.CharField(max_length=50)

class Evalucion(models.Model):
    descripcion = models.CharField(max_length=255)

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    codigo_tip = models.ForeignKey(TipoPregunta, on_delete=models.CASCADE)
    codigo_eval = models.ForeignKey(Evalucion, on_delete=models.CASCADE)

class Respuesta(models.Model):
    respuesta = models.CharField(max_length=255)
    validacion = models.CharField(max_length=50)
    codigo_pre = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

class Historial (models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    codigo_pre = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    codigo_est_cur =models.ForeignKey(EstudianteCurso, on_delete=models.CASCADE)



