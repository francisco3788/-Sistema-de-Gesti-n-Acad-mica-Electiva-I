# academico/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Estudiantes
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('estudiantes/nuevo/', views.estudiante_create, name='estudiante_create'),
    path('estudiantes/<int:pk>/editar/', views.estudiante_update, name='estudiante_update'),
    path('estudiantes/<int:pk>/eliminar/', views.estudiante_delete, name='estudiante_delete'),

    # Docentes
    path('docentes/', views.docente_list, name='docente_list'),
    path('docentes/nuevo/', views.docente_create, name='docente_create'),
    path('docentes/<int:pk>/editar/', views.docente_update, name='docente_update'),
    path('docentes/<int:pk>/eliminar/', views.docente_delete, name='docente_delete'),

    # Cursos
    path('cursos/', views.curso_list, name='curso_list'),
    path('cursos/nuevo/', views.curso_create, name='curso_create'),
    path('cursos/<int:pk>/editar/', views.curso_update, name='curso_update'),
    path('cursos/<int:pk>/eliminar/', views.curso_delete, name='curso_delete'),

    # Materias
    path('materias/', views.materia_list, name='materia_list'),
    path('materias/nuevo/', views.materia_create, name='materia_create'),
    path('materias/<int:pk>/editar/', views.materia_update, name='materia_update'),
    path('materias/<int:pk>/eliminar/', views.materia_delete, name='materia_delete'),

    # Inscripciones
    path('inscripciones/', views.inscripcion_list, name='inscripcion_list'),
    path('inscripciones/nuevo/', views.inscripcion_create, name='inscripcion_create'),
    path('inscripciones/<int:pk>/eliminar/', views.inscripcion_delete, name='inscripcion_delete'),
]
