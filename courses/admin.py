from django.contrib import admin
from .models import Course, Chapter, Purchase, Inicio, CiclosAcademia

class InicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha_inicio')  # Campos a mostrar en la lista
    # search_fields = ('titulo', 'subtitulo')  # Campos en los que se puede buscar
    # list_filter = ('fecha_inicio',)  # Filtros en la barra lateral
    # ordering = ('fecha_inicio',)  # Ordenar por fecha de inicio


# Register your models here.

admin.site.register(Course)

admin.site.register(Chapter)

admin.site.register(Purchase)

admin.site.register(Inicio)

admin.site.register(CiclosAcademia)




