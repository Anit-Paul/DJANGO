from django.http import HttpResponse

def homeAPI(request):
    return HttpResponse("Hello, this is the home API view.")