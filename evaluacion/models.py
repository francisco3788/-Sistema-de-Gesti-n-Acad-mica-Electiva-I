# evaluacion/models.py
from django.db import models
from academico.models import Estudiante, Materia, Docente


class Calificacion(models.Model):
    PERIODO_CHOICES = (
        ('P1', 'Periodo 1'),
        ('P2', 'Periodo 2'),
        ('P3', 'Periodo 3'),
        ('FIN', 'Final'),
    )

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='calificaciones'
    )
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name='calificaciones'
    )
    docente = models.ForeignKey(
        Docente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='calificaciones'
    )
    periodo = models.CharField(max_length=3, choices=PERIODO_CHOICES, default='P1')
    nota = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Escala 0.0 a 5.0"
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        unique_together = ('estudiante', 'materia', 'periodo')
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.estudiante} - {self.materia} ({self.periodo})"


class Asistencia(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='asistencias'
    )
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name='asistencias'
    )
    fecha = models.DateField()
    presente = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        unique_together = ('estudiante', 'materia', 'fecha')
        ordering = ['-fecha']

    def __str__(self):
        estado = "Presente" if self.presente else "Ausente"
        return f"{self.estudiante} - {self.materia} - {self.fecha} ({estado})"
