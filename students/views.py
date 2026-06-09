from django.shortcuts import render, redirect
from .models import students

# Create your views here.
def home(request):
    student = students.objects.all()
    return render(request, 'home.html', {'student': student})

def create_student(request):
    if request.method == 'POST':
        name =  request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        students.objects.create(name=name, age=age, email=email)
      
        return redirect('home')
    return render(request, 'create_student.html')

def update_student(request, id):
    student = students.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.save()
        return redirect('home')
    return render(request, 'update_student.html', {'student': student})

def delete_student(request, id):
    student = students.objects.get(id=id)
    if request.method == 'POST':

        student.delete()
        return redirect('home')
    return render(request, 'delete_student.html', {'student': student})
