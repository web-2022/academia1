# apps/courses/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título del curso')
    slug = models.SlugField(unique=True, blank=True, null=True)  # Campo slug agregado
    description = models.TextField()
    level = models.CharField(
        max_length=100, 
        choices=[('beginner', 'Principiante'), ('intermediate', 'Intermedio'), ('advanced', 'Avanzado')], 
        verbose_name='Nivel'
    )
    price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Precio')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    imagen = models.ImageField(upload_to='courses/img/', blank=True, null=True)  # Guardará las imágenes en la carpeta 'courses/'
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["title"] 
        
    def save(self, *args, **kwargs):
        # Si el slug está vacío, lo genera automáticamente a partir del título
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=200)    
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()  # Aquí puedes usar TextField, pero en una implementación más compleja podrías manejar archivos o videos.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    order = models.IntegerField()  # Para ordenar los capítulos 
    url_recursos = models.URLField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    
    
         
    class Meta:
        verbose_name = "Capítulo"
        verbose_name_plural = "Capítulos"
        ordering = ["order"]    
        
    def save(self, *args, **kwargs):
        if not self.slug:  # Solo generar el slug si no existe
            self.slug = slugify(self.title)  # Crear el slug a partir del título
        super().save(*args, **kwargs)   
    
    def __str__(self):
        return f"{self.title}-{self.course}"   

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

class Inicio(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Nombre del Ciclo')
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
    
    
    
