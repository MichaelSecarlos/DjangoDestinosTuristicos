from django.shortcuts import render
from .models import DestinosTuristicos
from .forms import DestinosForm

# Create your views here.
def index(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request , 'index.html' , {'destinos':destinos})

#Registro de los nuevos destinos turisticos
def destinosRegister(request):
    if request.method == 'POST':
        form = DestinosForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            form = DestinosForm()
    else:
        form = DestinosForm(request.POST or None)
    context = {
        'form':form
    }
    return render(request , 'registroDestinos.html' , context)

#Editar los destinos turisticos
def destinosEdit(request , id_destino):
    obj = DestinosTuristicos.objects.get(id=id_destino)
    form = DestinosForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    form = DestinosForm(instance=obj)
    context = {
        'form':form
    }
    return render(request , 'editarDestinos.html' , context)

#Listar los destinos turisticos
def destinosLista(request):
    destinos = DestinosTuristicos.objects.all()
    context = {
        'destinos':destinos,
    }
    return render(request , 'listarDestinos.html' , context)