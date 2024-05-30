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
        {{ message }}
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