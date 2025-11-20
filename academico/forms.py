# academico/forms.py
from django import forms
from .models import Estudiante, Docente, Curso, Materia, Inscripcion


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'codigo', 'nombres', 'apellidos', 'documento',
            'fecha_nacimiento', 'email', 'telefono', 'curso_actual', 'activo'
        ]


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = [
            'nombres', 'apellidos', 'documento',
            'email', 'telefono', 'activo'
        ]


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'nombre', 'anio', 'descripcion',
            'director_grupo', 'activo'
        ]


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = [
            'nombre', 'codigo', 'curso',
            'docente', 'intensidad_horaria', 'activo'
        ]


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'activo']
