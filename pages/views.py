# pages/views.py

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello world from Django!")
