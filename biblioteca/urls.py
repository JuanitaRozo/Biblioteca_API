# biblioteca/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Importa las vistas de biblioteca

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gestion.urls')),
    path('', views.home, name='home'),  # Página principal
]