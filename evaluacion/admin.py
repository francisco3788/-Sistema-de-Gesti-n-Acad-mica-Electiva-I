# evaluacion/admin.py
from django.contrib import admin
from .models import Calificacion, Asistencia


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'materia', 'periodo', 'nota', 'docente', 'fecha_registro')
    list_filter = ('periodo', 'materia', 'docente')
    search_fields = (
        'estudiante__nombres', 'estudiante__apellidos', 'estudiante__codigo',
        'materia__nombre'
    )


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'materia', 'fecha', 'presente')
    list_filter = ('materia', 'fecha', 'presente')
    search_fields = (
        'estudiante__nombres', 'estudiante__apellidos', 'estudiante__codigo',
        'materia__nombre'
    )
