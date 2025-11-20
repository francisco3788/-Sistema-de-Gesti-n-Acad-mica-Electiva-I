# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    ROL_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('DOCENTE', 'Docente'),
        ('ESTUDIANTE', 'Estudiante'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='ESTUDIANTE')

    def __str__(self):
        return f"{self.user.username} ({self.get_rol_display()})"
