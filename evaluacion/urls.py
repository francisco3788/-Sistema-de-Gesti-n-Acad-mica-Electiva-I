# evaluacion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Calificaciones
    path('calificaciones/', views.calificacion_list, name='calificacion_list'),
    path('calificaciones/nueva/', views.calificacion_create, name='calificacion_create'),
    path('calificaciones/<int:pk>/editar/', views.calificacion_update, name='calificacion_update'),
    path('calificaciones/<int:pk>/eliminar/', views.calificacion_delete, name='calificacion_delete'),

    # Asistencias
    path('asistencias/', views.asistencia_list, name='asistencia_list'),
    path('asistencias/nueva/', views.asistencia_create, name='asistencia_create'),
    path('asistencias/<int:pk>/editar/', views.asistencia_update, name='asistencia_update'),
    path('asistencias/<int:pk>/eliminar/', views.asistencia_delete, name='asistencia_delete'),
]
