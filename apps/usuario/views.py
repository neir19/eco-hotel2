from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


from apps.usuario.forms import RegistroForm

# Create your views here.
class RegistroUsuario(CreateView):
  model = User
  template_name = 'usuario/registrar.htm'
  form_class = RegistroForm
  succes_url = reverse_lazy('huesped_listar')
