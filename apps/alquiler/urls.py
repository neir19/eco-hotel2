from django.conf.urls import url
from apps.alquiler.views import index, AlquilerList, AlquilerCreate,  AlquilerUpdate, AlquilerDelete, RegistradorList, RegistradorCreate, RegistradorUpdate, RegistradorDelete

urlpatterns =[
  url(r'^$',index),
  url(r'^listar/', AlquilerList.as_view(), name='Alquiler_listar'),
  url(r'^form/', AlquilerCreate.as_view(), name='Alquiler_crear'),
  url(r'^editar/(?P<pk>\d+)', AlquilerUpdate.as_view(), name='Alquiler_editar'),
  url(r'^eliminar/(?P<pk>\d+)', AlquilerDelete.as_view(), name='Alquiler_eliminar'),
  url(r'^Rform/', RegistradorCreate.as_view(), name='Registrador_crear'),
  url(r'^Rlistar/', RegistradorList.as_view(), name='Registrador_listar'),
  url(r'^Reditar/(?P<pk>\d+)', RegistradorUpdate.as_view(), name='Registrador_editar'),
  url(r'^Reliminar/(?P<pk>\d+)', RegistradorDelete.as_view(), name='Registrador_eliminar'),

]