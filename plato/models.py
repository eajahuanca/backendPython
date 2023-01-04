from django.db import models
from .validators import validar_precio


class Plato(models.Model):
    OFERTA_CHOICES = (
        ('SI', 'SI'),
        ('NO', 'NO')
    )
    color=models.CharField('Color', max_length=15, null=False, blank=False)
    precio=models.DecimalField('Precio', decimal_places=2, max_digits=10, default=9,
                               validators=[validar_precio, ])
    campos=models.CharField('Campos', max_length=20, null=True, blank=True)
    nombre=models.CharField('Nombre del plato', max_length=50, null=False, blank=False)
    fecha_inicio=models.DateField()
    oferta=models.CharField('Oferta', max_length=2, choices=OFERTA_CHOICES, default='NO')

