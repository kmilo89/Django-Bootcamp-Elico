from django.contrib import admin
from .models import *

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]

admin.site.register(Department, DepartmentAdmin)

class ProgramAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Program._meta.fields]

admin.site.register(Program, ProgramAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Professor._meta.fields]

admin.site.register(Professor, ProfessorAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields]

admin.site.register(Course, CourseAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]

admin.site.register(Student, StudentAdmin)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Enrollment._meta.fields]

admin.site.register(Enrollment, EnrollmentAdmin)