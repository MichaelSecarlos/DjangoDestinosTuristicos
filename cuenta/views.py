from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth
# Create your views here.
def registro(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username):
                messages.info(request , "El nombre de usuario ya esta ocupado.")
                return redirect('./registro')
    
            elif User.objects.filter(email=email):
                messages.info(request , "La direccion de correo ya esta ocupada.")
                return redirect('./registro')
            else:
                usuario = User.objects.create_user(username=username , password=password1 , email=email, first_name=first_name, last_name=last_name)
                usuario.save()
        else:
            messages.info(request , "Las contraseñas no coinciden.")
            return redirect('./registro')
        return redirect('/')
    else:
        return render(request , 'registro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Verificacion del usuario, su nombre y contraseña
        user = auth.authenticate(username=username , password=password)

        #Logueo del usuario, si es que existe
        if user is not None:
            auth.login(request , user)
            return redirect('/')
        else:
            messages.info(request , "Usuario o contraseña incorrectos.")
            return redirect('./login')
    else:
        return render(request , 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")