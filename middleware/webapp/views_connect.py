from django.http import HttpResponse

def receive_event(request):
    return HttpResponse("Hello, world!")
