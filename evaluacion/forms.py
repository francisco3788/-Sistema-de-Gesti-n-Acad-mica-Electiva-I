# evaluacion/forms.py
from django import forms
from .models import Calificacion, Asistencia


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'materia', 'periodo', 'nota', 'observaciones']


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['estudiante', 'materia', 'fecha', 'presente', 'observaciones']
