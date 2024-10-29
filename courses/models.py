# apps/courses/models.py

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título del curso')
    description = models.TextField()
    level = models.CharField(
        max_length=100, 
        choices=[('beginner', 'Principiante'), ('intermediate', 'Intermedio'), ('advanced', 'Avanzado')], 
        verbose_name='Nivel'
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Aquí puedes usar TextField, pero en una implementación más compleja podrías manejar archivos o videos.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    order = models.IntegerField()  # Para ordenar los capítulos 
    class Meta:
        verbose_name = "Capítulos"
        verbose_name_plural = "Capítulos"
        ordering = ["order"]       
    
    def __str__(self):
        return f"{self.title}-{self.course}"   

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

class Inicio(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Nombre del Ciclo a publicar')
    subtitulo = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='courses/img/', blank=True)  # Guardará las imágenes en la carpeta 'courses/'
    fecha_inicio = models.DateField(default='2025-12-31')
    fecha_fin = models.DateField(blank=True, null=True, default='2025-12-31')
    class Meta:
        verbose_name = "Pagina principal"
        verbose_name_plural = "Pagina de Inicio"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
    
class CiclosAcademia(models.Model):
    imagen = models.ImageField(upload_to='courses/img/', blank=True)  # Guardará las imágenes en la carpeta 'courses/'
    ciclo = models.CharField(max_length=200)
    duracion = models.CharField(max_length=200, blank=True)
    dirigido = models.TextField()
    objetivo = models.CharField(max_length=200)
    cursos = models.CharField(max_length=200)
    temas = models.TextField(blank=True, null=True)
    costo = models.CharField(max_length=200)
    pago = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "Pagina principal"
        verbose_name_plural = "Pagina de Ciclos"
        ordering = ["ciclo"]

    def __str__(self):
        return self.ciclo  # Este campo se muestra en el panel administrador
    
    
    
