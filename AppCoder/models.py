from django.db import models

# Create your models here.
class Cerveceria(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} ------- Direccion: {self.direccion}"
    
    nombre = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

class Producto(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} ------- Marca: {self.marca}"

    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60, default="Sin marca")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Cliente(models.Model):

    def __str__(self):
        return f"Usuario: {self.usuario} ------- Cliente: {self.cliente}"
    
    usuario = models.CharField(max_length=60, unique=True)
    cliente = models.CharField(max_length=60)


