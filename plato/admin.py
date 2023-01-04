from django.contrib import admin
from .models import Plato


@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'color', 'precio', 'campos', 'fecha_inicio', )
    search_fields = ('nombre', 'precio',)
