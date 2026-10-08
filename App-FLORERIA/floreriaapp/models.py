from django.core.validators import MinValueValidator
from django.db import models


class Producto(models.Model):
    CATEGORIAS = [
        ('ramo', 'Ramo de flores'),
        ('arreglo', 'Arreglo floral'),
        ('planta', 'Planta de interior'),
        ('maceta', 'Maceta / Accesorio'),
        ('evento', 'Flores para eventos'),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10, decimal_places=0,
        validators=[MinValueValidator(1, message='El precio debe ser mayor que cero.')],
    )
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
