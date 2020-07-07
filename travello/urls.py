from django.urls import path
from . import views 
urlpatterns = [
    path('' , views.index , name='index'),
    path('registro' , views.destinosRegister , name='registrarDestino'), #La vista para el registro del destino
    path('listar' , views.destinosLista , name='listarDestinos'), #La vista para listar los destinos
    path('editar/<int:id_destino>' , views.destinosEdit , name='editarRegistro'), #La vista para editar los destinos
]