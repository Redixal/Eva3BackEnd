from django.contrib import admin
from .models import Genero, Videojuego

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_filter = ('nombre',)

@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'precio', 'fecha_lanzamiento', 'en_stock')
    list_filter = ('genero', 'en_stock')
    search_fields = ('titulo', 'genero__nombre')