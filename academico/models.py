from django.db import models
from django.contrib.auth.models import User


class Docente(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='docente'
    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"


class Curso(models.Model):
    nombre = models.CharField(
        max_length=50,
        help_text="Ej: 6A, 10B, 1er semestre Ingeniería"
    )
    anio = models.IntegerField(help_text="Año académico, ej: 2025")
    descripcion = models.TextField(blank=True)
    director_grupo = models.ForeignKey(
        Docente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cursos_dirigidos'
    )
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('nombre', 'anio')
        ordering = ['-anio', 'nombre']

    def __str__(self):
        return f"{self.nombre} - {self.anio}"


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='materias'
    )
    docente = models.ForeignKey(
        Docente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='materias'
    )
    intensidad_horaria = models.IntegerField(
        default=0,
        help_text="Horas semanales"
    )
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['curso', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.curso})"


class Estudiante(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='estudiante'
    )
    codigo = models.CharField(
        max_length=20,
        unique=True,
        help_text="Código interno del estudiante"
    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    curso_actual = models.ForeignKey(
        Curso,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='estudiantes'
    )
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.apellidos}, {self.nombres} ({self.codigo})"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha_inscripcion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('estudiante', 'curso')
        ordering = ['-fecha_inscripcion']

    def __str__(self):
        return f"{self.estudiante} en {self.curso}"
