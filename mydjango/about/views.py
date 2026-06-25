from django.shortcuts import render
from .models import Student
# Create your views here.
def aboutAPI(request):
    data=Student.objects.all()
    return render(request, 'about.html',{'data':data})