from django.conf.urls import url
from apps.alquiler.views import index, AlquilerList, AlquilerCreate,  AlquilerUpdate, AlquilerDelete, RegistradorList, RegistradorCreate, RegistradorUpdate, RegistradorDelete,EstadoList, EstadoCrear,EstadoUpdate, EstadoDelete

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
  url(r'^estadolistar/', EstadoList.as_view(), name='Estado_listar'),
  url(r'^estadoform/', EstadoCrear.as_view(), name='Estado_crear'),
   url(r'^Estadoeditar/(?P<pk>\d+)', EstadoUpdate.as_view(), name='Estado_editar'),
  url(r'^estadoeliminar/(?P<pk>\d+)', EstadoDelete.as_view(),name='Estado_eliminar'), 
]