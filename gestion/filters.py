# gestion/filters.py (crea este archivo nuevo)

from rest_framework import filters

class LibroFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # Filtrar por autor
        autor_id = request.query_params.get('autor')
        if autor_id:
            queryset = queryset.filter(autor_id=autor_id)
        
        # Filtrar por editorial
        editorial_id = request.query_params.get('editorial')
        if editorial_id:
            queryset = queryset.filter(editorial_id=editorial_id)
        
        return queryset

class PrestamoFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # Filtrar por miembro
        miembro_id = request.query_params.get('miembro')
        if miembro_id:
            queryset = queryset.filter(miembro_id=miembro_id)
        
        # Filtrar por fecha de préstamo
        fecha_prestamo = request.query_params.get('fecha_prestamo')
        if fecha_prestamo:
            queryset = queryset.filter(fecha_prestamo=fecha_prestamo)
        
        return queryset