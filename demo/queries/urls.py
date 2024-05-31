from django.urls import path
from .views import * #con este import importamos todas las vistas en el mismo nivel de ruta de vistas.

urlpatterns = [
    path('data_query', data_query, name='data_query'),
    path('graphics', graphics, name='graphics')
]