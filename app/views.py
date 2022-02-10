from django.http import HttpRequest, HttpResponse  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.models import User  # type: ignore

from app.models import Car


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", context={
        "cars": Car.objects.all()
    })


def delete(request: HttpRequest, id_: str) -> HttpResponse:
    global cars
    Car.objects.get(id=id_).delete()
    return HttpResponse("", status=204)


def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        Car.objects.create(
            model=request.POST.get("model", ""),
            speed=int(request.POST.get("speed", "")),
            color=request.POST.get("color", ""),
        )
    return redirect("/")
