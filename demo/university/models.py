from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    building = models.CharField(max_length=2)

class Program(models.Model):
    name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

class Professor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)

class Course(models.Model):
    name = models.CharField(max_length=50)
    program_id = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)
    professor_id = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)
    credits = models.PositiveIntegerField()

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    program_id = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)

class Enrollment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    course_id = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    