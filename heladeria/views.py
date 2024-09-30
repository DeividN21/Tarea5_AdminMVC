from django.shortcuts import render, redirect
from heladeria.models import Producto
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"principal.html")

def consultar(request):
    productos = Producto.objects.all()
    return render(request,"productos.html",{'productos' : productos})

def guardar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    cantidad = request.POST["cantidad"]
    descripcion = request.POST["descripcion"]
    p = Producto(nombre=nombre, precio=precio,cantidad=cantidad,descripcion=descripcion)
    p.save()
    messages.success(request,'Producto agregado!')
    return redirect('consultar')