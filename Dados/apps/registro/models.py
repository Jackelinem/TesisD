from django.db import models
# Create your models here.

from django.db import models
from django.utils import timezone
from django.urls import reverse

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    confirmpass = models.CharField(max_length=50)

#tabla estudiante

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    GENERO_OPCS = (
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
    )
    genero = models.CharField(max_length=50, blank=True, null=True,
                              choices=GENERO_OPCS, default=None,)
    email = models.EmailField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    confirmpass = models.CharField(max_length=50)
    def __str__(self):
        return'{} {}'.format(self.nombre, self.apellido)


#tabla curso
class Curso(models.Model):
    CURSO_OPCS = (
        ('PRIMERO', '1'),
        ('SEGUNDO', '2'),
        ('TERCERO', '3'),
        ('CUARTO', '4'),
        ('QUINTO', '5'),
        ('SEXTO', '6'),
        ('SEPTIMO', '7'),
    )
    nombre = models.CharField(max_length=50, blank=True, null=True,
                              choices=CURSO_OPCS, default=None, )
    PARALELO_OPCS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    descripcion = models.CharField(max_length=50,blank=True, null=True,
                                   choices=PARALELO_OPCS, default=None,)

    def __str__(self):
        return'{} {}'.format(self.nombre, self.descripcion)

#tabla anio lectivo
class AnioLectivo(models.Model):
    anioLectivoInicio= models.DateField(blank=True, null=True)
    anioLectivoFin= models.DateField(blank=True, null=True)
    def __str__(self):
        return'{} {}'.format(self.anioLectivoInicio, self.anioLectivoFin)

#Agregar un estudiante a un Curso
class EstudianteCurso(models.Model):
    cupos = models.IntegerField()
    codigo_alec = models.ForeignKey(AnioLectivo, on_delete=models.CASCADE)
    codigo_est = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    codigo_profe = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    codigo_cur = models.ForeignKey(Curso, on_delete=models.CASCADE)

#Tipo de preguntas
class TipoPregunta(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return'{}'.format(self.tipo)


#tabla Evaluacion
class Evalucion(models.Model):
    descripcion = models.CharField(max_length=255)
    def __str__(self):
        return'{}'.format(self.descripcion)




#tabla pregunta
class Pregunta(models.Model):

    pregunta = models.TextField(max_length=255)
    codigo_tip = models.ForeignKey(TipoPregunta, on_delete=models.CASCADE)
    codigo_eval = models.ForeignKey(Evalucion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pregunta'

    #def get_absolute_url(self):
       #return reverse('registro:preguntas-update', kwargs={'pk': self.pk})

    def get_respuestas(self):
        return','.join(self.preguntas.all().values_list('pregunta', flat=True))

    def __str__(self):
        return self.pregunta

#Tabla de respuestas
class Respuesta(models.Model):
    VALIDACION_OPCS = (
        ('Correcto', 'Correcto'),
        ('Incorrecto', 'Incorrecto'),)


    respuesta = models.CharField(max_length=255)
    validacion = models.CharField(max_length=10, blank=True, null=True,
                              choices=VALIDACION_OPCS, default=None,)
    codigo_pre = models.ForeignKey(
        Pregunta,
        related_name='respuestas',
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'respuesta'

    def __str__(self):
        return self.pregunta


class Historial (models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    codigo_pre = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    codigo_est_cur =models.ForeignKey(EstudianteCurso, on_delete=models.CASCADE)

#***********************************************#

class Profile(models.Model):
    question = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    evaluacion = models.ForeignKey(Evalucion, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoPregunta, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('registro:profile-update', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.question, self.tipo)


class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answers = models.CharField(max_length=100)
    validation = models.CharField(max_length=100)
