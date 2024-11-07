from django.db import models

# Create your models here.
class Producto(models.Model):
    
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    

class Proveedor(models.Model):
    nombreProveedor = models.CharField(max_length=50)
    categoriaSuministrada = models.CharField(max_length=30)
    costoInsumo = models.FloatField()
    tiempoEntrega = models.IntegerField()