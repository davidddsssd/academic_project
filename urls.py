"""
Rutas principales del proyecto academic_project.

Las rutas conectan URLs con vistas.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academic.urls')),
]
