from django.shortcuts import render
from exam.models import Exam,Student,MobileNumber
from django.views.generic import ListView



def test(request):
    res=render(request,'exam/test.html')
    return res
def exam(request):
    
    e=Exam.objects.all()
    data={'Exam':e}
    res=render(request,'exam/exam.html',data)
    return res
def mobileDetails(request):
    students=Student.objects.all()
    data={'students':students}
    res=render(request,'exam/student_mobile.html',data)
    return  res

class StudentMobileNumber(ListView):
    model = Student
    template_name = 'exam/mobile.html'


# Create your views here.
