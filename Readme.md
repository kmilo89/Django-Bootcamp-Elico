## Course Django
## may 28 - 09:00

### Create venv
python3 -m venv .venv
### Activate .venv
source .venv/bin/activate
### Deactivate .venv
deactivate

### Install Django
pip install django==5.0.6

### Create project
django-admin startproject demo

### Create APP
python manage.py startapp home
python manage.py startapp dashboard

### Run server
python manage.py runserver

### Download templates Boostrap
https://startbootstrap.com/themes
download: https://github.com/startbootstrap/startbootstrap-sb-admin-2/archive/gh-pages.zip

- after Unzip file
- create templates folder in root_project
- copy index.html into templates
- create static folder in root_project/demo/
- copy folders css, img, js, scss, vendor into root_project/demo/static
- copy the content of index.html in a new file root_project/templates/base.html
- create folder partials into root_project/templates/
- create files _sidebar.html, _header.html and _footer.html into root_project/templates/partials/
- in base.html search <!-- Sidebar --> content <!-- End of Sidebar -->,  cut content into _sidebar.html and replace with {% include 'partials/_sidebar.html' %}
- in base.html search <!-- Topbar --> content <!-- End of Topbar -->,  cut content into _header.html and replace with {% include 'partials/_header.html' %}
- in base.html search  <!-- Footer --> content <!-- End of Footer -->, cut content into _footer.html and replace with {% include 'partials/_footer.html' %}
- in base.html, _sidebar.html, _header.html and _footer.html add in line 1 {% load static %} and replace links "src" with tags example: {% static 'img/undraw_profile_1.svg' %}
- find <!-- Begin Page Content --> content <!-- /.container-fluid --> and replace content with {% block content %} {% endblock %}

#### templates apps
- in home and dashboard create templates/nameAPP folder and nameAPP.html file


### home.html div extract of index.html <!-- Page Heading -->
{% extends 'base.html' %}
{% load static %}
<!--Add Tags for include libraries-->
{% block content %} 
<div class="d-sm-flex align-items-center justify-content-between mb-4">
    <h1 class="h3 mb-0 text-gray-800">Bienvenidos al Industrial Insights</h1>
</div>
{% endblock %}

### create view in home
in home/views.py

def home(request):
    return render(request, 'home/home.html')

create home/urls.py and copy the following lines

from .views import *
urlpatterns = [
    path('', home, name='home'),
]

'' is the project home 
in demo/urls.py add the following path

from django.urls import path, include
path('',include('home.urls')),


### setting dirs
in demo/settings.py add
import os
in INSTALLED_APPS add
'home',
'dashboard',
in TEMPLATES --> DIRS: [] add
DIRS: [BASE/DIR/'templates']
after static files section add
STATIC_URL = 'static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'demo/static')
]

python manage.py collectstatic
then a folder appears in Root_folder/static



## may 28 - 15:30

### home/views.py
def page1(request):
    dictionary = {
        'name': 'Camilo',
        'lastname': 'Londoño',
        'age':34,
        'areas': ['area1', 'area2', 'area3', 'area4']
    }
    return render(request, 'home/page1.html', context=dictionary)

In home/urls.py add path 
path('page1', page1, name='page1'),

in home/templates/home create page1.html
{% extends 'base.html' %}
{% load static %}
<!--Agregar Tags para incluir librerias-->
{% block content %} 
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800"> Información personal</h1>
    </div>
    <ul>
        <li>Nombre: {{ name }}</li>
        <li>Apellido: {{ lastname }}</li>
        <li>Edad: {{ age }}</li>
    </ul>
    <h1>Materias Cursadas</h1>
    <ul>
        {% for area in areas %}
            <li>{{ area }}</li>
        {% endfor %}
    </ul>


{% endblock %}


### Create home/templates/home/view-summary/data.html
{% extends 'base.html' %}
{% load static %}
<!--Agregar Tags para incluir librerias-->
{% block content %} 
<div class="d-sm-flex align-items-center justify-content-between mb-4">
    <h1 class="h3 mb-0 text-gray-800">Datos de la aplicación</h1>
</div>
{% endblock %}

in home/views.py add
def data(request):
    return render(request, 'home/view-summary/data.html')

### migrations
python manage.py makemigrations
python manage.py migrate

### help
python manage.py help

### create superuser
python manage.py createsuperuser

### access to admin 
127.0.0.1:8000/admin

### static in demo
create charts/dashboards.js file

var chart_font = {
    family: "Arial",
    size: 30,
    color: "#FFFFFF"
};

var gTacometer = new JustGage(
    {
        id: "tacometer",
        value: 80,
        min: 0,
        max: 200,
        valueMinFontSize: 40,
        gaugeWidthScale: 1.0,
        donut: true,
        levelColors: ["#a9d70b", "#f9c802", "#ff0000"]
      }
);


create dashboard/templates/dashboard/tacometer.html
{% extends 'base.html' %}
{% load static %}
<!--Agregar Tags para incluir librerias-->
{% block content %} 
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">Eficiencia Energética</h1>
    </div>

    <div id="tacometer"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/justgage@1.3.5/justgage.min.js"></script>

    <script src="{% static 'charts/dashboards.js' %}"></script>
{% endblock %}

### in dashboards/views.py add

def tacometer(request):
    return render(request, 'dashboard/tacometer.html')

### in dashboard/urls.py add path 
path('tacometer', tacometer, name='tacometer'),

### in demo/urls.py add path 
path('dashboards/',include('dashboard.urls')),



## may 29 - 08:00

### Edit links of sidebar
examples
<a class="collapse-item" href="{% url 'page1' %}">Page1</a>
<a class="collapse-item" href="{% url 'data' %}">data</a>


### Create model
in dashboard/models.py

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    id_number = models.CharField(max_length=10)
    profession = models.CharField(max_length=20)
    married = models.BooleanField()
    city = models.CharField(max_length=30)
    birth = models.DateField(null=True, blank=True)

### Register model
in dashboard/admin.py
from django.contrib import admin
from .models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Person._meta.fields]

admin.site.register(Person, PersonAdmin)

perform migrations

## may 29 - 12:00

### Access to shell
python manage.py shell

from dashboard.models import Person
new_person = Person.objects.create(
    name="Juan Camilo",
    age = 34,
    id_number="123456789",
    profession="Control Eng.",
    married=True,
    city="Copacabana"
)
### Update register
new_person.age=30
new_person.save()

### Interacting with Jupyter
see test.ipynb file

### new delivery "table" in dashboard/models.py

class Delivery(models.Model):
    timestamp = models.TimeField()
    orderid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=10)
    order = models.CharField(max_length=50)

run migrate
conection with DBeaver

in dashboards/views.py
def generate_data(request):
    return render(request, 'dashboard/forms/generate_data.html')

in dashboards/templates create using https://getbootstrap.com/docs/5.3/forms/validation/ Browser defaults
forms/generate_data.html

{% extends 'base.html' %}
{% load static %}

{% block content %} 
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">Bienvenido al sistema de generación de datos</h1>
    </div>
    <form class="row g-3" method="post" action="{% url 'generate_data' %}">
        {% csrf_token %} <!--Tag for security-->
        <div class="col-md-4">
          <label for="validationDefault01" class="form-label">Número de Pedidos</label>
          <input type="number" class="form-control" id="validationDefault01" name="number" required>
        </div>
        <div class="col-12">
          <button class="btn btn-primary" type="submit">Enviar</button>
        </div>
      </form>

      {% if message %}
        <div id="messages">
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                    <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                </div>
        </div>
      {% endif %}

{% endblock %}

in dashboard/urls add following path
path('forms/generate-data', generate_data, name='generate_data')

### in dashboards/views.py
### Create your views here.
from django.shortcuts import render
from .models import *
from faker import Faker

def generate_dummy_data():
    fake = Faker()
    data={
        'timestamp':fake.date_time(),
        'orderid': str(fake.unique.random_number(digits=10, fix_len=True)),
        'name': fake.name(),
        'city': fake.city(),
        'address': fake.address(),
        'phone': fake.phone_number(),
        'zipcode': str(fake.unique.random_number(digits=5, fix_len=True)),
        'order': fake.random_choices(elements=('computer', 'tv', 'smart phone', 'smart watch', 'book', 'tablet', 'toy'))[-1]
    }
    return data

# Create your views here.
def tacometer(request):
    return render(request, 'dashboard/tacometer.html')

def generate_data(request):
    if request.method=='POST':
        number = request.POST.get('number')
        for i in range(int(number)):
            data = generate_dummy_data()
            Delivery.objects.create(
                timestamp = data['timestamp'],
                orderid = data['orderid'],
                name = data['name'],
                city = data['city'],
                address = data['address'],
                phone = data['phone'],
                zipcode = data['zipcode'],
                order = data['order']
            )
        return render(request, 'dashboard/forms/generate_data.html', {"message": f"Successfully loaded {number} data"})
    return render(request, 'dashboard/forms/generate_data.html', {"message": ""})


### add link to sidebar 
in _sidebar.html search item and paste 
href="{% url 'generate_data' %}"


## may 30 - 08:00

create new app queries and university
python manage.py startapp queries
python manage.py startapp university

in university/models.py
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
    
in university/admin.py
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


register app in demo/settings.py
in installed apps
'university',
'queries'

run migrate

### create university templates
university/templates/university folder


In demo/urls.py add path
path('university/',include('university.urls')),

in university/urls.py
from django.urls import path
from .views import * #con este import importamos todas las vistas en el mismo nivel de ruta de vistas.

urlpatterns = [
    path('forms/insert_department', insert_department, name='insert_department')
]

in university/views.py
from django.shortcuts import render
from .models import *

def insert_department(request):
    if request.method=='POST':
        _department = request.POST.get('department')
        _building = request.POST.get('building')
        Department.objects.create(
                name = _department,
                building = _building
            )
        return render(request, 'university/forms/insert_department.html', {"message": f"Loaded department: {_department}, Building: {_building}"})
    return render(request, 'university/forms/insert_department.html', {"message": ""})

create university/templates/university/forms/insert_department.html


{% extends 'base.html' %}
{% load static %}

{% block content %} 
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">Create department</h1>
    </div>

    <form class="row g-3" method="post" action="{% url 'insert_department' %}">
        {% csrf_token %} <!--Tag for security-->

        <div class="col-md-4">
          <label for="validationDefault01" class="form-label">Department</label>
          <input type="text" class="form-control" id="validationDefault01" name="department" required>
        </div>

        <div class="col-md-4">
            <label for="validationDefault01" class="form-label">Building</label>
            <input type="text" class="form-control" id="validationDefault01" name="building" required>
          </div>

        <div class="col-12">
          <button class="btn btn-primary" type="submit">Insert</button>
        </div>

      </form>

      {% if message %}
        <div id="messages">
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                    <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                </div>
        </div>
      {% endif %}

{% endblock %}


### Follow the steps above to create insert_program.html

{% extends 'base.html' %}
{% load static %}

{% block content %} 
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">Create program</h1>
    </div>

    <form class="row g-3" method="post" action="{% url 'insert_program' %}">
        {% csrf_token %} <!--Tag for security-->

        <div class="col-md-4">
          <label for="validationDefault01" class="form-label">Program</label>
          <input type="text" class="form-control" id="validationDefault01" name="program" required>
        </div>

        <div class="col-md-4">
            <label for="department_id" class="form-label">Department</label>
            <select class="form-control" id="department_id" name="department_id" required>
                <option value="" disabled selected>Select a department</option>
                {% for department in departments %}
                    <option value="{{ department.id }}">{{ department.name }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="col-12">
          <button class="btn btn-primary" type="submit">Insert</button>
        </div>

      </form>

      {% if message %}
        <div id="messages">
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                    <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                </div>
        </div>
      {% endif %}

{% endblock %}



in views.py 
def insert_program(request):
    if request.method=='POST':
        _program = request.POST.get('program')
        _department_id = request.POST.get('department_id')
        department = Department.objects.get(id=_department_id)
        Program.objects.create(name=_program, department_id=department)
        return render(request, 'university/forms/insert_program.html', {"message": f"Loaded Program: {_program}", 'departments': departments})
    departments = Department.objects.all()
    return render(request, 'university/forms/insert_program.html', {"message": "", 'departments': departments})



### Follow the steps above to create insert_professor.html

{% extends 'base.html' %}
{% load static %}

{% block content %} 
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">Create professor</h1>
    </div>

    <form class="row g-3" method="post" action="{% url 'insert_professor' %}">
        {% csrf_token %} <!--Tag for security-->

        <div class="col-md-4">
          <label for="validationDefault01" class="form-label">Name</label>
          <input type="text" class="form-control" id="validationDefault01" name="name" required>
        </div>

        <div class="col-md-4">
            <label for="validationDefault01" class="form-label">Email</label>
            <input type="email" class="form-control" id="validationDefault01" name="email" required>
        </div>


        <div class="col-md-4">
            <label for="validationDefault01" class="form-label">Phone</label>
            <input type="tel" class="form-control" id="validationDefault01" name="phone" required>
        </div>

        <div class="col-12">
          <button class="btn btn-primary" type="submit">Insert</button>
        </div>

      </form>

      {% if message %}
        <div id="messages">
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                    <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                </div>
        </div>
      {% endif %}

{% endblock %}

in views.py


def insert_professor(request):
    if request.method=='POST':
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _phone = request.POST.get('phone')
        Professor.objects.create(
                name = _name,
                email = _email,
                phone = _phone
            )
        return render(request, 'university/forms/insert_professor.html', {"message": f"Loaded professor: {_name}"})
    return render(request, 'university/forms/insert_professor.html', {"message": ""})



### Follow the steps above to create insert_course.html
{% extends 'base.html' %}
{% load static %}

{% block content %} 
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">Create course</h1>
    </div>

    <form class="row g-3" method="post" action="{% url 'insert_course' %}">
        {% csrf_token %} <!--Tag for security-->

        <div class="col-md-4">
          <label for="validationDefault01" class="form-label">Name</label>
          <input type="text" class="form-control" id="validationDefault01" name="name" required>
        </div>

        <div class="col-md-4">
            <label for="department_id" class="form-label">Program</label>
            <select class="form-control" id="program_id" name="program_id" required>
                <option value="" disabled selected>Select a program</option>
                {% for program in programs %}
                    <option value="{{ program.id }}">{{ program.name }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="col-md-4">
          <label for="department_id" class="form-label">Professor</label>
          <select class="form-control" id="professor_id" name="professor_id" required>
              <option value="" disabled selected>Select a professor</option>
              {% for professor in professors %}
                  <option value="{{ professor.id }}">{{ professor.name }}</option>
              {% endfor %}
          </select>
      </div>

      <div class="col-md-4">
        <label for="validationDefault01" class="form-label">Credits</label>
        <input type="text" class="form-control" id="validationDefault01" name="credits" required>
      </div>

        <div class="col-12">
          <button class="btn btn-primary" type="submit">Insert</button>
        </div>

      </form>

      {% if message %}
        <div id="messages">
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                    <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                </div>
        </div>
      {% endif %}

{% endblock %}


In views.py
def insert_course(request):
    programs = Program.objects.all()
    professors = Professor.objects.all()
    if request.method=='POST':
        _name = request.POST.get('name')
        _program_id = request.POST.get('program_id')
        _professor_id = request.POST.get('professor_id')
        _credits = request.POST.get('credits')
        program = Program.objects.get(id=_program_id)
        professor = Professor.objects.get(id=_professor_id)
        Course.objects.create(
                name = _name,
                program_id = program,
                professor_id = professor,
                credits = _credits
            )
        return render(request, 'university/forms/insert_course.html', {"message": f"Loaded course: {_name}", 'programs': programs, 'professors': professors})
    return render(request, 'university/forms/insert_course.html', {"message": "", 'programs': programs, 'professors': professors})

### Follow the steps above to create insert_student.html
{% extends 'base.html' %}
{% load static %}

{% block content %} 
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">Create student</h1>
    </div>

    <form class="row g-3" method="post" action="{% url 'insert_student' %}">
        {% csrf_token %} <!--Tag for security-->

        <div class="col-md-4">
          <label for="validationDefault01" class="form-label">Name</label>
          <input type="text" class="form-control" id="validationDefault01" name="name" required>
        </div>

        <div class="col-md-4">
            <label for="validationDefault01" class="form-label">Email</label>
            <input type="email" class="form-control" id="validationDefault01" name="email" required>
        </div>


        <div class="col-md-4">
            <label for="validationDefault01" class="form-label">Phone</label>
            <input type="tel" class="form-control" id="validationDefault01" name="phone" required>
        </div>


        <div class="col-md-4">
            <label for="department_id" class="form-label">Program</label>
            <select class="form-control" id="program_id" name="program_id" required>
                <option value="" disabled selected>Select a program</option>
                {% for program in programs %}
                    <option value="{{ program.id }}">{{ program.name }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="col-12">
          <button class="btn btn-primary" type="submit">Insert</button>
        </div>

      </form>

      {% if message %}
        <div id="messages">
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                    <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                </div>
        </div>
      {% endif %}

{% endblock %}

in views.py

def insert_student(request):
    programs = Program.objects.all()
    if request.method=='POST':
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _phone = request.POST.get('phone')
        _program_id = request.POST.get('program_id')
        program = Program.objects.get(id=_program_id)
        Student.objects.create(
                name = _name,
                email = _email,
                phone = _phone,
                program_id = program
            )
        return render(request, 'university/forms/insert_student.html', {"message": f"Loaded student: {_name}", 'programs': programs})
    return render(request, 'university/forms/insert_student.html', {"message": "", 'programs': programs})
