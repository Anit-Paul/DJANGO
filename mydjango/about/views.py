from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.shortcuts import get_object_or_404
from .forms import StudentForm
# Create your views here.
def aboutAPI(request):
    data=Student.objects.all()
    return render(request, 'about.html',{'data':data})

def aboutDetailsAPI(request,data_id):
    obj=get_object_or_404(Student,pk=data_id)
    return render(request,'details.html',{'data':[obj]})

def formAPI(request):
    data=None
    if(request.method=='POST'):
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            form.save()
    return render(request,'form.html')