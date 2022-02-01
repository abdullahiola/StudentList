from django.db.models import fields
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student
from .forms import registerform




def studentHome(request):
  return render(request, 'students/home.html')

def studentList(request):
  all_students = Student.objects.all()

  return render(request,'students/studentlist.html',{'all_students':all_students})

#def register(request):
  if request.method == 'POST':
    student= Student()
    Fullname= request.POST.get('Fullname')
    Photo= request.POST.get('Photo')
    Gender= request.POST.get('Gender')
    Course = request.POST.get('Course')
    Grade = request.POST.get('Grade')

    student.Fullname= Fullname
    student.Gender= Gender
    student.Photo= Photo
    student.Course= Course

    
    student.save()
    return HttpResponse('Registered')
  return render(request, 'students/register.html')
  #This method did not save the Images 
   

def register(request):
  if request.method =='POST':
    form = registerform(data=request.POST,files=request.FILES)
    if form.is_valid():
      form.save()
      obj=form.instance
      return render(request,'students/register.html',{'obj':obj})
      
  else:
    form= registerform()
    std=Student.objects.all()

  return render(request,'students/register.html',
{'std':std,'form':form})
#This worked 

  
