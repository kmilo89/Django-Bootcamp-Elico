from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
import requests

# Create your views here.
def data_query(request):
    url = reverse('show_data_course')
    absolute_url = request.build_absolute_uri(url)
    data = requests.get(absolute_url)
    data_response = data.json()
    combined_data = zip(
        data_response['courses'],
        data_response['programs'],
        data_response['professors'],
        data_response['credits']
        )
    
    if request.method == 'GET' and 'course_filter' in request.GET:
        course_filter = request.GET['course_filter']
        combined_data = [
            (course, program, professor, credit) 
            for course, program, professor, credit in combined_data 
            if course_filter.lower() in course.lower()
        ]

    context = {
        'combined_data': combined_data,
        'course_filter': request.GET.get('course_filter', '')
    }
    return render(request, 'queries/data_query.html', context=context)


def graphics(request):
    return render(request, 'queries/graphics.html')

