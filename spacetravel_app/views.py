from django.http import HttpRequest, HttpResponse


def index(http_request: HttpRequest):
    return HttpResponse("Hello world")
