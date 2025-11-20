from django.contrib import admin
from .models import Docente, Estudiante, Curso, Materia, Inscripcion


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'documento', 'email', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombres', 'apellidos', 'documento', 'email')


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'codigo', 'documento', 'curso_actual', 'activo')
    list_filter = ('curso_actual', 'activo')
    search_fields = ('nombres', 'apellidos', 'codigo', 'documento', 'email')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'anio', 'director_grupo', 'activo')
    list_filter = ('anio', 'activo')
    search_fields = ('nombre',)
    ordering = ('-anio', 'nombre')


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'curso', 'docente', 'activo')
    list_filter = ('curso', 'activo')
    search_fields = ('nombre', 'codigo')


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_inscripcion', 'activo')
    list_filter = ('curso', 'activo')
    search_fields = ('estudiante__nombres', 'estudiante__apellidos', 'estudiante__codigo')
