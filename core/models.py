from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='videojuegos')
    titulo = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_lanzamiento = models.DateField()
    en_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} ({self.genero.nombre})"