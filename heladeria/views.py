from django.shortcuts import render, redirect
from heladeria.models import Producto, Proveedor
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def iniciar(request):
    if request.method=='GET':
        return render(request,"iniciar.html", {'form': AuthenticationForm})
    else:
        name = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=name,password=password)
        if user is None:
            messages.success(request,'Usuario y/o contraseña incorrecto!')
            return render(request,"iniciar.html", {'form': AuthenticationForm})
        else:
            login(request,user)
            return redirect('inicio')
        

def registro(request):
    if request.method=='GET':
        return render(request, "registro.html", {'form': UserCreationForm})
    else:
        if request.POST["password1"] != request.POST["password2"]:
            messages.error(request,'Las contraseñas no coinciden!')
            return render(request, "registro.html", {'form': UserCreationForm})
        else:
            name = request.POST["username"]
            password = request.POST["password2"]
            user = User.objects.create_user(username=name,password=password)
            user.save()
            messages.success(request,'Usuario creado con éxito!')
            return render(request, "registro.html", {'form': UserCreationForm})
            
@login_required
def home(request):
    return render(request,"principal.html")

@login_required
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

def eliminar(request, id):
    producto = Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado!')
    return redirect('consultar')

def detalle(request, id):
    producto = Producto.objects.get(pk=id)
    return render(request, "productoEditar.html", {'producto' : producto})
    
def editar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    cantidad = request.POST["cantidad"]
    descripcion = request.POST["descripcion"]
    id = request.POST["id"]
    Producto.objects.filter(pk=id).update(id=id,nombre=nombre,precio=precio,cantidad=cantidad,descripcion=descripcion)
    messages.success(request, 'Producto actualizado con exito!')
    return redirect('consultar')

@login_required
def consultarP(request):
    proveedores = Proveedor.objects.all()
    return render(request,"proveedores.html",{'proveedores' : proveedores})

def guardarP(request):
    nombreProveedor = request.POST["nombreProveedor"]
    categoriaSuministrada = request.POST["categoriaSuministrada"]
    costoInsumo = request.POST["costoInsumo"]
    tiempoEntrega = request.POST["tiempoEntrega"]
    pr = Proveedor(nombreProveedor=nombreProveedor, categoriaSuministrada=categoriaSuministrada,
                   costoInsumo=costoInsumo,tiempoEntrega=tiempoEntrega)
    pr.save()
    messages.success(request,'Proveedor agregado!')
    return redirect('consultarP')

def eliminarP(request, id):
    proveedor = Proveedor.objects.filter(pk=id)
    proveedor.delete()
    messages.success(request, 'Proveedor eliminado!')
    return redirect('consultarP')

def detalleP(request, id):
    proveedor = Proveedor.objects.get(pk=id)
    return render(request, "proveedorEditar.html", {'proveedor' : proveedor})

def editarP(request):
    nombreProveedor = request.POST["nombreProveedor"]
    categoriaSuministrada = request.POST["categoriaSuministrada"]
    costoInsumo = request.POST["costoInsumo"]
    tiempoEntrega = request.POST["tiempoEntrega"]
    id = request.POST["id"]
    Proveedor.objects.filter(pk=id).update(id=id,nombreProveedor=nombreProveedor,categoriaSuministrada=categoriaSuministrada,
                                            costoInsumo=costoInsumo,tiempoEntrega=tiempoEntrega)
    messages.success(request, 'Proveedor actualizado con exito!')
    return redirect('consultarP')

@login_required
def consultarRentabilidad(request):
    return render(request, "rentabilidad.html")

@login_required
def consultarCostoEficiencia(request):
    return render(request, "costoEficiencia.html")

def salir(request):
    logout(request)
    return redirect('iniciar')