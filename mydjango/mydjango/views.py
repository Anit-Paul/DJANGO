from django.http import HttpResponse
from django.shortcuts import render
def homeAPI(request):
    #return HttpResponse("Hello, this is the home API view.")
    return render(request, 'home/index.html')