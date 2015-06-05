from django import forms
#importar de git las librerias de validaciones de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationEmailForm(UserCreationForm):
    email = froms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')
