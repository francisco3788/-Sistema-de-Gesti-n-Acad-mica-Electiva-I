# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm

@login_required
def home(request):
    perfil = getattr(request.user, 'perfil', None)
    return render(request, 'accounts/home.html', {
        'perfil': perfil,
    })

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente. Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})
