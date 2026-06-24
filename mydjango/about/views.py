from django.shortcuts import render

# Create your views here.
def aboutAPI(request):
    return render(request, 'about.html')