from django.shortcuts import render

from .models import Producto

# Create your views here.

# Aqui se muestra la vista del productos 

def productos(request):
    producto=Producto.objects.all
    return render(request,"producto/productos.html",{ "producto":producto})
