from django.shortcuts import render, redirect
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
        
        usuario = User.objects.create_user(username=username , password=password1 , email=email, first_name=first_name, last_name=last_name)
        usuario.save()
        return redirect('/')
    else:
        print("aqui we -_-")
        return render(request , 'registro.html')