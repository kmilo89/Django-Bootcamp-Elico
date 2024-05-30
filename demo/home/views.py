from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def page1(request):
    dictionary = {
        'name': 'Camilo',
        'lastname': 'Londoño',
        'age':34,
        'areas': ['area1', 'area2', 'area3', 'area4']
    }
    return render(request, 'home/page1.html', context=dictionary)

def page(request):
    return render(request, 'home/page.html')

def data(request):
    return render(request, 'home/view-summary/data.html')