# apps/courses/models.py

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(
        max_length=100, 
        choices=[('beginner', 'Principiante'), ('intermediate', 'Intermedio'), ('advanced', 'Avanzado')]
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Aquí puedes usar TextField, pero en una implementación más compleja podrías manejar archivos o videos.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    order = models.IntegerField()  # Para ordenar los capítulos

    def __str__(self):
        return f"{self.order} - {self.title}"

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

class Ciclo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='courses/img/', blank=True)  # Guardará las imágenes en la carpeta 'ciclos/'

    def __str__(self):
        return self.titulo