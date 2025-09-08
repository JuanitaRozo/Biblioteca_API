# gestion/admin.py

from django.contrib import admin
from .models import Autor, Editorial, Libro, Miembro, Prestamo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido']

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'editorial']

@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email']

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['libro', 'miembro', 'fecha_prestamo', 'fecha_devolucion']
    