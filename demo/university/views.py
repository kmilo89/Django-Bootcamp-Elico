from django.shortcuts import render
from .models import *
from django.http import JsonResponse

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

def insert_program(request):
    departments = Department.objects.all()
    if request.method=='POST':
        _program = request.POST.get('program')
        _department_id = request.POST.get('department_id')
        department = Department.objects.get(id=_department_id)
        Program.objects.create(name=_program, department_id=department)
        return render(request, 'university/forms/insert_program.html', {"message": f"Loaded Program: {_program}", 'departments': departments})
    return render(request, 'university/forms/insert_program.html', {"message": "", 'departments': departments})

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


def insert_enrollment(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    if request.method=='POST':
        _student_id = request.POST.get('student_id')
        _course_id = request.POST.get('course_id')
        student = Student.objects.get(id=_student_id)
        course = Course.objects.get(id=_course_id)
        Enrollment.objects.create(
            student_id = student,
            course_id = course
        )
        return render(request, 'university/forms/insert_enrollment.html', {"message": "Loaded enrollment", 'students':students, 'courses': courses})
    return render(request, 'university/forms/insert_enrollment.html', {"message": "", 'students':students, 'courses': courses})


def show_data_course(request):
    courses = Course.objects.all()
    
    data = {
        'courses':[course.name for course in courses],
        'programs':[course.program_id.name for course in courses],
        'professors':[course.professor_id.name for course in courses],
        'credits':[course.credits for course in courses],
    }
    return JsonResponse(data)