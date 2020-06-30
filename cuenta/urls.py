from django.urls import path
from . import views
urlpatterns = [
    path('registro' , views.registro , name='Registrarse'),
    path('login' , views.login , name='Login'),
    path('logout' , views.logout , name='Logout')
]