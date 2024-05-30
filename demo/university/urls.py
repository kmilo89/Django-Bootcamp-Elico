from django.urls import path
from .views import * #con este import importamos todas las vistas en el mismo nivel de ruta de vistas.

urlpatterns = [
    path('forms/insert_department', insert_department, name='insert_department'),
    path('forms/insert_program', insert_program, name='insert_program'),
    path('forms/insert_professor', insert_professor, name='insert_professor'),
    path('forms/insert_course', insert_course, name='insert_course'),
    path('forms/insert_student', insert_student, name='insert_student')
]