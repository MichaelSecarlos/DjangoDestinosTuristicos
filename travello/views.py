from django.shortcuts import render , get_object_or_404 , redirect
from .models import DestinosTuristicos
from .forms import DestinosForm

# Create your views here.
def index(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request , 'index.html' , {'destinos':destinos})

#Registro de los nuevos destinos turisticos
def destinosRegister(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = DestinosForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                form = DestinosForm()
                return redirect('../listar')
        else:
            form = DestinosForm(request.POST or None)
        context = {
            'form':form
        }
        return render(request , 'registroDestinos.html' , context)
    else:
        return redirect("/")
#Editar los destinos turisticos
def destinosEdit(request , id_destino):
    if request.user.is_authenticated and request.user.is_staff:
        obj = DestinosTuristicos.objects.get(id=id_destino)
        form = DestinosForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('../listar')
        form = DestinosForm(instance=obj)
        context = {
            'form':form
        }
        return render(request , 'editarDestinos.html' , context)
    else:
        return redirect("/")
#Listar los destinos turisticos
def destinosLista(request):
    if request.user.is_authenticated and request.user.is_staff:
        destinos = DestinosTuristicos.objects.all()
        context = {
            'destinos':destinos,
        }
        return render(request , 'listarDestinos.html' , context)
    else:
        return redirect("/")
#Eliminar el destino seleccionado
def destinosEliminar(request , id_destino):
    if request.user.is_authenticated and request.user.is_staff:
        obj = get_object_or_404(DestinosTuristicos , id=id_destino)
        if request.method == 'POST':
            obj.delete()
            return redirect("/listar")
        context = {
            'obj':obj,
        }
        return render(request , 'eliminarDestinos.html' , context)
    else:
        return redirect("/")