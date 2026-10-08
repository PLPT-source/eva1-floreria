from django import forms
from .models import Producto

_ctl = {'class': 'form-control'}


class _ProductoBase(forms.ModelForm):
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio is None or precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio


class ProductoCrearForm(_ProductoBase):
    

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={**_ctl, 'placeholder': 'Ej: Ramo de rosas rojas'}),
            'precio': forms.NumberInput(attrs={**_ctl, 'min': 1, 'placeholder': 'CLP'}),
            'stock': forms.NumberInput(attrs={**_ctl, 'min': 0}),
        }

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock is None or stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo.')
        return stock


class ProductoEditarForm(_ProductoBase):
    

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs=_ctl),
            'precio': forms.NumberInput(attrs={**_ctl, 'min': 1}),
            'stock': forms.NumberInput(attrs={**_ctl, 'min': 0}),
        }
