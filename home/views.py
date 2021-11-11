from django.http import HttpRequest
from django.shortcuts import render


def index(http_request: HttpRequest):
    return render(http_request, 'home/home.html')
