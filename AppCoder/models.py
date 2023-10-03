from django.db import models

# Create your models here.
class Cerveceria(models.Model):
    nombre = models.CharField(max_length=60)
    pais = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60, default="Sin marca")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)
