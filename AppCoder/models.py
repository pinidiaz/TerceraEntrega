from django.db import models
from PIL import Image
from django.contrib.auth.models import User

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

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Avatar, self).save(*args, **kwargs)

        if self.imagen:
            img = Image.open(self.imagen.path)
            max_size = (100, 100)  
            img.thumbnail(max_size)
            img.save(self.imagen.path)

