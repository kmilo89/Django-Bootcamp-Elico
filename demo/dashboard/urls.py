from django.urls import path
from .views import * #con este import importamos todas las vistas en el mismo nivel de ruta de vistas.

urlpatterns = [
    path('tacometer', tacometer, name='tacometer'),
    path('forms/generate-data', generate_data, name='generate_data')
]