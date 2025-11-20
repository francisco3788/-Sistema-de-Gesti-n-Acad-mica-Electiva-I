# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rol = forms.ChoiceField(choices=PerfilUsuario.ROL_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'rol', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            PerfilUsuario.objects.create(
                user=user,
                rol=self.cleaned_data['rol']
            )
        return user
