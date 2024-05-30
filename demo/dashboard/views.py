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
