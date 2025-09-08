# biblioteca/views.py
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    # Datos para la página principal
    context = {
        'title': 'Sistema de Gestión de Biblioteca',
        'endpoints': [
            {'name': 'Autores', 'url': '/api/autores/', 'method': 'GET'},
            {'name': 'Editoriales', 'url': '/api/editoriales/', 'method': 'GET'},
            {'name': 'Libros', 'url': '/api/libros/', 'method': 'GET'},
            {'name': 'Miembros', 'url': '/api/miembros/', 'method': 'GET'},
            {'name': 'Préstamos', 'url': '/api/prestamos/', 'method': 'GET'},
        ]
    }
    return render(request, 'home.html', context)