from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):

    #atributos
    name = models.CharField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="precio")
    status = models.BooleanField(default=True, verbose_name="estado")
    photo = models.ImageField(null=True, blank=True, verbose_name="foto")
    date_created =  models.DateTimeField(default=timezone.now, verbose_name="fecha de creación")


    def __str__(self):
        return self.name
