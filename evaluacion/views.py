# evaluacion/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from accounts.models import PerfilUsuario
from .models import Calificacion, Asistencia
from .forms import CalificacionForm, AsistenciaForm


def _usuario_es_docente_o_admin(user):
    perfil = getattr(user, 'perfil', None)
    return perfil and perfil.rol in ('ADMIN', 'DOCENTE')


# --------- CALIFICACIONES ---------
@login_required
def calificacion_list(request):
    if not _usuario_es_docente_o_admin(request.user):
        messages.error(request, 'No tienes permiso para ver calificaciones.')
        return redirect('home')

    query = request.GET.get('q')
    calificaciones = Calificacion.objects.select_related('estudiante', 'materia')

    if query:
        calificaciones = calificaciones.filter(
            Q(estudiante__nombres__icontains=query) |
            Q(estudiante__apellidos__icontains=query) |
            Q(estudiante__codigo__icontains=query) |
            Q(materia__nombre__icontains=query)
        )

    return render(request, 'evaluacion/calificacion_list.html', {
        'calificaciones': calificaciones,
        'query': query,
    })


@login_required
def calificacion_create(request):
    if not _usuario_es_docente_o_admin(request.user):
        messages.error(request, 'No tienes permiso para registrar calificaciones.')
        return redirect('home')

    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            calificacion = form.save(commit=False)
            # Asignar docente automáticamente si tiene perfil de docente
            perfil = getattr(request.user, 'perfil', None)
            if perfil and perfil.rol == 'DOCENTE' and hasattr(request.user, 'docente'):
                calificacion.docente = request.user.docente
            calificacion.save()
            messages.success(request, 'Calificación registrada correctamente.')
            return redirect('calificacion_list')
    else:
        form = CalificacionForm()
    return render(request, 'evaluacion/calificacion_form.html', {'form': form})


@login_required
def calificacion_update(request, pk):
    if not _usuario_es_docente_o_admin(request.user):
        messages.error(request, 'No tienes permiso para editar calificaciones.')
        return redirect('home')

    calificacion = get_object_or_404(Calificacion, pk=pk)

    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calificación actualizada correctamente.')
            return redirect('calificacion_list')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'evaluacion/calificacion_form.html', {'form': form})


@login_required
def calificacion_delete(request, pk):
    if not _usuario_es_docente_o_admin(request.user):
        messages.error(request, 'No tienes permiso para eliminar calificaciones.')
        return redirect('home')

    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        messages.success(request, 'Calificación eliminada correctamente.')
        return redirect('calificacion_list')
    return render(request, 'evaluacion/confirm_delete.html', {
        'obj': calificacion,
        'tipo': 'Calificación',
    })


# --------- ASISTENCIAS ---------
@login_required
def asistencia_list(request):
    if not _usuario_es_docente_o_admin(request.user):
        messages.error(request, 'No tienes permiso para ver asistencias.')
        return redirect('home')

    query = request.GET.get('q')
    asistencias = Asistencia.objects.select_related('estudiante', 'materia')

    if query:
        asistencias = asistencias.filter(
            Q(estudiante__nombres__icontains=query) |
            Q(estudiante__apellidos__icontains=query) |
            Q(estudiante__codigo__icontains=query) |
            Q(materia__nombre__icontains=query)
        )

    return render(request, 'evaluacion/asistencia_list.html', {
        'asistencias': asistencias,
        'query': query,
    })


@login_required
def asistencia_create(request):
    if not _usuario_es_docente_o_admin(request.user):
        messages.error(request, 'No tienes permiso para registrar asistencias.')
        return redirect('home')

    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asistencia registrada correctamente.')
            return redirect('asistencia_list')
    else:
        form = AsistenciaForm()
    return render(request, 'evaluacion/asistencia_form.html', {'form': form})


@login_required
def asistencia_update(request, pk):
    if not _usuario_es_docente_o_admin(request.user):
        messages.error(request, 'No tienes permiso para editar asistencias.')
        return redirect('home')

    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asistencia actualizada correctamente.')
            return redirect('asistencia_list')
    else:
        form = AsistenciaForm(instance=asistencia)
    return render(request, 'evaluacion/asistencia_form.html', {'form': form})


@login_required
def asistencia_delete(request, pk):
    if not _usuario_es_docente_o_admin(request.user):
        messages.error(request, 'No tienes permiso para eliminar asistencias.')
        return redirect('home')

    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        asistencia.delete()
        messages.success(request, 'Asistencia eliminada correctamente.')
        return redirect('asistencia_list')
    return render(request, 'evaluacion/confirm_delete.html', {
        'obj': asistencia,
        'tipo': 'Asistencia',
    })
