from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def plus_view(request: HttpRequest, a: int, b: int) -> HttpResponse:
    c = a + b
    return HttpResponse(str(c))


def minus_view(request: HttpRequest, a: int, b: int) -> HttpResponse:
    c = a - b
    return HttpResponse(str(c))


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")
