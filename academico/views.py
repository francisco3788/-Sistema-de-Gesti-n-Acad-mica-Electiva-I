# academico/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Estudiante, Docente, Curso, Materia, Inscripcion
from .forms import (
    EstudianteForm, DocenteForm, CursoForm,
    MateriaForm, InscripcionForm
)


# --------- ESTUDIANTES ---------
@login_required
def estudiante_list(request):
    query = request.GET.get('q')
    estudiantes = Estudiante.objects.all()

    if query:
        estudiantes = estudiantes.filter(
            Q(nombres__icontains=query) |
            Q(apellidos__icontains=query) |
            Q(codigo__icontains=query) |
            Q(documento__icontains=query)
        )

    return render(request, 'academico/estudiante_list.html', {
        'estudiantes': estudiantes,
        'query': query,
    })


@login_required
def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante creado correctamente.')
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    return render(request, 'academico/estudiante_form.html', {'form': form})


@login_required
def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante actualizado correctamente.')
            return redirect('estudiante_list')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'academico/estudiante_form.html', {'form': form})


@login_required
def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        messages.success(request, 'Estudiante eliminado correctamente.')
        return redirect('estudiante_list')
    return render(request, 'academico/confirm_delete.html', {
        'obj': estudiante,
        'tipo': 'Estudiante',
    })


# --------- DOCENTES ---------
@login_required
def docente_list(request):
    docentes = Docente.objects.all()
    return render(request, 'academico/docente_list.html', {
        'docentes': docentes,
    })


@login_required
def docente_create(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docente creado correctamente.')
            return redirect('docente_list')
    else:
        form = DocenteForm()
    return render(request, 'academico/docente_form.html', {'form': form})


@login_required
def docente_update(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docente actualizado correctamente.')
            return redirect('docente_list')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'academico/docente_form.html', {'form': form})


@login_required
def docente_delete(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        messages.success(request, 'Docente eliminado correctamente.')
        return redirect('docente_list')
    return render(request, 'academico/confirm_delete.html', {
        'obj': docente,
        'tipo': 'Docente',
    })


# --------- CURSOS ---------
@login_required
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'academico/curso_list.html', {
        'cursos': cursos,
    })


@login_required
def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso creado correctamente.')
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'academico/curso_form.html', {'form': form})


@login_required
def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso actualizado correctamente.')
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'academico/curso_form.html', {'form': form})


@login_required
def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado correctamente.')
        return redirect('curso_list')
    return render(request, 'academico/confirm_delete.html', {
        'obj': curso,
        'tipo': 'Curso',
    })


# --------- MATERIAS ---------
@login_required
def materia_list(request):
    materias = Materia.objects.select_related('curso', 'docente')
    return render(request, 'academico/materia_list.html', {
        'materias': materias,
    })


@login_required
def materia_create(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Materia creada correctamente.')
            return redirect('materia_list')
    else:
        form = MateriaForm()
    return render(request, 'academico/materia_form.html', {'form': form})


@login_required
def materia_update(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Materia actualizada correctamente.')
            return redirect('materia_list')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'academico/materia_form.html', {'form': form})


@login_required
def materia_delete(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        materia.delete()
        messages.success(request, 'Materia eliminada correctamente.')
        return redirect('materia_list')
    return render(request, 'academico/confirm_delete.html', {
        'obj': materia,
        'tipo': 'Materia',
    })


# --------- INSCRIPCIONES ---------
@login_required
def inscripcion_list(request):
    inscripciones = Inscripcion.objects.select_related('estudiante', 'curso')
    return render(request, 'academico/inscripcion_list.html', {
        'inscripciones': inscripciones,
    })


@login_required
def inscripcion_create(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscripción creada correctamente.')
            return redirect('inscripcion_list')
    else:
        form = InscripcionForm()
    return render(request, 'academico/inscripcion_form.html', {'form': form})


@login_required
def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        messages.success(request, 'Inscripción eliminada correctamente.')
        return redirect('inscripcion_list')
    return render(request, 'academico/confirm_delete.html', {
        'obj': inscripcion,
        'tipo': 'Inscripción',
    })
