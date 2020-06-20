from django.shortcuts import render
from .models import Destino

# Create your views here.
def index(request):
    dest1 = Destino()
    dest1.nombre = 'Peru'
    dest1.descripcion = 'Donde la gente come palomas.'
    dest1.precio = 10
    dest1.img = 'destination_1.jpg'
    
    dest2 = Destino()
    dest2.nombre = 'Arequipa'
    dest2.descripcion = 'Pais independiente.'
    dest2.precio = 15000
    dest2.img = 'destination_2.jpg'

    dest3 = Destino()
    dest3.nombre = 'Chile'
    dest3.descripcion = 'La wea fome culiao.'
    dest3.precio = 9000
    dest3.img = 'destination_3.jpg'
    
    destinos = [dest1 , dest2, dest3]

    return render(request , 'index.html' , {'destinos':destinos})