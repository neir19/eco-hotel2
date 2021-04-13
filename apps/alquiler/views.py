from django.shortcuts import render
from django.http import HttpResponse
from apps.alquiler.models import Alquiler, Registrador,Estado
from apps.alquiler.form import AlquilerForm, RegistradorForm,EstadoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    return HttpResponse("index")

class AlquilerList(ListView):
    model=Alquiler
    template_name='alquiler/alquileer_list.html'

class AlquilerCreate(CreateView):
    model=Alquiler
    form_class = AlquilerForm
    template_name='alquiler/alquiler_form.html'
    success_url = reverse_lazy('Alquiler_listar')

class AlquilerUpdate(UpdateView):
    model=Alquiler
    form_class = AlquilerForm
    template_name='alquiler/alquiler_form.html'
    success_url = reverse_lazy('Alquiler_listar')

class AlquilerDelete(DeleteView):
    model=Alquiler
    template_name='alquiler/alquiler_delete.html'
    success_url = reverse_lazy('Alquiler_listar')

#REGISTRADOR

class RegistradorList(ListView):
    model=Registrador
    template_name='alquiler/registrador_list.html'

class RegistradorCreate(CreateView):
    model=Registrador
    form_class = RegistradorForm
    template_name='alquiler/alquiler_form.html'
    success_url = reverse_lazy('Registrador_listar')

class RegistradorUpdate(UpdateView):
    model=Registrador
    form_class = RegistradorForm
    template_name='alquiler/alquileer_form.html'
    success_url = reverse_lazy('Registrador_listar')

class RegistradorDelete(DeleteView):
    model=Registrador
    template_name='alquiler/registrador_delete.html'
    success_url = reverse_lazy('Registrador_listar')

class EstadoList(ListView):
    model=Estado
    template_name='alquiler/estado_list.html'
class EstadoCrear(CreateView):
    model=Estado
    form_class = EstadoForm
    template_name='alquiler/alquiler_form.html'
    success_url = reverse_lazy('Estado_listar')
class EstadoUpdate(UpdateView):
    model=Estado
    form_class = EstadoForm
    template_name='alquiler/alquiler_form.html'
    success_url = reverse_lazy('Estado_listar')
class EstadoDelete(DeleteView):
    model=Estado
    template_name='alquiler/Estado_delete.html'
    success_url = reverse_lazy('Estado_listar')  

