from rest_framework import viewsets
from gestion.models import Autor, Editorial, Libro, Miembro, Prestamo
from gestion.serializers import (
    AutorSerializer, EditorialSerializer, LibroSerializer, 
    MiembroSerializer, PrestamoSerializer
)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class EditorialViewSet(viewsets.ModelViewSet):  # ¡Esta vista debe existir!
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class MiembroViewSet(viewsets.ModelViewSet):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
