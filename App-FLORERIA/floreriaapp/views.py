from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductoCrearForm, ProductoEditarForm
from .models import Producto


def inicio(request):
    
    return render(request, 'floreriaapp/inicio.html')


def listar_productos(request):
    
    productos = Producto.objects.all()
    return render(request, 'floreriaapp/listado.html', {'productos': productos})


def crear_producto(request):
    
    form = ProductoCrearForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_productos')
    return render(request, 'floreriaapp/crear.html', {'form': form})


def detalle_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'floreriaapp/detalle.html', {'producto': producto})


def editar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    form = ProductoEditarForm(request.POST or None, instance=producto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_productos')
    return render(request, 'floreriaapp/editar.html', {'form': form, 'producto': producto})


def eliminar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'floreriaapp/eliminar.html', {'producto': producto})
