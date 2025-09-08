from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'editoriales', views.EditorialViewSet)  # ¡Falta esta línea!
router.register(r'libros', views.LibroViewSet)
router.register(r'miembros', views.MiembroViewSet)
router.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]