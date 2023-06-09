from typing import Any
from django.db import models
from categorias.models import Categoria
from django.urls import reverse

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField( max_length=200, unique=True)
    slug = models.SlugField( max_length=200, unique=True)
    descripcion = models.TextField( max_length=200, unique=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='photos/products')
    stock= models.IntegerField()
    is_avaliable = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('detalles_productos', args=[self.categoria.slug, self.slug])

    def __str__(self):
        return self.nombre_producto