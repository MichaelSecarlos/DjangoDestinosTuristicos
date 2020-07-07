from django.shortcuts import render , get_object_or_404 , redirect
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

#Eliminar el destino seleccionado
def destinosEliminar(request , id_destino):
    obj = get_object_or_404(DestinosTuristicos , id=id_destino)
    if request.method == 'POST':
        print("Borrando elemento...")
        obj.delete()
        print("Se ha borrado el elemento de la base de datos.")
        redirect("lista")
    context = {
        'obj':obj,
    }
    return render(request , 'eliminarDestinos.html' , context)