from django.urls import path
from . import views 
urlpatterns = [
    path('' , views.index , name='index'),
    path('registro' , views.destinosRegister , name='registrarDestino') #La vista para el registro del destino
]