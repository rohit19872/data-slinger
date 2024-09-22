from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def recieve_event(request):
    return HttpResponse("Hello, world2!")