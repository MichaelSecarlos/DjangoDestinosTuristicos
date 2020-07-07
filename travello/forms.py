from django import forms
from .models import DestinosTuristicos

class DestinosForm(forms.ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = [
            'nombreCiudad',
            'descripcionCiudad',
            'imagenCiudad',
            'precioTour',
            'ofertaTour'
        ]
        labels = {
            'nombreCiudad':'',
            'nombreCiudad':'',
            'descripcionCiudad':'',
            'imagenCiudad':'',
            'precioTour':'',
            'ofertaTour':'Esta en oferta'
        }
        widgets={
            'nombreCiudad': forms.TextInput(attrs={
                'placeholder':'Destino',
                'class':'search_input'
            }),
            "descripcionCiudad": forms.Textarea(attrs={
                'placeholder':'Descripcion de la ciudad',
                'class':'search_input',
                'cols':26,
                'rows':3
            }),
            'precioTour': forms.TextInput(attrs={
                'placeholder':'Precio Tour',
                'class':'search_input'
            })
            

        }
    